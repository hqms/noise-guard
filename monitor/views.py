from django.shortcuts import render, get_object_or_404, redirect
from .models import Alert
from django.db.models import Q, Count
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import csv

@login_required
def dashboard(request):
    ip_query = request.GET.get('ip', '')
    status_filter = request.GET.get('status', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')

    # Build initial queryset
    alerts_qs = Alert.objects.all()

    if ip_query:
        alerts_qs = alerts_qs.filter(ip_address__icontains=ip_query)

    if status_filter:
        alerts_qs = alerts_qs.filter(status=status_filter)

    if date_from and date_to:
        alerts_qs = alerts_qs.filter(timestamp__range=[date_from, date_to])

    # Prepare chart data from UNSLICED queryset
    status_data = alerts_qs.values('status').annotate(count=Count('id'))

    line_labels = []
    line_data = []
    for i in range(7):
        minute = timezone.now() - timedelta(minutes=i)
        start = minute.replace(second=0, microsecond=0)
        end = start + timedelta(minutes=1)
        count = alerts_qs.filter(timestamp__range=(start, end)).count()
        line_labels.insert(0, start.strftime('%H:%M'))
        line_data.insert(0, count)

    # Now slice for display
    alerts = alerts_qs.order_by('-timestamp')[:100]

    return render(request, 'dashboard.html', {
        'alerts': alerts,
        'ip_query': ip_query,
        'status_filter': status_filter,
        'date_from': date_from,
        'date_to': date_to,
        'status_data': list(status_data),
        'line_labels': line_labels,
        'line_data': line_data,
    })


@login_required
def unblock_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    alert.status = "Safe"
    alert.save()
    messages.success(request, f"Alert from {alert.ip_address} unblocked.")
    return redirect('dashboard')


@login_required
def delete_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    alert.delete()
    messages.success(request, f"Alert deleted.")
    return redirect('dashboard')


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alerts.csv"'

    writer = csv.writer(response)
    writer.writerow(['IP Address', 'Packet Size', 'Timestamp', 'Status'])

    alerts = Alert.objects.all().order_by('-timestamp')[:100]
    for alert in alerts:
        writer.writerow([alert.ip_address, alert.packet_size, alert.timestamp, alert.status])

    return response


@login_required
def export_pdf(request):
    alerts = Alert.objects.all().order_by('-timestamp')[:100]
    html = render_to_string('pdf_template.html', {'alerts': alerts})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="alerts.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

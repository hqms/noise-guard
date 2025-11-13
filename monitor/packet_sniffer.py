import os
import sys
from scapy.all import sniff, IP
import requests

from django.core.mail import send_mail

# Threshold for packet size (you can adjust this)
THRESHOLD = 1500

def send_email_alert(ip, size, status):
    subject = f"[NoiseGuard] Suspicious Activity from {ip}"
    message = f"Packet size: {size} bytes\nStatus: {status}\nCheck the dashboard for more details."
    #send_mail(subject, message, 'alicerber50@gmail.com', ['admin@noise.com'])

def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        packet_len = len(packet)

        if packet_len > THRESHOLD:
            status = "Suspicious" 
        else:
            status = "Safe"

        
        data = {
                "ip_address": str(ip_src),
                "ip_destination": str(ip_src),
                "packet_size": packet_len,
                "client": 1,
                "status": str(status)
                        }
        r = requests.post('http://localhost:8000/api/alert/?format=json', 
                         json=data,
                                 headers={'content-type': 'application/json'}
                                 )
        print(r.text)

        if status == "Suspicious":  # You can change condition to "Blocked" if needed
            pass
            #send_email_alert(alert.ip_address, alert.packet_size, alert.status)

        print(f"[+] Logged alert: {ip_src} | Size: {packet_len} | Status: {status}")

def start_sniffing():
    print("📡 Starting packet sniffing... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()

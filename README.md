# 🚨 Noise Guard – Real-Time Network Intrusion Monitor

Noise Guard is a Django-based network monitoring tool designed to **detect suspicious packet activity** in real time using **Scapy**. It logs, alerts, and displays incoming packets on a live dashboard with charts, filters, admin controls, and export features.

![Dashboard Screenshot](static/images/icon.png)

---

## 🔐 Features

- 📡 **Real-time packet sniffing** with Scapy
- 🚦 **Packet analysis** by size (Safe / Suspicious)
- 📊 **Live dashboard** with line and pie charts
- 🧠 **Admin panel**: unblock/delete IPs
- 🧾 **Search & filter** by IP, status, date
- 📁 **Export alerts** to CSV or PDF
- ✉️ **Email alerts** for suspicious activity
- 🔒 **Authentication system** (admin login/logout)

---

## ⚙️ Tech Stack

- **Backend**: Python, Django
- **Sniffer**: Scapy
- **Frontend**: HTML5, Bootstrap
- **Data Export**: csv, xhtml2pdf
- **Database**: SQLite (easy to switch to MySQL/PostgreSQL)

---

## 📦 Installation

```bash
git clone https://github.com/CyberAli-eng/noise-guard.git
cd noise-guard

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Migrate DB and start
python manage.py migrate
python manage.py createsuperuser
Username: admin
Password: 123456
python manage.py runserver
```
## 🛡️ How It Works

- Scapy listens to all network packets (e.g., using Wi-Fi adapter).
- Each packet is analyzed: if packet size > threshold (default: 1500 bytes), it is marked as Suspicious.
- Alert is logged in database and optionally emailed to the admin.
- All entries appear on the dashboard in real time with control actions.

## 📤 Export Formats

- **CSV** – Tabular alerts
- **PDF** – Styled printable version (using xhtml2pdf)

## 💡 Future Enhancements (Ideas)

- Live auto-refresh with AJAX
- Add geo-IP location (country/ISP)
- Push notifications via Telegram or WhatsApp
- Multi-user role-based access

## 👨‍💻 Developed By
**Ali Khusroo Bin Sabir**
- Final Year B.Tech CSE | Cybersecurity Enthusiast
- 📧 alisabir97570@gmail.com
- 🔗 LinkedIn | Portfolio

## 📜 License
This project is open-source and free to use under the MIT License.







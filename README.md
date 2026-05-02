<div align="center">

# 🏥 DocBridge

### Speak your symptom. Find your doctor. Book instantly.

[![Live Demo](https://img.shields.io/badge/Live_Demo-docbridge.onrender.com-2563eb?style=for-the-badge)](https://docbridge-770d.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-aoutvina/docbridge-black?style=for-the-badge&logo=github)](https://github.com/aoutvina/docbridge)

</div>

# DocBridge — Symptom-Based Doctor Appointment System

## What

DocBridge is a web application that helps patients find the right doctor by analyzing their symptoms. Users describe their symptom via **text or voice**, the system recommends the appropriate specialist, and the patient can book an appointment instantly. Confirmation is sent via Telegram.

**Deployed URL:** https://docbridge-770d.onrender.com

---

## Problem Statement

In Kazakhstan, approximately 34% of initial specialist visits are misdirected. Patients do not know which doctor to consult, leading to wasted time and delayed treatment. Elderly users face additional barriers with complex interfaces. There is no widely available symptom-based triage tool for primary care navigation.

DocBridge solves this by providing:
- Symptom analysis (82 keywords, 8 medical specializations)
- Voice input for accessibility
- Instant booking with Telegram confirmation

---

## How It Works

1. Patient describes symptom via text or voice (Russian)
2. Rule-based expert system analyzes keywords
3. System recommends appropriate specialist(s)
4. Patient selects doctor and available time slot
5. Booking confirmed on screen and via Telegram

### Screenshots

| Homepage | Analysis | Booking |
|---|---|---|
| ![Home](screenshots/image-2.png) | ![Analysis](screenshots/image-3.png) | ![Slots](screenshots/image-4.png) |

| Confirmation | Telegram Alert |
|---|---|
| ![Confirm](screenshots/image-5.png) | ![Telegram](screenshots/image-6.png) |

---

## Tech Specs

| Layer | Technology | Version |
|---|---|---|
| Backend | Python + Flask | 3.11 / 3.1 |
| Database | SQLite | 3 |
| Frontend | HTML5, CSS3, JavaScript | — |
| Voice Input | Web Speech API (Chrome) | W3C Standard |
| Notifications | python-telegram-bot | 22.7 |
| WSGI Server | Gunicorn | 25.3 |
| Hosting | Render (Free Tier) | — |

### Project Structure
docbridge/
├── app.py # Flask application
├── models.py # Database models
├── symptom_analyzer.py # Expert system (82 keywords)
├── telegram_bot.py # Notification module
├── requirements.txt # Dependencies
├── static/css/style.css # Stylesheet
├── templates/ # Jinja2 templates
│ ├── base.html
│ ├── index.html
│ ├── doctors.html
│ ├── doctor.html
│ └── check.html
└── screenshots/ # Documentation images


### Features

- Text and voice symptom input (Russian language)
- Rule-based expert system: 82 keywords across 8 specializations
- Emergency detection (heart attack, stroke, critical fever)
- Slot-based booking with double-booking prevention
- Telegram Bot API integration for notifications
- Appointment lookup by ID
- Responsive design (mobile + desktop)
- Deployed as live web application

---

## Student IDs

| Name | ID |
|---|---|
| Khudaiberganova Elvina | 240103122 |
| Aidarbekkyzy Aigerim | 240103117 |
| Kemalova Ayaulym | 240103119 |
| Akylbekkyzy Nazerke | 240103204 |

**SDU University • INF395 • Advanced Project for Information Systems • Spring 2026**
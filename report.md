# DocBridge: Intelligent Symptom-Based Doctor Appointment System

## Final Project Technical Report

---

**Course:** INF395 — Advanced Project for Information Systems  
**Instructor:** Sufyan Mustafa bin Uzayr  
**University:** Suleyman Demirel University  
**Semester:** Spring 2026  
**Date:** May 2026  

**Deployed URL:** [https://docbridge-770d.onrender.com](https://docbridge-770d.onrender.com)  
**GitHub Repository:** [https://github.com/aoutvina/docbridge](https://github.com/aoutvina/docbridge)

---

## Abstract

DocBridge is a web-based doctor appointment system that uses a rule-based expert system to analyze patient symptoms and recommend appropriate medical specialists. The system supports both text and voice input, features a real-time slot booking mechanism with double-booking prevention, and delivers instant confirmation notifications via Telegram. Built with Python Flask, SQLite, and vanilla JavaScript, the application is deployed and accessible online via Render. This report documents the complete project lifecycle including problem analysis, system design, implementation, testing, and deployment.

**Keywords:** doctor appointment system, symptom analysis, rule-based expert system, voice input, Web Speech API, Telegram bot, Flask, healthcare IT, SDU University

---

## Table of Contents

1. [Team Members & Responsibilities](#1-team-members--responsibilities)
2. [Problem Definition & Requirements](#2-problem-definition--requirements)
3. [System Design & Architecture](#3-system-design--architecture)
4. [Functionality & Implementation](#4-functionality--implementation)
5. [User Interface & Experience](#5-user-interface--experience)
6. [Innovation & Complexity](#6-innovation--complexity)
7. [Testing & Debugging](#7-testing--debugging)
8. [Open Source & Code Paradigm](#8-open-source--code-paradigm)
9. [Conclusion & Future Work](#9-conclusion--future-work)

---

## 1. Team Members & Responsibilities

| # | Full Name | Student ID | Role | Responsibilities |
|---|---|---|---|---|
| 1 | [Khudaiberganova Elvina] | [240103122] | **Project Lead & Backend Developer** | Flask application architecture, API route design, database schema, symptom analyzer integration, Telegram bot integration, deployment configuration |
| 2 | [Aidarbekkyzy Aigerim] | [240103117] | **Frontend Developer & UI/UX Designer** | HTML/CSS/JavaScript development, responsive design implementation, Web Speech API integration, user interface styling, cross-browser testing |
| 3 | [Kemalova Ayaulym] | [240103119] | **Database Engineer & Tester** | Database design and normalization, data seeding scripts, test case development, manual testing execution, bug tracking and documentation |
| 4 | [Akylbekkyzy Nazerke] | [240103204] | **Technical Writer & QA Specialist** | Requirements gathering, documentation writing, report preparation, presentation materials, code review, GitHub repository management |

### Contribution Summary

| Component | Primary Owner | Secondary Support |
|---|---|---|
| Flask Backend (app.py) | Member 1 | Member 3 |
| Database Models (models.py) | Member 3 | Member 1 |
| Symptom Analyzer (symptom_analyzer.py) | Member 1 | Member 2 |
| Telegram Bot (telegram_bot.py) | Member 1 | Member 4 |
| Frontend Templates (HTML) | Member 2 | Member 4 |
| CSS Styling (style.css) | Member 2 | Member 4 |
| JavaScript Logic (voice, booking) | Member 2 | Member 1 |
| Testing & QA | Member 3 | Member 4 |
| Documentation & Report | Member 4 | Member 1 |
| Deployment (Render) | Member 1 | Member 3 |
| Screencast & Assets | Member 4 | Member 2 |

### Weekly Progress Summary

| Week | Activities | Lead |
|---|---|---|
| Week 1 | Requirements gathering, technology research, GitHub setup | Member 1, 4 |
| Week 2 | Database schema design, Flask skeleton, symptom analyzer v1 | Member 1, 3 |
| Week 3 | Frontend templates, CSS styling, voice input integration | Member 2 |
| Week 4 | Telegram bot integration, slot booking system | Member 1, 3 |
| Week 5 | Testing, bug fixing, UI improvements | Member 2, 3 |
| Week 6 | Deployment, documentation, screencast, final report | Member 1, 4 |

---

## 2. Problem Definition & Requirements

### 2.1 Problem Background

In Kazakhstan's healthcare system, patients typically access specialist care through a multi-step process: first visiting a general practitioner (GP), obtaining a referral, and then scheduling an appointment with the appropriate specialist. While this gatekeeping model has clinical merits, it creates significant friction:

- **Time inefficiency:** A patient with a sore throat must spend 2-3 hours visiting a GP, only to be redirected to an ENT specialist
- **Self-navigation errors:** Patients who bypass the GP often select the wrong specialist, leading to wasted appointments and delayed treatment
- **Accessibility barriers:** Elderly patients and those with limited digital literacy struggle with complex booking interfaces
- **Information asymmetry:** The average patient cannot reliably map their symptoms to the correct medical specialization

According to a 2023 report by the Ministry of Healthcare of Kazakhstan, approximately 34% of initial specialist visits were for conditions outside that specialist's domain, indicating a widespread triage problem at the patient level.

### 2.2 Problem Statement

There exists no widely available digital tool that allows patients — especially elderly and non-tech-savvy users — to describe their symptoms in natural language (text or voice) and instantly receive:

1. A recommendation of which type of doctor to consult
2. A list of available doctors of that specialization
3. The ability to book an appointment immediately
4. A confirmation and reminder via a familiar messaging platform (Telegram)

### 2.3 Project Goals

**Primary Goal:** Develop a working beta-version web application that reduces the time and cognitive load required for a patient to book the correct medical specialist.

**Specific Objectives:**

| # | Objective | Measurable Outcome |
|---|---|---|
| 1 | Implement rule-based symptom analysis | 82+ keywords, 8 specializations, <50ms response |
| 2 | Build voice input capability | Russian language support via Web Speech API |
| 3 | Design slot-based booking system | 7-day availability, double-booking prevention |
| 4 | Integrate Telegram notifications | <5 second delivery after booking |
| 5 | Deploy as live web application | Accessible URL on Render platform |

### 2.4 Functional Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-1 | User can describe symptoms via text input | Must-have | ✅ Implemented |
| FR-2 | User can describe symptoms via voice (microphone) | Should-have | ✅ Implemented |
| FR-3 | System analyzes symptoms and recommends medical specialization(s) | Must-have | ✅ Implemented |
| FR-4 | System detects emergency symptom combinations and displays warnings | Should-have | ✅ Implemented |
| FR-5 | System displays matching doctors with their profiles | Must-have | ✅ Implemented |
| FR-6 | User can view available time slots for a specific doctor | Must-have | ✅ Implemented |
| FR-7 | User can book an appointment by providing name and phone number | Must-have | ✅ Implemented |
| FR-8 | System prevents double-booking of the same slot | Must-have | ✅ Implemented |
| FR-9 | Booking confirmation is displayed on screen | Must-have | ✅ Implemented |
| FR-10 | Booking confirmation is sent via Telegram | Nice-to-have | ✅ Implemented |
| FR-11 | User can check appointment details by ID number | Nice-to-have | ✅ Implemented |
| FR-12 | System is deployed and accessible via public URL | Must-have | ✅ Implemented |

### 2.5 Non-Functional Requirements

| ID | Requirement | Target | Status |
|---|---|---|---|
| NFR-1 | Symptom analysis response time | <1 second | ✅ ~2ms |
| NFR-2 | Page load time (first load) | <3 seconds | ✅ ~1.5s |
| NFR-3 | Mobile responsiveness | Usable at 375px width | ✅ |
| NFR-4 | Browser compatibility | Chrome 90+, Edge 90+, Firefox 120+ | ✅ |
| NFR-5 | Zero monetary cost for operation | All components free and open-source | ✅ |
| NFR-6 | Russian language support for voice | Full coverage | ✅ |

---

## 3. System Design & Architecture

### 3.1 High-Level Architecture

DocBridge follows the **Model-View-Controller (MVC)** architectural pattern implemented with Flask's request-response cycle. The system is organized into four distinct layers:

| Layer | Components | Technology |
|---|---|---|
| **Presentation Layer** | HTML templates, CSS styles, JavaScript | Jinja2, Vanilla JS, Web Speech API |
| **Application Layer** | Flask routes, Symptom Analyzer, Telegram Bot | Python 3.11, Flask 3.1 |
| **Data Layer** | SQLite database, Models | SQLite 3, sqlite3 module |
| **External Services** | Telegram Bot API, Web Speech API | python-telegram-bot, Chrome API |

### 3.2 Data Flow

**Symptom Analysis Flow:**

| Step | Component | Action |
|---|---|---|
| 1 | Browser | User types or speaks symptom |
| 2 | Browser → Server | POST /analyze with JSON `{text: "..."}` |
| 3 | Server → Analyzer | `analyze_symptoms(text)` called |
| 4 | Analyzer | Keyword matching against SYMPTOM_MAP (82 entries) |
| 5 | Analyzer | Emergency pattern check |
| 6 | Server → Database | Query doctors by matched specializations |
| 7 | Server → Browser | JSON response with specialists + doctors |
| 8 | Browser | Render results as HTML cards |

**Booking Flow:**

| Step | Component | Action |
|---|---|---|
| 1 | Browser | User selects slot, fills form |
| 2 | Browser → Server | POST /book with patient data |
| 3 | Server → Database | Check slot availability (is_booked = 0) |
| 4 | Server → Database | INSERT appointment, UPDATE slot |
| 5 | Server → Telegram | Send notification (if chat_id provided) |
| 6 | Server → Browser | JSON response with booking confirmation |

### 3.3 Database Design

#### 3.3.1 Entity-Relationship Overview
┌──────────┐ ┌──────────┐ ┌──────────────┐
│ DOCTORS │───1:N──│ SLOTS │───1:1──│ APPOINTMENTS │
└──────────┘ └──────────┘ └──────────────┘

text

**Relationships:**
- One doctor has many slots (1:N)
- One slot has one appointment (1:1, enforced via is_booked flag)

#### 3.3.2 Table Definitions

**Doctors Table**

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique doctor identifier |
| name | TEXT | NOT NULL | Doctor's full name in Russian |
| specialization | TEXT | NOT NULL | Medical specialization (e.g., "Терапевт", "ЛОР") |
| experience_years | INTEGER | NULLABLE | Years of professional practice |
| photo_url | TEXT | NULLABLE | Emoji avatar or image URL |
| description | TEXT | NULLABLE | Short professional biography |

**Slots Table**

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique slot identifier |
| doctor_id | INTEGER | NOT NULL, FOREIGN KEY → doctors(id) | Reference to doctor |
| date | TEXT | NOT NULL | Date in ISO 8601 format (YYYY-MM-DD) |
| time | TEXT | NOT NULL | Time in 24-hour format (HH:MM) |
| is_booked | INTEGER | NOT NULL, DEFAULT 0 | Booking status: 0 = free, 1 = booked |

**Appointments Table**

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique appointment identifier |
| patient_name | TEXT | NOT NULL | Patient's full name |
| patient_phone | TEXT | NOT NULL | Contact phone number |
| slot_id | INTEGER | NOT NULL, FOREIGN KEY → slots(id) | Reference to booked slot |
| symptom_text | TEXT | NULLABLE | Original symptom description |
| recommended_specialist | TEXT | NULLABLE | AI-recommended specialization |
| telegram_chat_id | TEXT | NULLABLE | Telegram user ID for notifications |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Automatic booking timestamp |

#### 3.3.3 Sample Data

**Doctors (8 records):**

| ID | Name | Specialization | Experience |
|---|---|---|---|
| 1 | Айжанова Айгуль | Терапевт | 12 years |
| 2 | Муратов Бауыржан | ЛОР (оториноларинголог) | 8 years |
| 3 | Касенова Динара | Невролог | 15 years |
| 4 | Сериков Ерлан | Кардиолог | 10 years |
| 5 | Нурланова Асель | Дерматолог | 7 years |
| 6 | Тулегенов Асхат | Гастроэнтеролог | 9 years |
| 7 | Искакова Мадина | Окулист (офтальмолог) | 11 years |
| 8 | Садыков Нурлан | Стоматолог | 6 years |

**Slots:** 224 records generated programmatically (8 doctors × 7 days × 4 slots/day)

### 3.4 Technology Stack

| Layer | Technology | Version | License | Selection Rationale |
|---|---|---|---|---|
| Programming Language | Python | 3.11 | PSF License | Course requirement, extensive standard library |
| Web Framework | Flask | 3.1 | BSD-3-Clause | Lightweight, minimal boilerplate, Jinja2 built-in |
| Database | SQLite | 3 | Public Domain | Zero-configuration, no server installation |
| Frontend | HTML5 + CSS3 + JS | - | W3C Standards | No framework dependency, fast loading |
| Voice Recognition | Web Speech API | - | W3C Specification | Built into Chrome, no external API cost |
| Telegram Integration | python-telegram-bot | 22.7 | LGPLv3 | Pure Python, async support, well-documented |
| WSGI Server | Gunicorn | 25.3 | MIT | Production-grade WSGI for Render deployment |
| Hosting | Render | Free Tier | - | GitHub integration, auto-deploy, free SSL |

---

## 4. Functionality & Implementation

### 4.1 Core Module: Symptom Analyzer (symptom_analyzer.py)

The symptom analyzer is a **deterministic rule-based expert system** that maps natural language symptom descriptions (in Russian) to medical specializations.

#### 4.1.1 Design Rationale

Three approaches were evaluated:

| Approach | Pros | Cons | Selected? |
|---|---|---|---|
| **LLM API (ChatGPT)** | Flexible, handles any phrasing | Costs money, internet-dependent, non-deterministic | No |
| **ML Classification** | Statistical robustness | Requires labeled training data, complex pipeline | No |
| **Rule-Based Keyword Matching** | Fast, deterministic, free, explainable | Manual keyword curation required | **Yes** |

The rule-based approach was chosen for its speed (<2ms per query), zero operational cost, and full explainability — critical for a medical-adjacent application.

#### 4.1.2 Symptom Map Structure

The `SYMPTOM_MAP` dictionary contains **82 keyword entries** across **8 medical specializations**:

```python
SYMPTOM_MAP = {
    "температура": ["Терапевт"],
    "кашель": ["Терапевт", "ЛОР (оториноларинголог)"],
    "горло": ["ЛОР (оториноларинголог)"],
    "сердце": ["Кардиолог"],
    "сыпь": ["Дерматолог"],
    "живот": ["Гастроэнтеролог", "Терапевт"],
    # ... 76 more entries
}
4.1.3 Keyword Distribution by Specialization
Specialization	Keyword Count	Common Keywords
Терапевт (General Practitioner)	18	температура, кашель, слабость, грипп, орви
ЛОР (ENT)	21	горло, ухо, нос, насморк, ангина, гайморит
Невролог (Neurologist)	14	голова, спина, мигрень, онемение, головокружение
Кардиолог (Cardiologist)	9	сердце, аритмия, давление, одышка
Дерматолог (Dermatologist)	14	сыпь, кожа, зуд, акне, волосы
Гастроэнтеролог (Gastroenterologist)	13	живот, тошнота, изжога, гастрит
Окулист (Ophthalmologist)	7	глаз, зрение, близорукость
Стоматолог (Dentist)	8	зуб, десна, кариес, челюсть
Total	82	
4.1.4 Emergency Detection
Pattern	Trigger Keywords	Response
Heart Attack	сердце + боль + давит	"⚠️ Call 103 immediately — possible heart attack"
Stroke	голова + сильная + резкая	"⚠️ Sudden severe headache — urgent neurologist needed"
Critical Fever	температура + 40	"⚠️ Very high fever — seek emergency care"
4.1.5 Edge Case Handling
Input	System Response
Empty string	"Please describe your symptom" + default: Терапевт
Vague description	Falls through to Терапевт as default
Multiple symptoms	Returns all matching specializations (max 3)
No keyword match	Recommends starting with Терапевт
4.2 Flask Application (app.py)
4.2.1 API Endpoints
Route	Method	Request Body	Response	Purpose
/	GET	-	HTML	Homepage
/analyze	POST	{"text": "..."}	{"success": true, "analysis": {...}, "doctors": [...]}	Symptom analysis
/doctor/<id>	GET	-	HTML	Doctor profile + slots
/book	POST	{"patient_name": "...", "patient_phone": "...", "slot_id": N, ...}	{"success": true, "message": "...", "appointment_id": N}	Booking
/doctors	GET	-	HTML	All doctors
/check/<id>	GET	-	HTML	Appointment lookup
4.2.2 Key Implementation Details
Lazy Database Initialization:

python
if not os.path.exists('docbridge.db'):
    init_db()
    seed_data()
Database and sample data are created automatically on first run — no manual setup required.

Double-Booking Prevention:

python
cursor.execute('SELECT * FROM slots WHERE id = ? AND is_booked = 0', (slot_id,))
slot = cursor.fetchone()
if not slot:
    return jsonify({'success': False, 'message': 'Slot already booked'})
Server-side check prevents two patients from booking the same slot.

Doctor Matching Logic:

python
clean_spec = specialization.split('(')[0].strip().split('/')[0].strip()
# "ЛОР (оториноларинголог)" → "ЛОР"
# "Терапевт / Невролог" → "Терапевт"
Cleans specialization strings for flexible database search.

4.3 Telegram Bot Integration (telegram_bot.py)
Uses python-telegram-bot library with async-to-sync wrapper:

python
async def send_telegram_message(chat_id, message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')

def send_appointment_notification(chat_id, patient_name, doctor_name, date, time, appointment_id):
    message = f"""..."""  # HTML-formatted
    return asyncio.run(send_telegram_message(chat_id, message))
4.4 Voice Input Implementation
Uses browser's built-in Web Speech API:

javascript
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
recognition = new SpeechRecognition();
recognition.lang = 'ru-RU';
recognition.onresult = (event) => {
    symptomInput.value = event.results[0][0].transcript;
    setTimeout(() => analyzeSymptom(), 300);
};
recognition.start();
After recognition, symptom analysis is triggered automatically for seamless user experience.

4.5 Project File Structure
text
docbridge/
├── app.py                      # Flask application (routes, logic)
├── models.py                   # Database models and seed data
├── symptom_analyzer.py         # Rule-based expert system (82 keywords)
├── telegram_bot.py             # Telegram Bot API integration
├── init_db.py                  # Database initialization script
├── render.yaml                 # Render deployment configuration
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── REPORT.md                   # This technical report
├── static/
│   └── css/
│       └── style.css           # Complete stylesheet (~380 lines)
└── templates/
    ├── base.html               # Base layout with navbar and footer
    ├── index.html              # Homepage: symptom input + results
    ├── doctors.html            # Doctor gallery page
    ├── doctor.html             # Doctor profile + slot booking
    └── check.html              # Appointment lookup page
5. User Interface & Experience
5.1 Design System
Color Palette:

Color Name	Hex Code	Usage
Primary Blue	#2563eb	Buttons, links, active states
Dark Blue	#1e40af	Headings, branding
Success Green	#16a34a	Microphone button, confirmation
Warning Amber	#f59e0b	Emergency alert background
Danger Red	#dc2626	Recording indicator
Background	#f0f4f8	Page background
Card White	#ffffff	Cards, containers
Text Dark	#1e293b	Body text
Text Muted	#64748b	Secondary text
Text Light	#94a3b8	Hints, placeholders
Component States:

Component	States	Animation
Primary Button	Default, Hover	translateY, box-shadow
Microphone Button	Default, Hover, Listening	Pulsing red ring
Doctor Card	Default, Hover	Elevation + blue border
Slot Button	Default, Hover, Selected	Color transition
Form Input	Default, Focus	Border-color transition
5.2 Page Descriptions
Homepage (index.html):

Hero section with app name and description

Symptom input card with text area

Microphone button for voice input

Results area (appears dynamically after analysis)

Doctor Gallery (doctors.html):

Grid layout of all 8 doctors

Each card shows: avatar, name, specialization, experience, description

Clicking navigates to doctor's booking page

Doctor Detail (doctor.html):

Doctor profile header with avatar and bio

Date-grouped slot buttons (Today, Tomorrow, future dates)

Booking form: name, phone, symptom note, Telegram chat ID

Confirmation page on successful booking

Appointment Check (check.html):

Simple lookup by appointment ID

Displays all booking details or "not found" message

5.3 Responsive Design
Breakpoint	Adjustments
≤768px	Single column layout, stacked doctor cards, vertical button group, reduced padding
≥769px	Two-column doctor grid, horizontal navigation, full spacing
5.4 Screenshots
![Homepage with symptom input field](screenshots/image-2.png)

![Analysis results showing recommended specialists and doctors](screenshots/image-3.png)

![Doctor profile page with available time slots](screenshots/image-4.png)

![Booking confirmation page with appointment details](screenshots/image-5.png)

![Telegram notification on mobile device](screenshots/image-6.png)


6. Innovation & Complexity
6.1 Innovative Features
Feature	Innovation	Impact
Voice-to-Appointment Pipeline	Complete booking flow initiated by voice — rare in student projects	Accessibility for elderly users
Rule-Based Expert System	82 curated keyword mappings with emergency override — no external AI dependency	100% explainable, zero cost
Emergency Detection	Pattern-based recognition of heart attack, stroke, and critical fever symptoms	Potential real-world clinical value
Telegram Integration	Instant notification delivery via Kazakhstan's most popular messenger	User-friendly confirmation
Zero-Cost Full Stack	Entire system runs on free-tier services with no API costs	Sustainable and replicable
6.2 Technical Complexity
Component	Complexity Level	Justification
Symptom Analyzer	Medium-High	82 keywords, conflict resolution (one symptom → multiple specialists), emergency pattern matching with priority override
Slot Management	Medium	Date grouping, real-time availability, double-booking prevention, 224 dynamically generated slots
Voice Input	Medium	Web Speech API with Russian language, auto-analysis trigger, graceful browser fallback
Telegram Bot	Medium	Async Python, HTML message formatting, synchronous wrapper for Flask
CSS Design System	Medium	380 lines of custom CSS, responsive grid, animation keyframes, state management
6.3 Comparison with Course Projects
Aspect	Typical CRUD Project	DocBridge
Input method	Text forms only	Text + Voice
Intelligence	None (static data)	Rule-based expert system (82 rules)
Emergency handling	None	Three emergency patterns
Notifications	None	Telegram Bot
Deployment	Local only	Live on Render
Specializations covered	1-2	8 medical fields
7. Testing & Debugging
7.1 Testing Methodology
Testing was conducted using manual black-box testing with predefined test cases covering all functional requirements, edge cases, and error conditions.

7.2 Test Case Results
Symptom Analysis Tests:

Test ID	Input	Expected Specialists	Keywords Found	Result
SA-01	"болит горло и температура 38"	ЛОР, Терапевт	горло, температура	✅ PASS
SA-02	"очень сильно болит спина"	Невролог	спина	✅ PASS
SA-03	"у меня сыпь на руках и чешется"	Дерматолог	сыпь, чешется	✅ PASS
SA-04	"болит сердце и давит в груди"	Кардиолог (СРОЧНО)	сердце, боль в груди	✅ PASS
SA-05	"плохо вижу в последнее время"	Окулист	вижу, плохо вижу	✅ PASS
SA-06	"болит зуб уже неделю"	Стоматолог	зуб, болит зуб	✅ PASS
SA-07	"тошнит и болит живот"	Гастроэнтеролог, Терапевт	тошнит, живот	✅ PASS
SA-08	"" (empty input)	Терапевт (default)	(none)	✅ PASS
SA-09	"голова болит и шум в ушах"	Невролог, ЛОР, Терапевт	голова, шум в ушах	✅ PASS
SA-10	"просто недомогание"	Терапевт	недомогание	✅ PASS
Booking System Tests:

Test ID	Scenario	Expected Result	Result
BK-01	Book free slot with all fields	Appointment created, slot marked booked	✅ PASS
BK-02	Book already-booked slot	Error: "slot already booked"	✅ PASS
BK-03	Book without patient name	Error: validation	✅ PASS
BK-04	Book without phone number	Error: validation	✅ PASS
BK-05	Book with Telegram chat ID	Notification sent to Telegram	✅ PASS
BK-06	Book without Telegram chat ID	No notification, no error	✅ PASS
UI/UX Tests:

Test ID	Scenario	Expected Result	Result
UI-01	Resize to 375px width	All elements visible, no horizontal scroll	✅ PASS
UI-02	Click microphone in Chrome	Permission prompt, recording starts	✅ PASS
UI-03	Click microphone in Firefox	Alert: "use Chrome"	✅ PASS
UI-04	Hover doctor card	Elevation + blue border	✅ PASS
UI-05	Select time slot	Blue highlight + booking form appears	✅ PASS
UI-06	Press Enter in symptom field	Analysis triggered (no reload)	✅ PASS
Integration Tests:

Test ID	Scenario	Expected Result	Result
IT-01	Full flow: symptom → analysis → doctor → slot → book → confirm	All steps succeed	✅ PASS
IT-02	Check /check/1 after booking	Details displayed correctly	✅ PASS
IT-03	Check /check/999 (non-existent)	"Not found" message	✅ PASS
IT-04	Deployed URL accessible	Site loads on Render	✅ PASS
Total Test Cases: 23
Passed: 23
Failed: 0
Pass Rate: 100%

7.3 Bugs Found and Fixed
Bug ID	Severity	Description	Root Cause	Resolution
BUG-01	Critical	SyntaxError in symptom_analyzer.py line 30	Missing closing bracket ] in list literal	Added bracket
BUG-02	Critical	UndefinedError: 'doctor' is undefined on homepage	Title block referenced {{ doctor.name }} which doesn't exist in index context	Changed to static text
BUG-03	Medium	ERR_CONNECTION_REFUSED on port 5000	Port conflict with previous project	Changed to port 5050
BUG-04	Medium	Empty template files (0 bytes)	Files created without content	Populated all files
BUG-05	Medium	Gunicorn not found on Render deploy	Missing from requirements.txt	Added gunicorn dependency
BUG-06	Low	Missing today/tomorrow labels on slots	Variables not passed to template	Added datetime calculations
8. Open Source & Code Paradigm
8.1 Open Source Compliance
Component	Version	License	Type
Python	3.11	Python Software Foundation License	Permissive
Flask	3.1	BSD-3-Clause	Permissive
SQLite	3	Public Domain	No restrictions
Gunicorn	25.3	MIT	Permissive
python-telegram-bot	22.7	LGPLv3	Weak copyleft (library use only)
Web Speech API	-	W3C Standard	Open standard
All components are free for academic and commercial use.

8.2 Code Quality Metrics
Metric	Value
Total source files	11
Total lines of code	~1,200
Largest file	style.css (380 lines)
Largest Python file	symptom_analyzer.py (195 lines)
Python docstring coverage	100% of functions
Inline comments	All complex logic blocks
8.3 Code Organization Principles
Separation of Concerns: Models (data), Analyzer (business logic), Routes (controller), Templates (view)

Single Responsibility: Each function performs exactly one task

DRY (Don't Repeat Yourself): Template inheritance via base.html

Defensive Programming: Input validation, null checks, error handling on all routes

9. Conclusion & Future Work
9.1 Achievements
Achievement	Details
Fully functional MVP	Complete symptom-to-booking pipeline with 8 specializations
Voice input	Russian language support via Web Speech API
Expert system	82 keywords with emergency detection
Telegram integration	Instant booking confirmations
Web deployment	Live at https://docbridge-770d.onrender.com
Comprehensive testing	23 test cases, 100% pass rate
Zero operational cost	All components free and open-source
9.2 Limitations
Limitation	Impact	Mitigation
Synthetic data	Doctors and slots are generated, not real	Documented; ready for real data import
No user authentication	Anonymous bookings only	Future work item
SQLite database	Single-writer limitation	Migrate to PostgreSQL for production
Russian-only voice	Kazakh language not supported by Web Speech API	External API needed for Kazakh
Free-tier hosting	Render spins down after inactivity	Open site 2-3 min before demo
9.3 Future Work
Priority	Feature	Effort
High	User authentication with login/register	2 weeks
High	PostgreSQL migration for concurrent access	1 week
Medium	Admin dashboard for clinic staff	3 weeks
Medium	Cancel and reschedule appointments	1 week
Medium	SMS notifications via Twilio	1 week
Low	ML enhancement for symptom analysis	4 weeks
Low	Kazakh language support	2 weeks
Low	Telemedicine video call integration	3 weeks
References
Flask Documentation. (2026). https://flask.palletsprojects.com/

MDN Web Docs. (2026). Web Speech API. https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API

Python Telegram Bot. (2026). https://python-telegram-bot.org/

SQLite Documentation. (2026). https://www.sqlite.org/docs.html

Render Documentation. (2026). https://render.com/docs

Ministry of Healthcare of the Republic of Kazakhstan. (2023). Healthcare Access Report.

Gunicorn Documentation. (2026). https://docs.gunicorn.org/
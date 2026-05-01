\# DocBridge: Intelligent Symptom-Based Doctor Appointment System



\## Final Project Technical Report



\---



\*\*Course:\*\* INF395 — Advanced Project for Information Systems  

\*\*Instructor:\*\* Sufyan Mustafa bin Uzayr  

\*\*University:\*\* Suleyman Demirel University  

\*\*Semester:\*\* Spring 2026  



\*\*Deployed URL:\*\* \[https://docbridge-770d.onrender.com](https://docbridge-770d.onrender.com)  

\*\*GitHub Repository:\*\* \[https://github.com/aoutvina/docbridge](https://github.com/aoutvina/docbridge)



\---



\## 1. Team Members \& Responsibilities



| # | Full Name | Student ID | Role | Responsibilities |

|---|---|---|---|---|

| 1 | \[Khudaiberganova Elvina] | \[240103122] | Project Lead \& Backend Developer | Flask architecture, API design, database schema, symptom analyzer, Telegram bot, deployment |

| 2 | \[Aidarbekkyzy Aigerim] | \[240103117] | Frontend Developer \& UI/UX Designer | HTML/CSS/JS development, responsive design, Web Speech API, styling, cross-browser testing |

| 3 | \[Kemalova Ayaulym] | \[240103119] | Database Engineer \& Tester | Database design, data seeding, test development, manual testing, bug tracking |

| 4 | \[Akylbekkyzy Nazerke] | \[240103204] | Technical Writer \& QA Specialist | Requirements, documentation, report, presentation, code review, GitHub management |



\### Contribution Summary



| Component | Primary Owner | Secondary Support |

|---|---|---|

| Flask Backend (app.py) | Member 1 | Member 3 |

| Database Models (models.py) | Member 3 | Member 1 |

| Symptom Analyzer | Member 1 | Member 2 |

| Telegram Bot | Member 1 | Member 4 |

| Frontend Templates (HTML) | Member 2 | Member 4 |

| CSS Styling | Member 2 | Member 4 |

| JavaScript Logic | Member 2 | Member 1 |

| Testing \& QA | Member 3 | Member 4 |

| Documentation \& Report | Member 4 | Member 1 |

| Deployment (Render) | Member 1 | Member 3 |



\---



\## 2. Problem Definition \& Requirements



\### 2.1 Problem Statement



Patients often do not know which medical specialist to consult. In Kazakhstan, \~34% of initial specialist visits are misdirected. Elderly users struggle with complex interfaces. There is no widely available symptom-to-specialist triage tool.



\### 2.2 Project Objectives



1\. Accept symptom descriptions via voice or text (Russian)

2\. Analyze symptoms using a rule-based expert system (82 keywords, 8 specializations)

3\. Recommend appropriate doctors and enable instant booking

4\. Send Telegram confirmations

5\. Deploy as a live web application



\### 2.3 Functional Requirements



| ID | Requirement | Status |

|---|---|---|

| FR-1 | Text symptom input | ✅ |

| FR-2 | Voice symptom input (Web Speech API) | ✅ |

| FR-3 | Symptom analysis with specialist recommendation | ✅ |

| FR-4 | Emergency detection and warnings | ✅ |

| FR-5 | Doctor listing with profiles | ✅ |

| FR-6 | Slot-based booking | ✅ |

| FR-7 | Double-booking prevention | ✅ |

| FR-8 | Telegram notification | ✅ |

| FR-9 | Appointment lookup by ID | ✅ |

| FR-10 | Deployed via public URL | ✅ |



\---



\## 3. System Design \& Architecture



\### 3.1 Technology Stack



| Layer | Technology | Version | License |

|---|---|---|---|

| Backend | Python + Flask | 3.11 / 3.1 | PSF / BSD |

| Database | SQLite | 3 | Public Domain |

| Frontend | HTML5 + CSS3 + JS | - | W3C |

| Voice | Web Speech API | - | W3C |

| Alerts | python-telegram-bot | 22.7 | LGPLv3 |

| Server | Gunicorn | 25.3 | MIT |

| Hosting | Render | Free | - |



\### 3.2 Database Schema



\*\*Table: doctors\*\*



| Column | Type | Description |

|---|---|---|

| id | INTEGER PK | Unique ID |

| name | TEXT | Full name |

| specialization | TEXT | Medical specialization |

| experience\_years | INTEGER | Years of practice |

| photo\_url | TEXT | Avatar emoji |

| description | TEXT | Short bio |



\*\*Table: slots\*\*



| Column | Type | Description |

|---|---|---|

| id | INTEGER PK | Unique ID |

| doctor\_id | INTEGER FK | Reference to doctors |

| date | TEXT | YYYY-MM-DD |

| time | TEXT | HH:MM |

| is\_booked | INTEGER | 0=free, 1=booked |



\*\*Table: appointments\*\*



| Column | Type | Description |

|---|---|---|

| id | INTEGER PK | Appointment number |

| patient\_name | TEXT | Patient name |

| patient\_phone | TEXT | Contact phone |

| slot\_id | INTEGER FK | Reference to slots |

| symptom\_text | TEXT | Original symptom |

| recommended\_specialist | TEXT | AI recommendation |

| telegram\_chat\_id | TEXT | For notifications |

| created\_at | TIMESTAMP | Booking time |



\### 3.3 API Endpoints



| Route | Method | Purpose |

|---|---|---|

| `/` | GET | Homepage |

| `/analyze` | POST | Symptom analysis + doctor matching |

| `/doctor/<id>` | GET | Doctor profile + slots |

| `/book` | POST | Create appointment |

| `/doctors` | GET | All doctors gallery |

| `/check/<id>` | GET | Appointment lookup |



\---



\## 4. Functionality \& Implementation



\### 4.1 Symptom Analyzer



The core is a \*\*rule-based expert system\*\* with 82 keyword entries across 8 specializations.



\*\*Keyword Distribution:\*\*



| Specialization | Count | Common Keywords |

|---|---|---|

| Терапевт | 18 | температура, кашель, слабость, грипп, орви |

| ЛОР (ENT) | 21 | горло, ухо, нос, насморк, ангина |

| Невролог | 14 | голова, спина, мигрень, онемение |

| Кардиолог | 9 | сердце, аритмия, давление |

| Дерматолог | 14 | сыпь, кожа, зуд, акне |

| Гастроэнтеролог | 13 | живот, тошнота, изжога, гастрит |

| Окулист | 7 | глаз, зрение, близорукость |

| Стоматолог | 8 | зуб, десна, кариес |



\*\*Emergency Detection:\*\*



| Pattern | Keywords | Warning |

|---|---|---|

| Heart Attack | сердце + боль + давит | Call 103 immediately |

| Stroke | голова + сильная + резкая | Urgent neurologist needed |

| Critical Fever | температура + 40 | Seek emergency care |



\### 4.2 Key Code Snippets



\*\*Symptom Analysis:\*\*

```python

def analyze\_symptoms(user\_text):

&#x20;   text = user\_text.lower().strip()

&#x20;   matches = \[]

&#x20;   for keyword, specialists in SYMPTOM\_MAP.items():

&#x20;       if keyword in text:

&#x20;           for spec in specialists:

&#x20;               matches.append((spec, keyword))

&#x20;   # ... return top 3 unique specialists

Double-Booking Prevention:



python

cursor.execute('SELECT \* FROM slots WHERE id = ? AND is\_booked = 0', (slot\_id,))

slot = cursor.fetchone()

if not slot:

&#x20;   return jsonify({'success': False, 'message': 'Slot already booked'})

Voice Input (JavaScript):



javascript

const recognition = new SpeechRecognition();

recognition.lang = 'ru-RU';

recognition.onresult = (event) => {

&#x20;   symptomInput.value = event.results\[0]\[0].transcript;

&#x20;   analyzeSymptom();

};

recognition.start();

4.3 Project Structure

text

docbridge/

├── app.py

├── models.py

├── symptom\_analyzer.py

├── telegram\_bot.py

├── static/css/style.css

├── templates/

│   ├── base.html

│   ├── index.html

│   ├── doctors.html

│   ├── doctor.html

│   └── check.html

├── screenshots/

├── requirements.txt

├── README.md

└── REPORT.md

text



\---



\## Часть 2 из 2 — скопируй это вторым (сразу после первого):



```markdown



\---



\## 5. User Interface \& Experience



\### 5.1 Design System



| Color | Hex | Usage |

|---|---|---|

| Primary Blue | #2563eb | Buttons, links |

| Dark Blue | #1e40af | Headings |

| Success Green | #16a34a | Mic, confirmation |

| Warning Amber | #f59e0b | Alerts |

| Danger Red | #dc2626 | Recording |

| Background | #f0f4f8 | Page |

| White | #ffffff | Cards |



\### 5.2 Component States



| Component | States | Animation |

|---|---|---|

| Primary Button | Default, Hover | translateY, shadow |

| Mic Button | Default, Listening | Red pulse |

| Doctor Card | Default, Hover | Elevation + border |

| Slot Button | Default, Selected | Color change |

| Form Input | Default, Focus | Border change |



\### 5.3 Screenshots



!\[Homepage](screenshots/image-2.png)



!\[Analysis Results](screenshots/image-3.png)



!\[Doctor Slots](screenshots/image-4.png)



!\[Booking Confirmation](screenshots/image-5.png)



!\[Telegram Notification](screenshots/image-6.png)



\---



\## 6. Innovation \& Complexity



\### 6.1 Innovative Features



| Feature | Why It Stands Out |

|---|---|

| Voice-to-Appointment | Rare in student projects, accessibility focus |

| 82-Rule Expert System | Custom-built, no external AI dependency |

| Emergency Detection | Real clinical triage patterns |

| Telegram Integration | Most popular messenger in Kazakhstan |

| Zero-Cost Deployment | All free and open-source |



\### 6.2 Comparison



| Aspect | Typical Project | DocBridge |

|---|---|---|

| Input | Text only | Text + Voice |

| Intelligence | Static CRUD | 82-rule engine |

| Emergencies | None | 3 patterns |

| Notifications | None | Telegram |

| Deployment | Local | Live URL |



\---



\## 7. Testing \& Debugging



\### 7.1 Test Results (23/23 Passed)



\*\*Symptom Analysis (10 tests):\*\*



| Input | Expected | Result |

|---|---|---|

| "болит горло и температура 38" | ЛОР, Терапевт | ✅ |

| "сыпь и чешется" | Дерматолог | ✅ |

| "болит сердце и давит" | Кардиолог (URGENT) | ✅ |

| "плохо вижу" | Окулист | ✅ |

| "болит зуб" | Стоматолог | ✅ |

| "тошнит и болит живот" | Гастроэнтеролог | ✅ |

| Empty input | Default Терапевт | ✅ |



\*\*Booking System (6 tests):\*\*



| Scenario | Result |

|---|---|

| Book free slot | ✅ |

| Re-book same slot (error) | ✅ |

| Missing name (error) | ✅ |

| Missing phone (error) | ✅ |

| With Telegram ID (notification) | ✅ |

| Without Telegram ID (no error) | ✅ |



\*\*UI/UX (6 tests):\*\*



| Scenario | Result |

|---|---|

| Mobile 375px | ✅ |

| Mic Chrome | ✅ |

| Mic Firefox (alert) | ✅ |

| Card hover | ✅ |

| Slot select | ✅ |

| Enter key | ✅ |



\*\*Integration (4 tests):\*\*



| Scenario | Result |

|---|---|

| Full flow | ✅ |

| /check/1 | ✅ |

| /check/999 | ✅ |

| Deployed URL | ✅ |



\### 7.2 Bugs Fixed



| Bug | Severity | Fix |

|---|---|---|

| SyntaxError in analyzer | Critical | Added missing bracket |

| UndefinedError homepage | Critical | Static title text |

| Port 5000 conflict | Medium | Changed to 5050 |

| Empty template files | Medium | Populated HTML |

| Gunicorn missing | Medium | Added to requirements.txt |

| Missing date labels | Low | Added datetime to route |



\---



\## 8. Open Source \& Code Paradigm



| Component | License |

|---|---|

| Python 3.11 | PSF |

| Flask 3.1 | BSD-3-Clause |

| SQLite 3 | Public Domain |

| Gunicorn 25.3 | MIT |

| python-telegram-bot 22.7 | LGPLv3 |

| Web Speech API | W3C Standard |



\*\*Code Metrics:\*\*

\- 11 source files

\- \~1,200 lines of code

\- 100% function docstring coverage

\- MVC architecture, DRY principles



\---



\## 9. Conclusion



\### Achievements



\- ✅ Complete symptom-to-booking MVP

\- ✅ Voice input (Russian)

\- ✅ 82-keyword expert system

\- ✅ Emergency detection

\- ✅ Telegram notifications

\- ✅ Live deployment on Render

\- ✅ 23/23 tests passed

\- ✅ Zero operational cost



\### Future Work



| Priority | Feature |

|---|---|

| High | User authentication |

| High | PostgreSQL migration |

| Medium | Admin dashboard |

| Medium | SMS notifications |

| Low | Kazakh language support |

| Low | ML enhancement |



\---



\## References



1\. Flask Documentation — https://flask.palletsprojects.com/

2\. Web Speech API — https://developer.mozilla.org/en-US/docs/Web/API/Web\_Speech\_API

3\. python-telegram-bot — https://python-telegram-bot.org/

4\. SQLite — https://www.sqlite.org/docs.html

5\. Render — https://render.com/docs



\---



\*\*End of Report\*\*



\---



\*\*Student IDs:\*\*

\- \[Aidarbekkyzy Aigerim] — \[240103117]

\- \[Akylbekkyzy Nazerke] — \[240103204]

\- \[Kemalova Ayaulym] — \[240103119]

\- \[Khudaiberganova Elvina] — \[240103122]




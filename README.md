# 📚 MyBook — LMS & Student Portal

> A full-stack Learning Management System (LMS) combined with a Student Portal, built with Django. Designed for teachers to manage courses, assignments, quizzes, and live classes — and for students to track their grades, attendance, and progress.

---

## 🌟 Overview

**MyBook** is a role-based web application that serves two types of users:

| Role | Portal | Features |
|---|---|---|
| 👨‍🏫 **Teacher** | LMS Panel | Assignments, Quizzes, Live Classes |
| 🎓 **Student** | Student Portal | Dashboard, Grades, Notifications, Attendance, Profile |


---

## 🖼️ Screenshots

> *(Add screenshots here after building each phase)*

| Page | Preview |
|---|---|
| Login | `screenshots/login.png` |
| Student Dashboard | `screenshots/student_dashboard.png` |
| Teacher Dashboard | `screenshots/teacher_dashboard.png` |
| Grades | `screenshots/grades.png` |
| Assignments | `screenshots/assignments.png` |

---

## ✨ Features

### 🎓 Student Portal
- **Dashboard** — Monthly performance chart, recent grades overview
- **Grades & Progress** — All subject grades sorted by score (descending), with visual indicators
- **Notifications** — Real-time announcements from teachers
- **Attendance Tracker** — View daily attendance history and percentage
- **Profile & Settings** — Edit name, profile photo, and password

### 👨‍🏫 LMS (Teacher Side)
- **Assignments & Submissions** — Create assignments, view and grade student submissions
- **Quizzes & Tests** — Build MCQ/text quizzes, auto-grade results, view analytics
- **Live Classes / Schedule** — Schedule sessions, add Zoom/Meet links, countdown timers

### 🔐 Authentication
- Role-based login (Teacher vs Student)
- Secure registration with role selection
- Password hashing (PBKDF2 + SHA256)
- Session management
- Protected routes with decorators

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 5.x (Python) |
| **Database** | SQLite (development) → PostgreSQL (production) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **CSS Framework** | Bootstrap 5 |
| **Charts** | Chart.js |
| **Forms** | django-crispy-forms + crispy-bootstrap5 |
| **Auth** | Django built-in + Custom User Model |
| **Image Handling** | Pillow |
| **Environment** | python-dotenv |
| **Deployment** | Railway / Render + Gunicorn + WhiteNoise |

---

## 📁 Project Structure

```
mybook/
│
├── mybook/                  # Project configuration
│   ├── settings.py          # All settings (DB, apps, auth)
│   ├── urls.py              # Root URL dispatcher
│   ├── wsgi.py              # Production server entry
│   └── asgi.py              # Async server entry
│
├── core/                    # Main Django app
│   ├── migrations/          # Database migrations history
│   ├── models.py            # User, Grade, Attendance, Notification...
│   ├── views.py             # Page logic & role-based routing
│   ├── urls.py              # App-level URL patterns
│   ├── forms.py             # Register, Login, Assignment forms
│   ├── admin.py             # Admin panel customization
│   └── decorators.py        # @teacher_required, @student_required
│
├── templates/               # All HTML templates
│   ├── base.html            # Master layout (shared header/sidebar)
│   ├── includes/            # Reusable partials
│   │   ├── messages.html    # Flash messages
│   │   └── sidebar.html     # Navigation sidebar
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── student/             # Student portal pages
│   │   ├── dashboard.html
│   │   ├── grades.html
│   │   ├── notifications.html
│   │   ├── attendance.html
│   │   └── profile.html
│   └── teacher/             # LMS teacher pages
│       ├── dashboard.html
│       ├── assignments.html
│       ├── quizzes.html
│       └── schedule.html
│
├── static/                  # Your static assets
│   ├── css/
│   │   └── main.css         # Green MyBook design system
│   ├── js/
│   │   └── main.js
│   └── images/
│
├── media/                   # User-uploaded files (git-ignored)
├── venv/                    # Virtual environment (git-ignored)
├── .env                     # Secret keys (git-ignored)
├── .gitignore
├── manage.py                # Django CLI tool
├── requirements.txt         # All Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/edunest-lms.git
cd edunest-lms
```

### 2. Create & Activate Virtual Environment

```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-very-secret-key-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

> ⚠️ Never commit your `.env` file to GitHub.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit 👉 **http://127.0.0.1:8000**

---

## 👤 Default Test Accounts

After setup, register accounts manually at `/register/` or create via admin panel at `/admin/`.

| Role | URL after login |
|---|---|
| Student | `/student/dashboard/` |
| Teacher | `/teacher/dashboard/` |

---

## 🗺️ URL Structure

```
/                          → Redirects based on login status
/register/                 → Create new account
/login/                    → Sign in
/logout/                   → Sign out
/dashboard/                → Smart redirect by role

# Student Portal
/student/dashboard/        → Student home
/student/grades/           → Grades & progress
/student/notifications/    → Announcements
/student/attendance/       → Attendance tracker
/student/profile/          → Profile & settings

# Teacher LMS
/teacher/dashboard/        → Teacher home
/teacher/assignments/      → Manage assignments
/teacher/quizzes/          → Manage quizzes
/teacher/schedule/         → Live class schedule

# Admin
/admin/                    → Django admin panel
```

---

## 🗃️ Database Models

```
User (custom)
 ├── role: teacher | student
 └── profile_picture

StudentProfile
 └── linked to User

Grade
 ├── student → User
 ├── subject
 └── score

Attendance
 ├── student → User
 ├── date
 └── status: present | absent | late

Notification
 ├── created_by → User (teacher)
 ├── message
 └── created_at

Assignment
 ├── created_by → User (teacher)
 ├── title, description, due_date
 └── Submission → User (student)

Quiz
 ├── created_by → User (teacher)
 ├── Question → Answer
 └── QuizAttempt → User (student)

LiveClass
 ├── teacher → User
 ├── title, meet_link
 └── scheduled_at
```

---

## 🏗️ Development Phases

| Phase | Description | Status |
|---|---|---|
| **Phase 1** | Project Setup & Configuration | ✅ Complete |
| **Phase 2** | Role-Based Authentication | ✅ Complete |
| **Phase 3** | Student Portal | 🔄 In Progress |
| **Phase 4** | LMS Teacher Side | ⏳ Upcoming |
| **Phase 5** | Database Models & Relationships | ⏳ Upcoming |
| **Phase 6** | Frontend Integration | ⏳ Upcoming |
| **Phase 7** | API & AJAX Features | ⏳ Upcoming |
| **Phase 8** | Admin Panel & Deployment | ⏳ Upcoming |

---

## 🎨 Design System

MyBook uses a green-based color palette inspired by the original design:

```css
--green-dark:  #5aab00   /* Sidebar, buttons */
--green-mid:   #72c900   /* Hover states */
--green-light: #c8f060   /* Header bar */
--grade-green: #6cc000   /* High grades (7+) */
--grade-orange:#e07000   /* Medium grades (5–7) */
--grade-red:   #c83030   /* Low grades (<5) */
```

**Fonts:**
- `Bangers` — Headings & titles
- `Nunito` — Body text & UI

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📦 Dependencies

```
Django==5.0.1
Pillow==10.2.0
django-crispy-forms==2.1
crispy-bootstrap5==2024.2
python-dotenv==1.0.0
gunicorn==21.2.0          # Production server
whitenoise==6.6.0         # Static files in production
psycopg2-binary==2.9.9    # PostgreSQL adapter (production)
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🚢 Deployment (Railway / Render)

> Full deployment guide covered in **Phase 8** of the build series.

Quick steps:
1. Set `DEBUG=False` in `.env`
2. Add `ALLOWED_HOSTS=yourdomain.com`
3. Run `python manage.py collectstatic`
4. Use `gunicorn mybook.wsgi` as start command
5. Configure PostgreSQL database URL

---

## 👨‍💻 Author

**Sam** — AI & Automation Engineer
- GitHub: [@your-username](https://github.com/your-username)
- Project Repo: [edunest-lms](https://github.com/your-username/edunest-lms)

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)

---

<div align="center">
  <p>Built with ❤️ using Django & Python</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>

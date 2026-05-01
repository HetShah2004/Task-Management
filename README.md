# Task Management System

A robust and simple Task Management System built with Django and Django REST Framework. It features role-based access control, task assignment, status tracking, and an automated overdue indicator.

## 🚀 Features

- **Authentication**: Secure Login/Logout with JWT support for API requests.
- **Admin Managed Users**: User registration is restricted to administrators only.
- **Role-Based Access Control**:
  - **Admin/Manager**: Full access to view, create, and manage all tasks.
  - **User**: Can view tasks assigned to them and update their status (Pending, Ongoing, Completed).
- **Task Tracking**:
  - Assign tasks to specific team members.
  - Track progress through three states: `Pending`, `Ongoing`, and `Completed`.
  - Automated **Overdue** label for tasks past their due date.
- **Dashboard**: A clean, responsive web interface for managing daily tasks.
- **REST API**: Fully documented API endpoints for third-party integrations.

## 📂 Project Structure

```text
TaskManagement/
├── core/               # Project configuration and main views
│   ├── settings.py     # Main configuration (DB, Apps, Middleware)
│   ├── urls.py         # Main URL routing (Web & API)
│   ├── views.py        # Dashboard and Task action views
│   └── templates/      # HTML templates (Dashboard, Login, Base)
├── task/               # Task management application
│   ├── models.py       # Task model and Status choices
│   ├── serializers.py  # API serialization and validation logic
│   ├── permission.py   # Custom RBAC logic
│   └── views.py        # REST API ViewSets
├── users/              # User and Role management
│   ├── models.py       # Custom User model with Role field
│   ├── admin.py        # Optimized Admin panel configuration
│   └── views.py        # Authentication views
├── db.sqlite3          # SQLite Database
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd TaskManagement
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Web App: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## 🔑 Demo Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin |
| User | User | User@123 |

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT token pair |
| POST | `/api/token/refresh/` | Refresh JWT token |
| GET | `/api/tasks/` | List available tasks |
| POST | `/api/tasks/` | Create a new task (Admin/Manager) |
| PATCH | `/api/tasks/{id}/` | Update task status (Assigned User) |

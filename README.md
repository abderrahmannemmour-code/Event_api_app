# 🎯 Event Management System API

A professional REST API built with Django REST Framework for managing academic and professional events, paper submissions, and user registrations.

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-3.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.12-red.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [API Endpoints](#-api-endpoints)
- [Authentication](#-authentication)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Contributing](#-contributing)

## ✨ Features

### User Management
- 🔐 Token-based authentication
- 👤 User registration and profile management
- 🎭 Role-based access control (Participant, Author, Admin)

### Event Management
- 📅 Create and manage events with full CRUD operations
- 📍 Event details including location, dates, and descriptions
- 🏷️ Topic-based categorization and filtering
- 📆 Event schedules with day-by-day activities
- ✅ Event registration for participants

### Paper Submission System
- 📝 Submit papers with PDF uploads
- 📊 Paper status tracking (Submitted, Accepted, Rejected)
- 🏷️ Paper types: Oral, Poster, Workshop
- 👨‍💼 Admin review and status management

### Contact System
- 📧 Contact form submissions
- 💬 Message management

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Django 3.2** | Web Framework |
| **Django REST Framework** | API Development |
| **PostgreSQL 13** | Database |
| **Docker & Docker Compose** | Containerization |
| **drf-spectacular** | API Documentation (OpenAPI 3.0) |
| **Token Authentication** | Security |

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose installed
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Event_api_app
   ```

2. **Start the application with Docker**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - API: http://localhost:8000/api/
   - API Documentation: http://localhost:8000/api/docs/
   - Admin Panel: http://localhost:8000/admin/

### Create Superuser

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

## 📚 API Documentation

### Interactive Documentation (Swagger UI)
Access the interactive API documentation at:
```
http://localhost:8000/api/docs/
```

### OpenAPI Schema
Download the OpenAPI 3.0 schema at:
```
http://localhost:8000/api/schema/
```

## 🔗 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/user/create/` | Register new user |
| `POST` | `/api/user/token/` | Get authentication token |
| `GET/PUT` | `/api/user/me/` | Manage current user profile |

### Events
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/event/events/` | List all events |
| `POST` | `/api/event/events/` | Create new event (Admin) |
| `GET` | `/api/event/events/{id}/` | Get event details |
| `PUT/PATCH` | `/api/event/events/{id}/` | Update event (Admin) |
| `DELETE` | `/api/event/events/{id}/` | Delete event (Admin) |
| `POST` | `/api/event/events/{id}/register/` | Register for event |
| `DELETE` | `/api/event/events/{id}/cancel_registration/` | Cancel registration |

### Topics
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/event/topics/` | List all topics |
| `POST` | `/api/event/topics/` | Create topic (Admin) |
| `PUT/PATCH` | `/api/event/topics/{id}/` | Update topic (Admin) |
| `DELETE` | `/api/event/topics/{id}/` | Delete topic (Admin) |

### Papers
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/paper/{event_id}/papers/` | List papers for event |
| `POST` | `/api/paper/{event_id}/papers/` | Submit paper (Author) |
| `GET` | `/api/paper/{event_id}/papers/{id}/` | Get paper details |
| `PATCH` | `/api/paper/{event_id}/papers/{id}/set-status/` | Set paper status (Admin) |
| `POST` | `/api/paper/{event_id}/papers/{id}/upload-pdf/` | Upload PDF (Admin) |

### Contact
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/contact_us/` | Submit contact message |
| `GET` | `/api/contact_us/` | List messages (Admin) |

## 🔐 Authentication

This API uses **Token Authentication**. 

### Get Token
```bash
curl -X POST http://localhost:8000/api/user/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

### Use Token
Include the token in your request headers:
```bash
curl -X GET http://localhost:8000/api/user/me/ \
  -H "Authorization: Token your-token-here"
```

### User Roles

| Role | Permissions |
|------|-------------|
| **Participant** | Register for events, view content |
| **Author** | Submit papers, all participant permissions |
| **Admin** | Full access to all resources |

## 📁 Project Structure

```
Event_api_app/
├── app/
│   ├── app/              # Django project settings
│   │   ├── settings.py
│   │   └── urls.py
│   ├── core/             # Core models and admin
│   │   ├── models.py     # User, Event, Paper, Topic models
│   │   └── admin.py
│   ├── user/             # User authentication API
│   ├── event/            # Event management API
│   ├── paper/            # Paper submission API
│   └── contact_us/       # Contact form API
├── docs/                 # Additional documentation
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🧪 Testing

Run tests using Docker:

```bash
# Run all tests
docker-compose run --rm app sh -c "python manage.py test"

# Run specific app tests
docker-compose run --rm app sh -c "python manage.py test user"
docker-compose run --rm app sh -c "python manage.py test event"

# Run with coverage
docker-compose run --rm app sh -c "coverage run manage.py test && coverage report"
```

## 🔧 Development

### Code Linting
```bash
docker-compose run --rm app sh -c "flake8"
```

### Database Migrations
```bash
# Create migrations
docker-compose run --rm app sh -c "python manage.py makemigrations"

# Apply migrations
docker-compose run --rm app sh -c "python manage.py migrate"
```

## 🌐 Deployment

For production deployment, ensure you:

1. Set `DEBUG = False` in settings
2. Configure proper `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Set up proper database credentials
5. Configure static files serving
6. Use HTTPS

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Made with ❤️ using Django REST Framework**
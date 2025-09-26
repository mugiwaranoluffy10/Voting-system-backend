# Voting System Backend

A Django REST API for a voting system with user authentication, nominations, and business rule-based voting.

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/voting-system-backend.git
   cd voting-system-backend
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\Activate.ps1
   # Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - API: http://127.0.0.1:8000/api/
   - Admin: http://127.0.0.1:8000/admin/

## Features

- User registration and JWT authentication
- Category-based user profiles
- Nomination system with approval workflow
- Voting system with business rules
- Admin panel for system management

## API Endpoints

- `POST /api/auth/register/` - User registration
- `POST /api/auth/token/` - Login
- `GET /api/categories/` - List categories
- `GET /api/nominations/` - List nominations
- `POST /api/vote/` - Cast vote

## Business Rules

- Service Providers and Designers cannot vote
- Manufacturers can only vote for Designers and Service Providers
- Retailers cannot vote for other Retailers
- Users cannot vote for the same candidate twice
- Only users with approved nominations can receive votes

## Technology Stack

- Django 5.2.6
- Django REST Framework
- JWT Authentication
- SQLite (development)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
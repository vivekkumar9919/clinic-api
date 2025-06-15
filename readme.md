
# Clinic API

## 📝 Summary
This is a Django REST Framework-based API for managing doctors and appointments in a clinic system. It includes features like pagination, filtering, error handling, and seed data setup.

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vivekkumar9919/clinic-api
cd clinic-api
```

### 2. Create a Virtual Environment and Activate It
```bash
python -m venv env
source env/bin/activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed Initial Data
```bash
python manage.py seed
```

### 6. Run Server
```bash
python manage.py runserver
```

---

## 🗃️ Database Creation
Django handles DB creation using migrations. Just ensure your database is configured in `settings.py` and run:

```bash
python manage.py migrate
```

---

## 📁 Folder Structure

- `api/constants.py` – Constants like default page size, max page size, etc.
- `api/exception_handler.py` – Custom exception handler for unified error response format.
- `api/models.py` – Models for `Doctor` and `Appointment`.
- `api/pagination.py` – Custom pagination class supporting dynamic page and size.
- `api/serializers.py` – Serializers for models with validation and custom fields.
- `api/urls.py` – API route definitions.
- `api/views.py` – Views for handling GET and POST requests with filtering and pagination.
- `api/utils/response_utils.py` – Helper function for standard JSON responses.
- `api/management/commands/seed.py` – Command to seed sample doctors and appointments.
- `requirements.txt` – All Python dependencies for the project.

---

## 🌟 Features

- Add and retrieve appointments.
- Filter appointments by doctor and date.
- Paginate results with page and page_size query params.
- Add and list doctors.
- Custom exception handler returning consistent error structure.
- Custom response format for both success and failure.
- Seed data using a custom Django management command.
- Simple and scalable project layout.

---
## 🔗 API Endpoints

| Method | Endpoint             | Description                         |
|--------|----------------------|-------------------------------------|
| GET    | `/api/doctors/`      | List doctors (paginated)            |
| GET    | `/api/appointments/` | List appointments with filters      |
| POST   | `/api/appointments/` | Create a new appointment            |

---

### 📌 Query Parameters for `/api/appointments/`

You can filter and paginate appointments using the following query parameters:

| Parameter   | Type   | Description                        |
|-------------|--------|------------------------------------|
| `doctor`    | int    | Doctor ID to filter appointments   |
| `date`      | string | Appointment date in `YYYY-MM-DD`   |
| `page`      | int    | Page number (for pagination)       |
| `page_size` | int    | Number of items per page (max limit set in code) |

---

### 📤 Request Body for `POST /api/appointments/`

Use the following JSON format to create a new appointment:

```json
{
  "patient_name": "Vivek",
  "doctor": 1,
  "date": "2025-06-15",
  "time_slot": "1:30:00",
  "status": "Scheduled"
}

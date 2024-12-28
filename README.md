# Form Builder Application

 **POSTMAN COLLECTION** : https://documenter.getpostman.com/view/37271849/2sAYJ6CzZD

This project is a Django-based Form Builder application inspired by Google Forms. It allows administrators to create forms, users to submit responses, and provides analytics for form responses.

---

## Features

### Admin Features
- Create unlimited forms.
- Add up to 100 questions per form.
- Define question types: Text, Dropdown, or Checkbox.
- Configure questions with relevant options.
- View a list of all created forms.

### End User Features
- Submit responses to forms anonymously.
- Submit responses multiple times.

### Shared Features
- View analytics at a public URL:
  - Total response count for each form.
  - Question-specific analytics:
    - Text Field: Top 5 most common words.
    - Checkbox: Top 5 option combinations.
    - Dropdown: Top 5 selected options.

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 4.x
- Django REST Framework
- SQLite (or another database of your choice)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd form-builder
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API root: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

### Create a Superuser
To manage forms via the Django Admin interface, create a superuser:
```bash
python manage.py createsuperuser
```

---

## Usage Guide

### Admin APIs

1. **Create a Form**:
   - **Endpoint**: `POST /api/forms/`
   - **Request Body**:
     ```json
     {
       "title": "Customer Feedback Form",
       "description": "Form to collect customer feedback",
       "questions": [
         {
           "text": "What is your name?",
           "question_type": "text",
           "options": null
         },
         {
           "text": "What is your gender?",
           "question_type": "dropdown",
           "options": ["Male", "Female", "Other"]
         }
       ]
     }
     ```

2. **View All Forms**:
   - **Endpoint**: `GET /api/forms/`

3. **View Form Details**:
   - **Endpoint**: `GET /api/forms/<form_id>/`

4. **Delete a Form**:
   - **Endpoint**: `DELETE /api/forms/<form_id>/`

### End User APIs

1. **Submit a Response**:
   - **Endpoint**: `POST /api/forms/<form_id>/responses/`
   - **Request Body**:
     ```json
     {
       "responses": {
         "What is your name?": "John Doe",
         "What is your gender?": "Male"
       }
     }
     ```

2. **View Form Analytics**:
   - **Endpoint**: `GET /api/forms/<form_id>/analytics/`

---

## Project Structure

```
form_builder/
|-- FormApp/
|   |-- migrations/
|   |-- templates/
|   |-- admin.py        # Admin configurations
|   |-- models.py       # Database models
|   |-- serializers.py  # API serializers
|   |-- views.py        # API views
|   |-- urls.py         # Application routes
|-- form_builder/
|   |-- settings.py     # Django settings
|   |-- urls.py         # Project routes
|-- manage.py           # Django management script
|-- requirements.txt    # Dependencies
```

---

## Testing APIs

1. **Using Postman**:
   - Import the API details into Postman.
   - Set the base URL to `http://127.0.0.1:8000/api/`.

2. **Using `curl`**:
   Example request:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/forms/ -H "Content-Type: application/json" -d '{"title": "Survey", "description": "Sample survey", "questions": [{"text": "What is your name?", "question_type": "text"}]}'
   ```

---

## Future Enhancements
- Add authentication for Admin users.
- Allow users to edit and delete responses.
- Introduce additional question types (e.g., rating scale, file upload).
- Support export of analytics as CSV/Excel files.


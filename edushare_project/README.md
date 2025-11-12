# EduShare

EduShare is an Educational Resource Exchange Platform built with Django and JavaScript.
The platform allows teachers and students to upload, share, and discover learning materials,
such as lesson plans, worksheets, slides, and small classroom activities. The focus is on
collaborative sharing and reusing educational content — not buying and selling.

## Distinctiveness and Complexity

EduShare is intentionally distinct from standard course projects like social networks or e-commerce sites.
Unlike a social network, the application centers on **structured resource sharing** rather than interpersonal social
feeds, follows, or profile-driven networks. Unlike an e-commerce store, there are no transactional purchase
flows, shopping carts, or payment integrations; the purpose is redistribution of educational materials to
support learning and reduce waste.

The project demonstrates complexity in several technical areas:
- **Relational data modelling:** multiple Django models represent `Subject`, `GradeLevel`, `Resource`, and `Comment`.
  These models capture real relationships (foreign keys, related names) and allow rich queries and filtering.
- **File and image handling:** resources can include uploaded files and preview images, stored via Django's
  `FileField`/`ImageField`. This requires correct static/media configuration and forms handling.
- **AJAX-driven frontend:** the search and filter UI uses JavaScript Fetch API to query the server asynchronously,
  returning JSON and rendering results without a full page reload.
- **Mobile-responsive design:** the UI uses Bootstrap and responsive CSS to ensure usability on phones and tablets.
- **Security and authentication:** posting resources and comments requires login (built on Django's auth).
These elements together provide depth beyond basic CRUD and demonstrate a real-world application design.

## Files and What They Contain

- `manage.py` – Django management entrypoint.
- `edushare/` – Project settings and WSGI configuration (`settings.py` is pre-configured for PostgreSQL with environment variable support).
- `main/` – Primary application:
  - `models.py` – Django models: Subject, GradeLevel, Resource, Comment.
  - `views.py` – Views for index, resource detail, add resource, and an AJAX search API.
  - `forms.py` – Forms for Resource uploads and Comments.
  - `urls.py` – App URL routes.
  - `admin.py` – Admin registration for models.
- `templates/` – HTML templates (base layout, index, resource detail, add resource).
- `static/` – Static assets: `css/styles.css` and `js/main.js` (AJAX search).
- `requirements.txt` – Python package list needed to run the app.
- `README.md` – This documentation.

## How to run (development)

1. Clone or unzip this project.
2. Create a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure PostgreSQL:
   - Create a database and user (example names used in `edushare/settings.py`).
   - Alternatively, set environment variables: `EDUSHARE_DB_NAME`, `EDUSHARE_DB_USER`, `EDUSHARE_DB_PASS`, `EDUSHARE_DB_HOST`, `EDUSHARE_DB_PORT`.
5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```
7. (Optional) Collect static files / ensure MEDIA directories exist.
8. Run the server:
   ```bash
   python manage.py runserver
   ```
9. Visit `http://127.0.0.1:8000/`.

## Additional notes

- For quick testing without PostgreSQL, you may temporarily change `DATABASES` in `edushare/settings.py` to the default SQLite configuration.
- If you intend to deploy, remember to set `DEBUG=False`, configure `ALLOWED_HOSTS`, and secure `SECRET_KEY`.
- This scaffold provides a complete starting point. You should customize subjects and grade levels via the admin, and expand features (tagging, ratings, tagging, messaging) as needed for your final submission.


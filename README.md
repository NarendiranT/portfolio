# Developer Portfolio

A decoupled developer portfolio with a **Vue 3** frontend and **Django REST** backend. Manage projects and blog posts through Django Admin with a rich text editor.

## Stack

- **Frontend:** Vue 3, Vite, TypeScript, Vue Router, Tailwind CSS, Axios
- **Backend:** Django, Django REST Framework, django-ckeditor-5, SQLite
- **Admin:** Django Admin at `/admin/` for content management

## Project Structure

```
portfolio/
├── backend/     # Django API + Admin
└── frontend/    # Vue 3 SPA
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+

### Backend

```bash
cd portfolio/backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo     # optional: load sample data
python manage.py runserver
```

Backend runs at **http://localhost:8000**

- Admin panel: http://localhost:8000/admin/
- API endpoints:
  - `GET /api/profile/`
  - `GET /api/projects/`
  - `GET /api/projects/{slug}/`
  - `GET /api/blog/`
  - `GET /api/blog/{slug}/`

### Frontend

```bash
cd portfolio/frontend
npm install
npm run dev
```

Frontend runs at **http://localhost:5173**

## Environment Variables

**Backend** (`backend/.env`):

```
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ORIGIN=http://localhost:5173
```

**Frontend** (`frontend/.env`):

```
VITE_API_URL=http://localhost:8000
```

## Managing Content

1. Log in to Django Admin at http://localhost:8000/admin/
2. Add or edit **Projects**, **Blog posts**, and **Profile**
3. Use the rich text editor for full project write-ups and blog content
4. Set `published=True` to make content visible on the public site
5. Mark projects as `featured` to show them on the homepage

## Pages

| Route | Description |
|---|---|
| `/` | Homepage with hero, featured projects, recent blog posts |
| `/projects` | All projects grid |
| `/projects/:slug` | Project detail |
| `/blog` | Blog listing |
| `/blog/:slug` | Blog post detail |
| `/about` | Developer profile, bio, skills |

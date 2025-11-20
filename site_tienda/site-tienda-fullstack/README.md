# site-tienda-fullstack

This project is a full-stack application consisting of a Django backend and an Angular frontend.

## Project Structure

```
site-tienda-fullstack
├── frontend          # Angular frontend application
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   ├── tsconfig.app.json
│   ├── tsconfig.spec.json
│   ├── .eslintrc.json
│   └── src
│       ├── index.html
│       ├── main.ts
│       ├── polyfills.ts
│       ├── styles.scss
│       ├── assets
│       └── app
│           ├── app.module.ts
│           ├── app.component.ts
│           ├── app.component.html
│           ├── app-routing.module.ts
│           ├── components
│           │   └── home
│           │       ├── home.component.ts
│           │       └── home.component.html
│           └── services
│               └── api.service.ts
├── backend           # Django backend application
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env
│   ├── site_tienda
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   └── my_apps
│       ├── __init__.py
│       ├── category
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── serializers.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── tests.py
│       └── product
│           ├── __init__.py
│           ├── models.py
│           ├── views.py
│           └── serializers.py
└── .gitignore
```

## Getting Started

### Prerequisites

- Node.js and npm for the Angular frontend
- Python and pip for the Django backend

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Start the Angular development server:
   ```
   ng serve
   ```

### Backend Setup

1. Navigate to the `backend` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the Django development server:
   ```
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License.
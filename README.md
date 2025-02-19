# Django React JWT Authentication with PostgreSQL

A complete authentication and order management system using Django REST Framework for the backend and React for the frontend. It features JWT authentication with secure HttpOnly cookie-based storage and PostgreSQL as the database.

## Features

- JWT authentication with secure httpOnly cookie storage
- PostgreSQL database integration
- Automatic token refresh
- Role-based user authentication
- Material-UI user interface
- Protected routes in both frontend and backend
- Scalable system architecture
- CORS configured for local development
- API endpoints for order management, inventory, logistics, and users

## Using this Template

To use this project as a starting point for your own application:

1. Clone the repository:
```bash
git clone https://github.com/juliomeza/django-react-postgres.git your-project-name
```

2. Move into your project directory:
```bash
cd your-project-name
```

3. Remove the existing git repository and initialize a new one:
```bash
rm -rf .git
git init
```

## Backend Setup

1. Create and activate a virtual environment:
```bash
cd server
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure PostgreSQL database in `settings.py`:

Before proceeding, ensure you have created a PostgreSQL database and a user with appropriate permissions. Avoid using special characters like `@` in the password, as they may cause connection issues.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

To create a PostgreSQL database and user, you can use the following commands:
```sql
CREATE DATABASE your_database_name;
CREATE USER your_database_user WITH PASSWORD 'your_secure_password';
ALTER ROLE your_database_user SET client_encoding TO 'utf8';
ALTER ROLE your_database_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_database_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

## Frontend Setup

1. Install dependencies:
```bash
cd client
npm install
```

2. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

The backend provides a set of API endpoints for managing different modules. Below are some key API routes:

- **Authentication:**
  - `POST /api/auth/login/` - Login user and return JWT tokens
  - `POST /api/auth/refresh/` - Refresh JWT token
  - `POST /api/auth/logout/` - Logout user and clear tokens

- **Users & Roles:**
  - `GET /api/users/` - List all users
  - `POST /api/users/` - Create a new user
  - `GET /api/roles/` - List available roles

- **Enterprise & Clients:**
  - `GET /api/enterprises/` - List enterprises
  - `GET /api/owners/` - List clients
  - `GET /api/projects/` - List projects

- **Orders & Inventory:**
  - `GET /api/orders/` - List orders
  - `POST /api/orders/` - Create a new order
  - `GET /api/inventories/` - List inventory items

- **Logistics:**
  - `GET /api/warehouses/` - List warehouses
  - `GET /api/addresses/` - List addresses
  - `GET /api/carriers/` - List carriers

## Security Features

- JWT tokens stored in HttpOnly cookies
- CSRF protection
- Specific CORS configuration
- Secure session handling
- Automatic token refresh handling

## Database Tables

The application includes several models that structure the database:

- **Users:** Custom user model with roles and permissions.
- **Enterprise & Clients:** Enterprises, clients, and projects linked to users.
- **Orders:** Orders, order lines, and order statuses.
- **Inventory:** Inventory records with serial numbers and tracking information.
- **Logistics:** Warehouses, carriers, and addresses.
- **Materials:** Materials, material types, and unit of measure (UOM).

## License

Distributed under the MIT License. See `LICENSE` for more information.


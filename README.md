# Django React JWT Authentication

A complete authentication system implementation using Django REST Framework for the backend and React for the frontend, featuring JWT authentication with secure cookie-based storage.

## Features

- JWT authentication with secure httpOnly cookie storage
- Automatic token refresh
- Material-UI user interface
- Protected routes in both frontend and backend
- Persistent session handling
- Scalable system architecture
- CORS configured for local development

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

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Start the development server:
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

## Usage

1. Access `http://localhost:3000`
2. The application will automatically redirect to the login page
3. Use the superuser credentials created during backend setup
4. Once authenticated, you'll be redirected to the secure page

## Security Features

The system implements several security measures:
- JWT tokens stored in httpOnly cookies
- CSRF protection
- Specific CORS configuration
- Secure session handling
- Automatic token refresh handling

## Development

To contribute to the project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

[Your Name] - [your@email.com]

Project Link: [https://github.com/yourusername/project]
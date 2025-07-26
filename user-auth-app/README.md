# User Authentication Web Application

A complete full-stack web application featuring user registration and authentication with React frontend, Python Flask backend, and MySQL database.

## Features

- **User Registration (Sign Up)**: Create new user accounts with username, email, and password
- **User Authentication (Login)**: Secure login with JWT token-based authentication
- **Protected Dashboard**: Authenticated users can access a personalized dashboard
- **Responsive Design**: Modern, mobile-friendly UI with beautiful styling
- **Password Security**: Passwords are hashed using bcrypt before storage
- **Form Validation**: Client-side and server-side validation for all forms
- **Session Management**: Automatic token handling and logout functionality

## Technology Stack

### Frontend
- **React 18** with functional components and hooks
- **React Router DOM** for client-side routing
- **Axios** for HTTP requests
- **Modern CSS** with responsive design

### Backend
- **Python Flask** web framework
- **Flask-Bcrypt** for password hashing
- **PyJWT** for JSON Web Token authentication
- **Flask-CORS** for cross-origin requests
- **MySQL Connector** for database connectivity

### Database
- **MySQL** for data persistence
- User table with proper constraints and indexing

## Project Structure

```
user-auth-app/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── setup_database.py      # Database setup script
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   └── venv/                  # Python virtual environment
└── frontend/
    ├── public/                # Static files
    ├── src/
    │   ├── components/
    │   │   ├── Login.js       # Login component
    │   │   ├── SignUp.js      # Registration component
    │   │   ├── Dashboard.js   # Protected dashboard
    │   │   ├── PrivateRoute.js # Route protection
    │   │   ├── Auth.css       # Authentication styles
    │   │   └── Dashboard.css  # Dashboard styles
    │   ├── services/
    │   │   └── api.js         # API service layer
    │   ├── App.js             # Main React component
    │   └── App.css            # Global styles
    ├── package.json           # Node.js dependencies
    └── package-lock.json
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- MySQL 8.0+

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd user-auth-app/backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database:**
   ```bash
   # Start MySQL service
   sudo service mysql start
   
   # Create database and user
   sudo mysql -u root -p
   ```
   
   Then run these SQL commands:
   ```sql
   CREATE DATABASE user_auth_db;
   CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON user_auth_db.* TO 'auth_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

5. **Configure environment variables:**
   Update the `.env` file with your database credentials:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=password
   DB_NAME=user_auth_db
   JWT_SECRET_KEY=your_jwt_secret_key_here_change_in_production
   ```

6. **Run the Flask application:**
   ```bash
   python app.py
   ```
   The backend will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd user-auth-app/frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```
   The frontend will run on `http://localhost:3000`

## Usage

1. **Access the application** by opening `http://localhost:3000` in your browser

2. **Create a new account:**
   - Click "Sign Up" or navigate to `/signup`
   - Fill in username, email, and password
   - Submit the form to create your account

3. **Login to your account:**
   - Navigate to `/login` (default page)
   - Enter your email and password
   - Successfully login to access the dashboard

4. **Dashboard features:**
   - View your profile information
   - Access protected content
   - Logout to end your session

## API Endpoints

### Authentication Routes
- `POST /api/signup` - Register a new user
- `POST /api/login` - Authenticate user and get JWT token
- `GET /api/dashboard` - Get user dashboard data (protected)

### Request/Response Examples

**Sign Up:**
```json
POST /api/signup
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Login:**
```json
POST /api/login
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

## Security Features

- **Password Hashing**: All passwords are hashed using bcrypt before storage
- **JWT Authentication**: Secure token-based authentication system
- **Input Validation**: Both client-side and server-side validation
- **CORS Protection**: Configured to allow requests only from the frontend
- **SQL Injection Prevention**: Using parameterized queries
- **XSS Protection**: Input sanitization and validation

## Development

### Running Tests
```bash
# Backend tests (if implemented)
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production
```bash
# Build React app
cd frontend
npm run build

# The build files will be in the `build/` directory
```

## Troubleshooting

### Common Issues

1. **Database Connection Error:**
   - Ensure MySQL service is running
   - Check database credentials in `.env` file
   - Verify database and user exist

2. **CORS Error:**
   - Ensure Flask-CORS is installed and configured
   - Check that backend is running on port 5000

3. **JWT Token Issues:**
   - Clear localStorage and login again
   - Check JWT secret key configuration

4. **Port Already in Use:**
   - Change ports in the configuration files
   - Kill existing processes using the ports

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please create an issue in the repository or contact the development team.
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import re

# Load environment variables
load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'autocommit': True,
    'raise_on_warnings': True
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_users_table():
    """Create the users table if it doesn't exist"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                email VARCHAR(120) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Users table created successfully")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password (minimum 6 characters)"""
    return len(password) >= 6

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or not all(key in data for key in ['username', 'email', 'password']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        username = data['username'].strip()
        email = data['email'].strip().lower()
        password = data['password']
        
        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400
        
        if not validate_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        
        if not validate_password(password):
            return jsonify({'error': 'Password must be at least 6 characters long'}), 400
        
        # Hash password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Connect to database
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        try:
            cursor = connection.cursor()
            
            # Check if user already exists
            check_query = "SELECT id FROM users WHERE username = %s OR email = %s"
            cursor.execute(check_query, (username, email))
            existing_user = cursor.fetchone()
            
            if existing_user:
                # Check which field already exists
                check_username_query = "SELECT id FROM users WHERE username = %s"
                cursor.execute(check_username_query, (username,))
                if cursor.fetchone():
                    return jsonify({'error': 'Username already exists'}), 400
                else:
                    return jsonify({'error': 'Email already exists'}), 400
            
            # Insert new user
            insert_query = """
            INSERT INTO users (username, email, password_hash) 
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (username, email, password_hash))
            connection.commit()
            
            return jsonify({'message': 'Registration successful!'}), 201
            
        except Error as e:
            print(f"Database error: {e}")
            return jsonify({'error': 'Database error occurred'}), 500
        finally:
            cursor.close()
            connection.close()
            
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or not all(key in data for key in ['email', 'password']):
            return jsonify({'error': 'Missing email or password'}), 400
        
        email = data['email'].strip().lower()
        password = data['password']
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Connect to database
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        try:
            cursor = connection.cursor()
            
            # Find user by email
            query = "SELECT id, username, email, password_hash FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            
            if not user or not bcrypt.check_password_hash(user[3], password):
                return jsonify({'error': 'Invalid email or password'}), 401
            
            # Generate JWT token
            payload = {
                'user_id': user[0],
                'username': user[1],
                'email': user[2],
                'exp': datetime.utcnow() + timedelta(days=1)  # Token expires in 1 day
            }
            
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            
            return jsonify({
                'message': 'Login successful',
                'token': token,
                'user': {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2]
                }
            }), 200
            
        except Error as e:
            print(f"Database error: {e}")
            return jsonify({'error': 'Database error occurred'}), 500
        finally:
            cursor.close()
            connection.close()
            
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    try:
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid authorization header'}), 401
        
        token = auth_header.split(' ')[1]
        
        try:
            # Decode and verify token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['user_id']
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        # Connect to database
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        try:
            cursor = connection.cursor()
            
            # Get user data
            query = "SELECT id, username, email, created_at FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            
            if not user:
                return jsonify({'error': 'User not found'}), 404
            
            return jsonify({
                'message': 'Dashboard data retrieved successfully',
                'user': {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'created_at': user[3].isoformat() if user[3] else None
                }
            }), 200
            
        except Error as e:
            print(f"Database error: {e}")
            return jsonify({'error': 'Database error occurred'}), 500
        finally:
            cursor.close()
            connection.close()
            
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    # Create database table on startup
    create_users_table()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
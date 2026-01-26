# Cat Emotion Detection Backend

A FastAPI-based backend for detecting cat emotions from image and/or audio inputs.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite
- **Authentication**: JWT Token-based authentication
- **Password Hashing**: bcrypt

## Project Structure

```
cat-emotion-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection and setup
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # User database models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py          # Pydantic schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   └── auth.py          # Authentication routes
│   └── utils/
│       ├── __init__.py
│       ├── auth.py          # Authentication utilities
│       └── security.py     # Security utilities
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy environment template
copy .env.example .env

# Edit .env file with your configuration
```

### 4. Run the Server

```bash
# Option 1: Using the convenience script
python start_server.py

# Option 2: Direct uvicorn command
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 5. Test the Setup

```bash
# Make sure server is running, then in another terminal:
python test_setup.py
```

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/register` | User registration | No |
| POST | `/auth/login` | User login | No |
| POST | `/auth/logout` | User logout | Yes |
| GET | `/auth/me` | Get current user info | Yes |

### General Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/` | API root/health check | No |
| GET | `/health` | Health check | No |

## API Documentation & Testing

### 1. User Registration

**Endpoint**: `POST /auth/register`
**Authentication**: Not required

**Request Body**:
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "is_active": true,
  "created_at": "2024-01-26T10:30:00.000Z"
}
```

**Error Responses**:
- 400: Email already registered or username taken

### 2. User Login

**Endpoint**: `POST /auth/login`
**Authentication**: Not required

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Error Responses**:
- 401: Incorrect email or password
- 400: Inactive user

### 3. User Logout

**Endpoint**: `POST /auth/logout`
**Authentication**: Required (Bearer token)

**Headers**:
```
Authorization: Bearer <your_jwt_token>
```

**Response** (200 OK):
```json
{
  "message": "User user@example.com logged out successfully"
}
```

### 4. Get Current User

**Endpoint**: `GET /auth/me`
**Authentication**: Required (Bearer token)

**Headers**:
```
Authorization: Bearer <your_jwt_token>
```

**Response** (200 OK):
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "is_active": true,
  "created_at": "2024-01-26T10:30:00.000Z"
}
```

## Postman Testing

### Setup
1. Create a new Postman collection named "Cat Emotion Detection API"
2. Set base URL variable: `{{base_url}}` = `http://localhost:8000`

### Test Sequence

#### 1. Register User
- **Method**: POST
- **URL**: `{{base_url}}/auth/register`
- **Body** (JSON):
```json
{
  "email": "test@example.com",
  "username": "testuser",
  "password": "testpassword123"
}
```

#### 2. Login User
- **Method**: POST
- **URL**: `{{base_url}}/auth/login`
- **Body** (JSON):
```json
{
  "email": "test@example.com",
  "password": "testpassword123"
}
```
- **Test Script** (save token):
```javascript
if (pm.response.code === 200) {
    const response = pm.response.json();
    pm.environment.set("jwt_token", response.access_token);
}
```

#### 3. Get Current User
- **Method**: GET
- **URL**: `{{base_url}}/auth/me`
- **Headers**: 
  - `Authorization`: `Bearer {{jwt_token}}`

#### 4. Logout User
- **Method**: POST
- **URL**: `{{base_url}}/auth/logout`
- **Headers**: 
  - `Authorization`: `Bearer {{jwt_token}}`

## Features Implemented

- ✅ User Registration
- ✅ User Login  
- ✅ User Logout
- ✅ JWT Token Authentication
- ✅ Password Hashing
- ✅ Protected Routes
- ✅ SQLite Database
- ✅ API Documentation

## Development Status

**Current Stage**: Authentication System Complete
**Next Stage**: Cat emotion detection endpoints
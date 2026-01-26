#!/usr/bin/env python3
"""
Simple test script to verify the FastAPI setup works correctly.
Run this after installing dependencies to test the basic functionality.
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint."""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on localhost:8000")
        return False

def test_user_registration():
    """Test user registration."""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        if response.status_code == 201:
            print("✅ User registration passed")
            return True, response.json()
        else:
            print(f"❌ User registration failed: {response.status_code} - {response.text}")
            return False, None
    except Exception as e:
        print(f"❌ User registration error: {e}")
        return False, None

def test_user_login():
    """Test user login."""
    login_data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        if response.status_code == 200:
            print("✅ User login passed")
            return True, response.json()
        else:
            print(f"❌ User login failed: {response.status_code} - {response.text}")
            return False, None
    except Exception as e:
        print(f"❌ User login error: {e}")
        return False, None

def main():
    """Run all tests."""
    print("🧪 Testing Cat Emotion Detection API Setup...")
    print("=" * 50)
    
    # Test health check
    if not test_health_check():
        print("\n❌ Server is not running. Please start it with:")
        print("uvicorn app.main:app --reload")
        sys.exit(1)
    
    # Test registration
    reg_success, user_data = test_user_registration()
    if not reg_success:
        sys.exit(1)
    
    # Test login
    login_success, token_data = test_user_login()
    if not login_success:
        sys.exit(1)
    
    print("\n🎉 All tests passed! Your Cat Emotion Detection API is working correctly.")
    print(f"📝 User created: {user_data['email']}")
    print(f"🔑 Token received: {token_data['access_token'][:20]}...")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import requests
import json
import time

def test_backend():
    """Test the backend API endpoints"""
    print("🔄 Testing Backend API...")
    
    base_url = "http://localhost:5000/api"
    
    # Test data
    test_user = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        # Test signup
        print("📝 Testing user registration...")
        signup_response = requests.post(f"{base_url}/signup", json=test_user)
        print(f"   Signup Status: {signup_response.status_code}")
        
        if signup_response.status_code == 201:
            print("   ✅ User registration successful!")
        elif signup_response.status_code == 400:
            response_data = signup_response.json()
            if "already exists" in response_data.get('error', ''):
                print("   ⚠️  User already exists (this is expected if running multiple times)")
            else:
                print(f"   ❌ Registration failed: {response_data}")
        else:
            print(f"   ❌ Unexpected response: {signup_response.text}")
        
        # Test login
        print("🔐 Testing user login...")
        login_data = {
            "email": test_user["email"],
            "password": test_user["password"]
        }
        
        login_response = requests.post(f"{base_url}/login", json=login_data)
        print(f"   Login Status: {login_response.status_code}")
        
        if login_response.status_code == 200:
            response_data = login_response.json()
            token = response_data.get('token')
            user_info = response_data.get('user')
            print("   ✅ Login successful!")
            print(f"   👤 User: {user_info.get('username')} ({user_info.get('email')})")
            
            # Test dashboard access
            print("🏠 Testing dashboard access...")
            headers = {"Authorization": f"Bearer {token}"}
            dashboard_response = requests.get(f"{base_url}/dashboard", headers=headers)
            
            if dashboard_response.status_code == 200:
                print("   ✅ Dashboard access successful!")
                dashboard_data = dashboard_response.json()
                print(f"   📊 Dashboard data: {dashboard_data}")
            else:
                print(f"   ❌ Dashboard access failed: {dashboard_response.status_code}")
        else:
            print(f"   ❌ Login failed: {login_response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Backend server is not running on localhost:5000")
        return False
    except Exception as e:
        print(f"   ❌ Error testing backend: {e}")
        return False
    
    return True

def test_frontend():
    """Test if the frontend is accessible"""
    print("🔄 Testing Frontend...")
    
    try:
        response = requests.get("http://localhost:3000")
        if response.status_code == 200:
            print("   ✅ Frontend is accessible!")
            print(f"   📄 Content length: {len(response.text)} characters")
            return True
        else:
            print(f"   ❌ Frontend returned status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Frontend server is not running on localhost:3000")
        return False
    except Exception as e:
        print(f"   ❌ Error testing frontend: {e}")
        return False

def main():
    print("🚀 Full Stack Application Test")
    print("=" * 40)
    
    # Wait a moment for servers to start
    print("⏳ Waiting for servers to start...")
    time.sleep(3)
    
    frontend_ok = test_frontend()
    backend_ok = test_backend()
    
    print("\n" + "=" * 40)
    print("📋 Test Summary:")
    print(f"   Frontend: {'✅ WORKING' if frontend_ok else '❌ FAILED'}")
    print(f"   Backend:  {'✅ WORKING' if backend_ok else '❌ FAILED'}")
    
    if frontend_ok and backend_ok:
        print("\n🎉 Application is fully functional!")
        print("📝 Next steps:")
        print("   1. Open http://localhost:3000 in your browser")
        print("   2. Try registering a new account")
        print("   3. Login with your credentials")
        print("   4. Access the dashboard")
    else:
        print("\n⚠️  Some components are not working properly.")
        print("   Check the server logs for more details.")

if __name__ == "__main__":
    main()
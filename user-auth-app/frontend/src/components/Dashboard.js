import React, { useState, useEffect } from 'react';
import { useAuth } from '../App';
import { authAPI } from '../services/api';
import './Dashboard.css';

const Dashboard = () => {
  const { currentUser, logout } = useAuth();
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await authAPI.getDashboard();
      setUserData(response.user);
    } catch (error) {
      setError(error.error || 'Failed to load dashboard data');
      console.error('Dashboard error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    if (window.confirm('Are you sure you want to logout?')) {
      logout();
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="dashboard-container">
        <div className="loading">
          <div className="loading-spinner"></div>
          <p>Loading dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <div className="header-content">
          <h1 className="dashboard-title">
            Welcome, {currentUser?.username || userData?.username}! 👋
          </h1>
          <button onClick={handleLogout} className="logout-button">
            Logout
          </button>
        </div>
      </div>

      <div className="dashboard-content">
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <div className="dashboard-card">
          <h2 className="card-title">Your Profile Information</h2>
          <div className="profile-info">
            <div className="info-item">
              <span className="info-label">User ID:</span>
              <span className="info-value">{currentUser?.id || userData?.id}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Username:</span>
              <span className="info-value">{currentUser?.username || userData?.username}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Email:</span>
              <span className="info-value">{currentUser?.email || userData?.email}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Member Since:</span>
              <span className="info-value">
                {formatDate(userData?.created_at)}
              </span>
            </div>
          </div>
        </div>

        <div className="dashboard-card">
          <h2 className="card-title">Dashboard Features</h2>
          <div className="features-grid">
            <div className="feature-item">
              <div className="feature-icon">🔐</div>
              <h3>Secure Authentication</h3>
              <p>Your account is protected with JWT token-based authentication</p>
            </div>
            <div className="feature-item">
              <div className="feature-icon">👤</div>
              <h3>User Profile</h3>
              <p>View and manage your personal information</p>
            </div>
            <div className="feature-item">
              <div className="feature-icon">🚀</div>
              <h3>Modern Interface</h3>
              <p>Built with React and modern web technologies</p>
            </div>
            <div className="feature-item">
              <div className="feature-icon">🔒</div>
              <h3>Protected Routes</h3>
              <p>Access control ensures only authenticated users can view this page</p>
            </div>
          </div>
        </div>

        <div className="dashboard-card">
          <h2 className="card-title">Quick Actions</h2>
          <div className="actions-grid">
            <button className="action-button primary">
              Update Profile
            </button>
            <button className="action-button secondary">
              Change Password
            </button>
            <button className="action-button secondary">
              Account Settings
            </button>
            <button onClick={handleLogout} className="action-button danger">
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../App';

const PrivateRoute = ({ children }) => {
  const { currentUser, loading } = useAuth();

  if (loading) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        fontSize: '18px',
        color: '#666'
      }}>
        Loading...
      </div>
    );
  }

  return currentUser ? children : <Navigate to="/login" replace />;
};

export default PrivateRoute;
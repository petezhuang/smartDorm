// components/ProtectedRoute.tsx
import { Navigate } from 'react-router-dom';
import { message } from 'antd';
import { useEffect } from 'react';
import { useState } from 'react';

const ProtectedRoute = ({ children }: { children }) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    if (!isLoggedIn) {
      const timer = setTimeout(() => {
        setRedirect(true);
      }, 1500);
      return () => clearTimeout(timer);
    }
  }, [isLoggedIn]);

  if (!isLoggedIn) {
    //  页面保持挂载
    return redirect ? <Navigate to="/" replace /> : <div style={{display:'flex',alignItems:'center',justifyContent:'center'}}>未登录，即将跳转到登录页...</div>;
  }

  return children;
};

export default ProtectedRoute;

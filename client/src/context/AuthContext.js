import { createContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api, { setupInterceptors } from '../services/apiService';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  const checkAuthStatus = async () => {
    try {
      const response = await api.get('auth-status/');
      setUser(response.data.user ? response.data.user : null);
    } catch (error) {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkAuthStatus();
  }, []);

  // Configuramos el interceptor de api con el navigate
  useEffect(() => {
    setupInterceptors(navigate);
  }, [navigate]);

  const login = async (credentials) => {
    try {
      const response = await api.post('login/', credentials);
      if (response.status === 200) {
        await checkAuthStatus();
        navigate('/secure');
      }
    } catch (error) {
      console.error('Error de login', error);
    }
  };

  const logout = async () => {
    try {
      await api.post('logout/');
      setUser(null);
      navigate('/login');
    } catch (error) {
      console.error('Error de logout', error);
    }
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;

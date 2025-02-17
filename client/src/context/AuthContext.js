import { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    const checkAuthStatus = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/user/auth-status/', { withCredentials: true });
            if (response.data.user) {
                setUser(response.data.user);
            } else {
                setUser(null);
            }
        } catch (error) {
            setUser(null);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        checkAuthStatus();
    }, []);

    // Interceptor para refrescar token automáticamente
    useEffect(() => {
        const interceptor = axios.interceptors.response.use(
            response => response,
            async error => {
                const originalRequest = error.config;
    
                // Evitar bucle infinito: si la petición ya es para el endpoint de refresh, no se reintenta.
                if (originalRequest.url.includes('/refresh/')) {
                    return Promise.reject(error);
                }
    
                if (error.response && error.response.status === 401 && !originalRequest._retry) {
                    originalRequest._retry = true;
                    try {
                        await axios.post('http://localhost:8000/api/user/refresh/', {}, { withCredentials: true });
                        return axios(originalRequest);
                    } catch (err) {
                        navigate('/login');
                        return Promise.reject(err);
                    }
                }
                return Promise.reject(error);
            }
        );
        return () => axios.interceptors.response.eject(interceptor);
    }, [navigate]);

    const login = async (credentials) => {
        try {
            const response = await axios.post('http://localhost:8000/api/user/login/', credentials, { withCredentials: true });
            if (response.status === 200) {
                await checkAuthStatus(); // Actualiza el estado del usuario
                navigate('/secure'); // Redirige si el usuario se autenticó correctamente
            }
        } catch (error) {
            console.error('Error de login', error);
        }
    };

    const logout = async () => {
        try {
            await axios.post('http://localhost:8000/api/user/logout/', {}, { withCredentials: true });
            setUser(null);
            navigate('/login'); // Redirige a login después del logout
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

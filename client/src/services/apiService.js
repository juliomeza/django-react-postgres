import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/users/',
  withCredentials: true,
});

export const setupInterceptors = (navigate) => {
  api.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      // Si la petición ya es para refresh, no reintentar para evitar bucles
      if (originalRequest.url.includes('refresh/')) {
        return Promise.reject(error);
      }
      if (error.response && error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        try {
          await api.post('refresh/');
          return api(originalRequest);
        } catch (err) {
          navigate('/login');
          return Promise.reject(err);
        }
      }
      return Promise.reject(error);
    }
  );
};

export default api;

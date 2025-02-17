import { useContext } from 'react';
import AuthContext from '../context/AuthContext';
import { Navigate } from 'react-router-dom';

const SecurePage = () => {
  const { user, logout, loading } = useContext(AuthContext);

  if (loading) return <p>Cargando...</p>;
  if (!user) return <Navigate to="/login" />;

  return (
    <div>
      <h2>Página Segura</h2>
      <p>Bienvenido, {user}!</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default SecurePage;

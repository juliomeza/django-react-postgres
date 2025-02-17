import { useContext } from 'react';
import { Container, Typography, Button, CircularProgress } from '@mui/material';
import AuthContext from '../context/AuthContext';
import { Navigate } from 'react-router-dom';

const SecurePage = () => {
  const { user, logout, loading } = useContext(AuthContext);

  if (loading) {
    return (
      <Container maxWidth="sm" sx={{ textAlign: 'center', mt: 4 }}>
        <CircularProgress />
        <Typography variant="h6" mt={2}>Cargando...</Typography>
      </Container>
    );
  }

  if (!user) return <Navigate to="/login" />;

  return (
    <Container maxWidth="sm" sx={{ textAlign: 'center', mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Página Segura
      </Typography>
      <Typography variant="h6" gutterBottom>
        Bienvenido, {user?.first_name}!
      </Typography>
      <Button variant="contained" color="secondary" onClick={logout}>
        Logout
      </Button>
    </Container>
  );
};

export default SecurePage;

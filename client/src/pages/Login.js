import { useState, useContext } from 'react';
import { TextField, Button, Container, Typography, Box } from '@mui/material';
import AuthContext from '../context/AuthContext';

const Login = () => {
  const [credentials, setCredentials] = useState({ email: '', password: '' });
  const [error, setError] = useState('');
  const { login } = useContext(AuthContext);

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Reinicia el mensaje de error
    try {
      await login(credentials);
    } catch (err) {
      if (err.response && err.response.status === 401) {
        setError('Incorrect email address or password');
      } else {
        setError('Incorrect email address or password.');
      }
    }
  };

  return (
    <Container maxWidth="xs" sx={{ mt: 8 }}>
      <Box
        sx={{
          p: 4,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          borderRadius: 2,
          boxShadow: 3,
          bgcolor: 'background.paper',
        }}
      >
        <Typography variant="h4" component="h2" gutterBottom>
          Sign in
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Email"
            name="email"
            margin="normal"
            variant="outlined"
            onChange={handleChange}
          />
          <TextField
            fullWidth
            label="Password"
            type="password"
            name="password"
            margin="normal"
            variant="outlined"
            onChange={handleChange}
          />
          {error && (
            <Typography color="error" sx={{ mt: 2 }}>
              {error}
            </Typography>
          )}
          <Button fullWidth variant="contained" color="primary" type="submit" sx={{ mt: 2 }}>
            Sign in
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default Login;

import { useState, useContext } from 'react';
import { TextField, Button, Container, Typography, Box } from '@mui/material';
import AuthContext from '../context/AuthContext';

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const { login } = useContext(AuthContext);

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    login(credentials);
  };

  return (
    <Container maxWidth="xs" sx={{ mt: 8 }}>
      <Box sx={{p: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', borderRadius: 2, boxShadow: 3, bgcolor: 'background.paper', }}>
        <Typography variant="h4" component="h2" gutterBottom>
          Sign in
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Username"
            name="username"
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
          <Button fullWidth variant="contained" color="primary" type="submit">
            Sign in
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default Login;

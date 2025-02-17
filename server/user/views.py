from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            response = JsonResponse({'message': 'Login exitoso'})
            response.set_cookie(
                key='access_token',
                value=str(access),
                httponly=True,
                secure=False,  # Usa True en producción con HTTPS
                samesite='Lax'
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite='Lax'
            )
            return response
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class TokenRefreshView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'No se proporcionó refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
            new_access = refresh.access_token
            response = JsonResponse({'message': 'Token refrescado'})
            response.set_cookie(
                key='access_token',
                value=str(new_access),
                httponly=True,
                secure=False,
                samesite='Lax'
            )
            return response
        except Exception:
            return Response({'error': 'Refresh token inválido o expirado'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        response = JsonResponse({'message': 'Logout exitoso'})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response

class AuthStatusView(APIView):
    # No forzamos permisos aquí para que, en caso de token inválido, request.user sea Anonymous
    def get(self, request):
        user = request.user
        if user and user.is_authenticated:
            return Response({'user': user.username}, status=status.HTTP_200_OK)
        return Response({'user': None}, status=status.HTTP_200_OK)

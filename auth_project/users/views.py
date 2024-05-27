from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"message": "User registered successfully"}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        form = AuthenticationForm(data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "Logout successful"}, status=200)

@method_decorator(login_required, name='dispatch')
class ProtectedView(View):
    def get(self, request):
        return JsonResponse({"message": "This is a protected view accessible only to logged-in users."})
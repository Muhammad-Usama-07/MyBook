from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model

from .forms import RegisterForm, LoginForm

User = get_user_model()


# ─────────────────────────────────────────
# HOME — redirect to login or dashboard
# ─────────────────────────────────────────
def home(request):
    """
    Root URL handler.
    If already logged in → go to dashboard.
    If not → go to login page.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


# ─────────────────────────────────────────
# REGISTER
# ─────────────────────────────────────────
@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    GET  → Show empty registration form
    POST → Process form, create user, log them in, redirect to dashboard
    """

    # If already logged in, no need to register again
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Save user to database (password is auto-hashed)
            user = form.save()

            # Log the user in immediately after registration
            login(request, user)

            messages.success(
                request,
                f'Welcome to MyBook, {user.first_name}! 🎉'
            )

            # Redirect based on role
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fix the errors below.')

    else:  # GET request
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})


# ─────────────────────────────────────────
# LOGIN
# ─────────────────────────────────────────
@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    GET  → Show empty login form
    POST → Verify credentials, log in, redirect by role
    """

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            # AuthenticationForm already verified username/password
            user = form.get_user()
            login(request, user)  # Creates session in database

            messages.success(request, f'Welcome back, {user.first_name}! 👋')

            # ── ROLE-BASED REDIRECT ──
            if user.is_teacher():
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')

        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = LoginForm(request)

    return render(request, 'auth/login.html', {'form': form})


# ─────────────────────────────────────────
# LOGOUT
# ─────────────────────────────────────────
def logout_view(request):
    """
    Clears the user session and redirects to login.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# ─────────────────────────────────────────
# DASHBOARD — role-based router
# ─────────────────────────────────────────
@login_required
def dashboard(request):
    """
    Generic dashboard URL.
    Figures out the user's role and sends them to the right dashboard.
    @login_required → redirects to /login/ if not authenticated
    """
    if request.user.is_teacher():
        return redirect('teacher_dashboard')
    return redirect('student_dashboard')


# ─────────────────────────────────────────
# STUDENT DASHBOARD
# ─────────────────────────────────────────
@login_required
def student_dashboard(request):
    """
    Main student portal page.
    Only students should see this.
    """
    # Role guard — teacher trying to access student page → redirect
    if request.user.is_teacher():
        return redirect('teacher_dashboard')

    context = {
        'user': request.user,
        'page': 'dashboard',
    }
    return render(request, 'student/dashboard.html', context)


# ─────────────────────────────────────────
# TEACHER DASHBOARD
# ─────────────────────────────────────────
@login_required
def teacher_dashboard(request):
    """
    Main LMS teacher page.
    Only teachers should see this.
    """
    # Role guard — student trying to access teacher page → redirect
    if request.user.is_student():
        return redirect('student_dashboard')

    context = {
        'user': request.user,
        'page': 'dashboard',
    }
    return render(request, 'teacher/dashboard.html', context)
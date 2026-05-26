from django.shortcuts import redirect
from functools import wraps


def teacher_required(view_func):
    """
    Decorator for views that should only be accessible by teachers.

    Usage:
        @teacher_required
        def my_view(request):
            ...
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_teacher():
            # Student trying to access teacher page
            return redirect('student_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


def student_required(view_func):
    """
    Decorator for views that should only be accessible by students.

    Usage:
        @student_required
        def my_view(request):
            ...
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_student():
            # Teacher trying to access student page
            return redirect('teacher_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper
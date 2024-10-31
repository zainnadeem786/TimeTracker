import pyautogui
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from .models import WorkSession
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'tracking/profile.html')

def home(request):
    return render(request, 'tracking/home.html')



@login_required  # Ensure that only authenticated users can access this view
def start_session(request):
    if request.method == "POST":
        session = WorkSession(user=request.user, active=True)
        session.save()
        return redirect('tracking:session_detail', session.id)
    return render(request, 'tracking/start.html')

def end_session(request, session_id):
    session = WorkSession.objects.get(id=session_id)
    session.end_time = timezone.now()
    session.active = False
    session.save()
    return redirect('tracking:profile')  # Change this to the appropriate URL


def take_screenshot(request, session_id):
    if request.user.is_authenticated:
        session = WorkSession.objects.get(id=session_id, user=request.user)
        if session and session.active:
            img = pyautogui.screenshot()
            session.save_screenshot(img)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

def session_detail(request, session_id):
    session = WorkSession.objects.get(id=session_id)
    return render(request, 'tracking/session_detail.html', {'session': session})

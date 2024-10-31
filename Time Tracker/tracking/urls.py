from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('start/', views.start_session, name='start_session'),
    path('end/<int:session_id>/', views.end_session, name='end_session'),
    path('take_screenshot/<int:session_id>/', views.take_screenshot, name='take_screenshot'),
    path('session/<int:session_id>/', views.session_detail, name='session_detail'),
    path('profile/', views.profile, name='profile'),  # Add this line
]

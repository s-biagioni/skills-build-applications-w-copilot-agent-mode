"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

from octofit_tracker import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')


@api_view(['GET'])
def api_root(request):
    """Return API resource URLs using Codespace domain if available else compute from request."""
    code = os.environ.get('CODESPACE_NAME')
    if code:
        base = f"https://{code}-8000.app.github.dev/api/"
    else:
        base = request.build_absolute_uri('/api/')
    return Response({
        'users': base + 'users/',
        'teams': base + 'teams/',
        'activities': base + 'activities/',
        'workouts': base + 'workouts/',
        'leaderboard': base + 'leaderboard/',
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/', include(router.urls)),
    path('', api_root),
]
"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router = DefaultRouter()
from octofit_tracker import views

router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

# API root view that uses Codespace env variable to construct absolute URLs when present
@api_view(['GET'])
def api_root(request):
    code = os.environ.get('CODESPACE_NAME')
    if code:
        base = f"https://{code}-8000.app.github.dev/api/"
    else:
        base = request.build_absolute_uri('/api/')
    return Response({
        'users': base + 'users/',
        'teams': base + 'teams/',
        'activities': base + 'activities/',
        'workouts': base + 'workouts/',
        'leaderboard': base + 'leaderboard/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    # Expose API root at '/api/' and map router endpoints under /api/
    path('api/', api_root),
    path('api/', include(router.urls)),
    # Map '/' to redirect to /api/
    path('', api_root),
]

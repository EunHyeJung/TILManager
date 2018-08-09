from django.urls import path, include
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    #path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},  name='logout'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]

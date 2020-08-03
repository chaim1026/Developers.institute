from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('animal/<str:x>/', views.animal, name='animal'),
    path('family/<str:x>/', views.family_list, name='family'),
]
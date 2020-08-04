from django.urls import path 
from . import views 

urlpatterns = [
    path('people/', views.all_people, name='people'),
    path('<int:x>/', views.person_id, name='person_id'),
]
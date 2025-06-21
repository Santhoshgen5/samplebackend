from django.urls import path
from .views import Dataview



urlpatterns = [
    path('api/', Dataview.as_view())
    
]

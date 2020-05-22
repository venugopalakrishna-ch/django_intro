from django.urls import path
from .views import HomeView,AboutView

urlpatterns = [
    path("kitkathome/", HomeView.as_view(), name="khome"),    
    path("kitkatabout/", AboutView.as_view(), name="kabout"),
]
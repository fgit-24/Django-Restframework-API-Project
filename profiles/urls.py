from django.urls import path
from profiles import views

urlpatterns = [
    ('profiles/, views.ProfileList.as_view()'),
]
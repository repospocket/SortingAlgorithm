from django.urls import path
from .views import submit_form_view

urlpatterns = [
    path('', submit_form_view, name='submit_form'),
]
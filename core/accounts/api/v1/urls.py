from django.urls import path
from . import views
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registrations
    path('registration/', views.RegistrationApiView.as_view(), name='registration')
]

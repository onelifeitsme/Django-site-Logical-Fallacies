from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('fallacy/<int:fallacy_id>/', show_fallacy, name='fallacy'),
]


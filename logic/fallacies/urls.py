from django.urls import path
from .views import Home, show_fallacy

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('fallacy/<int:fallacy_id>/', show_fallacy, name='fallacy'),
]

from django.urls import path
from fallacies.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact),
    path('about/', about),
    path('fallacy/<int:fallacy_id>/', show_fallacy, name='fallacy'),
    path('test/', test),
    path('testus/', testus)

]


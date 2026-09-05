from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pro Insight Payroll Solutions!")

urlpatterns = [
    path('', home, name='home'),       
    path('admin/', admin.site.urls),   
    path('accounts/', include('django.contrib.auth.urls')),  # adds login/logout/password reset
]

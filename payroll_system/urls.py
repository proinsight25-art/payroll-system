from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pro Insight Payroll Solutions!")

urlpatterns = [
    path('', home, name='home'),       # Root URL
    path('admin/', admin.site.urls),   # Admin
]

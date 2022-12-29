from django.contrib import admin
from django.urls import path, include
from .import views
from setor.views import tor,tar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setortunai/',tor),
    path('tariktunai/',tar),
    path('tabungan/',include('koperasi.urls')),
    path('gadai/',include('tabungan.urls')),
    path('',views.web),
]

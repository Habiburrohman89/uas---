from django.contrib import admin

from .models import setorTunai,tarikTunai

class set(admin.ModelAdmin):
    list_display = ['Nama', 'No_Tabungan', 'Tanggal', 'Alamat', 'N_Penyetoran', 'Terbilang', 'Nama_Penyetor' ]
    search_fields = ['Nama', 'No_Tabungan']
    list_filter = ['No_Tabungan']
    list_per_page = 10
class tar(admin.ModelAdmin):
    list_display =  ['Nama', 'No_Tabungan', 'Tanggal', 'Alamat', 'N_Penarikan', 'Terbilang', 'Nama_Penarik' ]
    search_fields = ['Nama', 'No_Tabungan']
    list_filter = ['No_Tabungan']
    list_per_page = 10

admin.site.register(setorTunai,set)
admin.site.register(tarikTunai,tar)


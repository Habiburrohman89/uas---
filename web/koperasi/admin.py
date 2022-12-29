from django.contrib import admin
from.models import tabungan

class tab(admin.ModelAdmin):
    list_display = ['Nama', 'No_Tabungan', 'Alamat', 'Jumlah_tabungan', 'Antrian', 'Biaya_administrasi']
    search_fields = [ 'Nama', 'No_tabungan']
    list_filter = ['Antrian']
    list_per_page = 8

admin.site.register(tabungan,tab)

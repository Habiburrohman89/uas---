from django.contrib import admin

from .models import gadai

class gad(admin.ModelAdmin):
    list_display = ['Nama', ' Nik', ' Alamat', 'Jumlah_Pinjaman', 'Barang_Jaminan', 'Bunga_Per_Th', 'Biaya_administrasi']
    search_fields = ['Nama']
    list_filter = ['Nik']
    list_per_page = 5

admin.site.register(gadai)  

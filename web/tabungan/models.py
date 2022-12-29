from django.db import models

class gadai(models.Model):
    Nama = models.CharField(max_length=30)
    Nik = models.CharField(max_length=30,null=True)
    Alamat = models.TextField()
    Jumlah_Pinjaman = models.CharField(max_length=30, blank=True)
    Barang_Jaminan = models.CharField(max_length=50)
    Bunga_Per_Th = models.BigIntegerField(null=True)
    Biaya_administrasi = models.CharField(max_length=30, blank=True)

   
    
   
    
    def __str__(self):
        return "{}.{}".format(self.Nama,self.Nik)

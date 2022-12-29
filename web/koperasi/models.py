from django.db import models

class tabungan(models.Model):
    Nama = models.CharField(max_length=50)
    No_Tabungan = models.CharField(max_length=20)
    Alamat = models.TextField()
    Jumlah_tabungan = models.CharField(max_length=200)
    Antrian = models.CharField(max_length=50)
    Biaya_administrasi = models.CharField(max_length=20)

    def __str__(self):
        return "{}. {}".format(self.Nama,self.No_Tabungan)

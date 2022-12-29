from django.db import models

class setorTunai(models.Model):
    Nama = models.CharField(max_length=50)
    No_Tabungan = models.CharField(max_length=30)
    Tanggal = models.DateField()
    Alamat = models.TextField()
    N_Penyetoran = models.CharField(max_length=20)
    Terbilang = models.CharField(max_length=50)
    Nama_Penyetor = models.CharField(max_length=50)

    def __str__(self):
        return"{}".format(self.Nama)


class tarikTunai(models.Model):
    Nama = models.CharField(max_length=50)
    No_Tabungan = models.CharField(max_length=30)
    Tanggal = models.DateField()
    Alamat = models.TextField()
    N_Penarikan = models.CharField(max_length=20)
    Terbilang = models.CharField(max_length=50)
    Nama_Penarik = models.CharField(max_length=50)


    def __str__(self):
        return"{}".format(self.Nama)





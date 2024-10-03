from django.db import models

class CSVData(models.Model):
    SUBSTANCIA = models.CharField(max_length=500)
    CNPJ = models.CharField(max_length=500)
    LABORATORIO = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.SUBSTANCIA}, {self.CNPJ}, {self.LABORATORIO}"
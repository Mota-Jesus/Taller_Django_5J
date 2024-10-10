from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    A_Paterno = models.CharField(max_length=50, verbose_name = "Apellido paterno")
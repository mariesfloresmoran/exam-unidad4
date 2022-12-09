from django.db import models

# Create your models here.
class Proyectos(models.Model):
    foto=models.URLField()
    titulo_proyecto=models.CharField(max_length=200)
    descripcion_proyecto=models.CharField(max_length=400)

    def __str__(self):
        return self.titulo_proyecto

    class Meta:
        db_table = "proyectos"
        ordering = ["titulo_proyecto"]

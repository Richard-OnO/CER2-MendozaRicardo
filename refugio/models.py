from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    
    genero = [
    ('Macho','Macho'),
    ('Hembra','Hembra'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    sexo = models.CharField(max_length=20, choices=genero)
    edad_aproximada = models.CharField(max_length=50) 
    imagen = models.URLField(help_text="URL de la imagen de la mascota")
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} ({self.especie.nombre})"
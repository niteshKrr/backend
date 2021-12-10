from django.db import models

# Create your models here.
class Cure(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    disease=models.CharField(max_length=100)
    medicine=models.CharField(max_length=100)
    images = models.CharField(max_length=500, auto_created=True ,default="")


    def __str__(self):
        return self.disease

               
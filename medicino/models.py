from django.db import models

# Create your models here.
class Cure(models.Model):
    id=models.IntegerField(primary_key=True)
    disease=models.CharField(max_length=100)
    medicine=models.CharField(max_length=100)
    images = models.ImageField(upload_to ='medicine/images', default = "")


    def __str__(self):
        return self.disease

               
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.CharField(max_length=500)


#ORM Queries
"""
Tablename.Objects.all()
Tablename.Objects.all().values() 
Tablename.Objects.get(id=1)
delete()
save()




"""




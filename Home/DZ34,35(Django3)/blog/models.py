from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/image')
    date = models.DateField()
    date_time = models.DateTimeField()
    time_1 = models.TimeField()
    number = models.BigIntegerField()
    number_1 = models.DecimalField(max_digits=5, decimal_places=2)
    time_2 = models.DurationField()
    number_2 = models.FloatField()
    number_3 = models.IntegerField()
    number_4 = models.PositiveBigIntegerField()
    number_5 = models.PositiveIntegerField()
    number_6 = models.PositiveSmallIntegerField()
    number_7 = models.SmallIntegerField()
    text = models.SlugField()
    e_mail = models.EmailField()
    car = models.BooleanField()
    text_1 = models.BinaryField()
    I_P = models.GenericIPAddressField()


from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)  # Строка с ограниченными знаками
    desc = models.CharField(max_length=150)  # Строка с ограниченными знаками
    image = models.ImageField(upload_to='blog/image/')  # Строка под изображение
    date = models.DateField()  # Дата
    url = models.URLField()  # Ссылка
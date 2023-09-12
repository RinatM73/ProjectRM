from django.db import models

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=50)  # Строка с ограниченными знаками
    desc = models.TextField('Описание')  # Строка с ограниченными знаками
    image = models.ImageField('Изображение', upload_to='blog/image/')  # Строка под изображение
    date = models.DateField('Дата')  # Дата
    url = models.URLField('Доп.источник', blank=False)  # Ссылка

    def __str__(self):
        return f"{self.title} | {self.date}"  # это для красивого отображения в админке
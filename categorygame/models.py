from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название игры')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    
    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name

class Buld(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название игры')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='categorygame_imgas',blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'buld'
    
    def __str__(self):
        return self.name
    

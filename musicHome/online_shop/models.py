from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.TextField(verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    short_desc = models.TextField(verbose_name="Короткое описание")
    long_desc = models.TextField(verbose_name="Длинное описание")
    cost = models.FloatField(verbose_name="Цена")
    count = models.IntegerField(verbose_name="Количество")
    custom_name = models.ForeignKey('Customers', on_delete=models.PROTECT, verbose_name="Поставщик")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['time_update', 'name']


class Customers(models.Model):
    name = models.TextField(verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")
    contacts = models.IntegerField(verbose_name="Контакты")

    class Meta:
        verbose_name = 'Поставщики'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer', kwargs={'custom_id': self.pk})


class Category(models.Model):
    name = models.TextField(db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    ID_client = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="ID клиента")
    ID_product = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name="ID товара")
    status = models.TextField(verbose_name="Статус")
    sum_cost = models.FloatField(verbose_name="Сумма заказа")

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('orders', kwargs={'order_id': self.pk})

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['date']


class CostChange(models.Model):
    ID_product = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name="ID товара")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    new_cost = models.FloatField(verbose_name="Измененная цена")

    class Meta:
        verbose_name = 'Изменение цен'
        verbose_name_plural = 'Изменение цен'
        ordering = ['date']


class Deliveries(models.Model):
    ID_product = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name="ID товара")
    ID_customer = models.ForeignKey('Customers', on_delete=models.PROTECT, verbose_name="ID поставщика")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    count = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = 'Поставки'
        verbose_name_plural = 'Поставки'
        ordering = ['date']

#class Users(models.Model):
  #  first_name = models.TextField()
  #  last_name = models.TextField()
   # email = models.EmailField()
   # password = models.TextField()
   # is_admin = models.BooleanField()

 #   class Meta:
  #      verbose_name = 'Пользователи сайта'
  #      verbose_name_plural = 'Пользователи сайта'
        #ordering = []

#def get_absolute_url(self):
 #   return reverse('post', kwards={})


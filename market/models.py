from django.db import models

from django.contrib.auth.models import User

from django.utils.safestring import mark_safe

from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer
from config.settings import BACKEND_URL


class UserProfile(User):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    rating = models.IntegerField(default=0)
    image = ImageCropField(blank=True, upload_to='user_photo')
    cropping = ImageRatioField('image', '60x60')

    @property
    def get_small_image(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_url)

    @property
    def get_small_image_url(self):
        try:
            return BACKEND_URL+get_thumbnailer(self.image).get_thumbnail({
                'size': (60, 60),
                'box': self.cropping,
                'crop': 'smart',
            }).url
        except:
            return BACKEND_URL+'noimage.png'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='category', null=True, blank=True)

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" />')
        except:
            return 'None'

    @property
    def image_url(self):
        return BACKEND_URL + self.image.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    image = ImageCropField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)

    cropping = ImageRatioField('image', '100x100')

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" />')
        except:
            return 'None'

    @property
    def get_small_image(self):
        return mark_safe(f'<img src="%s" />' % self.get_small_image_url)

    @property
    def get_small_image_url(self):
        return BACKEND_URL + get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.cropping,
            'crop': 'smart',
        }).url


class Store(models.Model):
    provider = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Order(models.Model):

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    consumer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='new', choices=STATUS)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0)

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

# Create your models here.#

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте, если торг возможен')
    create_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата последнего обновления', auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/', blank=True, null=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if timezone.now().date() == self.create_at.date():
            created_time = self.create_at.time().strftime('%H:%M')
            return format_html(
                '<span style="color: green; font-weight: bold;">сегодня в {}</span>', created_time
            )

        if timezone.now().year == self.create_at.year and timezone.now().month == self.create_at.month and timezone.now().day - self.create_at.day == 1:
            created_time = self.create_at.time().strftime('%H:%M')
            return format_html(
                '<span style="color: yellow; font-weight: bold;">вчера в {}</span>', created_time
            )

        return self.create_at.strftime('%d:%m:%Y в %H:%M')

    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if timezone.now().date() == self.updated_at.date():
            updated_time = self.updated_at.time().strftime('%H:%M')
            return format_html(
                '<span style="color: green; font-weight: bold;">сегодня в {}</span>', updated_time
            )

        if timezone.now().year == self.updated_at.year and timezone.now().month == self.updated_at.month and timezone.now().day - self.updated_at.day == 1:
            updated_time = self.updated_at.time().strftime('%H:%M')
            return format_html(
                '<span style="color: yellow; font-weight: bold;">вчера в {}</span>', updated_time
            )

        return self.updated_at.strftime('%d:%m:%Y в %H:%M')


    @admin.display(description='изображение')
    def set_picture(self):
        if self.image:
            return format_html(
                '<img src={} style="width: auto; height: 100px;">', self.image.url
            )

    # def __str__(self):
    #     return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'
    def __str__(self):
        return "{}(id={id}, title={title}, price={price})".format(self.__class__.__name__, **self.__dict__)

    class Meta:
        db_table = "advertisements"
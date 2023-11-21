from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name_category = models.CharField(verbose_name='катигория расходов', max_length=100, unique=True)

    class Meta:
        db_table = "category"
        verbose_name = 'катигория'
        verbose_name_plural = 'катигории'

    def __str__(self):
        return self.name_category



class UserCategory(models.Model):
    my_category = models.ForeignKey(Category, on_delete=models.CASCADE ,verbose_name='Категории пользователя')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = "user_category"
        verbose_name = 'катигория '
        verbose_name_plural = 'выбранные катигории'

    def __str__(self):
        return self.my_category

    def get_absolute_url(self):
        return reverse('detail', kwargs={'user_id':self.pk})


class Consumption(models.Model):
    expenses = models.IntegerField(verbose_name='сумма расхода', default=0)
    data = models.DateField(verbose_name='дата', )

    class Meta:
        db_table = "consumption"
        verbose_name = 'расход'
        verbose_name_plural = 'расходы'








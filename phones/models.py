from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(
        primary_key=True,
        serialize=False
    )

    name = models.CharField(
        max_length=50
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )

    image = models.ImageField()

    release_date = models.DateField()

    lte_exists = models.BooleanField(default=True)

    slug = models.SlugField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
        ordering = ['id']
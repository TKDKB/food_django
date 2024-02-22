
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField, CKEditorWidget


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    calories = models.IntegerField(verbose_name="Кол-во каллорий на 100 грамм")
    description = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    preview_image = models.ImageField(upload_to='images/', blank=True, verbose_name="Превью")
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ингредиенты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    time_minutes = models.IntegerField(
        validators=[MinValueValidator(1)],
        default=1,
        verbose_name="Время приготовления",
        help_text="в минутах",
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Category(models.TextChoices):
        breakfast = ('B', 'Завтрак')
        lunch = ('L', 'Обед')
        dinner = ('D', 'Ужин')

    category = models.CharField(max_length=1, choices=Category.choices, verbose_name="Приём пищи")

    class Meta:
        ordering = ("-created_at",),





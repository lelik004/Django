from django.db import models

NULLABLE = {'blank': True, 'null': True}


class NewsManager(models.Manager):

    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(models.Model):

    # objects = NewsManager()

    title = models.CharField(max_length=256, verbose_name='Название')
    preamble = models.CharField(max_length=1024, verbose_name='Описание')
    body = models.TextField(blank=True, null=True, verbose_name='Тело')
    body_as_markdown = models.BooleanField(default=False, verbose_name='As markdown')
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Создан'
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Обновлен'
    )
    deleted = models.BooleanField(default=False, verbose_name='Удалено')
    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Course(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField( verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Стоимость')

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Создан'
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Обновлен'
    )
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.pk} {self.title}'
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Создан'
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Обновлен'
    )
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CourseTeacher(models.Model):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Создан'
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Обновлен'
    )
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.pk} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'курс к учителю'
        verbose_name_plural = 'курсы к учителям'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

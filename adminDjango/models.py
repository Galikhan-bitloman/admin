# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from adminDjango.helper_models import DatetimeField, UUIDField



class Api_Aboutus(models.Model):
    title = models.CharField(max_length=250, blank=True, primary_key=True, verbose_name='Заголовок')
    text = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Текст')
    image = models.FileField(max_length=100, blank=True, null=True, upload_to='imgAboutUs', verbose_name='Картинка')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'API_AboutUs'
        verbose_name = _('О нас')
        verbose_name_plural =  _('О нас')

    def __str__(self):
        return self.title


class Api_Analyses(models.Model):
    short_title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Короткий заголовок')
    long_title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Длинный заголовк')
    is_unique = models.BooleanField(blank=True, null=False, verbose_name='Уникальный')
    research_id = models.CharField(max_length=100, blank=True, primary_key=True, verbose_name='Код анализа')
    research_time = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Время анализа')
    biomaterial = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Биоматериал')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    preparation_doctor = models.TextField(blank=True, null=True, verbose_name='Инструкция для врача ')
    banner_img = models.FileField(max_length=1000, blank=True, null=True, upload_to='imgAnalyse', verbose_name='Картинка для баннера')
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Тип анализа')
    document_img = models.FileField(max_length=1000, blank=True, null=True, upload_to='imgAnalyse', verbose_name='Картинка для документа')
    main_img = models.FileField(max_length=1000, blank=True, null=True, upload_to='imgAnalyse', verbose_name='Главная картинка')
    description_patient = models.TextField(blank=True, null=True, verbose_name='Описание для пациентов')
    preparation_patient = models.TextField(blank=True, null=True, verbose_name='Инструкция для пациентов')
    description_doctor = models.TextField(blank=True, null=True, verbose_name='Описание для врачей')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Analyses'
        verbose_name = _('Анализ')
        verbose_name_plural = _('Анализы')

    def __str__(self):
        return self.short_title

class Api_Appointments(models.Model):
    title_appointment = models.CharField(max_length=100, blank=True, primary_key=True, verbose_name='Заголовок записи')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дата')
    time = models.CharField(max_length=255, blank=True, null=True, verbose_name='Время')
    description = models.CharField(max_length=1000, blank=True, null=True)
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    apiuser = models.ForeignKey('Api_Users', on_delete=models.CASCADE, db_column='APIUser_id', blank=True, null=True,
                                verbose_name='Кому принадлежит')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Appointments'
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')

    def __str__(self):
        return self.title_appointment

class Api_Contacts(models.Model):
    address = models.CharField(max_length=100, blank=True, primary_key=True, verbose_name='Адрес')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')
    map = models.CharField(max_length=250, blank=True, null=True, verbose_name='Карта')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'API_Contacts'
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')

    def __str__(self):
        return '{} {} {}'.format(self.address, self.phone_number, self.map)


class Api_News(models.Model):
    img_news = models.FileField(max_length=255, blank=True, null=True, upload_to='imgNews')
    title = models.CharField(max_length=1000, blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_News'
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title

class Api_Notifications(models.Model):
    title_notification = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок уведомления')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дата')
    result = models.CharField(max_length=255, blank=True, null=True, verbose_name='Результат')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.
    apiuser = models.ForeignKey('Api_Users', models.DO_NOTHING, db_column='APIUser_id', blank=True, null=True, verbose_name='Кому принадлежит')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Notifications'
        verbose_name = _('Уведомление')
        verbose_name_plural = _('Уведомления')

    def __str__(self):
        return self.title_notification


class Api_Promotions(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name='Заголовок акций')
    text = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Promotions'
        verbose_name = _('Скидка')
        verbose_name_plural = _('Скидки')

    def __str__(self):
        return self.title

class Api_Qaas(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_QaAs'
        verbose_name = _('Вопрос и ответ')
        verbose_name_plural = _('Вопросы и ответы')


    def __str__(self):
        return '{} {}'.format(self.question, self.answer)


class Api_Results(models.Model):
    title_result = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок результатов')
    isready = models.IntegerField(db_column='isReady', blank=True, null=True, verbose_name='Готовность')  # Field name made lowercase.
    file = models.FileField(max_length=255, blank=True, null=True, upload_to='fileResult')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.
    apiuser = models.ForeignKey('Api_Users', models.DO_NOTHING, db_column='APIUser_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Results'
        verbose_name = _('Результат')
        verbose_name_plural = _('Результаты')

    def __str__(self):
        return self.title_result

class Api_Reviews(models.Model):
    firstname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')
    avatar = models.FileField(max_length=255, blank=True, null=True, upload_to='imgAvatar')
    text_review = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дата')
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.
    username = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'API_Reviews'
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return '{} {} {} {}'.format(self.firstname, self.lastname, self.username, self.date)


class Api_Users(models.Model):
    email = models.CharField(max_length=255, verbose_name='Электронная почта')
    password = models.CharField(max_length=255, blank=True, null=True)
    password2 = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    avatar = models.FileField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', auto_now=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now_add=True)  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    username = models.CharField(max_length=20, verbose_name='Имя пользователя', unique=True)
    firstname = models.CharField(max_length=20, blank=True, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=20, blank=True, null=True, verbose_name='Фамилия')

    class Meta:
        managed = False
        db_table = 'API_Users'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.username)

class Sequelizemeta(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'SequelizeMeta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

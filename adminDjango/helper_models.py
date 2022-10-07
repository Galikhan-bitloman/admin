from django.db import models
import uuid

class DatetimeField(models.Model):
    createdat = models.DateTimeField(db_column='createdAt', verbose_name='Создан')
    updatedat = models.DateTimeField(db_column='updatedAt', verbose_name='Обновлен')

    class Meta:
        abstract = True


class UUIDField(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

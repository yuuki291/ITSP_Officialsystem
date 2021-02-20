from django.core import validators
from django.db import models


# 会社マスタ
class MstCompanys(models.Model):
    CompanyId = models.ForeignKey('MstUsers', to_field='CompanyId', on_delete=models.SET_NULL, null=True)
    CompanyName = models.CharField(blank=True, null=True, max_length=25, db_index=True, unique=True)

    def __str__(self):
        return self.CompanyName


# ユーザー
class MstUsers(models.Model):
    UserId = models.IntegerField(
        blank=True,
        null=True,
        default=0,
        unique=True,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100)]
    )
    # db_indexは消すかもそれない
    UserName = models.CharField(blank=True, null=True, max_length=10, db_index=True, unique=True)
    Pass = models.CharField(max_length=15, db_index=True, unique=True)
    CompanyId = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.UserName


from django.core import validators
from django.db import models


# 会社マスタ
class MstCompanys(models.Model):
    CompanyName = models.CharField(blank=True, null=True, max_length=25, db_index=True, unique=True)
    CompanyId = models.AutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.CompanyName


# ユーザー
class MstUsers(models.Model):
    UserId = models.AutoField(
        auto_created=True, primary_key=True, serialize=False
    )
    # db_indexは消すかもそれない
    UserName = models.CharField(blank=True, null=True, max_length=10, db_index=True, unique=True)
    Pass = models.CharField(max_length=15, db_index=True)
    Company = models.ForeignKey('MstCompanys', to_field='CompanyId', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.UserName

   # CompanyIdがnullなので後から修正
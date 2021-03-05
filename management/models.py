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


# 勤務表
class Roster(models.Model):
    Date = models.DateField()
    Work_Status = models.CharField(max_length=20)
    CHOICES = (
        ('Paid', '有給'),
        ('Paid_AM_PM', '有給(午前・午後)'),
        ('Paid_hours', '有給(時間)'),
        ('Substitute_holiday', '代休'),
        ('Transfer_holiday', '振替休'),
    )
    Application = models.CharField(max_length=20, choices=CHOICES)
    Arrive_At_Work = models.DateTimeField()
    Leave_The_Company = models.DateTimeField()
    Man_Hours = models.IntegerField()
    Remarks = models.TextField(max_length=500)

    def __str__(self):
        return self.Work_Status


# CompanyIdがnullなので後から修正

# ユーザ詳細
class UserDetails(models.Model):
    User_No = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    User_Name = models.CharField(blank=True, null=True, max_length=50, db_index=True, unique=True)
    User_Name_kana = models.CharField(blank=True, null=True, max_length=50, db_index=True)
    Gender = models.CharField(max_length=2, blank=True, null=True)
    Birthday = models.DateField(blank=True, null=True)
    Hire_Date = models.DateField(blank=True, null=True)
    Type_Of_Contract = models.BooleanField(blank=True, null=True, max_length=15, db_index=True)
    Affiliation_Department = models.BooleanField(blank=True, null=True, max_length=15, db_index=True)
    Affiliation_Section = models.BooleanField(blank=True, null=True, max_length=15, db_index=True)
    Position = models.CharField(blank=True, null=True, max_length=10, db_index=True)
    Notices = models.TextField(max_length=1000)

    def __str__(self):
        return self.User_Name

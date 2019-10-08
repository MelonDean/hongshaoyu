from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


def addZero(time):
    if time<10:
        return "0" + str(time)
    else:
        return time
# Create your models here.


class UserProfile(AbstractUser):
    telephone = models.IntegerField(verbose_name="手机号码", unique=True, null=True, blank=True)

    def __str__(self):
        return f"<UserProfile> {self.username}"

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class BaseModel(models.Model):
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updateTime = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        time_obj = self.createTime
        self.createTime =  f'{time_obj.year}-{addZero(time_obj.month)}-{addZero(time_obj.day)} {addZero(time_obj.hour)}:{addZero(time_obj.minute)}:{addZero(time_obj.second)}'
        time_obj = self.updateTime
        self.updateTime = f'{time_obj.year}-{addZero(time_obj.month)}-{addZero(time_obj.day)} {addZero(time_obj.hour)}:{addZero(time_obj.minute)}:{addZero(time_obj.second)}'

    class Meta:
        abstract = True


class Department(BaseModel):
    name = models.CharField(verbose_name="所属机构", max_length=50)
    parent_dept = models.ForeignKey("self", on_delete=models.CASCADE, related_name="departments_of_department", null=True, blank=True)

    def __str__(self):
        return f"<Department> {self.name}"

    class Meta:
        verbose_name = "机构表"
        verbose_name_plural = verbose_name

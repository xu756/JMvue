from django.db import models


class User(models.Model):  # 用户
    id = models.AutoField(verbose_name="用户id", primary_key=True)
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="用户密码", max_length=128)
    rid = models.DecimalField(verbose_name="权限", max_digits=9, decimal_places=0, choices=(
        (0, "会员"), (5, "管理员"), (9, "开发人员")))
    emial = models.EmailField(verbose_name="邮箱")
    token = models.CharField(verbose_name="token令牌", max_length=128)
    CreatTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    LoginTime = models.DateTimeField(verbose_name="最后登录时间", auto_now=True)
    isLogin=models.BooleanField(verbose_name="登录状态",default=False)
    class Meta:
        verbose_name_plural = '用户管理'


class Userproject(models.Model):
    id = models.AutoField(verbose_name="项目id", primary_key=True)
    ProjectName = models.CharField(verbose_name="项目名", max_length=64)
    fid = models.DecimalField(verbose_name="项目属于者",
                              max_digits=10000, decimal_places=0)
    data = models.JSONField()
    CreatTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    LoginTime = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)
    class Meta:
        verbose_name_plural = '项目列表'

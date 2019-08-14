from django.db import models


# Create your models here.
# 自定义模型 执行迁移后会在mysql中创建一个 应用名_类名的表 home_users
class Users(models.Model):
    # 属性
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.IntegerField()
    addtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + self.username


# 定义stu类 元选项
class Stu(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    email = models.CharField(max_length=100, null=True)

    # 元选项
    class Meta():
        db_table = 'stu'


# 定义班级模型
class ClassInfo(models.Model):
    cname = models.CharField(max_length=10)
    code = models.IntegerField()

# 创建学员模型 一对多
class student(models.Model):
    sname = models.CharField(max_length=6)
    age = models.IntegerField()
    # 一对多
    cid = models.ForeignKey(ClassInfo,on_delete=models.CASCADE)


    def __str__(self):
        return self.sname


# 创建学员详情模型 一对一
class stuinfo(models.Model):
    jiguan = models.CharField(max_length=10)
    xueli = models.CharField(max_length=10)
    # 第一个参数：是被关联的模型名称
    # 第二个参数：当一张表数据删除时，与之关联的表中数据也会删除
    uid = models.OneToOneField(student,on_delete=models.CASCADE)

# 创建学生模型
class stus(models.Model):
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

# 创建社团模型 多对多
class club(models.Model):
    name = models.CharField(max_length=16)
    members = models.ManyToManyField("stus")

    def __str__(self):
        return self.name
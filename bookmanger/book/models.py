from django.db import models
class BookInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="名字")
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0,verbose_name="阅读量")
    commentcount = models.IntegerField(default=0,verbose_name="评论量")
    is_delete = models.BooleanField(default=False,verbose_name="逻辑删除")
# Create your models here.
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (0,'male'),
        (1,'female')
    )

    name = models.CharField(max_length=20,verbose_name="姓名")
    gender = models.BooleanField(choices=GENDER_CHOICE,default=0,verbose_name="性别")
    description = models.CharField(max_length=100,null=True,verbose_name="描述信息")
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name="图书")
    is_delete = models.BooleanField(default=False,verbose_name="逻辑删除")

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
    def __str__(self):
        return self.name



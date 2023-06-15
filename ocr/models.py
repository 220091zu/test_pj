from django.db import models

# Create your models here.
class Ocr(models.Model):
    company = models.CharField(max_length=50)   # 会社名
    location = models.CharField(max_length=100) # 所在地
    employee = models.IntegerField()            # 従業員数
    sales_amount = models.IntegerField()        # 売上高
    company_url = models.URLField()             # 企業ホームページ
    listed = models.CharField(max_length=10)    # 上場先
    # ☆複数選択にするにはどうすれば良い？
    occupation = None                           # 募集職種
    work_time = models.CharField(max_length=100)# 就業時間(X:XX～X:XX)
    work_hours = models.IntegerField()          # 就業時間(X時間)
    over_time = models.IntegerField()           # 月平均残業時間
    basic_salary = models.IntegerField()        # 基本給
    bonus_salary = models.IntegerField()        # 基本給(計Xヶ月)
    holiday = models.IntegerField()             # 年間休日
    work_location = None                        # 勤務先候補
    on_site_choices = ((False, "無し"), (True, "有り"))
    on_site = models.BooleanField(              # 客先常駐か
        default=False, choices=on_site_choices, help_text="客先常駐有=TRUE")
    
    def __str__(self):
        return self.company
    
    
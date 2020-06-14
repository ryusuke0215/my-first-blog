from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model: ポストがDjango Modelだという意味。Djangoが、これはデータベースに保存すべきものだとわかるようにしている。
class Post(models.Model):
    # models.CharField    : 文字数が制限されたテキストを定義するフィールド
    # models.TextField    : これは制限なしの長いテキスト用。ブログポストのコンテンツに理想的なフィールド
    # models.DateTimeField: 日付と時間のフィールド
    # models.ForeignKey   : これは他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# ブログを公開するメソッドそのもの
def publishe(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
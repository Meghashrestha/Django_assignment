from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import timezone

# Create your models here.
# def validate_my_age(age):
#     if age < 20:
#         raise ValueError("your age is less")
class Writername(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Writernames"
# class Writeremail(models.Model):
#     email = models.EmailField(max_length=100)
#     writername : models.ForeignKey(Writername, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.email
#     class Meta:
#         verbose_name_plural = "Writeremails"



class Blogdetails(models.Model):
    writer_name = models.ForeignKey(Writername, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=500)
    blog = models.TextField(max_length=20000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name_plural = "Blogdetails"
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.full_clean()
    # def clean(self):
    #     if self.age > 40:
    #         if not self.bio:
    #             raise ValidationError("enter bio")
    # def full_clean(self, exclude=None, validate_unique=True):
    #     pass


from django.db import models


class School(models.Model):
    school_code = models.CharField(max_length=20, null=False)
    school_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.school_name
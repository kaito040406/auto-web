from django.db import models

# Create your models here.
# ['o','h','i','c']

class Jpyutc(models.Model):
    time = models.TextField("time")
    open_data = models.TextField("open_data")
    high_data = models.TextField("high_data")
    row_data = models.TextField("row_data")
    close_data = models.TextField("close_data")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    #create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Todo"
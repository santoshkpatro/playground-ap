from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todos"

    def __str__(self) -> str:
        return self.name
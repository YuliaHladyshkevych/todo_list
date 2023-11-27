from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-datetime_created"]

    def __str__(self):
        return f"{self.name}"

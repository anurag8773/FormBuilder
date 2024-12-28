from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
        ('checkbox', 'Checkbox'),
    ]
    form = models.ForeignKey(Form, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_type = models.CharField(choices=QUESTION_TYPES, max_length=50)
    options = models.JSONField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

class Response(models.Model):
    form = models.ForeignKey(Form, related_name='responses', on_delete=models.CASCADE)
    data = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class AnalyticsCache(models.Model):
    form = models.OneToOneField(Form, related_name='analytics', on_delete=models.CASCADE)
    data = models.JSONField() 
    updated_at = models.DateTimeField(auto_now=True)


# home/models.py
from django.db import models

class CodeSnippet(models.Model):
    id = models.AutoField(primary_key=True)  # Starts from 1 and increments
    code_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Code {self.id}"
    
    class Meta:
        ordering = ['id']
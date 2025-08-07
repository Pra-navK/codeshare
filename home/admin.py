# home/admin.py
from django.contrib import admin
from .models import CodeSnippet

@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'code_preview')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    
    def code_preview(self, obj):
        return obj.code_content[:50] + '...' if len(obj.code_content) > 50 else obj.code_content
    code_preview.short_description = 'Code Preview'
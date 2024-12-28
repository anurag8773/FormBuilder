from django.contrib import admin
from .models import Form, Question, Response, AnalyticsCache

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)  
    list_filter = ('created_at',)  
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'form', 'text', 'question_type', 'order') 
    list_filter = ('question_type',)  
    search_fields = ('text',)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'form', 'submitted_at')  
    list_filter = ('submitted_at',)  
    search_fields = ('form__name',)  

@admin.register(AnalyticsCache)
class AnalyticsCacheAdmin(admin.ModelAdmin):
    list_display = ('form', 'updated_at')  
    search_fields = ('form__name',)  
    readonly_fields = ('data',) 

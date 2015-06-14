from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['pub_date']}),
        ('Date information',   {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
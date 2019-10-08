from django.contrib import admin

from .models import Question

#admin.site.register(Question)   # se reeplaza por las lineas siguientes

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
admin.site.register(Question, QuestionAdmin)

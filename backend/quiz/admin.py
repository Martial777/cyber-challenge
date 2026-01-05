from django.contrib import admin
from .models import Question, Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'score')
    list_filter = ('user',)
    search_fields = ('user__username',)

admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)

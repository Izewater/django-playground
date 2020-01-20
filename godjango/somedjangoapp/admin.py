from django.contrib import admin

from .models import Question, Choice

# Register your models here.
admin.site.site_header = "My Django Header"
admin.site.site_title = "My Django Title"
admin.site.index_title = "welcome to my Django : index title"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Info', {'fields': [
                  'pub_date'], 'classes':['collaps']}),
                 ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

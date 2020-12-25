from django.contrib import admin
from test_module.models import Tests, Questions, Answers, Results
# Register your models here.

admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Results)


class ResultsAdmin(admin.ModelAdmin):
    list_display = ("user", "test_id", "number_of_correct_answers")
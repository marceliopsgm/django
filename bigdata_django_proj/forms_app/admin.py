from django.contrib import admin
from forms_app.models import Meta1P, Meta3P
# Register your models here.
from . import models


admin.site.register(Meta1P)
admin.site.register(Meta3P)

# class GoalAdmin(admin.ModelAdmin):
#     fields = ['name', 'description', 'goal_value', 'expected_date', 'csv_file']
#     search_fields = ['name', 'expected_date']
#     list_filter = ['name', 'expected_date']
#     list_display = ['name', 'description', 'goal_value', 'expected_date']
#     # list_editable = ['expected_date']
#
# admin.site.register(models.Goal, GoalAdmin)

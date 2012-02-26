from django.contrib import admin
from ins.models import Snippet, Task, Instruction
from guardian.admin import GuardedModelAdmin

class TaskInline(admin.TabularInline):
    model = Task
    extra = 3

class InstAdmin(GuardedModelAdmin):
    inlines = [TaskInline]

class SnippetInline(admin.TabularInline):
    model = Snippet
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    inlines = [SnippetInline]

admin.site.register(Snippet)
admin.site.register(Task, TaskAdmin)
admin.site.register(Instruction, InstAdmin)



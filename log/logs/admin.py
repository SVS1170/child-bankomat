from django.contrib import admin

from logs.models import Topic, Entry, Person

admin.site.register(Topic)

admin.site.register(Entry)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
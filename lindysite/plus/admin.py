from django.contrib import admin
from plus.models import Event, Person, Teacher, TeachesInEvent, DanceType

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "city","info_source","is_published","create_date")
    list_filter = ("is_published","info_source",)


class TeachesInEventAdmin(admin.ModelAdmin):
    list_display = ("teacher", "event")
    list_filter = ("event",)
    search_fields = ["event__name",]

class TeacherInline(admin.TabularInline):
    model = Teacher
    fk_name = 'person'

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name",)}
    list_display = ("last_name", "first_name","city")
    inlines = [
            TeacherInline,
            ]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("person", 'get_person_city','present_city','claimed','first_speciality')
    search_fields = ['person']

    def get_person_city(self,obj):
        return obj.person.city

admin.site.register(Event, EventAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeachesInEvent, TeachesInEventAdmin)
admin.site.register(Person, PersonAdmin)

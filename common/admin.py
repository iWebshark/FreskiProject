from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Example, ExampleImage, Contact

admin.site.unregister(Group)


class ExampleImageAdmin(admin.StackedInline):
    model = ExampleImage
    extra = 0


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    inlines = [ExampleImageAdmin]

    class Meta:
        model = Example


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('tag', 'value')

    class Meta:
        model = Contact

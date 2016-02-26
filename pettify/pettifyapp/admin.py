from django.contrib import admin

from .models import Animal, Selector, House
# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "category", "timestamp"]
	list_filter = ["timestamp"]
	search_fields = ["animal_name"]

	class Meta:
		model = Animal

admin.site.register(Selector)
admin.site.register(House)
admin.site.register(Animal, AnimalAdmin)
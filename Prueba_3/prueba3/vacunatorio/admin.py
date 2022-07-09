from django.contrib import admin

# Register your models here.
from vacunatorio.models import Informacion
from vacunatorio.models import Vacuna
admin.site.register(Informacion)
admin.site.register(Vacuna)
from django.contrib import admin
from .models import Math
from .models import Computer
from .models import Science
from .models import English
admin.site.register(Math)
admin.site.register(Science)
admin.site.register(Computer)
admin.site.register(English)

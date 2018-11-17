from django.contrib import admin
from .models.seance import Seance
from .models.film import Film
from .models.hall import Hall
from .models.cinema import Cinema
from .models.seance import Ticket

admin.site.register(Cinema)
admin.site.register(Film)
admin.site.register(Hall)
admin.site.register(Seance)
admin.site.register(Ticket)

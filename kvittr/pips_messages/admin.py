from django.contrib import admin
#'Picks up' the class Pip from pips_messages/models.py
from pips_messages.models import Pip

admin.site.register(Pip)
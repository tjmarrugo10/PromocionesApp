# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Promocion)
admin.site.register(Comentario)

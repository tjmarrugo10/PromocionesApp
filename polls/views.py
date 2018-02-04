# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Promocion

def index (request):
    list_promociones = Promocion.objects.all()
    context = ('list_promociones': list_promociones)
    return render(request, 'templates/index.html', context)
# Create your views here

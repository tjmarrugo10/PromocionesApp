# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Promocion

def index(request):

    lista_promociones = Promocion.objects.all()
    context = {'lista_promociones': lista_promociones}
    return render(request, 'polls/index.html', context)
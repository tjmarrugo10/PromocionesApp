# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .models import Promocion

def index (request):
    list_promociones = Promocion.objects.all()
    template = loader.get_template("index.html")
    context = Context ({'list_promociones':list_promociones})

    return HttpResponse(template.render(context))

# Create your views here

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	html_var = randint(0, 10000000)
	#return HttpResponse("fff")
	return render(request, "base.html", {"html_var" : html_var})

def home1(request):
	html_var = randint(0, 10000000)
	#return HttpResponse("fff")
	return render(request, "home1.html", {"html_var" : html_var})

def home2(request):
	html_var = randint(0, 10000000)
	#return HttpResponse("fff")
	return render(request, "home2.html", {"html_var" : html_var})

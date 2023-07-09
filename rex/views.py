from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import forms
from django.template import loader
import datetime, time, traceback
# Create your views here.
def home(request):
	template = loader.get_template('home.html')
	context = {}
	return HttpResponse(template.render(context,request))
def projects(request):
	template = loader.get_template('projects.html')
	context = {}
	return HttpResponse(template.render(context,request))
def contact(request):
	template = loader.get_template('contact.html')
	context = {}
	return HttpResponse(template.render(context,request))
def deboos(request):
	template = loader.get_template('deboos.html')
	context = {}
	return HttpResponse(template.render(context,request))
def contractr(request):
	template = loader.get_template('contractr.html')
	context = {}
	return HttpResponse(template.render(context,request))
def curatr(request):
	template = loader.get_template('curatr.html')
	context = {}
	return HttpResponse(template.render(context,request))
def votr(request):
	template = loader.get_template('votr.html')
	context = {}
	return HttpResponse(template.render(context,request))
def docify(request):
	template = loader.get_template('docify.html')
	context = {}
	return HttpResponse(template.render(context,request))
def acronymify(request):
	template = loader.get_template('acronymify.html')
	context = {}
	return HttpResponse(template.render(context,request))
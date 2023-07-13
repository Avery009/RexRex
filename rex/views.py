from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import forms
from .models import Contact
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
	if request.method == 'GET':
		form = forms.Inquiry()
		context = {
			'form' : form,
			'reqGet' : True
		}
		template = loader.get_template('contact.html')
	elif request.method == 'POST':
		form = forms.Inquiry(request.POST)
		if form.is_valid():
			cd = datetime.datetime.now()
			cp = form.cleaned_data['contact_phone']
			ce = form.cleaned_data['contact_email']
			ci = form.cleaned_data['contact_inquiry']
			try:
				c = Contact(contact_date=cd, contact_number = cp, contact_email=ce, contact_inquiry=ci)
				c.save()
				time.sleep(1)
				context = {
					'success' : True,
				}
				template = loader.get_template('home.html')
				return HttpResponse(template.render(context,request))
			except Exception as e:
				template = loader.get_template('home.html')
				context = {
					'error' : str(e)
				}
		else:
			context = {
				'error' : '701 Form Validation Error',
			
			}
			template = loader.get_template('home.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol',
		}
		template = loader.get_template('home.html')
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
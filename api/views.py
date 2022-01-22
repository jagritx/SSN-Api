from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


import json

from api.models import Socialsecurity

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response,content_type = 'text/json')

def get_details(request,id):
    if request.method == 'GET':
        try:
            entity = Socialsecurity.objects.get(ssnumber = id)
            response = json.dumps([{'Name':entity.name,'Social Security Number':entity.ssnumber,'Location':entity.location}])
        except:
            response = json.dumps([{'Error':'No such person exists'}])
    return HttpResponse(response,content_type='text/json')


@csrf_exempt
def add_person(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        ssnumber = payload['ssnumber']
        location = payload['location']
        entity = Socialsecurity(name=name,ssnumber=ssnumber,location = location)

        try:
            entity.save()
            response = json.dumps([{'Success':'Added to the database!'}])
        except:
            response = json.dumps([{'Error':"Could not be added!"}])

    return HttpResponse(response,content_type = 'text/json')
    
def delete_person(request, id):
    goodbyePerson = Socialsecurity.objects.get(ssnumber = id)
    try:
        goodbyePerson.delete()
        response = json.dumps([{ 'Success': f'Person with {id} deleted successfully!'}])
    except:
        response = json.dumps([{ 'Error': 'Person could not be deleted!'}])

    return HttpResponse(response, content_type='text/json')

   

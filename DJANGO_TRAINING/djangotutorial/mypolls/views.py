from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
import requests
import json

# Create your views here.

#def index(request):
   # return requests.response("Hello WOrld This is Aakriti")
   # data  =  {"Hello":"World","account-id" : 123456}
   # response = json.dumps(data)
    #return Response(response)
    #data = {"message": "Hello, Django REST Framework!"}
   # return Response(data)  # This returns a properly formatted response
def index(request):
    return render(request,'index.html',{'name':'Aakriti'})

def add(request):
        val1 = int(request.POST['num1']) #add int in front to make it integer.
        val2 = int(request.POST['num2']) #withouth int, it was calculated as string so when added 2+2 , we aere getting 22 instead of 4.
        res = val1 + val2
        return render(request, 'result.html', {'result' :res})

  

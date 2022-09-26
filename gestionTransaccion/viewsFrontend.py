from cgitb import reset
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def principal(request):
    return render(request,"administrador.html")
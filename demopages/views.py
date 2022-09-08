from pickletools import read_string1
from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("Hello, world")

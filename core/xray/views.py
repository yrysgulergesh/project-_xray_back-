from django.shortcuts import render, HttpResponse, redirect, get_object_or_404


def homepage(request):
    return render(request, 'index.html')
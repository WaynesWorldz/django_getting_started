from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory

from meetings.models import Meeting, Room, Drivers


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I am me")


def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
                  {"rooms": Room.objects.all()})


def drivers_list(request):
    return render(request, "meetings/drivers_list.html",
                  {"rooms": Drivers.objects.all()})


DriverForm = modelform_factory(Drivers, exclude=[])


def drivers(request):
    if request.method == "POST":
        # form has been submitted, process data
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("drivers")
    else:
        form = DriverForm()
    return render(request, "meetings/drivers.html", {"form": form})
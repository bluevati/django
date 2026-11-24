from django.shortcuts import render
from .models import Flight,Passengers
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })

def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passenger_id= int(request.POST["passenger"])
        passenger=Passengers.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",arg=(flight.id,)))


def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    passengers=flight.passengers.all()
    non_passengers=flight.objects.exclude(flights=flight).all()
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":passengers,
        "non_passengers": non_passengers
    })
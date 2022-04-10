from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight,Airport,Passenger
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Poll does not exist")
    #flight = Flight.objects.filter(pk=flight_id)
    #flight = Flight.objects.get(id=flight_id)
    passenger=flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":passenger,
        "non_passengers":non_passengers,
    })


def book(request,flight_id):
    if request.method == 'POST':
        flight=Flight.objects.get(pk=flight_id)
        passenger_id = request.POST.get('passengerid', False)
        if passenger_id == False:
            return HttpResponseRedirect(reverse('flight',args=(flight_id,)))
        else:
        #passenger_id=int(request.POST['passengerid'])
            passenger=Passenger.objects.get(pk=passenger_id)
            passenger.flights.add(flight)
            return HttpResponseRedirect(reverse('flight',args=(flight_id,)))
    else:
        return HttpResponse("Error")
        #return HttpResponseRedirect(reverse('flight',args=(flight_id,)))


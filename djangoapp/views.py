from datetime import datetime
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logut

from . import forms, models



from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



def index(request):

    return render(request, 'index.html')


def travels(request):

    if 'type' in request.GET:
        travels = models.Travel.objects.filter(vehicle__vehicle_type=request.GET['type'])

    else:
        travels = models.Travel.objects.filter(datetime__gte=datetime.now())


    response = {
        'travels': travels
    }

    return render(request, 'travels.html', response)



def travel(request, id):

    if request.method == 'POST':
        ticketform = forms.TicketForm(request.POST)
        ticket = ticketform.save()

        return redirect(f'/ticket/{ticket.id}')

    travel = models.Travel.objects.get(id=id)
    seats = set(range(1, 1 + travel.vehicle.capacity)) - \
                set([i.seat_number for i in list(models.Ticket.objects.filter(travel=id))])

    response = {
        'travel': travel,
        'info':{
            'seats': seats,
            'free': len(seats),
        }
    }

    return render(request, 'travel.html', response)



def ticket(request, id):
    ticket = models.Ticket.objects.get(id=id)

    response = {
        'ticket': ticket,
        'travel': ticket.travel,
    }
    return render(request, 'ticket.html', response)




@login_required(login_url='/login/')
def panel(request):
    if request.method == 'POST':
        if 'new_vehicle' in request.POST:
            form = forms.VehicleForm(request.POST)
            form.save()

        elif 'new_travel' in request.POST:
            origin = request.POST['origin']
            destination = request.POST['destination']
            price = request.POST['price']
            vehicle = request.POST['vehicle']
            datetime = request.POST['datetime']
            is_two_way = 'is_two_way' in request.POST

            t = models.Travel(origin=origin, destination=destination, price=price, datetime=datetime, vehicle_id=vehicle, is_two_way=is_two_way)
            t.save()


    vehicles = models.Vehicle.objects.filter(admin=request.user.id)
    travels = models.Travel.objects.filter(vehicle__admin=request.user.id)

    response = {
        'vehicles': vehicles,
        'travels': travels,
    }

    return render(request, 'panel.html', response)




def travel_edit(request, id):
    foundTravel = models.Travel.objects.get(id=id)

    if request.method == 'POST':
        foundTravel.origin = request.POST['origin']
        foundTravel.destination = request.POST['destination']
        foundTravel.price = request.POST['price']
        foundTravel.vehicle_id = request.POST['vehicle']
        foundTravel.is_two_way = 'is_two_way' in request.POST

        foundTravel.save()

    vehicles = models.Vehicle.objects.filter(admin=request.user.id)

    response = {
        'travel': foundTravel,
        'vehicles': vehicles,
    }
    return render(request, 'travel_edit.html', response)





def travel_delete(request, id):
    foundTravel = models.Travel.objects.get(id=id)
    foundTravel.delete()

    return redirect('/panel/')




def vehicle_delete(request, id):
    foundVehicle = models.Vehicle.objects.get(id=id)
    foundVehicle.delete()
    return redirect('/panel/')





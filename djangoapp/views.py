from datetime import datetime

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

from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.template import loader

from .models.cinema import Cinema
from .models.hall import Hall
from .models.film import Film
from .models.seance import Seance
from .models.seance import Ticket


def index(request):
    template = loader.get_template('default/form.html')
    try:
        booked_seates = {}
        for ticket in Ticket.objects.all():
            booked_seates[ticket.place] = 1

        context = {
            'cinemas': Cinema.objects.all(),
            'halls': Hall.objects.all(),
            'films': Film.objects.all(),
            'seances': Seance.objects.all(),
            'booked_seats': booked_seates,
        }

    except (Film.DoesNotExist, Hall.DoesNotExist):
        raise Http404("Page does not exist")

    return HttpResponse(template.render(context, request))


def order(request):
    seance_id = request.POST['seance']cd
    place = request.POST['place']
    user_name = request.POST['user_name']
    user_phone = request.POST['user_phone']
    user_email = request.POST['user_email']
    o = Ticket(seance_id=seance_id, place=place, user_name=user_name, user_email=user_email, user_phone=user_phone)
    o.save()
    return redirect('/success')


def success(request):
    template = loader.get_template('default/success.html')
    return HttpResponse(template.render({}, request))

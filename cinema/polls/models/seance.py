from django.db import models
import random
import names

from .film import Film
from .hall import Hall


class Seance(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.TimeField(blank=True)

    def __str__(self):
        return self.film.name + ' ' + self.hall.cinema.name + ' ' + self.hall.name + ' ' + self.time.strftime("%H:%M")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for seat in range(self.hall.capacity):
            if not seat:
                continue
            if random.getrandbits(1) == 1:
                ticket = Ticket(seance=self,
                                place=seat,
                                user_name=names.get_full_name(),
                                user_phone=Seance.generate_random_number(),
                                user_email=Seance.generate_random_email()
                                )

                print(ticket.user_phone)
                print(ticket.user_name)
                print(ticket.user_email)
                ticket.save()

    @staticmethod
    def generate_random_number():
        number = ''
        for x in range(10):
            number += str(random.randint(0, 10))

        return number

    @staticmethod
    def generate_random_email():
        return names.get_last_name().lower() + '@gmail.com'


class Ticket(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    place = models.IntegerField()
    user_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user_name + " " + self.user_phone + " place #" + str(self.place)



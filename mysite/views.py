from django.shortcuts import render, redirect


from .models import Attendee
from .forms import AttendeeForm
from btc_admin.models import Session

def index(request):
    session = Session.objects.latest('week_start')
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')

        if date1 == 'true':
            date1 = True
            date1_confirmed = session.tuesday
            print(date1_confirmed)
        else:
            date1 = False
            date1_confirmed = '2010-01-01'

        if date2 == 'true':
            date2 = True
            date2_confirmed = session.thursday
            print(date2_confirmed)
        else:
            date2 = False
            date2_confirmed = '2010-01-01'

        if date1 or date2:
            Attendee.objects.create(
                fullname = fullname,
                email = email,
                date1 = date1,
                date2 = date2,
                date1_confirmed = date1_confirmed,
                date2_confirmed = date2_confirmed
            ).save()

            form = AttendeeForm()

            context = {
                'form': form,
            }
            return render(request, 'index.html', context)
    else:
        form = AttendeeForm()
        session = Session.objects.latest('week_start')

        context = {
                'form': form,
                'session': session
        }
        return render(request, 'index.html', context)

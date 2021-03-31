from django.shortcuts import render
import datetime
from django.http import HttpResponse

from .forms import IndexCardForm

#important views:
 # Home Page
 # Profile
 # Key
 # This Week
 # Today

def index(request):
    return HttpResponse('Blank Page')

#Home Page
def index_card_view(request):
    if request.method == 'POST':
        form = IndexCardForm(request.POST)
        if form.is_valid():
            return HttpResponse(
                    'Hello {} ! Today is going to be a great day!'.format(
                        form.cleaned_data['name'],
                        )
                )
    else:
        form = IndexCardForm()
    return render(request, 'index.html', {'form': form})

def profile_view(request):
    return render(request, 'profile.html')

def key_view(request):
    return render(request, 'key.html')

def this_week_view(request):
    datetime.datetime.now()
    return render(request, 'this_week.html')

def today_view(request):
    datetime.datetime.now()
    return render(request, 'today.html')

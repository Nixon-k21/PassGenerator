from django.shortcuts import render
from django.http import HttpResponse
import random
import string
def home(request):
    return render(request,'generator/home.html', )
def password(request):

    low_letters = list(string.ascii_lowercase)
    high_letters = list(string.ascii_uppercase)
    special_symbols = list(string.punctuation)
    use_numbers = list(string.octdigits)

    if request.GET.get('uppercase'):
        low_letters.extend(list(high_letters))
    if request.GET.get('special'):
        low_letters.extend(list(special_symbols))
    if request.GET.get('numbers'):
        low_letters.extend(list(use_numbers))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(low_letters)

    return render(request,'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')
# Create your views here.

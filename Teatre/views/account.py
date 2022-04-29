from django.shortcuts import render
from Teatre.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from Teatre.validators import DNIValidator, PhoneValidator, IBANValidator


@login_required
def profile(request):
    user =request.user
    client = Client.objects.get(user=user)
    json = {'user': client ,}
    return render(request, 'User/profile.html', json)

@login_required
def edit_profile(request):
    user =request.user
    client = Client.objects.get(user=user)
    if request.method == 'GET':
        json = {'user': client ,}
        return render(request, 'User/ModifyProfile.html', json)
    elif request.method == 'POST':
        name = request.POST['name']
        DNI =request.POST['DNI']
        address = request.POST['address']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        alias = request.POST['alias']
        cardNumber = request.POST['cardNumber']

        error = validate_data(DNI, cardNumber, phoneNumber)
        if error:
            json = {'error': error, 'register': False}
            return render(request, 'registration/InvalidValues.html', json)

        if alias:
            if User.objects.filter(username=alias).exists() and not user.username == alias:
                json = {'error': 'Username already exist, you will have to choose another one.', 'register': False}
                return render(request, 'registration/InvalidValues.html', json)
            user.username = alias
        if name:
            user.first_name = name
        if email:
            user.email = email

        user.save()

        if DNI:
            client.DNI = DNI
        if cardNumber:
            client.cardNumber = cardNumber
        if phoneNumber:
            client.telephone = phoneNumber
        if address:
            client.address = address

        client.save()
        return redirect('profile')


def SignIn(request):
    if request.method == 'GET':
        return render(request, 'registration/SignIn.html')

    if request.method == 'POST':
        name = request.POST['name']
        DNI = request.POST['DNI']
        address = request.POST['address']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        alias = request.POST['alias']
        password = request.POST['password']
        cardNumber = request.POST['cardNumber']

        # Validate input data
        if not (name and DNI and address and phoneNumber and email and alias and password and cardNumber):
            # Missing values
            return render(request, 'registration/MissingValues.html')

        error = validate_data(DNI, cardNumber, phoneNumber)
        if error:
            json = {'error': error, 'register': True}
            return render(request, 'registration/InvalidValues.html', json)

        if User.objects.filter(username=alias).exists():
            json = {'error': 'Username already exist, you will have to choose another one.', 'register': True}
            return render(request, 'registration/InvalidValues.html', json)

        user = User(username=alias, email=email, first_name=name)
        user.set_password(password)
        user.save()

        client = Client.objects.get(user=user)
        client.address = address
        client.DNI = DNI
        client.cardNumber = cardNumber
        client.telephone = phoneNumber
        client.save()
        return redirect('login')


def validate_data(DNI='', cardNumber='', phoneNumber=''):
    error = ''
    if DNI:
        try:
            DNIValidator(DNI)
        except:
            error += 'DNI is not valid.'
    if cardNumber:
        try:
            IBANValidator(cardNumber)
        except:
            error += 'IBAN is not valid.   '
    if phoneNumber:
        try:
            PhoneValidator(phoneNumber)
        except:
            error += 'Phone number is not valid.   '
    return error
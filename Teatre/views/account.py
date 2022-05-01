from django.shortcuts import render

from Teatre.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Teatre.validators import DNIValidator, PhoneValidator, IBANValidator
from django.contrib.auth.decorators import user_passes_test

"""
How to check the user roles:

-Before the view function:
@user_passes_test(lambda user: user.is_active)   # Normal Client
@user_passes_test(lambda user: user.is_staff)   # Employee
@user_passes_test(lambda user: user.is_superuser) # Admin user

-Inside the view function:
if request.user.is_active:  # Normal client
if request.user.is_staff   # Employee
if request.user.is_superuser # Admin user

-Inside the html file:
# View
return render(request, 'hola.html', {'request': request})
# hola.html
{% if request.user.is_active %} # Normal client
{% if request.user.is_staff %} # Employee
{% if request.user.is_superuser %} # Admin user

"""

"""
This view shows on screen information of a logged user 
"""
@login_required
def profile(request):
    user = request.user
    client = Client.objects.get(user=user)
    json = {'user': client, }
    return render(request, 'User/profile.html', json)

"""
In this view you should be able to modify information of a logged user
Client modification
"""
@login_required
def edit_profile(request):
    # Get the logged client
    user = request.user
    client = Client.objects.get(user=user)

    # Show the form
    if request.method == 'GET':
        json = {'user': client, }
        return render(request, 'User/ModifyProfile.html', json)

    # Apply modifications
    elif request.method == 'POST':
        # Get form data
        name = request.POST['name']
        DNI = request.POST['DNI']
        address = request.POST['address']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        alias = request.POST['alias']
        cardNumber = request.POST['cardNumber']

        # Check errors
        error = validate_data(DNI, cardNumber, phoneNumber)
        if error:
            json = {'error': error, 'register': False}
            return render(request, 'registration/InvalidValues.html', json)

        # Apply changes
        if alias:
            # Check if user exists
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

"""
Creation of a new client
With this view you should be able to create a new client.
The default role of a new client is normal_user 
"""
def SignIn(request):
    # Show the form
    if request.method == 'GET':
        return render(request, 'registration/SignIn.html')

    # Create the client
    if request.method == 'POST':
        # Get form data
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

        # Check if user already exists
        if User.objects.filter(username=alias).exists():
            json = {'error': 'Username already exist, you will have to choose another one.', 'register': True}
            return render(request, 'registration/InvalidValues.html', json)

        # Create the client
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

"""
Client elimination
A logged client should be able to delete his own account
"""
@login_required
def delete_user(request):
    # Show form
    if request.method == 'GET':
        return render(request, 'User/delete_user.html', {'user': request.user})
    # Proceed to delete the client
    elif request.method == 'POST':
        user = request.user
        json = {'name': user.username,}
        client = Client.objects.get(user=user)
        client.delete()
        user.delete()
        return render(request, 'User/user_deleted.html', json)

"""
Only the superuser/admin can have access to this view.
This view provides to an admin user the tools to delete and change roles of the rest of the clients.
"""
@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_management(request):
    # Show a list of all the users
    if request.method == 'GET':
        staff_users = User.objects.filter(is_staff=True, is_superuser=False, is_active=True)
        normal_users = User.objects.filter(is_active=True, is_staff=False, is_superuser=False)
        admin_users = User.objects.filter(is_superuser=True, is_staff=True, is_active=True)
        return render(request, 'User/user_management.html', {'staff_clients': staff_users,
                                                             'normal_clients': normal_users,
                                                             'admin_clients': admin_users,
                                                             'user': request.user,})
    # Delete OR change roles of a single user.
    elif request.method == 'POST':
        # Delete client
        if 'delete' in request.POST.keys():
            user = User.objects.get(username=request.POST['delete'])
            client = Client.objects.get(user=user)
            client.delete()
            user.delete()

        # Change client role
        elif 'user_role' in request.POST.keys():
            user = User.objects.get(username=request.POST['username'])
            if request.POST['user_role'] == 'admin':
                user.is_staff = True
                user.is_active = True
                user.is_superuser = True
            elif request.POST['user_role'] == 'employee':
                user.is_staff = True
                user.is_active = True
                user.is_superuser = False
            elif request.POST['user_role'] == 'normal_client':
                user.is_staff = False
                user.is_active = True
                user.is_superuser = False

            user.save()

        return redirect('user_management')


"""
Given a DNI, cardNumber and a phoneNumber, this function validates if the given values are in a correct format
"""
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

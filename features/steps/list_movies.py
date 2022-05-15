from behave import *

@Given(u'create user staff')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    for row in context.table:

        # Register user
        user = User(username=row['alias'], email=row['email'], first_name=row['name'])
        user.set_password(row['password'])

        if row['alias'] == 'employee':
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False

        user.save()

        client = Client.objects.get(user=user)
        client.address = row['address']
        client.DNI = row['DNI']
        client.cardNumber = row['cardNumber']
        client.telephone = row['phoneNumber']
        client.save()


@Then(u'We look into the list of movies page')
def step_impl(context):
    context.browser.find_by_text('List of movies').first.click()
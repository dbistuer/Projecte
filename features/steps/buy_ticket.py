from behave import *
@Given(u'The staff has an account')
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

@Then (u'The staff is logged in the account')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('login'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()


@given(u'Exists the following room_cinema_movie')
def step_impl(context):
    from Teatre.models.movie_cinema_room_ import MovieCinemaRoom
    from Teatre.models.cinema_ import Cinema, Room
    from Teatre.models.movie_ import Movie
    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
        room = Room(number=row['number'],capacity=row['capacity'],Cinema_id=cinema.id)
        room.save()
        movie = Movie(name=row['mov_name'],gender=row['gender'],duration=row['duration'],synopsis=row['synopsis'],classification=row['classification'])

        movieCinemaRoom = MovieCinemaRoom(Cinema_id=cinema.id,Movie_id=movie.id,Room_id=room.id,date_movie=row['date_movie'])
        movieCinemaRoom.save()

@when(u'I visit the movie list')
def step_impl(context):
    context.browser.visit(context.get_url('select_tickets'))
    context.browser.find_by_value('test_click').first.click()

@then(u'I select how many tickets i want')
def step_impl(context):
    assert context.browser.url == context.get_url('buy_ticket',1)

    context.browser.find_by_name('buy').first.click()
@then(u'I confirm the ticket is bought')
def step_impl(context):
    assert context.browser.url == context.get.url('list_tickets')

    for row in context.table:
        for heading in row.headings:
            assert context.browser.is_text_present(row[heading])
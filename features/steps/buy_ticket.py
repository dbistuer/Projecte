from behave import *

@given(u'Exists the following room_cinema_movie')
def step_impl(context):
    from Teatre.models.movie_cinema_room_ import MovieCinemaRoom

    for row in context.table:
        movieCinemaRoom = MovieCinemaRoom(Cinema_id=row['Cinema'],Movie_id=row['Movie'],Room_id=row['Room'],date_movie=row['date_movie'])
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
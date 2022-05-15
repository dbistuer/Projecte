from behave import *

@Given(u'Add movie to database')
def step_impl(context):
    from Teatre.models.movie_ import Movie
    from Projecte.settings.base import BASE_DIR
    movie = Movie(name='test',duration=120,synopsis='test synopsis',classification='X',gender='War',image=str(BASE_DIR)+'\'features\'image\'test.png')
    movie.save()
    assert Movie.objects.filter(name='test').exists()

@When(u'We look into the list of movies page')
def step_impl(context):
    context.browser.find_by_text('List of movies').first.click()

@then(u'Pick on action button detail of one movie')
def step_impl(context):
    context.browser.find_by_text('Detail').first.click()
    finaly(context)


def finaly(context):
    from Teatre.models.movie_ import Movie
    movie = Movie.objects.get(name='test')
    movie.delete()
    context.browser.find_by_text('Home').first.click()
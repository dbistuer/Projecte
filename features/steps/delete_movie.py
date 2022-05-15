from behave import *

@Then(u'Create a movie on database and go to detail page')
def step_impl(context):
    from Teatre.models.movie_ import Movie
    from Projecte.settings.base import BASE_DIR
    movie = Movie(name='test', duration=120, synopsis='test synopsis', classification='X', gender='War',
                  image=str(BASE_DIR) + '\'features\'image\'test.png')
    movie.save()
    assert Movie.objects.filter(name='test').exists()
    context.browser.find_by_text('List of movies').first.click()
    context.browser.find_by_text('Detail').first.click()

@Given(u'push delete and verify that has been deleted')
def step_impl(context):
    from Teatre.models.movie_ import Movie
    context.browser.find_by_text('Delete').first.click()
    assert not Movie.objects.filter(name='test').exists()
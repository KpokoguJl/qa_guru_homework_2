import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def before_all(browser_settings):
    print('\nБраузер сконфигурирован!')


@pytest.fixture(autouse=True)
def before_each(browser_settings):
    browser.open('/')
    print('\nОткрыта страница!')


def test_valid_search():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_invalid_search():
    browser.element('[name="q"]').should(be.blank).type('gjksdhgklhjsdfgkljdfshgklsdfjglfksdghlksdfghldfksgh').press_enter()
    browser.element('[class="card-section"]').should(have.text('gjksdhgklhjsdfgkljdfshgklsdfjglfksdghlksdfghldfksgh'))

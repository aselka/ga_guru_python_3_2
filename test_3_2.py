import pytest
from selene import be, have
from selene.support.shared import browser


def test_positive_search():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI'))


def test_negative_search_():
    browser.element('[name="q"]').should(be.blank).type('nvjnvfvmk').press_enter()
    browser.element('p[aria-level]').should(have.text('По запросу nvjnvfvmk ничего не найдено'))
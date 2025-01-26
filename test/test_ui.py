import allure
import time
from Ui.MainPage import MainPage
from testdata.DataProvider import DataProvider


data_provider = DataProvider()

film_name = data_provider.get("film")
actor_name = data_provider.get("actor")
serial_name = data_provider.get("serial")
collection_name = data_provider.get("collection")
country_name = data_provider.get("country")


@allure.feature('Поиск фильмов')
@allure.story('Поиск фильма по имени')
@allure.severity(allure.severity_level.NORMAL)
def test_find_film():
    kinopoisk = MainPage()
    kinopoisk.go()
    time.sleep(15)
    result = kinopoisk.find_in(film_name)
    assert result == film_name


@allure.feature('Актеры')
@allure.story('Открытие страницы с наградами актера')
@allure.severity(allure.severity_level.HIGH)
def test_open_awards():
    kinopoisk = MainPage()
    kinopoisk.go()
    time.sleep(15)
    kinopoisk.find_in(actor_name)
    result = kinopoisk.open_awards()
    assert result == f'{actor_name} — награды и кинопремии — Кинопоиск'


@allure.feature('Коллекции')
@allure.story('Открытие коллекции фильмов')
@allure.severity(allure.severity_level.NORMAL)
def test_open_collection():
    kinopoisk = MainPage()
    kinopoisk.go()
    time.sleep(15)
    result = kinopoisk.go_to_collection()
    assert result == collection_name


@allure.feature('Поиск сериалов')
@allure.story('Поиск сериалов по имени')
@allure.severity(allure.severity_level.NORMAL)
def test_find_serial():
    kinopoisk = MainPage()
    kinopoisk.go()
    time.sleep(15)
    result = kinopoisk.find_in(serial_name)
    assert result == serial_name


@allure.feature('Поиск по странам')
@allure.story('Поиск фильмов по Австралии')
@allure.severity(allure.severity_level.NORMAL)
def test_find_by_Australia():
    kinopoisk = MainPage()
    kinopoisk.go()
    time.sleep(15)
    result = kinopoisk.find_by_Australia()
    assert result == country_name

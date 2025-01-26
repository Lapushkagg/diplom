import allure
from api.BoardsApi import BoardApi
from testdata.DataProvider import DataProvider

data_provider = DataProvider()

film_name = data_provider.get("film")
actor_name = data_provider.get("actor")


@allure.feature('Фильмы')
@allure.story('Поиск фильма по имени')
@allure.severity(allure.severity_level.NORMAL)
def test_find_film_by_name():
    kinopoisk = BoardApi()
    result = kinopoisk.find_film(film_name)
    assert result == film_name


@allure.feature('Фильмы')
@allure.story('Поиск случайного фильма')
@allure.severity(allure.severity_level.NORMAL)
def test_find_random_film():
    kinopoisk = BoardApi()
    result = kinopoisk.get_random()
    assert result == 200


@allure.feature('Актеры')
@allure.story('Поиск актера по имени')
@allure.severity(allure.severity_level.NORMAL)
def test_find_actor_by_name():
    kinopoisk = BoardApi()
    result = kinopoisk.find_actor(actor_name)
    assert result == actor_name


@allure.feature('Награды')
@allure.story('Получение наград актера')
@allure.severity(allure.severity_level.NORMAL)
def test_get_awards():
    kinopoisk = BoardApi()
    result = kinopoisk.get_awards()
    assert result == 200


@allure.feature('Коллекции')
@allure.story('Получение коллекций')
@allure.severity(allure.severity_level.NORMAL)
def test_get_collections():
    kinopoisk = BoardApi()
    result = kinopoisk.get_collections()
    assert result == 200

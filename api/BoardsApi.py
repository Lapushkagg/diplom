import requests
import configparser


class BoardApi:
    def __init__(self, config_file="test_config.ini") -> None:
        config = configparser.ConfigParser()
        config.read(config_file)
        self.base_url = config["api"]["base_url"]
        self.KEY = config["api"]["KEY"]

    def find_film(self, name: str) -> dict:
        url = f"{self.base_url}v1.4/movie/search"
        headers = {
            "X-API-KEY": self.KEY
        }
        params = {
            "page": 1,
            "limit": 10,
            "query": name
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()["docs"][0]["name"]

    def get_random(self):
        url = f"{self.base_url}v1.4/movie/search"
        headers = {
            "X-API-KEY": self.KEY
        }
        response = requests.get(url, headers=headers)
        return response.status_code

    def find_actor(self, name: str) -> dict:
        url = f"{self.base_url}v1.4/person/search"
        headers = {
            "X-API-KEY": self.KEY
        }
        params = {
            "page": 1,
            "limit": 10,
            "query": name
        }
        response = requests.get(url, params=params, headers=headers)
        return response.json()["docs"][0]["name"]

    def get_awards(self):
        url = f"{self.base_url}v1.4/person/awards"
        headers = {
            "X-API-KEY": self.KEY
        }
        response = requests.get(url, headers=headers)
        return response.status_code

    def get_collections(self):
        url = f"{self.base_url}v1.4/list"
        headers = {
            "X-API-KEY": self.KEY
        }
        response = requests.get(url, headers=headers)
        return response.status_code

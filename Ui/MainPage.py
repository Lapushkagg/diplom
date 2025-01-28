import allure
import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class MainPage:
    def __init__(self, config_file="test_config.ini", driver_path="path/to/chromedriver.exe") -> None:
        config = configparser.ConfigParser()
        config.read(config_file)
        self.base_url = config["ui"]["base_url"]
        self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.__driver.maximize_window()

    def go(self):
        self.__driver.get(self.base_url)

    @allure.step("Найти в поиске")
    def find_in(self, text: str) -> str:
        search_box = self.__driver.find_element(By.NAME, "kp_query")
        search_box.click()
        search_box.send_keys(text)
        self.__driver.find_element(
            By.CSS_SELECTOR,
            ".styles_iconActive__dJx1_.styles_icon__1bYKL"
        ).click()
        element = self.__driver.find_element(By.CSS_SELECTOR,
                                             ".search_results_topText b").text
        return element

    @allure.step("Перейти в награды")
    def open_awards(self) -> str:
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.element.most_wanted .name a'))
        ).click()

        self.__driver.execute_script("window.scrollBy(0, 1000);")

        WebDriverWait(self.__driver, 10).until(
          EC.element_to_be_clickable((
            By.XPATH,
            "/html/body/div[1]/div[1]/div[2]/div[4]/div/div/div[1]/"
            "div/div/div[1]/nav/ul/li[6]/a"
           ))
        ).click()

        element = self.__driver.title
        return element

    @allure.step("Перейти в коллекцию")
    def go_to_collection(self) -> str:
        self.__driver.find_element(
            By.XPATH,
            "//div[@class='styles_sidebarContainer__dxNPY']"
            "//a[text()='Фильмы']"
        ).click()
        self.__driver.execute_script("window.scrollBy(0, 1000);")
        link = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Фильмы про вампиров']]"))
        )
        link.click()
        element = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main h1"))
        ).text
        return element

    @allure.step("Сделать фильтрацию фильмов по стране Австралия")
    def find_by_Australia(self) -> str:
        self.__driver.find_element(
            By.CSS_SELECTOR,
            ".styles_advancedSearchIconActive__4bcK9"
        ).click()
        country = Select(self.__driver.find_element(By.ID, "country"))
        country.select_by_value("25")
        self.__driver.find_element(
            By.CSS_SELECTOR,
            "input.el_18.submit.nice_button"
        ).click()
        element = self.__driver.find_element(By.CSS_SELECTOR, "h1 span").text
        return element
    
    def close(self):
        self.__driver.quit()


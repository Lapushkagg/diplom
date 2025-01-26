# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Внимание! time.sleep(15) в ui тестах используется для ввода капчи!

### Шаги:
1. Склонировать проект 'git clone https://github.com/Lapushkagg/diplom.git'
2. Установить зависимости `pip install -r requirements.txt`
3. Запустить тесты 'python -m pytest'
   - Для запуска только api тестов : python -m pytest test\test_api.py 
   - Для запуска только ui тестов : python -m pytest test\test_ui.py 
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД (?)
./configuration - провайдер настроек
- test_config.ini - настройки для тестов
./testdata - провайдер тестовых данных
- test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/cheat-sheet/)  
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)  
- [Про configparser](https://docs.python.org/3/library/configparser.html#module-configparser)  
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests



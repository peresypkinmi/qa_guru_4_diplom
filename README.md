# Проект автотестов для https://kz.siberianwellness.com/kz-ru/

## UI + API  автотесты
* Тесты авторизации
    * ✅ Авторизация по номеру телефона UI
    * ✅ Авторизация по контракту UI
    * ✅ Ошибка авторизации - введен неверный пароль UI
    * ✅ Проверка схемы ответа авторизации API
* Тесты на работу с корзиной
    * ✅ Добавление товара в корзину без авторизации UI
    * ✅ Добавление товара в корзину авторизованного пользователя UI+API


## Применнные технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/labels/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/labels/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/labels/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/labels/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/labels/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/labels/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/labels/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/labels/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/labels/allure.png"></code>
  <code><img width="5%" title="Telegram" src="resources/labels/tg.png"></code>
</p>




## Запуск тестов
### Локально
Склонировать проект. Через консоль в папке проекта выполнить команду:
```
pytest
```

### Удаленно
```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry --version
poetry install --no-root
poetry update
pytest .

```

## <img width="6%" title="Jenkins" src="resources/labels/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/004-miihaNSK-diplom/)
Запуск тестов из Jenkins:
Добавить проект в Jenkins и нажать кнопку "Собрать сейчас".

<p><img src="resources/screenshots/jenkins_screen.jpg" alt="Jenkins"/></p>

Нажать на иконку Allure возле завершившегося процесса для просмотра отчета

<p><img src="resources/screenshots/chrome_37wxhxSSAY.png" alt="Allure in Jenkins"/></p>


### <img width="6%" title="Allure" src="resources/logo/allure.png"> [Allure](https://jenkins.autotests.cloud/job/qa_guru_python_4_25/allure/)

#### Примеры отчетов

<img src="resources/screenshots/chrome_svRy4SokZf.png" alt="Allure"/>

<img src="resources/screenshots/chrome_0fD0R4DN59.png" alt="Allure"/>

### <img width="6%" title="Telegram" src="resources/logo/tg.png"> Telegram

#### Настроена отправка отчета в Telegram

<img src="resources/screenshots/Telegram_XIvtt3wAXC.png" alt="Telegram"/>


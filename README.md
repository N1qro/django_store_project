# Тестовый проект веб приложения на Django
![Main check](https://github.com/N1qro/django_store_project/actions/workflows/python-package.yml/badge.svg?branch=main)  
### Инструкция по запуске в dev режиме на WINDOWS:

> 1. Перед первым запуском создаём окружение через ***"env-creator.bat"***

> 2. Файл **.env** в папке **/lyceum** заполнить соответственно:
```
ALLOWED_HOSTS = Хост1, Хост2, ...
INTERNAL_IPS = IP1, IP2, ...
DEBUG = <True/False>
ENABLE_COFFEE_MIDDLEWARE = <True/False>
SECRET_KEY = "..."
```

> 3. Для запуска сервера открыть ***"server-starter.bat"*** в папке проекта

### Зависимости

***requirements.txt*** - Содержит библиотеки для корректного запуска сервера. Устанавливаются после запуска ***env-creator.bat***  
***requirements-dev.txt*** - Дополнительные инструменты для удобства разработки (Black)  
***requirements-test.txt*** - Содержит библиотеки для тестирования. (PyTest)

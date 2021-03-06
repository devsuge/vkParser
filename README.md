# vkParser
_vkParser-сервис для получения списка друзей пользователя в Вконтакте_ — это приложение, которое выгражует отчет формата (CSV, TSV, JSON) о друзьях заданного пользователя Вконтакте
# Оглавление

1. [Установка зависимостей](#Установка_зависимостей)
2. [Запуск скрипта](#Запуск_скрипта)
3. [API ВКонтакте](#Vk_API)
4. [Методы](#Методы)


# Установка_зависимостей

Для установки зависимостей необходимо в терминале virtuallenv выполнить
	
```
pip3 install -r requirements.txt
```

# Запуск_скрипта

Чтобы запустить скрипт необходимо выполнить python-файл main.py

```
./python main.py
```	

# Vk_API

Подробнее: https://vk.com/dev

## Как_получить_токен

Токен - это ключ, который требуется для работы со всеми методами Vk_API, за исключением методов секции secure.

Ключ доступа — своего рода «подпись» пользователя в приложении. Он сообщает серверу, от имени какого пользователя осуществляются запросы, и какие права доступа он выдал приложению.

Получить ключ доступа пользователя можно одним из этих способов:

1. [Implicit flow. Для работы с API от имени пользователя в Javascript-приложениях и Standalone-клиентах (десктопных или мобильных)](https://vk.com/dev/implicit_flow_user)
2. [Authorization code flow. Для работы с API от имени пользователя с серверной стороны Вашего сайта](https://vk.com/dev/authcode_flow_user)

# Методы

Все необходимые методы вызываются в `main.py`

Список файлов:

1. [Файл настроек](#settings)
2. [Файл работы с API](#vk_api_only)
3. [Файл обработки отчета](#report)

## settings

Файл `settings.py` имеет один метод `get_settings()`, который возвращает первоначальные настройки приложения:

1. Токен пользователя: `token`
2. Id пользователя отчета: `u_id`
3. Формат файла: `format`


## vk_api_only

Файл `vk_api_only.py` имеет один метод `get_fiends(token, u_id)`, который возвращает необработанный список данных друзей пользователя с полями:

1. ФИО пользователя вместе с ником: `nickname`
2. Указанная страна пользователя: `country`
3. Указанный город пользователя: `city`
4. Указанная дата рождения пользователя: `bdate`
5. Указанный пол пользователя: `sex`

## report

Файл `report.py` ключает в себя методы обработки сырой информации из Vk_API и формирования отчета в файл:
Список методов:

1. [Метод предстваления данных в DataFrame](#list_to_df)
2. [Метод обработки сырых данных к требованию отчета](#full_refactor)
3. [Метод обработки данных пола пользователя](#refactor_sex)
4. [Метод обработки данных локации пользователя](#refactor_dict_location)
5. [Метод обработки данных даты рождения пользователя](#refactor_date)
6. [Метод сохранения отчета в файл](#save_report)

### list_to_df

Данный метод преобразует `list` в DataFrame с столбцами:

1. Имя пользователя `first_name`
2. Фамилия пользователя `last_name`
3. Страна пользователя `country`
4. Город пользователя `city`
5. Дата рождения пользователя `bdate`
6. Пол пользователя `sex`
Остальные данные в list не учитываются, так как не входят в требования отчета 

### full_refactor

Данный метод преобразует значения `data_df` к виду требуемому в отчете. Значения требующие преобразования:

1. `country` - необходимо преобразовать `dict` -> `str`
2. `city` - необходимо преобразовать `dict` -> `str`
3. `bdate` - необходимо преобразовать `str` -> `str(ISO)`
4. `sex` - необходимо преобразовать `int` -> `str`

### refactor_sex

Данный метод преобразует значения `sex` к виду требуемому в отчете.
Возращает `str`: `Female` или `Male`, если пол пользователя скрыт метод возвратит `Unknown`

### refactor_dict_location

Данный метод преобразует значения `dict_location` к виду требуемому в отчете.
Возращает `str`, где указан только `title` локации, если же локация будет скрыта метод возвратит `Unknown`

### refactor_date

Данный метод преобразует значения `date` к виду требуемому в отчете.
Возращает `str(ISO)` полные и короткие даты рождения, если же дата будет скрыта метод возвратит `0001-01-01`

### save_report

Данный метод сохраняет `df_data` в файл формата `format`, если же формат будет некорректно указан, то метод возвратит `ValueError`

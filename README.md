# Prettify JSON


Output of json format data in a readable form

# Quickstart

pprint_json.py data.json

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
#
File data - {"Cells":{"Address": "улица Академика Павлова, дом 10","AdmArea": "Западный административный округ","ClarificationOfWorkingHours": null,"District": "район Кунцево","IsNetObject": "да","Name": "Ароматный Мир","OperatingCompany": "Ароматный Мир","PublicPhone": [{"PublicPhone": "(495) 777-51-95"}],"TypeService": "реализация продовольственных товаров","WorkingHours": [{"DayOfWeek": "понедельник","Hours": "09:30-22:30"}


Result - {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                }
                }
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

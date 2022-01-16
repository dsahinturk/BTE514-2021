import csv
import json
import requests


def file_operations():
    print("******************* File operations ******************")
    with open("deneme.txt", "a+", encoding="utf-8") as my_file:
        # for line in my_file:
        #    print(line, end="")
        my_file.write("ABC DEF\n")
        my_file.seek(8)
        contents = my_file.read(2)
        print(contents)
    print("******************* File operations ******************\n")


def csv_files():
    print("******************* CSV Processing ******************")
    # Aşağıdaki kodlar için grades.csv dosyası oluşturmanız gerekir
    with open("grades.csv") as csv_file:
        my_csv = csv.reader(csv_file)
        csv_as_list = list(my_csv)
        print(csv_as_list)

    with open("grades.csv") as csv_file:
        my_csv = csv.DictReader(csv_file)
        csv_as_dict = list(my_csv)
        print(csv_as_dict)

    # Ornek python doc'lardan alınmıştır
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    print("******************* CSV Processing ******************\n")


def json_files():
    print("******************* JSON Processing ******************")
    my_weather = json.loads(
        r'{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}')
    with open("weather.json", "w") as wj:
        wj.write(json.dumps(my_weather))

    cities = ['Ankara', 'Bursa', 'Boston']
    str_req = r"http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}"
    # Aşağıdaki satır için kendi API_KEY'inizi edinmeniz gerekecektir
    api_key = ""
    for city in cities:
        response = requests.get(str_req.format(city, api_key))
        my_weather = response.json()
        print(city + " temp=", float(my_weather['main']['temp']) - 273)

    print("******************* JSON Processing ******************\n")

"""Contain devices data """

data = [
    {
        "id": "1",
        "temperature": "23 c",
        "humidity": "90%",
        "lat": 25.243143273449427,
        "lng": 55.32663345336914,
        "name": "sensor-1",
        "status": "on",
        "totalPowerConsumption": "23 kw"
    },
    {
        "id": "2",
        "temperature": "21 c",
        "humidity": "92%",
        "lat": 25.12235,
        "lng": 55.37482,
        "name": "sensor-2",
        "status": "off",
        "totalPowerConsumption": "22 kw"
    },
    {
        "id": "3",
        "temperature": "25 c",
        "humidity": "88%",
        "lat": 25.31245,
        "lng": 55.29012,
        "name": "sensor-3",
        "status": "on",
        "totalPowerConsumption": "26 kw"
    },
    {
        "id": "4",
        "temperature": "19 c",
        "humidity": "85%",
        "lat": 25.21234,
        "lng": 55.33412,
        "name": "sensor-4",
        "status": "off",
        "totalPowerConsumption": "18 kw"
    },
    {
        "id": "5",
        "temperature": "22 c",
        "humidity": "91%",
        "lat": 25.32145,
        "lng": 55.38923,
        "name": "sensor-5",
        "status": "on",
        "totalPowerConsumption": "20 kw"
    },
    {
        "id": "6",
        "temperature": "27 c",
        "humidity": "87%",
        "lat": 25.19876,
        "lng": 55.40123,
        "name": "sensor-6",
        "status": "on",
        "totalPowerConsumption": "28 kw"
    },
    {
        "id": "7",
        "temperature": "20 c",
        "humidity": "89%",
        "lat": 25.34567,
        "lng": 55.26789,
        "name": "sensor-7",
        "status": "off",
        "totalPowerConsumption": "19 kw"
    },
    {
        "id": "8",
        "temperature": "24 c",
        "humidity": "86%",
        "lat": 25.15678,
        "lng": 55.42345,
        "name": "sensor-8",
        "status": "on",
        "totalPowerConsumption": "25 kw"
    },
    {
        "id": "9",
        "temperature": "26 c",
        "humidity": "84%",
        "lat": 25.28765,
        "lng": 55.37890,
        "name": "sensor-9",
        "status": "off",
        "totalPowerConsumption": "21 kw"
    },
    {
        "id": "10",
        "temperature": "18 c",
        "humidity": "93%",
        "lat": 25.17654,
        "lng": 55.34567,
        "name": "sensor-10",
        "status": "on",
        "totalPowerConsumption": "17 kw"
    }
]
device_details = {
    "id": "1",
    "lat": 25.243143273449427,
    "lng": 55.32663345336914,
    "name": "sensor-1",
    "status": "on",
    "temperature": "23 c",
    "humidity": "90%",
    "totalPowerConsumption": "23 kw",
    "monthlyPowerConsumption": {  # Changed key name to avoid duplicate
        "jan": "24 kw",
        "feb": "21 kw",
        "march": "22 kw",
        "april": "28 kw",
        "may": "29 kw",
        "june": "31 kw",
        "july": "34 kw",
        "august": "23 kw",
        "september": "44 kw",
        "october": "41 kw",
        "november": "24 kw",
        "december": "21 kw"
    }
}
from datetime import datetime, timedelta
import pandas
import requests
import math
import os

KIWI_API = os.environ.get("KIWI_API")
cities_request = pandas.read_csv("Flight Deals - prices.csv")
CODES = [cities_request["IATA Code"].to_dict()[key] for key in cities_request["IATA Code"].to_dict()]

header = {
    "apikey": KIWI_API,
}


class FlightSearch:
    def __init__(self):
        self.from_place = "DFW"
        self.prices = []
        self.links = []
        self.keypoint = []
        self.dateFrom = datetime.now().strftime("%d/%m/%Y")
        self.dateTo = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.N = 0

    def deal_search(self):

        IATA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search?"

        for place in CODES:
            IATA_PARAMETERS = {
                "fly_from": "DFW",
                "fly_to": place,
                "dateFrom": self.dateFrom,
                "dateTo": self.dateTo,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "max_fly_duration": 20,
                "flight_type": "round",
                "curr": "USD",
                "selected_cabins": "M",
                "adults": 1,
                "one_for_city": 0,
                "one_per_date": 0,
                "price_from": 50,
                "vehicle_type": "aircraft",
                "max_stopovers": 4,
                "max_sector_stopovers": 4,
            }

            response = requests.get(url=IATA_ENDPOINT, params=IATA_PARAMETERS, headers=header)
            try:
                self.prices.append(response.json()['data'][0]['conversion']['USD'])
                self.links.append(response.json()['data'][0]["deep_link"])
                print(f"{self.N}% Complete")
            except IndexError:
                response = requests.get(url=IATA_ENDPOINT, params=IATA_PARAMETERS, headers=header)
                self.prices.append(response.json()['data'][0]['conversion']['USD'])
                self.links.append(response.json()['data'][0]["deep_link"])
            self.N += math.ceil(100 / int(len(CODES)))

        cities_request["Lowest Price"] = self.prices
        cities_request["Links"] = self.links

    def publish_prices(self):
        cities_request.to_csv("Flight Deals - links.csv", index=False)


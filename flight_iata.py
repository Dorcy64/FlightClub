import requests
import pandas
import os

KIWI_API = os.environ["KIWI_API"]
ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
header = {
    "apikey": KIWI_API,
}
cities_request = pandas.read_csv("Flight Deals - prices.csv")


class FlightData:
    def __init__(self):
        self.CITIES = [cities_request["City"].to_dict()[key] for key in cities_request["City"].to_dict()]
        self.CODES = []
        self.ID = 1

    def fetch_codes(self):
        for city in self.CITIES:
            parameters = {
                "term": city,
                "location_types": "airport",
                "limit": 10,
                "active_only": "true"
            }
            response = requests.get(url=ENDPOINT, params=parameters, headers=header)
            try:
                self.CODES.append(response.json()["locations"][0]["id"])
            except IndexError:
                print(f"{city} airport is unavailable,  try to get more precise")

        print(self.CODES)
        print("To publish the codes run .publish_codes")

    def publish_codes(self):
        cities_request["IATA Code"] = self.CODES
        cities_request.to_csv("Flight Deals - prices.csv", index=False)

        print(cities_request)



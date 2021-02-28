import flight_iata
import get_flight_deals
import get_upload_csv
import check_send
import pandas


# When Looking For New City Codes Use This:
# # new = flight_iata.FlightData()
# # new.fetch_codes()
# # new.publish_codes()
check_deals = check_send.Deals()


flight_prices = get_flight_deals.FlightSearch()
flight_prices.deal_search()

check_deals.check(generated_deals=flight_prices.prices, links=flight_prices.links)

# Upload files to google sheets
# # flight_prices.publish_prices()
# # check = get_upload_csv.Upload()
# # check.upload()


# mailing_list = pandas.read_csv("mailing_list.csv")
# print(mailing_list)
# for name in mailing_list.to_dict()["Name"]:
#     print(mailing_list.to_dict()["Name"][name])
#     print(mailing_list.to_dict()["Email"][name])

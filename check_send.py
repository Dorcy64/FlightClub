import pandas
import smtplib
import os

deals = pandas.read_csv("Flight Deals - prices.csv")


class Deals:
    def __init__(self):
        self.LOWEST_PRICES = [deals["Lowest Price"].to_dict()[key] for key in deals["Lowest Price"].to_dict()]
        self.CITIES = [deals["City"].to_dict()[key] for key in deals["City"].to_dict()]
        self.deal_position = []

    def check(self, generated_deals, links):

        for x in range(0, (len(self.LOWEST_PRICES) - 1)):
            if int(generated_deals[x]) <= int(self.LOWEST_PRICES[x]):
                self.deal_position.append(generated_deals.index(generated_deals[x]))
        if len(self.deal_position) > 0:
            print("Sending")
            self.send(links, generated_deals)
        else:
          print("No Deals Today")

    def send(self, link, generated):
        with open(file="email.txt", mode="w") as email:
            email.write("Dear [NAME],")

        with open(file="email.txt", mode="a") as email:
            for deal in self.deal_position:
                email.write(
                    f"\nYou\'ve got a deal at {self.CITIES[deal]} for ${generated[deal]}\nThe link is: {link[deal]}")

        mailing_list = pandas.read_csv("mailing_list.csv")

        for x in range(0, len(mailing_list.to_dict()["Name"])):
            with open(file="email.txt", mode="r") as send_email:
                send_var = send_email.read()
                new_email = send_var.replace("[NAME]", mailing_list.to_dict()["Name"][x])

            email = "dorcylicious@yahoo.com"
            to_address = mailing_list.to_dict()["Email"][x]
            server = "smtp.mail.yahoo.com"
            password = os.environ.get("MAILING_PASS")
            port = 587

            with smtplib.SMTP(host=server, port=port) as final:
                final.starttls()
                final.login(user=email, password=password)
                final.sendmail(from_addr=email, to_addrs=to_address,
                               msg=f"Subject: Flight Club Deals\n\n{new_email}")
                print("Sent Successfully")

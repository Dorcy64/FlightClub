import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Upload:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.client = gspread.authorize(self.credentials)

        self.spreadsheet = self.client.open('FlightDeals')

    def upload(self):
        with open('Flight Deals - links.csv', 'r') as file_obj:
            content = file_obj.read()
            self.client.import_csv(self.spreadsheet.id, data=content)

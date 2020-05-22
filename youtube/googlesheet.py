import gspread
from oauth2client.service_account import ServiceAccountCredentials

from utils import paths


def parse_args():
    import argparse
    parser = argparse.ArgumentParser('1upcoder ep 1. Simple sheet example')
    parser.add_argument('--sheet', help='the name of the sheet to load')
    parser.add_argument('--google-key', default='sheet-google-key.json',
                        help='the name of the credentials file')
    parser.add_argument('--create', default=False, action='store_true',
                        help='create a sheet if one does not exist')
    parser.add_argument('--list', default=False, action='store_true',
                        help='will list the sheets available to this '
                        'client')
    parser.add_argument('--upload-csv', help='will upload the contents'
                        'of the given csv to sheet1')
    return parser.parse_args()


def make_google_client(keyfile: str):
    """Creates a client that can be used to get access to google sheets
    keyfile: the name of the credentials file generated from google api
            manager. Because we are using paths.cfg_lookup this file can
            be located in ~/etc or in the current directory
    returns: a gspread client
    """
    url = ['https://spreadsheets.google.com/feeds',
           'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        paths.cfg_lookup(keyfile), url)
    return gspread.authorize(credentials)


def list_sheets(client):
    print('----- Useable sheets ------')
    for data in client.list_spreadsheet_files():
        print(f'Sheet name: {data["name"]}')


def find_sheet(name):
    for data in client.list_spreadsheet_files():
        if data['name'] == name:
            return data


if __name__ == '__main__':
    args = parse_args()
    client = make_google_client(args.google_key)
    if args.list:
        list_sheets(client)
    if not find_sheet(args.sheet) and args.create():
        print(f'create sheet: {args.sheet}')
        client.create(args.sheet)
    if args.sheet:
        sheet = client.open(args.sheet)
        print(sheet.sheet1.get_all_records())
    if args.upload_csv:
        def _get_rows():
            with open(args.upload_csv) as data:
                for line in data:
                    yield line.split(',')
        sheet = client.open(args.sheet)
        sheet.sheet1.append_rows(list(_get_rows()))

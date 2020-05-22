import simplejson

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import paths


def parse_args():
    import argparse
    parser = argparse.ArgumentParser('1upcoder ep 1. Simple sheet example')
    parser.add_argument('--sheet', required=True, help='the name of the sheet to load')
    parser.add_argument('--google-key', default='sheet-google-key.json', help='the name of the credentials file')
    parser.add_argument('--create', default=False, action='store_true', help='create a sheet if one does not exist')
    return parser.parse_args()

def make_google_client(args):
    url = ['https://spreadsheets.google.com/feeds',
           'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(paths.cfg_lookup(args.google_key), url)
    return gspread.authorize(credentials)

def list_sheets(client):
    print('----- Useable sheets ------')
    for data in client.list_spreadsheet_files():
        print(f'Sheet name: {data[name]}')


def find_sheet(name):
    for data in client.list_spreadsheet_files():
        if data['name'] == name:
            return data

if __name__ == '__main__':
    args = parse_args()
    client = make_google_client(args)
    if not find_sheet(args.sheet):
        if args.create():
            print(f'create sheet: {args.sheet}')
            client.create(args.sheet)
    sheet = client.open(arg.sheet)
    print(sheet.sheet1.get_all_records())

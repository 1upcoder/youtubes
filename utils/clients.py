import gspread
from oauth2client.service_account import ServiceAccountCredentials

from utils import paths


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

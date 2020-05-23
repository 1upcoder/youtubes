from utils.clients import make_google_client
import pandas


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        'loads in finance records from a google sheet')
    parser.add_argument('--sheet', help='the name of the sheet to load')
    parser.add_argument('--worksheet', default='sheet1',
                        help='the name of the worksheet to use',)
    parser.add_argument('--google-key', default='sheet-google-key.json',
                        help='the name of the credentials file')
    return parser.parse_args()


def get_header(data):
    if data:
        return data[0].keys()


def get_values(data: pandas.DataFrame):
    for rows in data:
        yield map(lambda x: x.lower(), rows.values())


def prepare(data: pandas.DataFrame):
    df.date = pandas.to_datetime(df.date)
    df.set_index('date', inplace=True)

    def _clean(value: str):
        return float(value.replace('$', '').replace(',', ''))
    for i in df.columns:
        df[i] = df[i].map(_clean)
    return df


if __name__ == '__main__':
    args = parse_args()
    client = make_google_client(args.google_key)
    sheet = client.open(args.sheet)
    allsheets = {w.title.lower(): w.id for w in sheet.worksheets()}
    worksheet = sheet.get_worksheet(allsheets[args.worksheet.lower()])
    data = worksheet.get_all_records()
    df = pandas.DataFrame(get_values(data), columns=get_header(data))
    print(prepare(df))

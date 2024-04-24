from os.path import isfile
from csv import DictReader, DictWriter


model: list[str] = ["Name", "Age", "Registration Number", "Email Address", "Password"]


def import_data() -> None:
    if isfile('./info.csv'):
        # Fetching data from CSV
        try:
            with open('./info.csv', 'r') as models:
                reader = DictReader(models)
                return list(reader)[0]
        except PermissionError: print('Reading Denied: Unable to access the file!')


def export_data(data) -> None:
    # Writing data to CSV
    try:
        with open('./info.csv', 'w', newline='') as models:
            writer = DictWriter(models, fieldnames=model)
            writer.writeheader()
            writer.writerow(data)
    except PermissionError: print('Writing Denied: Unable to access the file!')

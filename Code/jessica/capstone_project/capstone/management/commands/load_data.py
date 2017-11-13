from django.core.management.base import BaseCommand
from capstone.models import AccessData
import pandas as pd


# erase the database
def erase_database():
    AccessData.objects.all().delete()


# open xls (pick out relevant data)
def open_data():
    # file = pd.read_excel(open('food environment atlas.xls', 'rb'), sheetname = 'ACCESS')
    # df = load_file.parse()
    xl = pd.ExcelFile(r'C:\Users\Jessica\PycharmProjects\20170724-FullStack-Night\Code\jessica\capstone_project\capstone\management\commands\food_environment_atlas.xls')
    #print(xl.sheet_names)

    sheet = xl.parse('ACCESS')
    data_column = sheet['PCT_LACCESS_POP10']
    state_column = sheet['State']
    county_column = sheet['County']
    county_id_column = sheet['FIPS']
    #print(type(data_column))
    #print(len(data_column))
    #print(data_column[0])
    #for datum in sheet['PCT_LACCESS_POP10']:
    #    print(datum)

    for i in range(len(data_column)):
        pct_access = data_column[i]
        state = state_column[i]
        county = county_column[i]
        county_id = county_id_column[i]

        all_data = AccessData(state=state, county=county, pct_access=pct_access, county_id=county_id)
        all_data.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        erase_database()
        open_data()

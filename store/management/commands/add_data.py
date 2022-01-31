import pandas as pd
from django.core.management.base import BaseCommand
from store.models import Product
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):
  help = "A command to add data from an Excel file to the database"

  def handle(self, *args, **options):

    excel_file = 'Product_data.xlsx'
    df = pd.read_excel(excel_file)
    
    #connection to mysql
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(user=user,password=password,database_name=database_name)

    engine = create_engine(database_url, echo=False)

    df.to_sql(Product._meta.db_table, if_exists='append', con=engine, index=False)
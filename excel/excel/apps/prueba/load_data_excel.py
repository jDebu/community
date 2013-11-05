import sys,os
# ruta a nuestro archivo CSV

# ruta a nuestro proyecto de django
#your_djangoproject_home= os.path.dirname(os.path.dirname(__file__))
file_route= os.path.dirname(os.path.dirname(__file__))

#sys.path.append(your_djangoproject_home)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
print file_route
# importamos nuestro modelo
from django.core.management import setup_environ
sys.path.append('E:\projects\django\excel')
from excel import settings
setup_environ(settings)
from excel.apps.prueba.models import Pizza
import csv # first we need import necessary lib:csv
file=open("e:\p10_Pizza.csv") #prepare a csv file for our example

dataReader=csv.reader(file,delimiter=';', quotechar='|')
#now the testReader is an array,so we can iterate it
#for row in testReader:
#    print "|".join(row)


for row in dataReader:
    if row[0] != 'pizza_id': # ignoramos la primera linea del archivo CSV
		pizza = Pizza()
		pizza.pizza_id = row[0]
		pizza.pizza_nombre = row[1]
		pizza.pizza_precio = row[2]
		pizza.save()	
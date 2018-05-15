#!/usr/bin/env/python
#datos presupestarios general..
#ayuntamiento valencia...
import requests
import datetime
#from pymongo
#from urllib.request import urlopen, urlretrieve
#from bs4 import BeautifulSoup as bs


gastos = ["GASTOS DE PERSONAL", "GASTOS CORRIENTES EN BIENES Y SERVICIOS","GASTOS FINANCIEROS","TRANSFERENCIAS CORRIENTES","INVERSIONES REALES", "TRANSFERENCIAS DE CAPITAL", "ACTIVOS FINANCIEROS", "PASIVOS FINANCIEROS","FONDO DE CONTINGENCIA Y OTROS IMPREVISTOS"]




def presupuesto_general(geo,dat,leng):
  total = 0
  
  year = '2018'
  if geo == '':
    geo = 'Valencia'
  if geo != 'Valencia':
      if leng == 'Cast':
        return 'Disculpad, solo estamos funcionando en Valencia'
      else:
        return 'Disculpeu, només estem funcionant a València'
  if dat != '':
      for s in dat.split(): 
         s=s.split('-')
         if s[0].isdigit():
            
           year = s[0]

      if int(year) < 2011:
         if leng == 'Cast':
           return 'solo tenemos presupuesto desde el 2011'
         else:
           return 'Només tenim pressupost des del 2011'
         
 
  page = requests.get("http://www.valencia.es:8070/somclars/sql/datos_presupuestarios/SELECT%20g.cuenta%2Cp.descripcion%2Cg.CredIniciales%20FROM%20gastos%20g%20JOIN%20planes_detalle%20p%20ON%20g.cuenta%3Dp.codigo%20AND%20g.plan%3Dp.plan%20WHERE%20g.plan%3D1%20AND%20ejercicio%3D{}%20ORDER%20BY%20cuenta%2Cp.descripcion%20ASC".format(year))

  if page.status_code == 200:
   
    presupuesto_datos = page.json()
    for i in range(0, len(presupuesto_datos[0]["data"])):
       if presupuesto_datos[0]["data"][i][1] in gastos:
        #print(presupuesto_datos[0]["data"][i][1], presupuesto_datos[0]["data"][i][2] )
        total += float(presupuesto_datos[0]["data"][i][2])
        #print("%0.2f" %total)
    if leng == 'Cast':
      return 'el presupuesto de {} en el año {} es: {}'.format(geo,year,addComa(format(total,"0.2f"))) 
    else:
      return "El pressupost de {} en l'any {} és: {}".format(geo,year,addComa(format(total,"0.2f"))) 
#def salarios(nombre):
  

if __name__=='__main__':
   print(presupuesto_general('en 2014'))




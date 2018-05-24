#!/usr/bin/env/datos_valencia 
# -*- coding: utf-8 -*-
#datos presupestarios general..
#ayuntamiento valencia...
import logging
from pymongo import MongoClient
from variables import *
from texto import *

#gastos = ["GASTOS DE PERSONAL", "GASTOS CORRIENTES EN BIENES Y SERVICIOS","GASTOS FINANCIEROS","TRANSFERENCIAS CORRIENTES","INVERSIONES REALES", "TRANSFERENCIAS DE CAPITAL", "ACTIVOS FINANCIEROS", "PASIVOS FINANCIEROS","FONDO DE CONTINGENCIA Y OTROS IMPREVISTOS"]

client = MongoClient(host,port)
db = client.datos_valencia
presupuesto = db.presupuesto

def presupuesto_general(geo,dat,leng):
  total = 0
  
  year = 2018
  if geo == '':
    geo = 'Valencia'
  if geo != 'Valencia':
     return respuesta_bot("erroLugar",leng)
      
  if dat != '':
      for s in dat.split(): 
         s=s.split('-')
         if s[0].isdigit():
            
           year = int(s[0])

      if int(year) < 2011:
        return respuesta_bot("errorAñoPrep",leng)
       

  ## this function looks for budget in the year requested by the user 
  try:             
    total = presupuesto.find_one({'anio':year})['presupuesto']
  except Exception as e:
    logging.exception('-No se pudo encontrar presupuesto para el ano {}-'.format(year))
    return respuesta_bot("errorBusquedaPrep",leng).format(year)
  

  
  return respuesta_bot("res.presupuesto",leng).format(geo,year,total) 
  
#def salarios(nombre):
  

if __name__=='__main__':
   print(presupuesto_general('Valencia','2222-10-08','Cast'))
   print(presupuesto_general('Valencia','2012-10-08','Cast'))



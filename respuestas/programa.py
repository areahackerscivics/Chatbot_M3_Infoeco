#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
def program(dat,geo):
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

  return 2, './imagen/programas_{}.png'.format(year)

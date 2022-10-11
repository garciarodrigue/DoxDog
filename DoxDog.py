#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import requests
from colorama import Fore, Back, Style, init
init()

os.system("clear")
def Doxxeo():
    try:
        
        verde = Fore.GREEN
        amar = Fore.YELLOW
        rojo = Fore.RED
        cyan = Fore.CYAN
        magenta = Fore.MAGENTA

        key = input(magenta + "Numero >> " + cyan)
        print("")
        url = f"https://doxdog-68f97-default-rtdb.firebaseio.com/numeros/{key}.json"

        pedir = requests.get(url)
        respuesta = json.loads(pedir.content)
        
        print(amar +"Numero: "+ verde + respuesta["num"])
        print(amar +"Usuario: "+ verde + respuesta["nombre"])
        print(amar +"Compañia: "+ verde + respuesta["compañia"])
        print(amar +"Locacion: "+ verde + respuesta["locacion"])
        Doxxeo()
    except TypeError:
        print(rojo + f"No se encuenta en la{verde} DataBase\n")
        print(f"""
        {cyan}Comunicate con {verde}+50245472034{cyan}
        Manda el numero de telefono que quieres que
        añadan su info a la Data Base.
              """)
        Doxxeo()

Doxxeo()

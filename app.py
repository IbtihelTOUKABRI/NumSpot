""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Module name : app.py
## Author :      ITO
## Description : Distribution des goodies 
##          
## History :     Date         | By  | Modification
##               07/03/2023   | ITO | Init version
##               08/03/2023   | ITO | Changer le log dans la sortie standard , modifier la path de la BD
##               08/03/2023   | ITO | Changer la BD par un dict             
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import sqlite3
from datetime import datetime
from flask import *
import random

#####################


app = Flask(__name__)

stock = {
    'gourde': 1,
    'stylo': 1,
    'support_ordi': 1,
    'balle': 1,
    'support_bambou': 1,
    'pince': 1,
    'cache': 1 }


@app.route("/")
def list_goodies ():

    try:
        
        print(stock)
        
        return render_template("list_goodies.html",goodies=stock)

    except Exception as e:
        print('erreur listing goodies')
        print(e)

        return "erreur listing goodies"
  
###############################################
## New Tirage
###############################################
@app.route("/tirage", methods =['POST','GET'])
def tirage ():

    try:
        
        
        print("debut tirage")


        goodies_p = [i/sum(stock.values()) for i in list(stock.values())]

        print(f'goodies_p: {goodies_p}')

        

        while sum(stock.values()) > 0:

            print(f'sum(stock.values(): {sum(stock.values())}')

            
            item = random.choices(list(stock.keys()), goodies_p)[0]

            print(f'item: {item}')
            

            stock[item] -= 1
            if stock[item] == 0:
                # recalcul des probas avec le stock restant
                # on ajoute 1 au dénominateur pour éviter un /0 quand le stock est vide
                goodies_p = [i/(sum(stock.values())+1) for i in list(stock.values())]
                print(f'probas: {goodies_p}')
                print(f'tirage item: {item}, stock restant: {stock}, total: {sum(stock.values())}')
                if(sum(stock.values()) > 0):
                    return render_template("tirage.html",article=item)
                else:
                    
                    return render_template("list_goodies.html",goodies=stock)    
 
    except Exception as e:
        print("erreur tirage")
        
        print(e)

        return "erreur Tirage"

###############################################
## Remise à zéro
###############################################
@app.route("/raz", methods =['POST','GET'])
def raz ():

    try:
        stock = {
            'gourde': 1,
            'stylo': 1,
            'support_ordi': 1,
            'balle': 1,
            'support_bambou': 1,
            'pince': 1,
            'cache': 1 }

        print(stock)
        print("raz OK")
        
        return render_template("list_goodies.html",goodies=stock)
    except Exception as e:
        print("erreur Remise à zero")

        print(e)

        return "erreur Remise à zero"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)


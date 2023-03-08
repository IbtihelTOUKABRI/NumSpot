from datetime import datetime
from flask import Flask, render_template
import random

stock_init = {   
    'gourde': 50, 
    'stylo': 100, 
    'support ordi': 150, 
    'balle': 200,
    'support bambou': 300,
    'pince': 300,
    'cache webcam': 400
    }

stock = stock_init.copy()
goodies_p = [i/sum(stock.values()) for i in list(stock.values())]

app = Flask(__name__)

@app.route("/")
def list_goodies():
    global stock
    return render_template("list_goodies.html", goodies=list(stock.values()))
  
###############################################
## New Tirage
###############################################
@app.route("/tirage", methods =['POST','GET'])
def tirage ():
    global stock
    global goodies_p
    if sum(stock.values()) > 0:
        item = random.choices(list(stock.keys()), goodies_p)[0]
        stock[item] -= 1

        if stock[item] == 0:
            # recalcul des probas avec le stock restant
            # on ajoute 1 au dénominateur pour éviter un /0 quand le dernier item est pioché
            goodies_p = [i/(sum(stock.values())+1) for i in list(stock.values())]

        print(f'{stock}')
        return render_template("tirage.html", article=item)

    else:
        print(f'Stock is empty !')
        return render_template("tirage.html", article='Vide !')
    

###############################################
## Remise à zéro
###############################################
@app.route("/raz", methods =['POST','GET'])
def raz ():
    global stock
    global stock_init
    
    stock = stock_init.copy()

    return render_template("list_goodies.html", goodies=list(stock.items()))

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Module name : app.py
## Author :      ITO
## Description : Distribution des goodies 
##          
## History :     Date         | By  | Modification
##               07/03/2023   | ITO | Init version
##             
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import sqlite3
from datetime import datetime
from flask import *
from random import *
import logging
import numpy as np


#################"
## Code du log###
#################"
#change the log directory
# !!!!!!!!!!
log_dir="C:/Users/ITO/Desktop/numSpot/log/"

#now = datetime.now()
#aujourdhui = now.strftime("%Y%m%d")

log_name=log_dir+"numspot.log"

logging.basicConfig(filename=log_name, encoding='utf-8', level=logging.DEBUG,filemode='w')



app = Flask(__name__)
#@app.route("/")
#def home ():

    #return render_template("home.html") 

@app.route("/")
def list_goodies ():

    try:
        conn = sqlite3.connect('db/goodies.db')
        cursorSQLite = conn.cursor()

        sql = "SELECT qte,libelle FROM articles"
        cursorSQLite.execute(sql)
               
        rows = cursorSQLite.fetchall() 

        print(rows)

        logging.debug('listing goodies')

        
        return render_template("list_goodies.html",goodies=rows)

    except Exception as e:
        logging.error('erreur listing goodies')
        logging.error(e)

        return "erreur listing goodies"
  
###############################################
## New Tirage
###############################################
@app.route("/tirage", methods =['POST','GET'])
def tirage ():

    testQte=0

    try:

        while (testQte==0):
            conn = sqlite3.connect('db/goodies.db')
            cursorSQLite = conn.cursor()
            nbAleatoire = randint(1,7)
            print(nbAleatoire)

            sql = '''SELECT * FROM articles WHERE ID = ?'''
            cursorSQLite.execute(sql, (nbAleatoire,))


            row = cursorSQLite.fetchone() 
            article=row[2]
            
            logging.debug(row[1])
            logging.debug(type(row[1]))

            if row[1] > 0:
                qte=row[1]-1
                testQte=1
            

        sql = ''' UPDATE articles SET qte = ? WHERE id = ?'''
        cursorSQLite.execute(sql, (qte,nbAleatoire,))

        conn.commit()

        sql = "SELECT qte,libelle FROM articles"
        cursorSQLite.execute(sql)
               
        rows = cursorSQLite.fetchall() 
        

        for row in rows:
            print(row)
        
        logging.debug("affichage tirage")


        return render_template("tirage.html",article=article)

    except Exception as e:
        logging.error("erreur tirage")
        
        logging.error(e)

        return "erreur Tirage"

###############################################
## Remise à zéro
###############################################
@app.route("/raz", methods =['POST','GET'])
def raz ():

    try:
        conn = sqlite3.connect('db/goodies.db')
        cursorSQLite = conn.cursor()

        
        list = [1,50,100,150,200,300,300,400]


        for i in range(1,8):
        
            sql = ''' UPDATE articles SET qte = ? WHERE id = ?'''
            cursorSQLite.execute(sql, (list[i],i,))
            conn.commit()

        sql = "SELECT qte,libelle FROM articles"
        cursorSQLite.execute(sql)
               
        rows = cursorSQLite.fetchall() 
        

        for row in rows:
            print(row)

        logging.debug("Remse à zero OK")


        return render_template("list_goodies.html",goodies=rows)
    except Exception as e:
        logging.error("erreur Remise à zero")

        logging.error(e)

        return "erreur Remise à zero"



        


app.run("ibti",port=5002,debug = True,use_reloader = False,threaded=True)



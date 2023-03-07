

##########################
## code creation bd sqlite 
# change the directory
# !!!!!!!!!!


####
cnx = sqlite3.connect('C:/Users/ITO/Desktop/numSpot/db/goodies.db')

cursorSQLite = cnx.cursor()
cursorSQLite.execute('''CREATE TABLE articles
             (ID INTEGER PRIMARY KEY AUTOINCREMENT, qte int, libelle text)''')

cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (50,'gourde')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (100,'stylo')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (150,'support ordi')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (200,'balle')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (300,'support bambou')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (300,'pince smartphone')")
cursorSQLite.execute("INSERT INTO articles (qte, libelle)VALUES (400,'cache webcam')")

cnx.commit()
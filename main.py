#coding:utf-8
import sqlite3
# CRUD : Create, Read, Update, Delete

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "Toto", 12)
cursor.execute('INSERT INTO t_users VALUES(?,?,?)', new_user)

#Envoie les informations précédente
connection.commit()

print("Nouvelle utilisateur ajouter ! ")

#fermer la requête de la base de donnée
connection.close()


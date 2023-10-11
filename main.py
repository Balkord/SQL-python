#coding:utf-8
import sqlite3
# CRUD : Create, Read, Update, Delete

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "Jean", 20)
cursor.execute('INSERT INTO t_users VALUES(?,?,?)', new_user)

#Envoie les informations précédente
connection.commit()

print("Nouvelle utilisateur ajouter ! ")

#fermer la requête de la base de donnée
connection.close()

#On peux pas créer plusieur user a entré dans la base de donné.

#Voir comment intégré plusieur USER en même temp

#Voir la finalité de la base de donnée et comment l'utiliser pour switch sur SQL

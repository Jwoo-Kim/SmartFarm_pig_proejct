from tkinter import *
from log_join import *
import tkinter.messagebox
from tkinter import ttk
import pymysql

window = Tk()
window.geometry("600x480")

conn, cur = None, None
conn = pymysql.connect(host = "localhost", user = "root", password= "wlsdn8775!", db="db", charset ='utf8')
cur = conn.cursor()
sql = "create or replace view view_symptom as select p_ID from has where symptom = '감기'"
cur.execute(sql)

sql = "select * from view_symptom"
cur.execute(sql)

while(True):
    row = cur.fetchone()
    if row == None:
        break;
    print(row[0])
    #sql = "insert into view_sick_pig select * from view_symptom where p_ID = " + str(row[0])

window.mainloop()
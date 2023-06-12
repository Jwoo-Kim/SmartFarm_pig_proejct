from tkinter import *
import pymysql
from tkinter import messagebox

def join():
    def insertData():
        con, cur = None, None
        data1, data2 = "", ""
        sql = ""

        conn = pymysql.connect(host = 'localhost', user = 'root', password = "wlsdn8775!", db = "db")
        cur = conn.cursor()

        data1 = j_edt1.get(); data2 = j_edt2.get()

        try:
            sql = "insert into administrator values('"+ data1 +"','"+ data2 +"')"
            cur.execute(sql)
        except:
            messagebox.showerror('오류', '데이터 입력 오류가 발생함')
        else:
            messagebox.showinfo('성공','데이터 입력 성공')
        conn.commit()
        conn.close()

    w_join = Tk()
    w_join.title("Registration")
    w_join.geometry("400x250")
    w_join.resizable(False, False)

    j_id = Label(w_join, text="ID")
    j_pw = Label(w_join, text="PASSWORD")

    j_id.place(x=80, y=70)
    j_pw.place(x=50, y=90)

    j_edt1 = Entry(w_join, width=30)
    j_edt2 = Entry(w_join, width=30, show = "*")

    la1 = Label(w_join, text="PASSWORD는 15자리 이하로 입력하세요.")
    la1.place(x=130, y=110)

    j_edt1.place(x=130, y=70)
    j_edt2.place(x=130, y=90)

    j_btn1 = Button(w_join, text="OK", width=8, command = insertData)
    j_btn2 = Button(w_join, text="Cancel", width=8, command=w_join.destroy)

    j_btn1.place(x=190, y=150)
    j_btn2.place(x=280, y=150)

    w_join.mainloop()
from tkinter import *
from log_join import *
import tkinter.messagebox
from tkinter import ttk
import pymysql
import datetime

window = Tk()
window.title("Login")
window.geometry("400x250")
window.resizable(False,False)



def open():
    w_open = Tk()
    w_open.title("선택창")
    w_open.geometry("400x200")
    w_open.resizable(False, False)

    def p_input():
        w_open.destroy()
        p_open = Tk()
        p_open.title("돼지 정보 입력창")
        p_open.geometry("800x600")

        p_frame = LabelFrame(p_open, text = "돼지 정보")
        p_frame.pack(fill = BOTH, expand = 1, padx =10, pady = 10)

        p_la1 = Label(p_frame, text="돈사")
        p_la2 = Label(p_frame, text="돼지우리")
        p_la3 = Label(p_frame, text="출생일(0000-00-00)")
        p_la4 = Label(p_frame, text="나이")
        p_la5 = Label(p_frame, text="몸무게")
        p_la6 = Label(p_frame, text="증상")
        p_la7 = Label(p_frame, text="관리자")
        p_la8 = Label(p_frame, text="비고")

        p_edt1 = Entry(p_frame, width = 15)
        p_edt2 = Entry(p_frame, width=15)
        p_edt3 = Entry(p_frame, width=15)
        p_edt4 = Entry(p_frame, width=15)
        p_edt5 = Entry(p_frame, width=15)
        p_edt6 = Entry(p_frame , width=15)
        p_edt7 = Entry(p_frame, width = 15)
        p_txt = Text(p_open, width=30, height = 15)
        p_txt.insert(END, "글자를 입력하세요.")

        def p_insertData():
            conn, cur = None, None
            data1, data2, data3, data4 = "", "", "", ""
            sql = ""

            conn = pymysql.connect(host='127.0.0.1', user='root', password='wlsdn8775!', db='db', charset='utf8')
            cur = conn.cursor()

            data1 = p_edt1.get()
            data2 = p_edt2.get()
            data3 = p_edt3.get()
            data4 = p_edt4.get()
            data5 = p_edt5.get()
            data6 = p_edt6.get()
            data7 = p_edt7.get()
            data8 = p_txt.get("1.0",END)

            p_edt1.delete(0,END)
            p_edt2.delete(0,END)
            p_edt3.delete(0,END)
            p_edt4.delete(0,END)
            p_edt5.delete(0,END)
            p_edt6.delete(0,END)
            p_edt7.delete(0,END)
            p_txt.delete("1.0",END)

            try:
                sql = "INSERT INTO pig(company, pigpen, birth, age, weight, symptom, administrator, memo) VALUES('" +  data1 + "'," + data2 + ",'" + data3 + "'," + data4 + ","+data5+",'"+data6+"','"+data7+"','"+data8+"')"
                cur.execute(sql)
            except:
                messagebox.showerror('오류', '데이터 입력 오류가 발생함')
            else:
                messagebox.showinfo('성공', '데이터 입력 성공')
            conn.commit()

            sql ="truncate has"
            cur.execute(sql)
            conn.commit()

            sql = "select ID,symptom from pig "
            cur.execute(sql)
            rows = cur.fetchall()
            for data1, data2 in rows:
                data3 = data2.split(",")
                for data4 in data3:
                    sql = "insert into has(symptom,p_ID) values('" + data4 + "'," + str(data1) + ")"
                    cur.execute(sql)
                conn.commit()
            conn.close()

        def cancle():
            p_open.destroy()
            open()

        p_btn1 = Button(p_frame, text="입력",command = p_insertData)
        p_btn2 = Button(p_frame, text="취소",command = cancle)

        p_la1.place(x=100, y=50)
        p_edt1.place(x=150, y=50)
        p_la2.place(x=80, y=80)
        p_edt2.place(x=150, y=80)
        p_la3.place(x=30, y=110)
        p_edt3.place(x=150, y=110)
        p_la4.place(x=100, y=140)
        p_edt4.place(x=150, y=140)
        p_la5.place(x=90, y=170)
        p_edt5.place(x=150, y=170)
        p_la6.place(x=100, y=200)
        p_edt6.place(x=150, y=200)
        p_la7.place(x=100, y=230)
        p_edt7.place(x=150, y=230)
        p_la8.place(x=100, y=270)
        p_txt.place(x=160, y=300)

        p_btn1.place(x=160, y=520)
        p_btn2.place(x=210, y=520)

        p_open.mainloop()

    f1 = Button(text="돼지 정보 입력", command = p_input)

    def view():
        w_open.destroy()
        v_open = Tk()
        v_open.title("돼지 정보 리스트")
        v_open.geometry("1200x600")

        v_frame1 = LabelFrame(v_open,  text = "속성")
        v_frame2 = Frame(v_open)

        my_tree = ttk.Treeview(v_frame2)

        my_tree['columns'] = ("company","pigpen","ID","birth","age","weight","symptom","administrator","memo")
        my_tree.column("#0", width=0, minwidth=25, stretch = NO)
        my_tree.column("company",anchor=W,width=1)
        my_tree.column("pigpen", anchor=W, width=1)
        my_tree.column("ID", anchor=W, width=1)
        my_tree.column("birth", anchor=W, width=1)
        my_tree.column("age", anchor=W, width=1)
        my_tree.column("weight", anchor=W, width=1)
        my_tree.column("symptom", anchor=W, width=20)
        my_tree.column("administrator", anchor=W, width=1)
        my_tree.column("memo", anchor=W, width=60)

        my_tree.heading("#0", text = "", anchor=W)
        my_tree.heading("company", text="회사",anchor=W)
        my_tree.heading("pigpen", text="돼지우리", anchor=W)
        my_tree.heading("ID", text="ID", anchor=W)
        my_tree.heading("birth", text="출생일자", anchor=W)
        my_tree.heading("age", text="나이", anchor=W)
        my_tree.heading("weight", text="몸무게", anchor=W)
        my_tree.heading("symptom", text="증상", anchor=W)
        my_tree.heading("administrator", text="관리자", anchor=W)
        my_tree.heading("memo", text="비고", anchor=W)

        my_tree.pack(fill = BOTH, expand = 1)


        symptoms = ["돈사","증상","관리자"]
        search_combobox = ttk.Combobox(v_frame1, height = 5, values = symptoms, state = "readonly" )
        search_combobox.set("목록선택")
        search_combobox.pack(side=LEFT, padx= 5,pady =  5)

        v_edt1 = Entry(v_frame1, width = 20)
        v_edt1.pack(side = LEFT, padx = 5, pady = 5)

        def search():
            conn, cur = None, None
            search_data,combobox_data, select_what = "","",""

            sql = ""
            conn = pymysql.connect(host = 'localhost', user = 'root', password ="wlsdn8775!", db="db" )
            cur = conn.cursor()

            search_data,combobox_data = v_edt1.get(),search_combobox.get()
            if(combobox_data == "돈사"):
                select_what = "company"
                sql = "drop view if exists view_pigpen"
                cur.execute(sql)
                conn.commit()

                sql = "create view view_pigpen as select * from pig where " + select_what + " = '"+search_data+"'"
                cur.execute(sql)
                conn.commit()

                sql = "select * from view_pigpen"
                cur.execute(sql)
                # tree내용 삭제
                x = my_tree.get_children()
                for item in x:
                    my_tree.delete(item)
                # tree에 데이터 입력
                count = 0
                while(True):
                    row = cur.fetchone()
                    if row==None:
                        break
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                    count += 1

            elif(combobox_data == "증상"):
                select_what = "symptom"

                sql = "drop table if exists view_sick_pig"
                cur.execute(sql)

                sql = "create table view_sick_pig as select * from pig"
                cur.execute(sql)
                conn.commit()

                sql = "truncate view_sick_pig"
                cur.execute(sql)
                conn.commit()

                sql = "create or replace view view_symptom as select p_ID from has where " + select_what + " = '" + search_data+ "'"
                cur.execute(sql)
                conn.commit()

                sql = "select * from view_symptom"
                cur.execute(sql)

                row = cur.fetchall()

                for x in row:
                    sql = "insert into view_sick_pig select * from pig where ID = (select p_ID from view_symptom where p_ID = " + str(x[0])+")"
                    cur.execute(sql)

                # tree내용 삭제
                x = my_tree.get_children()
                for item in x:
                    my_tree.delete(item)

                # tree에 데이터 입력
                count = 0
                sql ="select * from view_sick_pig"
                cur.execute(sql)

                while (True):
                    row = cur.fetchone()
                    if row == None:
                        break
                    my_tree.insert(parent='', index='end', iid=count, text="",
                                    values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                    count += 1
            else:
                select_what = "administrator"
                sql = "drop view if exists view_administrator"
                cur.execute(sql)
                conn.commit()

                sql = "create view view_administrator as select * from pig where " + select_what + " = '" + search_data + "'"
                cur.execute(sql)
                conn.commit()

                sql = "select * from view_administrator"
                cur.execute(sql)
                # tree내용 삭제
                x = my_tree.get_children()
                for item in x:
                    my_tree.delete(item)
                # tree에 데이터 입력
                count = 0
                while (True):
                    row = cur.fetchone()
                    if row == None:
                        break
                    my_tree.insert(parent='', index='end', iid=count, text="",
                                   values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                    count += 1

        def back():
            v_open.destroy()
            open()

        def delete():
            conn, cur = None,None
            conn = pymysql.connect(host='127.0.0.1', user='root', password='wlsdn8775!', db='db', charset='utf8')
            cur = conn.cursor()

            search_data = v_edt1.get()
            if(search_data == "돈사"or "관리자"):
                for selected_item in my_tree.selection():
                    sql = "delete from pig where ID = " + "'" + my_tree.set(selected_item,'#3') + "'"
                    cur.execute(sql)
                    conn.commit()
                    conn.close()
                    my_tree.delete(selected_item)
            else:
                for selected_item in my_tree.selection():
                    sql = "delete from has where p_ID = " + my_tree.set(selected_item, '#3')
                    cur.execute(sql)
                    conn.commit()
                    conn.close()
                    my_tree.delete(selected_item)


        v_btn1 = Button(v_frame1, text = "검색", width = 5, command = search)
        v_btn2 = Button(v_frame1, text = "삭제", width = 5, command= delete)
        v_btn3 = Button(v_frame1, text = "이전", width = 5, command = back)

        v_btn1.pack(side = LEFT, padx = 5, pady = 5)
        v_btn2.pack(side=LEFT, padx=5, pady=5)
        v_btn3.pack(side=LEFT, padx=5, pady=5)

        v_frame1.pack(padx = 3, fill=BOTH,pady = 10)
        v_frame2.pack(padx = 3, fill=BOTH,pady = 10)


        v_open.mainloop()


    f2 = Button(text = "돼지 정보 리스트",command = view)

    def video_list():
        w_open.destroy()
        video_open = Tk()
        video_open.title("비디오 리스트")
        video_open.geometry("600x480")

        video_list_btn = Frame(video_open)
        video_list_btn.pack(fill = BOTH)

        def save():
            conn, cur = None,None
            conn = pymysql.connect(host="localhost", user="root", password="wlsdn8775!", db="db")
            cur = conn.cursor()
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H_%M_%S')
            try:
                for selected_item in video_list_tree.selection():
                    sql = "select videoClip from video where num = " + video_list_tree.set(selected_item, '#4') +" into dumpfile 'C:/SQL/Movies/video"+ nowDatetime +".mp4'"
                    cur.execute(sql)
            except:
                messagebox.showerror('오류', '같은 파일이 존재합니다.')
            else:
                conn.commit()
                conn.close()

        video_btn1 = Button(video_list_btn, text = "저장", width = 7, command = save)

        def cancle():
            video_open.destroy()
            open()

        video_btn2 = Button(video_list_btn, text="이전", width = 7, command = cancle)

        video_btn2.pack(side = RIGHT,padx= 5, pady = 5)
        video_btn1.pack(side = RIGHT,padx= 5, pady = 5)

        video_list = Frame(video_open)
        video_list.pack(fill = BOTH, expand = 1)

        video_list_tree = ttk.Treeview(video_list)

        video_list_tree['columns'] = ("company", "pigpen","Date","num")
        video_list_tree.column("#0", width=0, minwidth=25, stretch = NO)
        video_list_tree.column("company", anchor=W, width = 30)
        video_list_tree.column("pigpen", anchor=W, width = 30)
        video_list_tree.column("Date", anchor=W, width = 30)
        video_list_tree.column("num", anchor=W, width = 30)

        video_list_tree.heading("#0", text="", anchor=W)
        video_list_tree.heading("company", text="돈사", anchor = W)
        video_list_tree.heading("pigpen", text="돼지우리", anchor=W)
        video_list_tree.heading("Date", text="시간", anchor=W)
        video_list_tree.heading("num", text="번호", anchor=W)

        video_list_tree.pack(fill = BOTH, expand = 1)

        conn, cur = None, None
        conn = pymysql.connect(host="localhost", user="root", password="wlsdn8775!", db="db", charset="utf8")
        cur = conn.cursor()
        sql = "select * from video"
        cur.execute(sql)

        # tree내용 삭제
        x = video_list_tree.get_children()
        for item in x:
            video_list_tree.delete(item)
        # tree에 데이터 입력
        count = 0
        while (True):
            row = cur.fetchone()
            if row == None:
                break
            video_list_tree.insert(parent='', index='end', iid=count, text="",
                           values=(row[0], row[1], row[2], row[4]))
            count += 1
        conn.commit()
        conn.close()
        video_open.mainloop()

    f3 = Button(text = "비디오 리스트", command = video_list)

    f1.pack(side = LEFT,fill = BOTH, expand = 1)
    f2.pack(side = LEFT,fill = BOTH, expand = 1)
    f3.pack(side = LEFT,fill = BOTH, expand = 1)

    w_open.mainloop()


def check():
    strData1, strData2 = [], []
    enter = 0
    conn, cur = None, None
    conn = pymysql.connect(host = "localhost", user = "root", password = "wlsdn8775!", db ="db")
    cur = conn.cursor()
    cur.execute("select * from administrator")

    strId, strPw = edt1.get(), edt2.get()
    while(True):
        row = cur.fetchone()
        if row == None:
            break;
        strData1.append(row[0]); strData2.append(row[1])

    for r_id, r_pw in zip(strData1, strData2):
        if(strId == r_id and strPw == r_pw):
            enter = 1
            break;
        else:
            enter = 0

    if(enter == 1):
        window.destroy();
        open()
    else:
        messagebox.showwarning("경고창", "ID와 PASSWORD가 일치하지 않습니다!")

id = Label(window, text = "ID")
pw = Label(window, text = "PASSWORD")

id.place(x = 80, y= 70)
pw.place(x = 50, y =90)

edt1 = Entry(window,width = 30)
edt2 = Entry(window,width =30, show = "*")

edt1.place(x = 130, y =70)
edt2.place(x = 130, y =90)

btn1 = Button(window, text = "OK", width = 8, command = check)
btn2 = Button(window, text = "Cancel", width = 8, command = window.destroy )
btn3 = Button(window, text = "Join", width = 8, command = join)

btn1.place(x=100,y=150)
btn2.place(x=190,y=150)
btn3.place(x = 280, y=150)

window.mainloop()




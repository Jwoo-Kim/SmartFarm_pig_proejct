from tkinter import *



p_open = Tk()
p_open.title("돼지 정보 입력창")
p_open.geometry("600x600")

p_frame = LabelFrame(p_open, text="돼지 정보")
p_frame.pack(fill=BOTH, expand=1, padx=10, pady=10)

p_la1 = Label(p_frame, text="돈사")
p_la2 = Label(p_frame, text="돼지우리")
p_la3 = Label(p_frame, text="출생일(0000-00-00)")
p_la4 = Label(p_frame, text="나이")
p_la5 = Label(p_frame, text="몸무게")
p_la6 = Label(p_frame, text="증상")
p_la7 = Label(p_frame, text="관리자")
p_la8 = Label(p_frame, text="비고")

p_edt1 = Entry(p_frame, width=15)
p_edt2 = Entry(p_frame, width=15)
p_edt3 = Entry(p_frame, width=15)
p_edt4 = Entry(p_frame, width=15)
p_edt5 = Entry(p_frame, width=15)
p_edt6 = Entry(p_frame, width=15)
p_listbox = Listbox(p_open, selectmode="extended", height=3)
p_listbox.insert(END, "없음")
p_listbox.insert(END, "감기")
p_listbox.insert(END, "구제역")
p_listbox.insert(END, "폐렴")

p_txt = Text(p_open, width=30, height=15)
p_txt.insert(END, "글자를 입력하세요.")

p_btn1 = Button(p_frame, text="입력")
p_btn2 = Button(p_frame, text="삭제")
p_btn3 = Button(p_frame, text="취소")


p_open.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from OtherGUI import about, stdlogingui, adminlogingui
from VoiceSystem import call_voice

class main:
    def __init__(self, root):
        self.root = root
        root.geometry("800x600")
        root.maxsize(800,600)
        root.minsize(800,600)
        root.iconbitmap('logo.ico')
        root.title("Result Mangement System")
        #Start frame for title
        upper_frame = Frame(root, bg="DodgerBlue2", height=50)
        title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                            font=('Garuda', 20, 'bold', 'underline'))
        upper_frame.pack(side=TOP, fill=BOTH)
        title_label.pack(pady=15)

        #Center Frame 1 for logo
        middle1_Frame = Frame(root, bg="mint cream", height=200)
        self.logo_pic = Image.open("Superior University-01.png")
        self.mypic = ImageTk.PhotoImage(self.logo_pic)
        logo_label = Label(middle1_Frame, image=self.mypic)
        middle1_Frame.pack(side=TOP, fill=BOTH)
        logo_label.pack(pady=25)

        #buttons frame center 2
        middle2_frame = Frame(root, bg="mint cream", height=290)
        Frame_button = Frame(middle2_frame, bg="medium aquamarine", width=500, height=260)
        f1_button = Frame(Frame_button, bg="medium aquamarine", width=500, height=88.67)
        f2_button = Frame(Frame_button, bg="medium aquamarine", width=500, height=88.67)
        f3_button = Frame(Frame_button, bg="medium aquamarine", width=500, height=88.67)
        subheading_label = Label(f1_button, text="Welcome to Portal", font=('Garuda',14,'bold'), bg="DodgerBlue3", width=30, height=2)
        left_frame_f2 = Frame(f2_button, bg="medium aquamarine", height=88.67, width=250)
        right_frame_f2 = Frame(f2_button, bg="medium aquamarine", height=88.67, width=250)
        admin_buttonf2 = Button(left_frame_f2, text="Admin Login", bg="DodgerBlue3", font=('Garuda',12,'bold'), width=15, height=1,
                                fg="mint cream", activebackground="mint cream", activeforeground="DodgerBlue3",
                                    command=lambda : adminlogingui(root))
        std_buttonf2 = Button(right_frame_f2, text="Student Login", bg="DodgerBlue3", font=('Garuda',12,'bold'), width=15, height=1,
                                fg="mint cream", activebackground="mint cream", activeforeground="DodgerBlue3",
                                    command=lambda : stdlogingui(root))
        about_buttonf3 = Button(f3_button, text="About Us", bg="DodgerBlue3", font=('Garuda',12,'bold'), width=12, height=1,
                                fg="mint cream", activebackground="mint cream", activeforeground="DodgerBlue3",
                                command= lambda : about(root))

        middle2_frame.pack(side=TOP, fill=BOTH)
        Frame_button.pack(side=TOP,pady=15)
        f1_button.pack(side=TOP, fill=BOTH, expand=1)
        f2_button.pack(side=TOP, fill=BOTH, expand=1)
        f3_button.pack(side=TOP, fill=BOTH, expand=1)
        subheading_label.pack(pady=20)
        left_frame_f2.pack(side=LEFT, fill=BOTH, expand=1)
        right_frame_f2.pack(side=LEFT, fill=BOTH, expand=1)

        admin_buttonf2.pack(pady=25, padx=60)
        std_buttonf2.pack(pady=25, padx=60)
        about_buttonf3.pack(pady=25)


        #END FRAME for copy right
        bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
        copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved", bg="DodgerBlue3",
                                font=('Garuda',12,'bold'))
        bottom_frame.pack(side=BOTTOM, fill=BOTH)
        copytight_label.pack(pady=5)
        call_voice.wishme()


root = Tk()
obj = main(root)
mainloop()


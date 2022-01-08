from tkinter import *
from PIL import ImageTk, Image
from VoiceSystem import *
from tkinter import ttk
from db_query_admin import *
import random as ran
from DoublyLinkedList import *
from query_excel_result import *

ddl = DoublyLL()

capchata = ['ASD','KLI','KIU','BVN','PIJ','VIP','AAA','KAD','URL','OIQ','TRE','ZHI','LOQ','MMS','SMS','KKR','LQA','UNI',
            'UMT','PSL','IPL','TTT','KJH','ZXC','TCS','TGS','PPL','PIL','WIN','LRM','BSE','ALP','QRT','CCC','ZZZ','IOI']



def about(root):
    root.destroy()
    class aboutgui:
        def __init__(self, root):
            self.root = root
            root.geometry("800x650")
            root.maxsize(800, 650)
            root.minsize(800, 650)
            root.iconbitmap('logo.ico')
            root.title("Result Mangement System - About Us")

            # Start frame for title
            upper_frame = Frame(root, bg="DodgerBlue2", height=50)
            title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                font=('Garuda', 20, 'bold', 'underline'))
            upper_frame.pack(side=TOP, fill=BOTH)
            title_label.pack(pady=15)

            # Center Frame 1 for logo
            middle1_Frame = Frame(root, bg="mint cream", height=180)
            self.logo_pic = Image.open("Superior University-01.png")
            self.mypic = ImageTk.PhotoImage(self.logo_pic)
            logo_label = Label(middle1_Frame, image=self.mypic)
            middle1_Frame.pack(side=TOP, fill=BOTH)
            logo_label.pack(pady=10)

            # buttons frame center 2
            middle2_frame = Frame(root, bg="mint cream", height=333)
            haeding_frame = Frame(middle2_frame, bg="mint cream", height=40)
            subheading_label = Label(haeding_frame, text="CODER TECH TEAM", font=('Garuda', 14, 'bold'), bg="DodgerBlue3",
                                     width=30, height=2)
            team_detial_frame = Frame(middle2_frame, bg="mint cream", height=303)
            team1_frame = Frame(team_detial_frame, bg="medium aquamarine", height=283, width=236.67)
            self.team1_pic = Image.open("abdullah.png")
            self.resizedt1 = self.team1_pic.resize((180, 200), Image.ANTIALIAS)
            self.t1pic = ImageTk.PhotoImage(self.resizedt1)
            pic1_label = Label(team1_frame, bg="black", width=180.67, height=200, image=self.t1pic)
            t1_button = Button(team1_frame, text="Abdullah Maroof", bg="black", font=('Garuda', 12, 'bold'), width=15,
                                 height=1, fg="mint cream", activebackground="mint cream", activeforeground="black",
                               command= lambda : voice_aboutabdullah.wishme())
            team2_frame = Frame(team_detial_frame, bg="medium aquamarine", height=283, width=236.67)
            self.team2_pic = Image.open("kabeer.png")
            self.resizedt2 = self.team2_pic.resize((180, 200), Image.ANTIALIAS)
            self.t2pic = ImageTk.PhotoImage(self.resizedt2)
            pic2_label = Label(team2_frame, bg="black", width=180.67, height=200, image=self.t2pic)
            t2_button = Button(team2_frame, text="Abdul Kabeer", bg="black", font=('Garuda', 12, 'bold'),
                               width=15, height=1, fg="mint cream", activebackground="mint cream",
                               activeforeground="black", command= lambda : voice_aboutabdulkabeer.wishme())
            team3_frame = Frame(team_detial_frame, bg="medium aquamarine", height=283, width=236.67)
            self.team3_pic = Image.open("zubair.png")
            self.resizedt3 = self.team3_pic.resize((180, 200), Image.ANTIALIAS)
            self.t3pic = ImageTk.PhotoImage(self.resizedt3)
            pic3_label = Label(team3_frame, bg="black", width=180.67, height=200, image=self.t3pic)
            t3_button = Button(team3_frame, text="M Zubair Ali", bg="black", font=('Garuda', 12, 'bold'),
                               width=15, height=1, fg="mint cream", activebackground="mint cream",
                               activeforeground="black", command= lambda : voice_aboutZUBAIR.wishme())
            middle2_frame.pack(side=TOP, fill=BOTH)
            haeding_frame.pack(side=TOP, fill=BOTH, expand=1)
            team_detial_frame.pack(side=TOP, fill=BOTH, expand=1)
            subheading_label.pack(pady=10)
            team1_frame.pack(side=LEFT, fill=BOTH, padx=15)
            pic1_label.pack(side=TOP, fill=BOTH, padx=25, pady=5)
            t1_button.pack(pady=5)
            team2_frame.pack(side=LEFT, fill=BOTH, padx=15)
            pic2_label.pack(side=TOP, fill=BOTH, padx=25, pady=5)
            t2_button.pack(pady=5)
            team3_frame.pack(side=LEFT, fill=BOTH, padx=15)
            pic3_label.pack(side=TOP, fill=BOTH, padx=25, pady=5)
            t3_button.pack(pady=5)


            #center 3 frame back
            middle3_frame = Frame(root, bg="mint cream", height=40)
            back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", command = lambda : first_gui(root))
            middle3_frame.pack(side=TOP, fill=BOTH)
            back_button.pack(pady=5)

            # END FRAME for copy right
            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved", bg="DodgerBlue3",
                                    font=('Garuda', 12, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)
            voice_aboutus.wishme()


    root = Tk()
    obj = aboutgui(root)
    mainloop()



def first_gui(root):
    root.destroy()
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
                                    command=lambda : about(root))

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
            voice_backmain.wishme()


    root = Tk()
    obj = main(root)
    mainloop()




def stdlogingui(root):
    root.destroy()
    class stdlogin:
        def __init__(self, root):
            self.root = root
            root.geometry("800x635")
            root.maxsize(800,635)
            root.minsize(800,635)
            root.iconbitmap('logo.ico')
            root.title("Result Mangement System - Student Login")
            #Start frame for title
            upper_frame = Frame(root, bg="DodgerBlue2", height=50)
            title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                font=('Garuda', 20, 'bold', 'underline'))
            upper_frame.pack(side=TOP, fill=BOTH)
            title_label.pack(pady=15)

            #Center Frame 1 for logo
            middle1_Frame = Frame(root, bg="mint cream", height=180)
            self.logo_pic = Image.open("Superior University-01.png")
            self.mypic = ImageTk.PhotoImage(self.logo_pic)
            logo_label = Label(middle1_Frame, image=self.mypic)
            middle1_Frame.pack(side=TOP, fill=BOTH)
            logo_label.pack(pady=10)

            # LOGIN frame center 2
            middle2_frame = Frame(root, bg="mint cream", height=283)
            login_frame = Frame(middle2_frame, bg="medium aquamarine", height=263, width=500)
            subheading_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            subheading_label = Label(subheading_frame, text="Welcome to Student Login", font=('Garuda', 14, 'bold'), bg="DodgerBlue3",
                                     width=30, height=2)
            username_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            usernameleft = Frame(username_frame, bg="medium aquamarine", height=50, width=250)
            name_label = Label(usernameleft, text="User Name:  ", font=('arial', 12, 'bold'), anchor=E,
                               bg="medium aquamarine", width=24)
            usernameright = Frame(username_frame, bg="medium aquamarine", height=50, width=250)
            self.name_box = Entry(usernameright, width=25)
            password_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            passleft = Frame(password_frame, bg="medium aquamarine", height=50, width=250)
            pass_label = Label(passleft, text="Password:  ", font=('arial', 12, 'bold'), anchor=E,
                               bg="medium aquamarine", width=24)
            passright = Frame(password_frame, bg="medium aquamarine", height=50, width=250)
            self.pass_box = Entry(passright, width=25)
            capcha_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            capchaleft = Frame(capcha_frame, bg="medium aquamarine", height=50, width=250)
            capchaleft_1 = Frame(capchaleft, bg="medium aquamarine", height=50, width=100)
            capcha_statement = Label(capchaleft_1, text="CAPTCHA: ", anchor=E, width=15, font=('arial', 12, 'bold'),
                                     bg="medium aquamarine")
            capchaleft_2 = Frame(capchaleft, bg="DodgerBlue3", height=50, width=100)
            value = ran.randrange(0, len(capchata))
            ca = capchata[value]
            capcha = Label(capchaleft_2, text=ca, width=8, font=('arial', 12),
                                     bg="mint cream")
            capcharight = Frame(capcha_frame, bg="medium aquamarine", height=50, width=250)
            self.capcha_box = Entry(capcharight, width=10, font=('arial', 12), justify=CENTER)
            loginbut_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            login_button = Button(loginbut_frame, text="LOGIN", bg="black", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream", activeforeground="black",
                                  command = lambda : [
                                      stdlog(self.name_box.get(),self.pass_box.get(),self.capcha_box.get(),ca)
                                  ])
            middle2_frame.pack(side=TOP, fill=BOTH)
            login_frame.pack(side=TOP,fill=BOTH, pady=10, padx=150)
            subheading_frame.pack(side=TOP, fill=BOTH)
            username_frame.pack(side=TOP, fill=BOTH, expand=1)
            usernameleft.pack(side=LEFT, fill=BOTH)
            name_label.pack(side=RIGHT,pady=10, fill=BOTH, expand=1)
            usernameright.pack(side=LEFT, fill=BOTH, expand=1)
            self.name_box.pack(side=LEFT, pady=20)
            password_frame.pack(side=TOP, fill=BOTH, expand=1)
            passleft.pack(side=LEFT, fill=BOTH)
            pass_label.pack(side=RIGHT, pady=10, fill=BOTH, expand=1)
            passright.pack(side=LEFT, fill=BOTH, expand=1)
            self.pass_box.pack(side=LEFT, pady=20)
            capcha_frame.pack(side=TOP, fill=BOTH)
            capchaleft.pack(side=LEFT, fill=BOTH, expand=1)
            capchaleft_1.pack(side=LEFT, fill=BOTH, expand=1)
            capcha_statement.pack(side=RIGHT,pady=10, expand=1, fill=BOTH)
            capchaleft_2.pack(side=LEFT, fill=BOTH, expand=1)
            capcha.pack(pady=20, padx=5)
            capcharight.pack(side=LEFT, fill=BOTH, expand=1)
            self.capcha_box.pack(side=LEFT, pady=20, padx=10)
            loginbut_frame.pack(side=TOP, fill=BOTH)
            subheading_label.pack(pady=10)
            login_button.pack(pady=5)

            # center 3 frame back
            middle3_frame = Frame(root, bg="mint cream", height=40)
            back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", command=lambda: first_gui(root))
            middle3_frame.pack(side=TOP, fill=BOTH)
            back_button.pack(pady=5)

            # END FRAME for copy right
            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved", bg="DodgerBlue3",
                                    font=('Garuda', 12, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)
            call_stdlogin.wishme()


    def stdlog(name, password, cap, givencap):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT roll_no FROM std_info Where roll_no = '" + name + "'"
            cursor.execute(sql)
            if not cursor.fetchone():
                messagebox.showerror("Wrong Login", "Please enter correct username & password")
            else:
                if password == "student123*":
                    if givencap == cap:
                        ddl.add_at_begning(cap)
                        ddl.print_LL_backward()
                        ddl.print_LL_forward()
                        file = open("STDlogin_record.txt", "a")
                        file.write("Username: " + name)
                        file.write("\n")
                        file.write("Password: " + password)
                        file.write("\n")
                        file.write("Captcha: " + cap)
                        file.write("\n")
                        file.write("Login Time: " + dateAndTime)
                        file.write("\n\n")
                        file.close()
                        messagebox.showinfo("Successfull!!", name + ", you are login")
                        STD1semgui(root, name)
                    else:
                        messagebox.showerror("Wrong Login", "CAPTCHA is not valid!!!")
                else:
                    messagebox.showerror("Wrong Login", "Please enter correct username & password")
            con.commit()
            con.close()
        except Exception as error:
            print(error)

    root = Tk()
    obj = stdlogin(root)
    mainloop()



def adminlogingui(root):
    root.destroy()
    class adminlogin:
        def __init__(self, root):
            self.root = root
            root.geometry("800x635")
            root.maxsize(800,635)
            root.minsize(800,635)
            root.iconbitmap('logo.ico')
            root.title("Result Mangement System - Admin login")
            #Start frame for title
            upper_frame = Frame(root, bg="DodgerBlue2", height=50)
            title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                font=('Garuda', 20, 'bold', 'underline'))
            upper_frame.pack(side=TOP, fill=BOTH)
            title_label.pack(pady=15)

            #Center Frame 1 for logo
            middle1_Frame = Frame(root, bg="mint cream", height=180)
            self.logo_pic = Image.open("Superior University-01.png")
            self.mypic = ImageTk.PhotoImage(self.logo_pic)
            logo_label = Label(middle1_Frame, image=self.mypic)
            middle1_Frame.pack(side=TOP, fill=BOTH)
            logo_label.pack(pady=10)

            # LOGIN frame center 2
            middle2_frame = Frame(root, bg="mint cream", height=283)
            login_frame = Frame(middle2_frame, bg="medium aquamarine", height=263, width=500)
            subheading_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            subheading_label = Label(subheading_frame, text="Welcome to Admin Login", font=('Garuda', 14, 'bold'),
                                     bg="DodgerBlue3", width=30, height=2)
            username_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            usernameleft = Frame(username_frame, bg="medium aquamarine", height=50, width=250)
            name_label = Label(usernameleft, text="User Name:  ", font=('arial', 12, 'bold'), anchor=E,
                               bg="medium aquamarine", width=24)
            usernameright = Frame(username_frame, bg="medium aquamarine", height=50, width=250)
            self.name_box = Entry(usernameright, width=25)
            password_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            passleft = Frame(password_frame, bg="medium aquamarine", height=50, width=250)
            pass_label = Label(passleft, text="Password:  ", font=('arial', 12, 'bold'), anchor=E,
                               bg="medium aquamarine", width=24)
            passright = Frame(password_frame, bg="medium aquamarine", height=50, width=250)
            self.pass_box = Entry(passright, width=25)
            capcha_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            capchaleft = Frame(capcha_frame, bg="medium aquamarine", height=50, width=250)
            capchaleft_1 = Frame(capchaleft, bg="medium aquamarine", height=50, width=100)
            capcha_statement = Label(capchaleft_1, text="CAPTCHA: ", anchor=E, width=15, font=('arial', 12, 'bold'),
                                     bg="medium aquamarine")
            capchaleft_2 = Frame(capchaleft, bg="DodgerBlue3", height=50, width=100)
            value = ran.randrange(0, len(capchata))
            ca = capchata[value]
            capcha = Label(capchaleft_2, text=ca, width=8, font=('arial', 12),
                           bg="mint cream")
            capcharight = Frame(capcha_frame, bg="medium aquamarine", height=50, width=250)
            self.capcha_box = Entry(capcharight, width=10, font=('arial', 12), justify=CENTER)
            loginbut_frame = Frame(login_frame, bg="medium aquamarine", width=500, height=50)
            login_button = Button(loginbut_frame, text="LOGIN", bg="black", font=('Garuda', 12, 'bold'), width=12,
                                  height=1, fg="mint cream", activebackground="mint cream",
                                  activeforeground="black",
                                  command=lambda:
                                      adminlog(self.name_box.get(), self.pass_box.get(), self.capcha_box.get(), ca)
                                  )

            middle2_frame.pack(side=TOP, fill=BOTH)
            login_frame.pack(side=TOP, fill=BOTH, pady=10, padx=150)
            subheading_frame.pack(side=TOP, fill=BOTH)
            username_frame.pack(side=TOP, fill=BOTH, expand=1)
            usernameleft.pack(side=LEFT, fill=BOTH)
            name_label.pack(side=RIGHT, pady=10, fill=BOTH, expand=1)
            usernameright.pack(side=LEFT, fill=BOTH, expand=1)
            self.name_box.pack(side=LEFT, pady=20)
            password_frame.pack(side=TOP, fill=BOTH, expand=1)
            passleft.pack(side=LEFT, fill=BOTH)
            pass_label.pack(side=RIGHT, pady=10, fill=BOTH, expand=1)
            passright.pack(side=LEFT, fill=BOTH, expand=1)
            self.pass_box.pack(side=LEFT, pady=20)
            capcha_frame.pack(side=TOP, fill=BOTH)
            capchaleft.pack(side=LEFT, fill=BOTH, expand=1)
            capchaleft_1.pack(side=LEFT, fill=BOTH, expand=1)
            capcha_statement.pack(side=RIGHT, pady=10, expand=1, fill=BOTH)
            capchaleft_2.pack(side=LEFT, fill=BOTH, expand=1)
            capcha.pack(pady=20, padx=5)
            capcharight.pack(side=LEFT, fill=BOTH, expand=1)
            self.capcha_box.pack(side=LEFT, pady=20, padx=10)
            loginbut_frame.pack(side=TOP, fill=BOTH)
            subheading_label.pack(pady=10)
            login_button.pack(pady=5)

            # center 3 frame back
            middle3_frame = Frame(root, bg="mint cream", height=40)
            back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", command=lambda: first_gui(root))
            middle3_frame.pack(side=TOP, fill=BOTH)
            back_button.pack(pady=5)

            # END FRAME for copy right
            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved", bg="DodgerBlue3",
                                    font=('Garuda', 12, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)
            call_adminlogin.wishme()

        #def clear(self):
            #self.name_box.delete(0, END)
         #   self.pass_box.delete(0, END)
          #  self.capcha_box.delete(0, END)

    def adminlog(name, password, cap, givencap):

        try:
            con = connect("Admin.db")
            cursor = con.cursor()
            sql = "SELECT * FROM admin Where username = '" +name + "' AND password = '" + password + "'"
            cursor.execute(sql)
            if not cursor.fetchone():
                messagebox.showerror("Wrong Login", "Please enter correct username & password")
            else:
                if givencap == cap:
                    ddl.add_at_begning(cap)
                    ddl.print_LL_backward()
                    ddl.print_LL_forward()
                    file = open("adminlogin_record.txt", "a")
                    file.write("Username: "+name)
                    file.write("\n")
                    file.write("Password: "+password)
                    file.write("\n")
                    file.write("Captcha: "+cap)
                    file.write("\n")
                    file.write("Login Time: " + dateAndTime)
                    file.write("\n\n")
                    file.close()

                    messagebox.showinfo("Successfull!!",name+", you are login")
                    admingui(root)
                else:
                    messagebox.showerror("Wrong Login", "CAPTCHA is not valid!!!")
            con.commit()
            con.close()
        except Exception as error:
            print(error)

    root = Tk()
    obj = adminlogin(root)
    mainloop()


def admingui(root):
    root.destroy()
    class admin:
        def __init__(self, root):
            self.root = root
            root.geometry("1000x750")
            root.maxsize(1000,750)
            root.minsize(1000,750)
            root.iconbitmap('logo.ico')
            root.title("Result Mangement System - Admin Portal")
            #Start frame for title
            upper_frame = Frame(root, bg="DodgerBlue2", height=50)
            title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                font=('Garuda', 20, 'bold', 'underline'))
            upper_frame.pack(side=TOP, fill=BOTH)
            title_label.pack(pady=15)

            #Center Frame 1 for logo
            middle1_Frame = Frame(root, bg="mint cream", height=180)
            self.logo_pic = Image.open("Superior University-01.png")
            self.mypic = ImageTk.PhotoImage(self.logo_pic)
            logo_label = Label(middle1_Frame, image=self.mypic)
            middle1_Frame.pack(side=TOP, fill=BOTH)
            logo_label.pack(pady=10)

            #frame for the data getting
            middle2_frame = Frame(root, bg="mint cream", height=430)
            subheading_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=50)
            subheading_label = Label(subheading_frame, text="Welcome to Admin Portal", font=('Garuda', 14, 'bold'),
                                     bg="DodgerBlue3", width=40, height=2)


            # frame 1 in middle2 frame
            frame1_middle2 = Frame(middle2_frame, bg="medium aquamarine", width=900, height=100)
            frame_top_f1m2 = Frame(frame1_middle2, bg="medium aquamarine", width=900, height=50)
            ft1_f1m2 = Frame(frame_top_f1m2, bg="medium aquamarine", width=225, height=50)
            ft1_f1m2label = Label(ft1_f1m2, text="Department", width=15, height=1, font=('Garuda', 12, 'bold'),
                                  bg="DodgerBlue3")
            ft2_f1m2 = Frame(frame_top_f1m2, bg="medium aquamarine", width=225, height=50)
            self.deptf1_box = ttk.Combobox(ft2_f1m2, width=20, state="readonly", justify=CENTER, font=('Garuda', 12))
            self.deptf1_box['values'] = ("Select Department", "All", "Software Engineering", "Data Science"
                                          , "Artificial Intelligence")
            ft3_f1m2 = Frame(frame_top_f1m2, bg="medium aquamarine", width=225, height=50)
            ft3_f1m2label = Label(ft3_f1m2, text="Data Order", width=15, height=1, font=('Garuda', 12, 'bold'),
                                  bg="DodgerBlue3")
            ft4_f1m2 = Frame(frame_top_f1m2, bg="medium aquamarine", width=225, height=50)
            self.ascdes_box = ttk.Combobox(ft4_f1m2, width=20, state="readonly", justify=CENTER, font=('Garuda', 12))
            self.ascdes_box['values'] = ("Select Asc or Desc", "Ascending", "Descending")
            frame_bottom_f1m2 = Frame(frame1_middle2, bg="medium aquamarine", width=900, height=50)
            gatdata_f1button = Button(frame_bottom_f1m2, text="Get Data", bg="black", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="black",
                                 command = lambda :data_order_ascdesc(self.deptf1_box.get(),self.ascdes_box.get()))

            # frame 2 in middle2 frame
            frame2_middle2 = Frame(middle2_frame, bg="medium aquamarine", width=900, height=100)
            frame_top_f2m2 = Frame(frame2_middle2, bg="medium aquamarine", width=900, height=50)
            ft1_f2m2 = Frame(frame_top_f2m2, bg="medium aquamarine", width=225, height=50)
            ft1_f2m2label = Label(ft1_f2m2, text="Department", width=15, height=1, font=('Garuda', 12, 'bold'),
                                  bg="DodgerBlue3")
            ft2_f2m2 = Frame(frame_top_f2m2, bg="medium aquamarine", width=225, height=50)
            self.deptf2_box = ttk.Combobox(ft2_f2m2, width=20, state="readonly", justify=CENTER, font=('Garuda', 12))
            self.deptf2_box['values'] = ("Select Department", "All", "Software Engineering", "Data Science"
                                          , "Artificial Intelligence")
            ft3_f2m2 = Frame(frame_top_f2m2, bg="medium aquamarine", width=225, height=50)
            ft3_f2m2label = Label(ft3_f2m2, text="Semester", width=15, height=1, font=('Garuda', 12, 'bold'),
                              bg="DodgerBlue3")
            ft4_f2m2 = Frame(frame_top_f2m2, bg="medium aquamarine", width=225, height=50)
            self.sem_box = ttk.Combobox(ft4_f2m2, width=20, state="readonly", justify=CENTER, font=('Garuda', 12))
            self.sem_box['values'] = ("Select Semester", "Both Semester", "1st Semester","2nd Semester")
            frame_bottom_f2m2 = Frame(frame2_middle2, bg="medium aquamarine", width=900, height=50)
            gatdata_f2button = Button(frame_bottom_f2m2, text="Get Data", bg="black", font=('Garuda', 12, 'bold'),
                                      width=12, height=1, fg="mint cream", activebackground="mint cream",
                                      activeforeground="black",
                                      command = lambda :data_semester(self.deptf2_box.get(),self.sem_box.get()))


            # frame 3 in middle2 frame
            frame3_middle2 = Frame(middle2_frame, bg="medium aquamarine", width=900, height=50)
            ft3_left = Frame(frame3_middle2, bg="medium aquamarine", width=225, height=50)
            label_ft3 = Label(ft3_left, text="Total Student", width=15, height=1, font=('Garuda', 12, 'bold'), bg="DodgerBlue3")
            ft3_right = Frame(frame3_middle2, bg="medium aquamarine", width=225, height=50)
            self.deptft3_box = ttk.Combobox(ft3_right, width=20, state="readonly", justify=CENTER, font=('Garuda', 12))
            self.deptft3_box['values'] = ("Select Department","All","Software Engineering","Data Science"
                                          ,"Artificial Intelligence")

            ft4_f3m2 = Frame(frame3_middle2, bg="medium aquamarine", width=450, height=50)
            gatdata_f3botbutton = Button(ft4_f3m2, text="Get Data", bg="black", font=('Garuda', 12, 'bold'),
                                      width=12, height=1, fg="mint cream", activebackground="mint cream",
                                      activeforeground="black",
                                         command= lambda : total_student(self.deptft3_box.get()))


            middle2_frame.pack(side=TOP, fill=BOTH, expand=1)
            subheading_frame.pack(side=TOP, fill=BOTH, pady=10, padx=50)
            subheading_label.pack(pady=20)
            frame1_middle2.pack(side=TOP, fill=BOTH, pady=10, padx=50)
            frame2_middle2.pack(side=TOP, fill=BOTH, pady=10, padx=50)
            frame3_middle2.pack(side=TOP, fill=BOTH, pady=10, padx=50)
            frame_top_f1m2.pack(side=TOP, fill=BOTH, expand=1)
            ft1_f1m2.pack(side=LEFT, fill=BOTH, expand=1)
            ft1_f1m2label.pack(pady=10, padx=20)
            ft2_f1m2.pack(side=LEFT, fill=BOTH, expand=1)
            self.deptf1_box.pack(pady=10, padx=20)
            self.deptf1_box.current(0)
            ft3_f1m2.pack(side=LEFT, fill=BOTH, expand=1)
            ft3_f1m2label.pack(pady=10, padx=20)
            ft4_f1m2.pack(side=LEFT, fill=BOTH, expand=1)
            self.ascdes_box.pack(pady=10, padx=20)
            self.ascdes_box.current(0)
            frame_bottom_f1m2.pack(side=TOP, fill=BOTH, expand=1)
            gatdata_f1button.pack(pady=10)
            frame_top_f2m2.pack(side=TOP, fill=BOTH, expand=1)
            ft1_f2m2.pack(side=LEFT, fill=BOTH, expand=1)
            ft1_f2m2label.pack(pady=10, padx=20)
            ft2_f2m2.pack(side=LEFT, fill=BOTH, expand=1)
            self.deptf2_box.pack(pady=10, padx=20)
            self.deptf2_box.current(0)
            ft3_f2m2.pack(side=LEFT, fill=BOTH, expand=1)
            ft3_f2m2label.pack(pady=10, padx=20)
            ft4_f2m2.pack(side=LEFT, fill=BOTH, expand=1)
            self.sem_box.pack(pady=10, padx=20)
            self.sem_box.current(0)
            frame_bottom_f2m2.pack(side=TOP, fill=BOTH, expand=1)
            gatdata_f2button.pack(pady=10)
            ft3_left.pack(side=LEFT, fill=BOTH, expand=1)
            label_ft3.pack(pady=10, padx=40)
            ft3_right.pack(side=LEFT, fill=BOTH, expand=1)
            self.deptft3_box.pack(pady=10, padx=40)
            self.deptft3_box.current(0)
            ft4_f3m2.pack(side=LEFT, fill=BOTH, expand=1)
            gatdata_f3botbutton.pack(pady=10, padx=80)


            # center 3 frame back
            middle3_frame = Frame(root, bg="mint cream", height=40)
            back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'), width=12,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", command=lambda: adminlogingui(root))
            middle3_frame.pack(side=TOP, fill=BOTH)
            back_button.pack(pady=10)

            # END FRAME for copy right
            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved", bg="DodgerBlue3",
                                    font=('Garuda', 12, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)
            call_admin.wishme()




    root = Tk()
    obj = admin(root)
    mainloop()


def STD1semgui(root, name):
    root.destroy()
    try:
        con = connect("studentrecord.db")
        cursor = con.cursor()
        sql = "SELECT roll_no, Semester FROM std_semsec Where roll_no = '" + name + "' AND Semester ='1st'"
        cursor.execute(sql)
        if not cursor.fetchone():
            #2nd semester portal
            class std2se:
                def __init__(self, root):
                    self.root = root
                    root.geometry("1000x800")
                    root.maxsize(1000, 840)
                    root.minsize(1000, 840)
                    root.iconbitmap('logo.ico')
                    root.title("Result Mangement System - Student Portal - 2nd Semester")
                    # Start frame for title
                    upper_frame = Frame(root, bg="DodgerBlue2", height=50)
                    title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                        font=('Garuda', 20, 'bold', 'underline'))
                    upper_frame.pack(side=TOP, fill=BOTH)
                    title_label.pack(pady=10)

                    # Center Frame 1 for logo
                    middle1_Frame = Frame(root, bg="mint cream", height=180)
                    self.logo_pic = Image.open("Superior University-01.png")
                    self.mypic = ImageTk.PhotoImage(self.logo_pic)
                    logo_label = Label(middle1_Frame, image=self.mypic)
                    middle1_Frame.pack(side=TOP, fill=BOTH)
                    logo_label.pack(pady=5)

                    # frame for the data getting
                    middle2_frame = Frame(root, bg="mint cream", height=430)
                    subheading_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=30)
                    subheading_label = Label(subheading_frame, text="Welcome to Student Portal",
                                             font=('Garuda', 14, 'bold'),
                                             bg="DodgerBlue3", width=40, height=2)
                    Personalinfo_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=158)
                    piframe1 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pilabel = Label(piframe1, bg="DodgerBlue3", width=30, height=1, text="Personal Information",
                                    font=('Garuda',12,'bold'))
                    piframe2 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pif2_left = Frame(piframe2, bg="medium aquamarine", width=500, height=37.5)
                    name_label = Label(pif2_left, text="Name: ", font=('Garuda',10,'bold'), height=1, anchor=E,
                                       width=10, bg="medium aquamarine")
                    getname_label = Label(pif2_left, text=result.std_name(name), font=('Garuda',10), height=1, anchor=W,
                                          width=50, bg="medium aquamarine")
                    pif2_right = Frame(piframe2, bg="medium aquamarine", width=500, height=37.5)
                    fat_name_label = Label(pif2_right, text="Father Name: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                       width=12, bg="medium aquamarine")
                    getfatname_label = Label(pif2_right, text=result.std_fname(name), font=('Garuda', 10), height=1, anchor=W,
                                          width=50, bg="medium aquamarine")
                    piframe3 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pif3_left = Frame(piframe3, bg="medium aquamarine", width=500, height=37.5)
                    rollno_label = Label(pif3_left, text="Roll no: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                       width=10, bg="medium aquamarine")
                    getrollno_label = Label(pif3_left, text=result.std_rolno(name), font=('Garuda', 10), height=1, anchor=W,
                                          width=50, bg="medium aquamarine")
                    pif3_right = Frame(piframe3, bg="medium aquamarine", width=500, height=37.5)
                    batch_label = Label(pif3_right, text="Batch: ", font=('Garuda', 10, 'bold'), height=1,
                                           anchor=E, width=10, bg="medium aquamarine")
                    getbatch_label = Label(pif3_right, text=result.std_batch(name), font=('Garuda', 10), height=1, anchor=W,
                                             width=50, bg="medium aquamarine")
                    piframe4 = Frame(Personalinfo_frame, bg="blue", width=900, height=41.5)
                    pif4_left = Frame(piframe4, bg="medium aquamarine", width=500, height=41.5)
                    program_label = Label(pif4_left, text="Program: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                       width=10, bg="medium aquamarine")
                    getprogram_label = Label(pif4_left, text=result.std_program(name), font=('Garuda', 10), height=1, anchor=W,
                                          width=50, bg="medium aquamarine")
                    pif4_right = Frame(piframe4, bg="medium aquamarine", width=500, height=41.5)
                    dep_label = Label(pif4_right, text="Department: ", font=('Garuda', 10, 'bold'), height=1,
                                           anchor=E, width=12, bg="medium aquamarine")
                    getdep_label = Label(pif4_right, text=result.std_dept(name), font=('Garuda', 10), height=1, anchor=W,
                                             width=50, bg="medium aquamarine")

                    # result frame
                    result_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=282)
                    reframe1 = Frame(result_frame, bg="medium aquamarine", width=900, height=38)
                    relabel = Label(reframe1, bg="DodgerBlue3", width=30, height=1, text="Result Card",
                                    font=('Garuda', 12, 'bold'))
                    center_reframe = Frame(result_frame, bg="blue", width=900, height=214)
                    cere_frame1 = Frame(center_reframe, bg="medium aquamarine", width=900, height=30.6)
                    cref1_left = Frame(cere_frame1, bg="medium aquamarine", height=30.66, width=480)
                    hsub_cref1l = Label(cref1_left, bg="DodgerBlue3", width=20, height=1, text="Subject",
                                        font=('Garuda', 10, 'bold'))
                    hmark_cref1l = Label(cref1_left, bg="DodgerBlue3", width=15, height=1, text="Marks",
                                         font=('Garuda', 10, 'bold'))
                    hgrade_cref1l = Label(cref1_left, bg="DodgerBlue3", width=15, height=1, text="Grade",
                                          font=('Garuda', 10, 'bold'))
                    cref1_right = Frame(cere_frame1, bg="medium aquamarine", height=30.6, width=480)
                    hsub_cref1r = Label(cref1_right, bg="DodgerBlue3", width=20, height=1, text="Subject",
                                        font=('Garuda', 10, 'bold'))
                    hmark_cref1r = Label(cref1_right, bg="DodgerBlue3", width=15, height=1, text="Marks",
                                         font=('Garuda', 10, 'bold'))
                    hgrade_cref1r = Label(cref1_right, bg="DodgerBlue3", width=16, height=1, text="Grade",
                                          font=('Garuda', 10, 'bold'))
                    cere_frame2 = Frame(center_reframe, bg="medium aquamarine", width=900, height=30.6)
                    cref2_left = Frame(cere_frame2, bg="medium aquamarine", height=30.6, width=480)
                    calsub_cref2l = Label(cref2_left, bg="mint cream", width=20, height=1, text="Calculus",
                                          font=('Garuda', 10))
                    calmark_cref2l = Label(cref2_left, bg="mint cream", width=15, height=1, text=result.calculus(name),
                                           font=('Garuda', 10))
                    calgrade_cref2l = Label(cref2_left, bg="mint cream", width=15, height=1, text=grade.calgrade(name),
                                            font=('Garuda', 10))
                    cref2_right = Frame(cere_frame2, bg="medium aquamarine", height=30.6, width=480)
                    engsub_cref2r = Label(cref2_right, bg="mint cream", width=20, height=1, text="English",
                                          font=('Garuda', 10))
                    engmark_cref2r = Label(cref2_right, bg="mint cream", width=15, height=1, text=result.eng(name),
                                           font=('Garuda', 10))
                    enggrade_cref2r = Label(cref2_right, bg="mint cream", width=16, height=1, text=grade.enggrade(name),
                                            font=('Garuda', 10))
                    cere_frame3 = Frame(center_reframe, bg="medium aquamarine", width=900, height=30.6)
                    cref3_left = Frame(cere_frame3, bg="medium aquamarine", height=36, width=480)
                    itcsub_cref3l = Label(cref3_left, bg="mint cream", width=20, height=1,
                                          text="Introduction To Computing",
                                          font=('Garuda', 10))
                    itcmark_cref3l = Label(cref3_left, bg="mint cream", width=15, height=1, text=result.itc(name),
                                           font=('Garuda', 10))
                    itcgrade_cref3l = Label(cref3_left, bg="mint cream", width=15, height=1, text=grade.itcgrade(name),
                                            font=('Garuda', 10))
                    cref3_right = Frame(cere_frame3, bg="medium aquamarine", height=36, width=480)
                    pfsub_cref3r = Label(cref3_right, bg="mint cream", width=20, height=1,
                                         text="Programming Fundamental",
                                         font=('Garuda', 10))
                    pfmark_cref3r = Label(cref3_right, bg="mint cream", width=15, height=1, text=result.pf(name),
                                          font=('Garuda', 10))
                    pfgrade_cref3r = Label(cref3_right, bg="mint cream", width=16, height=1, text=grade.pfgrade(name),
                                           font=('Garuda', 10))
                    cere_frame4 = Frame(center_reframe, bg="medium aquamarine", width=900, height=30.6)
                    cref4_left = Frame(cere_frame4, bg="medium aquamarine", height=36, width=480)
                    apsub_cref4l = Label(cref4_left, bg="mint cream", width=20, height=1,
                                         text="Applied Physics", font=('Garuda', 10))
                    apmark_cref4l = Label(cref4_left, bg="mint cream", width=15, height=1, text=result.ap(name),
                                          font=('Garuda', 10))
                    apgrade_cref4l = Label(cref4_left, bg="mint cream", width=15, height=1, text=grade.apgrade(name),
                                           font=('Garuda', 10))
                    cref4_right = Frame(cere_frame4, bg="medium aquamarine", height=36, width=480)
                    disstsub_cref4r = Label(cref4_right, bg="mint cream", width=20, height=1,
                                        text="Discrete Structure", font=('Garuda', 10))
                    disstmark_cref4r = Label(cref4_right, bg="mint cream", width=15, height=1, text=result.disctruc(name),
                                         font=('Garuda', 10))
                    disstgrade_cref4r = Label(cref4_right, bg="mint cream", width=16, height=1, text=grade.disctrgrade(name),
                                          font=('Garuda', 10))
                    cere_frame5 = Frame(center_reframe, bg="orange", width=900, height=30.6)
                    cref5_left = Frame(cere_frame5, bg="medium aquamarine", height=36, width=480)
                    oopsub_cref5l = Label(cref5_left, bg="mint cream", width=20, height=1,
                                         text="Object Ori. Programming", font=('Garuda', 10))
                    oopmark_cref5l = Label(cref5_left, bg="mint cream", width=15, height=1, text=result.oop(name),
                                          font=('Garuda', 10))
                    oopgrade_cref5l = Label(cref5_left, bg="mint cream", width=15, height=1, text=grade.oopgrade(name),
                                           font=('Garuda', 10))
                    cref5_right = Frame(cere_frame5, bg="medium aquamarine", height=36, width=480)
                    prostatsub_cref5r = Label(cref5_right, bg="mint cream", width=20, height=1,
                                            text="Probability & Stat", font=('Garuda', 10))
                    prostatmark_cref5r = Label(cref5_right, bg="mint cream", width=15, height=1, text=result.stat(name),
                                             font=('Garuda', 10))
                    prostatgrade_cref5r = Label(cref5_right, bg="mint cream", width=16, height=1, text=grade.statgrade(name),
                                          font=('Garuda', 10))
                    cere_frame6 = Frame(center_reframe, bg="black", width=900, height=30.6)
                    cref6_left = Frame(cere_frame6, bg="medium aquamarine", height=36, width=480)
                    tbwsub_cref6l = Label(cref6_left, bg="mint cream", width=20, height=1,
                                          text="Tec. & Bus. Writing", font=('Garuda', 10))
                    tbwmark_cref6l = Label(cref6_left, bg="mint cream", width=15, height=1, text=result.tbw(name),
                                           font=('Garuda', 10))
                    tbwgrade_cref6l = Label(cref6_left, bg="mint cream", width=15, height=1, text=grade.tbwgrade(name),
                                            font=('Garuda', 10))
                    cref6_right = Frame(cere_frame6, bg="medium aquamarine", height=36, width=480)
                    issub_cref6r = Label(cref6_right, bg="mint cream", width=20, height=1,
                                              text="Islamic Studies", font=('Garuda', 10))
                    ismark_cref6r = Label(cref6_right, bg="mint cream", width=15, height=1, text=result.isl(name),
                                               font=('Garuda', 10))
                    isgrade_cref6r = Label(cref6_right, bg="mint cream", width=16, height=1, text=grade.islgrade(name),
                                                font=('Garuda', 10))
                    cere_frame7 = Frame(center_reframe, bg="orange", width=900, height=30.6)
                    cref7_left = Frame(cere_frame7, bg="medium aquamarine", height=36, width=480)
                    pssub_cref7l = Label(cref7_left, bg="mint cream", width=20, height=1,
                                          text="Pakistan Studies", font=('Garuda', 10))
                    psmark_cref7l = Label(cref7_left, bg="mint cream", width=15, height=1, text=result.pak(name),
                                           font=('Garuda', 10))
                    psgrade_cref7l = Label(cref7_left, bg="mint cream", width=15, height=1, text=grade.pakgrade(name),
                                            font=('Garuda', 10))
                    cref7_right = Frame(cere_frame7, bg="medium aquamarine", height=36, width=480)
                    tsub_cref7r = Label(cref7_right, bg="mint cream", width=20, height=1,
                                         text="Total", font=('Garuda', 10,'bold'))
                    tmark_cref7r = Label(cref7_right, bg="mint cream", width=15, height=1, text=grade.total_marks2sem(name),
                                          font=('Garuda', 10,'bold'))
                    tgrade_cref7r = Label(cref7_right, bg="mint cream", width=16, height=1,
                                          text=grade.gpa2sem(name),
                                           font=('Garuda', 10,'bold'))
                    re_lastframe = Frame(result_frame, bg="medium aquamarine", height=40, width=900)
                    getresult_button = Button(re_lastframe, text="Get Result", bg="black", font=('Garuda', 12, 'bold'),
                                              width=12, height=1, fg="mint cream", activebackground="mint cream",
                                              activeforeground="black", command=lambda : excelreport.sem2_resultreport(name))


                    middle2_frame.pack(side=TOP, fill=BOTH, expand=1)
                    subheading_frame.pack(side=TOP, fill=BOTH, pady=10, padx=20)
                    subheading_label.pack(pady=10)
                    Personalinfo_frame.pack(side=TOP, fill=BOTH, pady=5, padx=20)
                    piframe1.pack(side=TOP, fill=BOTH)
                    pilabel.pack(pady=5)
                    piframe2.pack(side=TOP, fill=BOTH)
                    pif2_left.pack(side=LEFT, fill=BOTH)
                    name_label.pack(side=LEFT)
                    getname_label.pack(side=LEFT)
                    pif2_right.pack(side=LEFT, fill=BOTH)
                    fat_name_label.pack(side=LEFT)
                    getfatname_label.pack(side=LEFT)
                    piframe3.pack(side=TOP, fill=BOTH)
                    pif3_left.pack(side=LEFT, fill=BOTH)
                    rollno_label.pack(side=LEFT)
                    getrollno_label.pack(side=LEFT)
                    pif3_right.pack(side=LEFT, fill=BOTH)
                    batch_label.pack(side=LEFT)
                    getbatch_label.pack(side=LEFT)
                    piframe4.pack(side=TOP, fill=BOTH, pady=2)
                    pif4_left.pack(side=LEFT, fill=BOTH)
                    program_label.pack(side=LEFT)
                    getprogram_label.pack(side=LEFT)
                    pif4_right.pack(side=LEFT, fill=BOTH)
                    dep_label.pack(side=LEFT)
                    getdep_label.pack(side=LEFT)
                    result_frame.pack(side=TOP, fill=BOTH, pady=5, padx=20)
                    reframe1.pack(side=TOP, fill=BOTH)
                    relabel.pack(pady=5)
                    center_reframe.pack(side=TOP, fill=BOTH)
                    cere_frame1.pack(side=TOP, fill=BOTH)
                    cref1_left.pack(side=LEFT, fill=BOTH)
                    hsub_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hmark_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hgrade_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    cref1_right.pack(side=LEFT, fill=BOTH)
                    hsub_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hmark_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hgrade_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    cere_frame2.pack(side=TOP, fill=BOTH)
                    cref2_left.pack(side=LEFT, fill=BOTH)
                    calsub_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    calmark_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    calgrade_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref2_right.pack(side=LEFT, fill=BOTH)
                    engsub_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    engmark_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    enggrade_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame3.pack(side=TOP, fill=BOTH)
                    cref3_left.pack(side=LEFT, fill=BOTH)
                    itcsub_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    itcmark_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    itcgrade_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref3_right.pack(side=LEFT, fill=BOTH)
                    pfsub_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    pfmark_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    pfgrade_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame4.pack(side=TOP, fill=BOTH)
                    cref4_left.pack(side=LEFT, fill=BOTH)
                    apsub_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    apmark_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    apgrade_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref4_right.pack(side=LEFT, fill=BOTH)
                    disstsub_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    disstmark_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    disstgrade_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame5.pack(side=TOP, fill=BOTH)
                    cref5_left.pack(side=LEFT, fill=BOTH)
                    oopsub_cref5l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    oopmark_cref5l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    oopgrade_cref5l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref5_right.pack(side=LEFT, fill=BOTH)
                    prostatsub_cref5r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    prostatmark_cref5r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    prostatgrade_cref5r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame6.pack(side=TOP, fill=BOTH)
                    cref6_left.pack(side=LEFT, fill=BOTH)
                    tbwsub_cref6l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tbwmark_cref6l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tbwgrade_cref6l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref6_right.pack(side=LEFT, fill=BOTH)
                    issub_cref6r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    ismark_cref6r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    isgrade_cref6r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame7.pack(side=TOP, fill=BOTH)
                    cref7_left.pack(side=LEFT, fill=BOTH)
                    pssub_cref7l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    psmark_cref7l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    psgrade_cref7l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref7_right.pack(side=LEFT, fill=BOTH)
                    tsub_cref7r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tmark_cref7r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tgrade_cref7r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    re_lastframe.pack(side=BOTTOM, fill=BOTH)
                    getresult_button.pack(pady=5)



                    # center 3 frame back
                    middle3_frame = Frame(root, bg="mint cream", height=40)
                    back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                                         width=12,
                                         height=1, fg="mint cream", activebackground="mint cream",
                                         activeforeground="DodgerBlue3", command=lambda: stdlogingui(root))
                    middle3_frame.pack(side=TOP, fill=BOTH)
                    back_button.pack(pady=5)

                    # END FRAME for copy right
                    bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
                    copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved",
                                            bg="DodgerBlue3",
                                            font=('Garuda', 12, 'bold'))
                    bottom_frame.pack(side=BOTTOM, fill=BOTH)
                    copytight_label.pack(pady=5)
                    call_std.wishme()

            root = Tk()
            obj = std2se(root)
            mainloop()
        else:
            #1st semester portal
            class std1se:
                def __init__(self, root):
                    self.root = root
                    root.geometry("1000x770")
                    root.maxsize(1000, 770)
                    root.minsize(1000, 770)
                    root.iconbitmap('logo.ico')
                    root.title("Result Mangement System - Student Portal - 1st Semester")
                    # Start frame for title
                    upper_frame = Frame(root, bg="DodgerBlue2", height=50)
                    title_label = Label(upper_frame, text="Result Portal", bg="DodgerBlue2",
                                        font=('Garuda', 20, 'bold', 'underline'))
                    upper_frame.pack(side=TOP, fill=BOTH)
                    title_label.pack(pady=15)

                    # Center Frame 1 for logo
                    middle1_Frame = Frame(root, bg="mint cream", height=180)
                    self.logo_pic = Image.open("Superior University-01.png")
                    self.mypic = ImageTk.PhotoImage(self.logo_pic)
                    logo_label = Label(middle1_Frame, image=self.mypic)
                    middle1_Frame.pack(side=TOP, fill=BOTH)
                    logo_label.pack(pady=10)

                    # frame for the data getting
                    middle2_frame = Frame(root, bg="mint cream", height=430)
                    subheading_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=30)
                    subheading_label = Label(subheading_frame, text="Welcome to Student Portal",
                                             font=('Garuda', 14, 'bold'),
                                             bg="DodgerBlue3", width=40, height=2)
                    #personal info frame
                    Personalinfo_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=158)
                    piframe1 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pilabel = Label(piframe1, bg="DodgerBlue3", width=30, height=1, text="Personal Information",
                                    font=('Garuda', 12, 'bold'))
                    piframe2 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pif2_left = Frame(piframe2, bg="medium aquamarine", width=500, height=37.5)
                    name_label = Label(pif2_left, text="Name: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                       width=10, bg="medium aquamarine")
                    getname_label = Label(pif2_left, text=result.std_name(name), font=('Garuda', 10), height=1, anchor=W,
                                          width=50, bg="medium aquamarine")
                    pif2_right = Frame(piframe2, bg="medium aquamarine", width=500, height=37.5)
                    fat_name_label = Label(pif2_right, text="Father Name: ", font=('Garuda', 10, 'bold'), height=1,
                                           anchor=E,
                                           width=12, bg="medium aquamarine")
                    getfatname_label = Label(pif2_right, text=result.std_fname(name), font=('Garuda', 10), height=1, anchor=W,
                                             width=50, bg="medium aquamarine")
                    piframe3 = Frame(Personalinfo_frame, bg="medium aquamarine", width=900, height=37.5)
                    pif3_left = Frame(piframe3, bg="medium aquamarine", width=500, height=37.5)
                    rollno_label = Label(pif3_left, text="Roll no: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                         width=10, bg="medium aquamarine")
                    getrollno_label = Label(pif3_left, text=result.std_rolno(name), font=('Garuda', 10), height=1, anchor=W,
                                            width=50, bg="medium aquamarine")
                    pif3_right = Frame(piframe3, bg="medium aquamarine", width=500, height=37.5)
                    batch_label = Label(pif3_right, text="Batch: ", font=('Garuda', 10, 'bold'), height=1,
                                        anchor=E, width=10, bg="medium aquamarine")
                    getbatch_label = Label(pif3_right, text=result.std_batch(name), font=('Garuda', 10), height=1, anchor=W,
                                           width=50, bg="medium aquamarine")
                    piframe4 = Frame(Personalinfo_frame, bg="blue", width=900, height=41.5)
                    pif4_left = Frame(piframe4, bg="medium aquamarine", width=500, height=41.5)
                    program_label = Label(pif4_left, text="Program: ", font=('Garuda', 10, 'bold'), height=1, anchor=E,
                                          width=10, bg="medium aquamarine")
                    getprogram_label = Label(pif4_left, text=result.std_program(name), font=('Garuda', 10),
                                             height=1, anchor=W, width=50, bg="medium aquamarine")
                    pif4_right = Frame(piframe4, bg="medium aquamarine", width=500, height=41.5)
                    dep_label = Label(pif4_right, text="Department: ", font=('Garuda', 10, 'bold'), height=1,
                                      anchor=E, width=12, bg="medium aquamarine")
                    getdep_label = Label(pif4_right, text=result.std_dept(name), font=('Garuda', 10), height=1,
                                         anchor=W,
                                         width=50, bg="medium aquamarine")
                    #result frame
                    result_frame = Frame(middle2_frame, bg="medium aquamarine", width=900, height=222)
                    reframe1 = Frame(result_frame, bg="medium aquamarine", width=900, height=38)
                    relabel = Label(reframe1, bg="DodgerBlue3", width=30, height=1, text="Result Card",
                                    font=('Garuda', 12, 'bold'))
                    center_reframe = Frame(result_frame, bg="medium aquamarine", width=900, height=144)
                    cere_frame1 = Frame(center_reframe, bg="medium aquamarine", width=900, height=36)
                    cref1_left = Frame(cere_frame1, bg="medium aquamarine", height=36, width=480)
                    hsub_cref1l = Label(cref1_left, bg="DodgerBlue3", width=20, height=1, text="Subject",
                                    font=('Garuda', 10, 'bold'))
                    hmark_cref1l = Label(cref1_left, bg="DodgerBlue3", width=15, height=1, text="Marks",
                                       font=('Garuda', 10, 'bold'))
                    hgrade_cref1l = Label(cref1_left, bg="DodgerBlue3", width=15, height=1, text="Grade",
                                        font=('Garuda', 10, 'bold'))
                    cref1_right = Frame(cere_frame1, bg="medium aquamarine", height=36, width=480)
                    hsub_cref1r = Label(cref1_right, bg="DodgerBlue3", width=20, height=1, text="Subject",
                                       font=('Garuda', 10, 'bold'))
                    hmark_cref1r = Label(cref1_right, bg="DodgerBlue3", width=15, height=1, text="Marks",
                                        font=('Garuda', 10, 'bold'))
                    hgrade_cref1r = Label(cref1_right, bg="DodgerBlue3", width=16, height=1, text="Grade",
                                         font=('Garuda', 10, 'bold'))
                    cere_frame2 = Frame(center_reframe, bg="medium aquamarine", width=900, height=36)
                    cref2_left = Frame(cere_frame2, bg="medium aquamarine", height=36, width=480)
                    calsub_cref2l = Label(cref2_left, bg="mint cream", width=20, height=1, text="Calculus",
                                        font=('Garuda', 10))
                    calmark_cref2l = Label(cref2_left, bg="mint cream", width=15, height=1, text=result.calculus(name),
                                         font=('Garuda', 10))
                    calgrade_cref2l = Label(cref2_left, bg="mint cream", width=15, height=1, text=grade.calgrade(name),
                                          font=('Garuda', 10))
                    cref2_right = Frame(cere_frame2, bg="medium aquamarine", height=36, width=480)
                    engsub_cref2r = Label(cref2_right, bg="mint cream", width=20, height=1, text="English",
                                          font=('Garuda', 10))
                    engmark_cref2r = Label(cref2_right, bg="mint cream", width=15, height=1, text=result.eng(name),
                                           font=('Garuda', 10))
                    enggrade_cref2r = Label(cref2_right, bg="mint cream", width=16, height=1, text=grade.enggrade(name),
                                            font=('Garuda', 10))
                    cere_frame3 = Frame(center_reframe, bg="medium aquamarine", width=900, height=36)
                    cref3_left = Frame(cere_frame3, bg="medium aquamarine", height=36, width=480)
                    itcsub_cref3l = Label(cref3_left, bg="mint cream", width=20, height=1, text="Introduction To Computing",
                                          font=('Garuda', 10))
                    itcmark_cref3l = Label(cref3_left, bg="mint cream", width=15, height=1, text=result.itc(name),
                                           font=('Garuda', 10))
                    itcgrade_cref3l = Label(cref3_left, bg="mint cream", width=15, height=1, text=grade.itcgrade(name),
                                            font=('Garuda', 10))
                    cref3_right = Frame(cere_frame3, bg="medium aquamarine", height=36, width=480)
                    pfsub_cref3r = Label(cref3_right, bg="mint cream", width=20, height=1, text="Programming Fundamental",
                                          font=('Garuda', 10))
                    pfmark_cref3r = Label(cref3_right, bg="mint cream", width=15, height=1, text=result.pf(name),
                                           font=('Garuda', 10))
                    pfgrade_cref3r = Label(cref3_right, bg="mint cream", width=16, height=1, text=grade.pfgrade(name),
                                            font=('Garuda', 10))
                    cere_frame4 = Frame(center_reframe, bg="medium aquamarine", width=900, height=36)
                    cref4_left = Frame(cere_frame4, bg="medium aquamarine", height=36, width=480)
                    apsub_cref4l = Label(cref4_left, bg="mint cream", width=20, height=1,
                                          text="Applied Physics", font=('Garuda', 10))
                    apmark_cref4l = Label(cref4_left, bg="mint cream", width=15, height=1, text=result.ap(name),
                                           font=('Garuda', 10))
                    apgrade_cref4l = Label(cref4_left, bg="mint cream", width=15, height=1, text=grade.apgrade(name),
                                            font=('Garuda', 10))
                    cref4_right = Frame(cere_frame4, bg="medium aquamarine", height=36, width=480)
                    tsub_cref4r = Label(cref4_right, bg="mint cream", width=20, height=1,
                                         text="Total", font=('Garuda', 10, 'bold'))
                    tmark_cref4r = Label(cref4_right, bg="mint cream", width=15, height=1, text=grade.total_marks1sem(name),
                                          font=('Garuda', 10, 'bold'))
                    tgrade_cref4r = Label(cref4_right, bg="mint cream", width=16, height=1, text=grade.gpa1sem(name),
                                           font=('Garuda', 10, 'bold'))
                    re_lastframe = Frame(result_frame, bg="medium aquamarine", height=40, width=900)
                    getresult_button = Button(re_lastframe, text="Get Result", bg="black", font=('Garuda', 12, 'bold'),
                                         width=12, height=1, fg="mint cream", activebackground="mint cream",
                                         activeforeground="black", command = lambda : excelreport.sem1_resultreport(name))

                    middle2_frame.pack(side=TOP, fill=BOTH, expand=1)
                    subheading_frame.pack(side=TOP, fill=BOTH, pady=10, padx=20)
                    subheading_label.pack(pady=10)
                    Personalinfo_frame.pack(side=TOP, fill=BOTH, pady=5, padx=20)
                    piframe1.pack(side=TOP, fill=BOTH)
                    pilabel.pack(pady=5)
                    piframe2.pack(side=TOP, fill=BOTH)
                    pif2_left.pack(side=LEFT, fill=BOTH)
                    name_label.pack(side=LEFT)
                    getname_label.pack(side=LEFT)
                    pif2_right.pack(side=LEFT, fill=BOTH)
                    fat_name_label.pack(side=LEFT)
                    getfatname_label.pack(side=LEFT)
                    piframe3.pack(side=TOP, fill=BOTH)
                    pif3_left.pack(side=LEFT, fill=BOTH)
                    rollno_label.pack(side=LEFT)
                    getrollno_label.pack(side=LEFT)
                    pif3_right.pack(side=LEFT, fill=BOTH)
                    batch_label.pack(side=LEFT)
                    getbatch_label.pack(side=LEFT)
                    piframe4.pack(side=TOP, fill=BOTH, pady=2)
                    pif4_left.pack(side=LEFT, fill=BOTH)
                    program_label.pack(side=LEFT)
                    getprogram_label.pack(side=LEFT)
                    pif4_right.pack(side=LEFT, fill=BOTH)
                    dep_label.pack(side=LEFT)
                    getdep_label.pack(side=LEFT)
                    result_frame.pack(side=TOP, fill=BOTH, pady=5, padx=20)
                    reframe1.pack(side=TOP, fill=BOTH)
                    relabel.pack(pady=5)
                    center_reframe.pack(side=TOP,fill=BOTH)
                    cere_frame1.pack(side=TOP, fill=BOTH)
                    cref1_left.pack(side=LEFT, fill=BOTH)
                    hsub_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hmark_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hgrade_cref1l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    cref1_right.pack(side=LEFT, fill=BOTH)
                    hsub_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hmark_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    hgrade_cref1r.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
                    cere_frame2.pack(side=TOP, fill=BOTH)
                    cref2_left.pack(side=LEFT, fill=BOTH)
                    calsub_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    calmark_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    calgrade_cref2l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref2_right.pack(side=LEFT, fill=BOTH)
                    engsub_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    engmark_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    enggrade_cref2r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame3.pack(side=TOP, fill=BOTH)
                    cref3_left.pack(side=LEFT, fill=BOTH)
                    itcsub_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    itcmark_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    itcgrade_cref3l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref3_right.pack(side=LEFT, fill=BOTH)
                    pfsub_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    pfmark_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    pfgrade_cref3r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cere_frame4.pack(side=TOP, fill=BOTH)
                    cref4_left.pack(side=LEFT, fill=BOTH)
                    apsub_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    apmark_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    apgrade_cref4l.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    cref4_right.pack(side=LEFT, fill=BOTH)
                    tsub_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tmark_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    tgrade_cref4r.pack(side=LEFT, fill=BOTH, padx=10, pady=5)
                    re_lastframe.pack(side=BOTTOM, fill=BOTH)
                    getresult_button.pack(pady=10)


                    # center 3 frame back
                    middle3_frame = Frame(root, bg="mint cream", height=40)
                    back_button = Button(middle3_frame, text="Back", bg="DodgerBlue3", font=('Garuda', 12, 'bold'),
                                         width=12,
                                         height=1, fg="mint cream", activebackground="mint cream",
                                         activeforeground="DodgerBlue3", command=lambda: stdlogingui(root))
                    middle3_frame.pack(side=TOP, fill=BOTH)
                    back_button.pack(pady=10)

                    # END FRAME for copy right
                    bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
                    copytight_label = Label(bottom_frame, text="© CODER TECH 2021, All Rights Reserved",
                                            bg="DodgerBlue3",
                                            font=('Garuda', 12, 'bold'))
                    bottom_frame.pack(side=BOTTOM, fill=BOTH)
                    copytight_label.pack(pady=5)
                    call_std.wishme()

            root = Tk()
            obj = std1se(root)
            mainloop()
        con.commit()
        con.close()

    except Exception as error:
        print(error)

from requirements import *
def vars():
    #---------Getting the username
    global enteredusername
    enteredusername = username.get().lower()
    return enteredusername
def login():
    #------------------------Checking if the password entered is correct or not
    with open("Database/acc.csv", "r") as pw:
    #--------------------------password
        list_reader = csv.reader(pw)
        for i in list_reader:
            if vars() == i[0]:
                if password.get() == i[1].strip():
                    staff(vars())
                    break
                else:
                    messagebox.showwarning("Wrong Password", "Enter the correct password")
            elif vars().lower() == "admin":
                if password.get() == "admin":
                    teacher()
                    break
                else:
                    messagebox.showwarning("Wrong Password", "Enter the correct password")
#-----------------------Changing the password
def changepassfunc(account):
    change_pass = Tk()
    change_pass.geometry("400x300")
    change_pass.config(bg=BG)
    change_pass.title("Change Password")
    adder_Font_tuple = ("Comic Sans MS", 20, "bold")
    desc = Label(change_pass, text="Enter", font=('Arial', 30, 'bold'), bg=BG, fg=text_color)
    desc.pack(pady=30)
    cpass_frame = Frame(change_pass, bg=BG)
    newpassword = CTkEntry(cpass_frame, show='*', width=225, placeholder_text="New Password")
    newpassword.configure(font = adder_Font_tuple)
    newpassword.grid(row=1, column=1, padx=5)
    repassword = CTkEntry(cpass_frame, show='*', width=225, placeholder_text="Renter New Password")
    repassword.configure(font = adder_Font_tuple)
    repassword.grid(row=2, column=1, padx=5)
    def check():
        if newpassword.get() == repassword.get():
            Password = newpassword.get()
            with open("Database/acc.csv", "r", newline="\n") as pw:
                list_reader = list(csv.reader(pw))
                for i in list_reader:
                    if account == i[0]:
                        i[1] = Password
                        break
                    else:
                        continue   
            with open("Database/acc.csv", "w", newline="\n") as pw:
                list_writer = csv.writer(pw)
                list_writer.writerows(list_reader)
                change_pass.destroy()
                change_pass.update()
                messagebox.showinfo("Password changed", "Password changed successfully!")
                logout()
    cpass_frame.pack()
    sub_button = CTkButton(change_pass, command=check, text="Submit", bg_color="#4b16b5", width=15)
    sub_button.configure(font=('Arial', 16), text_color = "white")
    sub_button.pack()
    
    change_pass.mainloop()
    Main(BG, text_color, adder_Font_tuple, login)
#-----------------------Main page
def Main(BG, text_color, adder_Font_tuple, login):
    global Log_in , password, username
    Log_in = Tk()
    Log_in.geometry("1100x400")
    Log_in.resizable(width=False, height=False)
    Log_in.config(bg="#4D90DF")
    Log_in.title("Student Progress Management System")
    Log_in.grid_columnconfigure(0, weight = 1)
    Log_in.grid_columnconfigure(1, weight = 1)
    Log_in.grid_rowconfigure(0, weight = 1)
    #---------------------------Login information frame
    frame1 = CTkFrame(Log_in, bg_color = "black", border_width=4, fg_color="#4D90DF")
    frame1.grid(row = 0, column = 0, sticky = "nesw")
    #---------------------------Login widgets for submission
    frame2 = CTkFrame(Log_in, bg_color = "black", border_width=4, fg_color="#4D90DF")
    frame2.grid(row = 0, column = 1, sticky = "nesw")
    #---------------------------Widgets
    img = ImageTk.PhotoImage(Image.open("pic/download.png").resize((701,400)))
    lbl = CTkLabel(frame2, image=img)
    lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    desc = Label(frame2, text="Login", font=adder_Font_tuple, bg="white", fg="black")
    desc.pack(pady=50)

    Login_frame = Frame(frame2, bg=BG)
    # ---------------------------Username

    username_ask = Label(Login_frame, text="Username", font=adder_Font_tuple, fg="black",bg = "white")
    username_ask.grid(row=0, column=0, sticky="nesw")
    username = CTkEntry(Login_frame, width=225, corner_radius = 20,bg_color= "white")

    username.configure(font = adder_Font_tuple)
    username.grid(row=0, column=1,sticky="nesw")
    # ---------------------------Password
    password_ask = Label(Login_frame, text="Password", font=adder_Font_tuple, fg="black",bg = "white")
    password_ask.grid(row=1, column=0,sticky="nesw")
    password = CTkEntry(Login_frame, show='*', width=225, corner_radius = 20,bg_color= "white")
    password.configure(font = adder_Font_tuple)
    password.grid(row=1, column=1,sticky="nesw")

    Login_frame.pack()
    def on_enter_key(event):
        Log_button.invoke()  # Simulates a button press
    #---------------------------Buttons
    Log_button = CTkButton(frame2, command=login, text="Submit", width=20, height = 20, hover_color = "dark blue",bg_color = "white", font=('Arial', 20), text_color="white")    
    Log_button.pack()
    Font_tuple = ("Comic Sans MS", 40, "bold")
    infoFont_tuple = ("Comic Sans MS", 15, "bold")
    Log_in.bind('<Return>', on_enter_key)

    a = """
        Student progress management system 
        is a very useful tool for teachers. 
        It allows them to track the progress 
        of their students and identify areas
        where they need improvement. This 
        system can also be used to monitor 
        the performance of individual students
        over time.
        """
    conname = CTkLabel(frame1, text=a,text_color="black", font=CTkFont(family="Helvetica"), bg_color="#4D90DF",)
    conname.pack()
    conname.place(relx=0.46, rely=0.62, anchor=CENTER)
    conname.configure(font = infoFont_tuple)
    desc = Label(frame1, text="""Student Progress
    Management
    ______________________""", font=('Arial', 23, 'bold'), bg=BG, fg=text_color)

    desc.pack(pady=50)
    desc.place(relx=0.5, rely=0.20, anchor=CENTER)
    ########################################################################
    # ---------------------------Finish
    Log_in.mainloop()
# ---------------------------------------------------------- Staff main panel
def staff(name):
    global staffpage, btnState
    # ______________________ Main_window
    try:
        Log_in.destroy()
        Log_in.update()
    except TclError:
        pass
    
    staffpage = CTk()
    staffpage.geometry("950x350")
    staffpage.resizable(width=False, height=False)
    staffpage.config(bg=BG)
    staffpage.title("Staff panel")
    # loading Navbar icon image:
    navIcon = PhotoImage(file="pic/menu.png")
    closeIcon = PhotoImage(file="pic/close.png")
    btnState = False
    # setting switch function:
    def switch():
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                navRoot.place(x=-x, y=0)
                topFrame.update()

            # turning button OFF:
            btnState = False
        else:
            # created animated Navbar opening:
            for x in range(-300, 0):
                navRoot.place(x=x, y=0)
                topFrame.update()

            # turing button ON:
            btnState = True

    # top Navigation bar:
    topFrame = Frame(staffpage, bg=color["orange"])
    topFrame.pack(side="top", fill=X)

    # Header label text:
    homeLabel = Label(topFrame, text="Staff Panel", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
    homeLabel.pack(side="top")

    # Main label text:
    framemain = Frame(staffpage, bg= "gray17", width=1450, height = 600)
    framemain.pack(anchor = CENTER)
    #-----------------------------------------------------
    with open("Database/acc.csv", "r") as file:
            file_reader = csv.reader(file)
            for i in file_reader:
                if name == i[0]:
                    course = i[2]
                    break
    stafflabel = CTkLabel(framemain, text="Name: Mr." + name.capitalize(), font=("", 30), fg_color="white")
    stafflabel.place(relx=0.50, rely=0.22, anchor=CENTER)

    stafflabel = CTkLabel(framemain, text="Course: " + course.upper(), font=("", 30), fg_color="white")
    stafflabel.place(relx=0.50, rely=0.35, anchor=CENTER)    

    def optionmenu_callback():
        mainwin(course, name)
    student_record = CTkButton(framemain, command=optionmenu_callback, text="Open Record",text_color="black", width=74, height=75,font=("",23), border_width=5)
    student_record.place(relx=0.5, rely=0.54, anchor=CENTER)
    def leave():
        staffpage.destroy()
        staffpage.update()

    change_pass = CTkButton(framemain, command=lambda: changepassfunc(name), text="Change Password",text_color="light blue", width=75,font=("",15, "underline"), border_width=5, border_color="gray17", fg_color="gray17", hover_color="gray17")
    change_pass.grid(row=5,column=2)
    change_pass.place(relx=0.10, rely=0.9, anchor=CENTER)
    leaver = CTkButton(framemain, command=leave, text="Log out",text_color="black",font=("",16), border_width=5)
    leaver.grid(row=5,column=2)
    leaver.place(relx=1, rely=1, anchor=SE)
    #------------------------------------------------------
    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
    navbarBtn.place(x=10, y=10)

    # setting Navbar frame:
    navRoot = Frame(staffpage, bg="gray17", height=1000, width=300)
    navRoot.place(x=-300, y=0)
    Label(navRoot, font="Bahnschrift 15", bg="dark blue", fg="black", height=2, width=300, padx=20).place(x=0, y=0)
    def processor():
        print("clicked")

    # option in the navbar:
    options = ["Help", "Feedback", "Log Out", "Credits"]
    # Navbar Option Buttons:
    but1 = Button(navRoot, text=options[0], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=lambda: helper(name)).place(x=25, y=80)
    but2 = Button(navRoot, text=options[1], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=lambda: feedback(name)).place(x=25, y=120)
    but3 = Button(navRoot, text=options[2], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=logout).place(x=25, y=160)
    but4 = Button(navRoot, text=options[3], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=lambda: credits(name)).place(x=25, y=450)

    # Navbar Close Button:
    closeBtn = Button(navRoot, image=closeIcon, bg="dark blue", activebackground=color["orange"], bd=0, command=switch)
    closeBtn.place(x=250, y=10)

    staffpage.mainloop()
# ---------------------------------------------------------- Teacher main panel
def teacher():
    global teacherpage, btnState
    # ______________________ Main_window
    try:
        Log_in.destroy()
        Log_in.update()
    except TclError:
        pass
    
    teacherpage = CTk()
    teacherpage.geometry("950x350")
    teacherpage.resizable(width=False, height=False)
    teacherpage.config(bg=BG)
    teacherpage.title("Admin panel")
    # loading Navbar icon image:
    navIcon = PhotoImage(file="pic/menu.png")
    closeIcon = PhotoImage(file="pic/close.png")
    btnState = False
    # setting switch function:
    def switch():
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                navRoot.place(x=-x, y=0)
                topFrame.update()

            # turning button OFF:
            btnState = False
        else:
            # created animated Navbar opening:
            for x in range(-300, 0):
                navRoot.place(x=x, y=0)
                topFrame.update()

            # turing button ON:
            btnState = True

    # top Navigation bar:
    topFrame = Frame(teacherpage, bg=color["orange"])
    topFrame.pack(side="top", fill=X)

    # Header label text:
    homeLabel = Label(topFrame, text="Admin Panel", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
    homeLabel.pack(side="top")

    # Main label text:
    framemain = Frame(teacherpage, bg= "gray17", width=1450, height = 600)
    framemain.pack(anchor = CENTER)
    #-----------------------------------------------------
    title = CTkLabel(framemain, text="Select Stream",text_color="white", width=74, height=75,font=titlefont)
    title.place(relx=0.5, rely=0.10, anchor=CENTER)
    options = StringVar(framemain)
    options.set(names[0])
    menu = CTkOptionMenu(framemain, values=names, variable = options ,button_color="white", button_hover_color="grey",font=menuFont_tuple, bg_color="#0566b5")
    menu.grid()
    menu.place(relx=0.43, rely=0.20)
    menu.set(names[len(names)-1])
    str_out= StringVar(framemain)
    str_out.set("Output")
    def my_show(*args):
        str_out.set(menu.get())
    options.trace_add('write',my_show)
    def optionmenu_callback():
        if menu.get() == "pcmc":
            mainwin("pcmc")
        if menu.get() == "pcmb":
            mainwin("pcmb")
    student_record = CTkButton(framemain, command=optionmenu_callback, text="Open Record",text_color="black", width=74, height=75,font=("",23), border_width=5)
    student_record.grid(row=5,column=2)
    student_record.place(relx=0.5, rely=0.54, anchor=CENTER)
    def leave():
        teacherpage.destroy()
        teacherpage.update()

    change_pass = CTkButton(framemain, command=stusers, text="Staff Users",text_color="light blue", width=75,font=("",15, "underline"), border_width=5, border_color="gray17", fg_color="gray17", hover_color="gray17")
    change_pass.grid(row=5,column=2)
    change_pass.place(relx=0.10, rely=0.9, anchor=CENTER)
    leaver = CTkButton(framemain, command=leave, text="Log out",text_color="black",font=("",16), border_width=5)
    leaver.grid(row=5,column=2)
    leaver.place(relx=1, rely=1, anchor=SE)
    #------------------------------------------------------
    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
    navbarBtn.place(x=10, y=10)

    # setting Navbar frame:
    navRoot = Frame(teacherpage, bg="gray17", height=1000, width=300)
    navRoot.place(x=-300, y=0)
    Label(navRoot, font="Bahnschrift 15", bg="dark blue", fg="black", height=2, width=300, padx=20).place(x=0, y=0)
    def processor():
        print("clicked")

    # option in the navbar:
    options = ["Help", "Feedback", "Log Out", "Credits"]
    # Navbar Option Buttons:
    but1 = Button(navRoot, text=options[0], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=helper).place(x=25, y=80)
    but2 = Button(navRoot, text=options[1], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=lambda: feedback("Admin")).place(x=25, y=120)
    but3 = Button(navRoot, text=options[2], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=logout).place(x=25, y=160)
    but4 = Button(navRoot, text=options[3], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0, command=credits).place(x=25, y=450)
    # but5 = Button(navRoot, text=options[4], font="BahnschriftLight 15", bg="gray17", fg="gray16", activebackground="gray18", activeforeground="green", bd=0, command=processor).place(x=25, y=500)

    # Navbar Close Button:
    closeBtn = Button(navRoot, image=closeIcon, bg="dark blue", activebackground=color["orange"], bd=0, command=switch)
    closeBtn.place(x=250, y=10)

    teacherpage.mainloop()
# ---------------------------------------------------------- List of Staff users
def stusers():
    users_window = CTkToplevel()
    users_window.title("Manage Users")
    
    # Read the CSV file
    df = pd.read_csv('Database/acc.csv')
    
    # Define font and row height
    custom_font = ("Helvetica", 16)  # Increase size as needed
    row_height = 30  # Increase row height to add spacing
    
    # Create a Treeview widget
    tree = ttk.Treeview(users_window, columns=("name", "password", "course"), show="headings", height=20)
    
    # Set font and row height for the Treeview
    style = ttk.Style()
    style.configure("Treeview", font=custom_font, rowheight=row_height)
    style.configure("Treeview.Heading", font=custom_font)
    
    tree.heading("name", text="Name")
    tree.heading("password", text="Password")
    tree.heading("course", text="Course")
    
    # Insert data into the Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", iid=f"row_{index}", values=(row['name'], row['password'], row['course']))
    
    tree.pack(pady=10, padx=10, fill='both', expand=True)

    # Scrollbars
    vsb = ttk.Scrollbar(users_window, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(users_window, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=hsb.set)

    # Add user functionality
    def add_user():
        add_user_window = CTkToplevel(users_window)
        add_user_window.title("Add User")
        add_user_window.geometry("300x400")  # Set a larger size for the add user window
        
        # Add padding to each widget to space them out
        CTkLabel(add_user_window, text="Username").pack(pady=10)
        entry_name = CTkEntry(add_user_window)
        entry_name.pack(pady=10, padx=20)
        
        CTkLabel(add_user_window, text="Password").pack(pady=10)
        entry_password = CTkEntry(add_user_window, show="*")
        entry_password.pack(pady=10, padx=20)
        
        CTkLabel(add_user_window, text="Confirm Password").pack(pady=10)
        entry_confirm_password = CTkEntry(add_user_window, show="*")
        entry_confirm_password.pack(pady=10, padx=20)

        # Dropdown for course selection
        CTkLabel(add_user_window, text="Select Course").pack(pady=10)
        course_var = StringVar(value="PCMC")  # Default value
        course_dropdown = CTkOptionMenu(add_user_window, variable=course_var, values=["PCMC", "PCMB"])
        course_dropdown.pack(pady=10, padx=20)
        
        error_label = CTkLabel(add_user_window, text="", fg_color="red")
        error_label.pack(pady=10)
        
        def save_user():
            name = entry_name.get()
            password = entry_password.get()
            confirm_password = entry_confirm_password.get()
            course = course_var.get()
            
            if password == confirm_password:
                # Append new user to the DataFrame
                new_row = pd.DataFrame({'name': [name], 'password': [password], 'course': [course]})
                df_updated = pd.concat([df, new_row], ignore_index=True)
                df_updated.to_csv('Database/acc.csv', index=False)
                add_user_window.destroy()
                stusers()  # Refresh the users window
            else:
                error_label.config(text="Passwords do not match!")
        
        add_button = CTkButton(add_user_window, text="Add User", command=save_user)
        add_button.pack(pady=20)

    add_user_button = CTkButton(users_window, text="Add User", command=add_user)
    add_user_button.pack(pady=10)
#-------------------------------Credits (sample only)
def credits(name="admin"):
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
    aboutmain = CTk()
    aboutmain.geometry("950x350")
    aboutmain.resizable(width=False, height=False)
    aboutmain.config(bg=BG)
    aboutmain.title("Credits")
    Font_tuple = ("Comic Sans MS", 40, "bold")
    infoFont_tuple = ("Comic Sans MS", 18, "bold")
    #######################################################################
    mainname = CTkLabel(aboutmain, text="-> Credits <-",text_color="black", width=50, height=90, bg_color="#00C9FF")
    mainname.pack()
    mainname.place(relx=0.5, rely=0.18, anchor=CENTER)
    mainname.configure(font = Font_tuple)
    ########################################################################
    def instagram():
        try:
            aboutmain.destroy()
            aboutmain.update()
        except TclError:
            pass
        insta = CTk()
        insta.geometry("950x350")
        insta.resizable(width=False, height=False)
        insta.config(bg=BG)
        insta.title("instagram")
        title = CTkLabel(insta, text="Instagram",text_color="black", width=74, height=75,font=apptitlefont)
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        def exit_btn():
            insta.destroy()
            insta.update()
            credits(name)            
        button2 = CTkButton(insta, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color=BG)
        button2.pack()
        button2.place(relx=1, rely=1, anchor=SE)
        insta.mainloop()
    def facebook():
        try:
            aboutmain.destroy()
            aboutmain.update()
        except TclError:
            pass
        Face = CTk()
        Face.geometry("950x350")
        Face.resizable(width=False, height=False)
        Face.config(bg=BG)
        Face.title("Facebook")
        
        title = CTkLabel(Face, text="Facebook",text_color="black", width=74, height=75,font=apptitlefont)
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        def exit_btn():
            Face.destroy()
            Face.update()
            credits(name)
            
        button2 = CTkButton(Face, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color=BG)
        button2.pack()
        button2.place(relx=1, rely=1, anchor=SE)
        Face.mainloop()
    def snapchat():
        try:
            aboutmain.destroy()
            aboutmain.update()
        except TclError:
            pass
        snap = CTk()
        snap.geometry("950x350")
        snap.resizable(width=False, height=False)
        snap.config(bg=BG)
        snap.title("Snapchat")
        title = CTkLabel(snap, text="Snapchat",text_color="black", width=74, height=75,font=apptitlefont)
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        def exit_btn():
            snap.destroy()
            snap.update()
            credits(name)
            
        button2 = CTkButton(snap, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color=BG)
        button2.pack()
        button2.place(relx=1, rely=1, anchor=SE)
        snap.mainloop()
    def discord():
        try:
            aboutmain.destroy()
            aboutmain.update()
        except TclError:
            pass
        Disc = CTk()
        Disc.geometry("950x350")
        Disc.resizable(width=False, height=False)
        Disc.config(bg=BG)
        Disc.title("Discord")
        
        title = CTkLabel(Disc, text="Discord",text_color="black", width=74, height=75,font=apptitlefont)
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        def exit_btn():
            Disc.destroy()
            Disc.update()
            credits(name)
            
        button2 = CTkButton(Disc, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color=BG)
        button2.pack()
        button2.place(relx=1, rely=1, anchor=SE)
        Disc.mainloop()

    ########################################################################
    instabut = CTkButton(aboutmain, command=instagram, text="Instagram", width=50, height=50, border_width=5, bg_color=BG)
    instabut.pack()
    instabut.place(relx=0.20, rely=0.5, anchor=CENTER)
    facebut = CTkButton(aboutmain, command=facebook, text="Facebook", width=50, height=50, border_width=5, bg_color=BG)
    facebut.pack()
    facebut.place(relx=0.40, rely=0.5, anchor=CENTER)
    snapbut = CTkButton(aboutmain, command=snapchat, text="Snapchat", width=50, height=50, border_width=5, bg_color=BG)
    snapbut.pack()
    snapbut.place(relx=0.60, rely=0.5, anchor=CENTER)
    discbut = CTkButton(aboutmain, command=discord, text="Discord", width=50, height=50, border_width=5, bg_color=BG)
    discbut.pack()
    discbut.place(relx=0.80, rely=0.5, anchor=CENTER)
    ########################################################################
    def exit_btn():
        aboutmain.destroy()
        aboutmain.update()
        if name == "admin":
            teacher()
        else:
            staff(name)
    button2 = CTkButton(aboutmain, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color="#00C9FF")
    button2.pack()
    button2.place(relx=1, rely=1, anchor=SE)
    aboutmain.mainloop()
#-------------------------------usage information
def helper(name="admin"):
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
    help = CTk()
    help.geometry("1000x500")
    help.title("Information page")
    help.configure(bg="#00C9FF")
    photo = PhotoImage(file = "pic/icon.png")
    help.iconphoto(False, photo)
    Font_tuple = ("Comic Sans MS", 40, "bold")
    infoFont_tuple = ("Comic Sans MS", 18, "bold")
    #######################################################################
    mainname = CTkLabel(help, text="-> Help <-",text_color="black", width=50, height=90, bg_color="#00C9FF")
    mainname.pack()
    mainname.place(relx=0.5, rely=0.18, anchor=CENTER)
    mainname.configure(font = Font_tuple)
    ########################################################################
    a = """1) To create a graph for a specific student double click the row of the student.

    2) To create an overall graph click the create graph button in the second tab.

    3)shortcut for creating a graph is "ctrl+g" which can be 
    accessed only in the overall sesction of both streams.

    4)There are only two streams in the science category.

    5)In each stream there are 4 different terms details.

--------------------THANK YOU FOR USING THIS APP--------------------
    """
    conname = CTkLabel(help, text=a,text_color="black", width=50, height=90, bg_color="#00C9FF")
    conname.pack()
    conname.place(relx=0.5, rely=0.60, anchor=CENTER)
    conname.configure(font = infoFont_tuple)
    ########################################################################
    def exit_btn():
        help.destroy()
        help.update()
        if name == "admin":
            teacher()
        else:
            staff(name)
    button2 = CTkButton(help, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color="#00C9FF")
    button2.pack()
    button2.place(relx=1, rely=1, anchor=SE)
    help.mainloop()
def logout():
    try:
        teacherpage.destroy()
        teacherpage.update()
        Main(BG, text_color, adder_Font_tuple, login)
    except:
        try:
            staffpage.destroy()
            staffpage.update()
            Main(BG, text_color, adder_Font_tuple, login)
        except:
            pass
def feedback(name="admin"):
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
    feed = CTk()
    feed.title("Feedback")
    feed.geometry("950x350")
    feed.resizable(width=False, height=False)
    feed.config(bg=BG)
    Font_tuple = ("Comic Sans MS", 25, "bold")
    #######################################################################
    mainname = CTkLabel(feed, text="-> FEEDBACK <-",text_color="black", width=50, height=50,font=("Helvetica", 15), bg_color=BG)
    mainname.pack()
    mainname.place(relx=0.5, rely=0.10, anchor=CENTER)
    mainname.configure(font = Font_tuple)

    textbox = Text(feed, width=50, height=7)
    textbox.pack()
    textbox.place(relx=0.5, rely=0.50, anchor=CENTER)
    textbox.configure(font=adder_Font_tuple)
    def submit():
        global text
        text = textbox.get("0.0", "end")
        if len(text)>=1:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            text = f"""
Time: {current_time} 
User: {name}
Feedback: {text} 
__________________________________________________________________________________"""
            with open("Database/feedback.txt", "a") as feedback:
                feedback.write(text)
    def clear():
        textbox.delete(1.0,END)
    def subcomp():
        submit()
        clear()
        messagebox.showinfo("Submitted", "Successfully submited")
        feed.destroy()
        feed.update()
        if name == "admin":
            teacher()
        else:
            staff(name)
    button2 = CTkButton(feed, command=subcomp, text="SUBMIT", width=50, height=50, border_width=2, bg_color=BG)
    button2.pack()
    button2.place(relx=0.5, rely=0.90, anchor=CENTER)
    def exit_btn():
        feed.destroy()
        feed.update()
        if name == "teacher":
            teacher()
        else:
            staff(name)
    button2 = CTkButton(feed, command=exit_btn, text="Return", width=50, height=50, border_width=2, bg_color="#00C9FF")
    button2.pack()
    button2.place(relx=1, rely=1, anchor=SE)
    feed.mainloop()
#------------------------------------for periodic test 1
def per1(course, name = "admin"):
    BG = "#333333"
    print(course, name)
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
        pass
    per1 = CTk()
    per1.geometry("1200x350")
    per1.resizable(width=False, height=False)
    per1.config(bg=BG)
    per1.title("Periodic Test 1")
    def exit_function():
        per1.destroy()
        per1.update()
        mainwin(course, name)
    per1.protocol('WM_DELETE_WINDOW', exit_function)
    per1.title("Periodic test 1")
    Record = f"Database/Progress/{course}/per1.csv"
    def display():
        global studlist
        with open(Record, 'r') as reader:
            data = csv.reader(reader)
            studlist = []
            for row in data:
                studlist.append(row)
    tabs = ttk.Notebook(per1)
    text_color = "#46c4eb"
    tabs.pack(side=RIGHT, fill=BOTH, expand=True)
    def leave():
        per1.destroy()
        per1.update()
        # teacher()

    #For adding a tab to the notebook
    data_frame = Frame(tabs, bg=BG, relief=SUNKEN, bd=5)
    data_frame.pack(fill=BOTH, expand=True)
    tabs.add(data_frame, text="Periodic Test 1 Record")

    # for adding title to the notebook
    description = Label(data_frame, text="Periodic Test 1 - Student Record", font=("Arial", 18, 'bold'), bg=BG, fg=text_color, relief=SUNKEN)
    description.pack(fill=X)

    mycanvas = Canvas(data_frame, scrollregion=(0,0,10000,1800))
    mycanvas.pack(side=LEFT, fill=BOTH, expand=True)


    display()
    game_frame = Frame(mycanvas)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)
    my_game = ttk.Treeview(game_frame, height=60)
    my_game.config(cursor="hand2")
    nametofont("TkHeadingFont").configure(size=20)
    nametofont("TkDefaultFont").configure(size=20)
    with open(Record, 'r') as reader:
        data = csv.reader(reader)
        studlist = []
        for row in data:
            studlist.append(row)
    col = []
    for i in studlist[0]:
        col.append(i)
    column = tuple(col)
    my_game['columns'] = column

    my_game.column("#0", width=0,  stretch=True)
    for i in column:
        my_game.column(i,anchor=W, width=160)


    my_game.heading("#0",text="",anchor=W)
    for i in column:
        my_game.heading(i,text=i,anchor=W)
    a = 0
    for i in studlist:
        if i[0] != studlist[0][0]:
            my_game.insert(parent='',index='end',iid=a,text='',values=tuple(i))
            a+=1

    def OnDoubleClick(event):
        lis = []
        item = my_game.selection()
        sets = []
        total_score = 0
        for i in item:
            name = my_game.item(i,"values")[1]
        with open(Record) as pcmb:
            read = csv.reader(pcmb)
            for i in read:
                sets.append(i)
            for i in sets:
                if name == i[1]:
                    if course == "pcmc":
                        start = 4
                        end = 10
                    elif course == "pcmb":
                        start = 3
                        end = 9
                    for item in range(start, end): 
                        lis.append(int(i[item]))
                        total_score += int(i[item])
        if course == "pcmb":
            labels = ["English", 'Maths', 'Physics', 'Chemistry','Biology', 'Media']
        else:
            labels = ["English", 'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Media']
        
        x = np.array(labels)
        y = np.array(lis)
        plt.figure(figsize=(10,5))
        plt.bar(x,y, align = "center")
        plt.ylabel("Total marks")
        plt.xticks(rotation = 50)
        plt.tight_layout()
        plt.show()

    my_game.bind("<Double-1>", OnDoubleClick)
    my_game.pack()
    game_frame.pack()
    per1.mainloop()
#------------------------------------for MidTerm
def Midterm(course, name = "admin"):
    BG = "#333333"
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
        pass
    mid = CTk()
    mid.geometry("1200x350")
    mid.resizable(width=False, height=False)
    mid.config(bg=BG)
    def exit_function():
        mid.destroy()
        mid.update()
        mainwin(course, name) 

    mid.protocol('WM_DELETE_WINDOW', exit_function)
    mid.title("Mid Term")
    Record = f"Database/Progress/{course}/mid.csv"
    def display():
        global studlist
        with open(Record, 'r') as reader:
            data = csv.reader(reader)
            studlist = []
            for row in data:
                studlist.append(row)
    tabs = ttk.Notebook(mid)
    text_color = "#46c4eb"
    tabs.pack(side=RIGHT, fill=BOTH, expand=True)

    #For adding a tab to the notebook
    data_frame = Frame(tabs, bg=BG, relief=SUNKEN, bd=5)
    data_frame.pack(fill=BOTH, expand=True)
    tabs.add(data_frame, text="Mid term Exam Record")

    # for adding title to the notebook
    description = Label(data_frame, text="Mid term Exam - Student Record", font=("Arial", 18, 'bold'), bg=BG, fg=text_color, relief=SUNKEN)
    description.pack(fill=X)

    mycanvas = Canvas(data_frame, scrollregion=(0,0,10000,1800))
    mycanvas.pack(side=LEFT, fill=BOTH, expand=True)
    display()
    game_frame = Frame(mycanvas)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)
    my_game = ttk.Treeview(game_frame, height=60)
    my_game.config(cursor="hand2")
    nametofont("TkHeadingFont").configure(size=20)
    nametofont("TkDefaultFont").configure(size=20)
    with open(Record, 'r') as reader:
        data = csv.reader(reader)
        studlist = []
        for row in data:
            studlist.append(row)
    col = []
    for i in studlist[0]:
        col.append(i)
    column = tuple(col)
    my_game['columns'] = column

    my_game.column("#0", width=0,  stretch=True)
    for i in column:
        my_game.column(i,anchor=W, width=160)

    my_game.heading("#0",text="",anchor=W)
    for i in column:
        my_game.heading(i,text=i,anchor=W)
    a = 0
    for i in studlist:
        if i[0] != studlist[0][0]:
            my_game.insert(parent='',index='end',iid=a,text='',values=tuple(i))
            a+=1

    if course == "pcmc":
        start = 4
        end = 10
    elif course == "pcmb":
        start = 3
        end = 9

    def OnDoubleClick(event):
        lis = []
        item = my_game.selection()
        sets = []
        for i in item:
            name = my_game.item(i,"values")[1]
            
        with open(Record) as file:
            read = csv.reader(file)
            for i in read:
                sets.append(i)
            for i in sets:
                if name == i[1]:
                    for item in range(start,end): 
                        lis.append(int(i[item]))
        if course == "pcmb":
            labels = ["English", 'Maths', 'Physics', 'Chemistry','Biology', 'Media']
        else:
            labels = ["English", 'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Media']
        x = np.array(labels)
        y = np.array(lis)
        plt.figure(figsize=(10,5))
        plt.bar(x,y, align = "center")
        plt.ylabel("Total marks")
        plt.xticks(rotation = 50)
        plt.tight_layout()
        plt.show()

    my_game.bind("<Double-1>", OnDoubleClick)
    my_game.pack()
    game_frame.pack()
    mid.mainloop()
#------------------------------------for periodic test 2
def per2(course, name = "admin"):
    BG = "#333333"
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
        pass
    per2 = CTk()
    per2.geometry("1200x350")
    per2.resizable(width=False, height=False)
    per2.config(bg=BG)
    per2.title("Periodic test 2")
    def exit_function():
        per2.destroy()
        per2.update()
        mainwin(course, name)

    per2.protocol('WM_DELETE_WINDOW', exit_function)
    Record = f"Database/Progress/{course}/per2.csv"
    def display():
        global studlist
        with open(Record, 'r') as reader:
            data = csv.reader(reader)
            studlist = []
            for row in data:
                studlist.append(row)
    tabs = ttk.Notebook(per2)
    text_color = "#46c4eb"
    tabs.pack(side=RIGHT, fill=BOTH, expand=True)
    def leave():
        per2.destroy()
        per2.update()
        # teacher()

    #For adding a tab to the notebook
    data_frame = Frame(tabs, bg=BG, relief=SUNKEN, bd=5)
    data_frame.pack(fill=BOTH, expand=True)
    tabs.add(data_frame, text="Periodic Test 2 Record")

    # for adding title to the notebook
    description = Label(data_frame, text="Periodic Test 2 - Student Record", font=("Arial", 18, 'bold'), bg=BG, fg=text_color, relief=SUNKEN)
    description.pack(fill=X)

    mycanvas = Canvas(data_frame, scrollregion=(0,0,10000,1800))
    mycanvas.pack(side=LEFT, fill=BOTH, expand=True)


    display()
    game_frame = Frame(mycanvas)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)
    my_game = ttk.Treeview(game_frame, height=60)
    my_game.config(cursor="hand2")
    nametofont("TkHeadingFont").configure(size=20)
    nametofont("TkDefaultFont").configure(size=20)
    with open(Record, 'r') as reader:
        data = csv.reader(reader)
        studlist = []
        for row in data:
            studlist.append(row)
    col = []
    for i in studlist[0]:
        col.append(i)
    column = tuple(col)
    my_game['columns'] = column

    my_game.column("#0", width=0,  stretch=True)
    for i in column:
        my_game.column(i,anchor=W, width=160)


    my_game.heading("#0",text="",anchor=W)
    for i in column:
        my_game.heading(i,text=i,anchor=W)
    a = 0
    for i in studlist:
        if i[0] != studlist[0][0]:
            my_game.insert(parent='',index='end',iid=a,text='',values=tuple(i))
            a+=1

    if course == "pcmc":
        start = 4
        end = 10
    elif course == "pcmb":
        start = 3
        end = 9

    def OnDoubleClick(event):
        lis = []
        item = my_game.selection()
        print(item)
        sets = []
        for i in item:
            name = my_game.item(i,"values")[1]
            
        with open(Record) as pcmb:
            read = csv.reader(pcmb)
            for i in read:
                sets.append(i)
            for i in sets:
                if name == i[1]:                   
                    for item in range(start, end): 
                        lis.append(int(i[item]))
        if course == "pcmb":
            labels = ["English", 'Maths', 'Physics', 'Chemistry','Biology', 'Media']
        else:
            labels = ["English", 'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Media']
        x = np.array(labels)
        y = np.array(lis)
        plt.figure(figsize=(10,5))
        plt.bar(x,y, align = "center")
        plt.ylabel("Total marks")
        plt.xticks(rotation = 50)
        plt.tight_layout()
        plt.show()

    my_game.bind("<Double-1>", OnDoubleClick)
    my_game.pack()
    game_frame.pack()
    per2.mainloop()
#------------------------------------for Final
def Final(course, name="admin"):
    BG = "#333333"
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
        pass
    fin = CTk()
    fin.geometry("1200x350")
    fin.resizable(width=False, height=False)
    fin.config(bg=BG)
    fin.title("Final Exam")
    Record = f"Database/Progress/{course}/final.csv"
    def exit_function():
        fin.destroy()
        fin.update()
        mainwin(course, name) 

    fin.protocol('WM_DELETE_WINDOW', exit_function)
    def display():
        global studlist
        with open(Record, 'r') as reader:
            data = csv.reader(reader)
            studlist = []
            for row in data:
                studlist.append(row)
    tabs = ttk.Notebook(fin)
    text_color = "#46c4eb"
    tabs.pack(side=RIGHT, fill=BOTH, expand=True)
    def leave():
        fin.destroy()
        fin.update()
        # teacher()

    #For adding a tab to the notebook
    data_frame = Frame(tabs, bg=BG, relief=SUNKEN, bd=5)
    data_frame.pack(fill=BOTH, expand=True)
    tabs.add(data_frame, text="Final Exam Record")

    # for adding title to the notebook
    description = Label(data_frame, text="Final Exam - Student Record", font=("Arial", 18, 'bold'), bg=BG, fg=text_color, relief=SUNKEN)
    description.pack(fill=X)

    mycanvas = Canvas(data_frame, scrollregion=(0,0,10000,1800))
    mycanvas.pack(side=LEFT, fill=BOTH, expand=True)


    display()
    game_frame = Frame(mycanvas)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)
    my_game = ttk.Treeview(game_frame, height=60)
    my_game.config(cursor="hand2")
    nametofont("TkHeadingFont").configure(size=20)
    nametofont("TkDefaultFont").configure(size=20)
    with open(Record, 'r') as reader:
        data = csv.reader(reader)
        studlist = []
        for row in data:
            studlist.append(row)
    col = []
    for i in studlist[0]:
        col.append(i)
    column = tuple(col)
    my_game['columns'] = column

    my_game.column("#0", width=0,  stretch=True)
    for i in column:
        my_game.column(i,anchor=W, width=160)


    my_game.heading("#0",text="",anchor=W)
    for i in column:
        my_game.heading(i,text=i,anchor=W)
    a = 0
    for i in studlist:
        if i[0] != studlist[0][0]:
            my_game.insert(parent='',index='end',iid=a,text='',values=tuple(i))
            a+=1
    if course == "pcmc":
        start = 4
        end = 10
    elif course == "pcmb":
        start = 3
        end = 9
    def OnDoubleClick(event):
        lis = []
        item = my_game.selection()
        print(item)
        sets = []
        for i in item:
            name = my_game.item(i,"values")[1]
            
        with open(Record) as pcmb:
            read = csv.reader(pcmb)
            for i in read:
                sets.append(i)
            for i in sets:
                if name == i[1]:
                    
                    for item in range(start, end): 
                        lis.append(int(i[item]))
        if course == "pcmb":
            labels = ["English", 'Maths', 'Physics', 'Chemistry','Biology', 'Media']
        else:
            labels = ["English", 'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Media']
        x = np.array(labels)
        y = np.array(lis)
        plt.figure(figsize=(10,5))
        plt.bar(x,y, align = "center")
        plt.ylabel("Total marks")
        plt.xticks(rotation = 50)
        plt.tight_layout()
        plt.show()

    my_game.bind("<Double-1>", OnDoubleClick)
    my_game.pack()
    game_frame.pack()
    fin.mainloop()
#------------------------------------for overall
def Overall(course, name = "admin"):
    global data_frame
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
        pass
    BG = "#333333"
    over = CTk()
    over.geometry("1200x350")
    over.resizable(width=False, height=False)
    over.config(bg=BG)
    over.title("Overall marks")
    def exit_function():
        over.destroy()
        over.update()
        mainwin(course, name) 

    over.protocol('WM_DELETE_WINDOW', exit_function)
    Record = f"Database/Progress/{course}/{course}.csv"
    Recordplotter = f"Database/Progress/{course}/plotter{course}.csv"
    #-----------------------------------------------------------plotter for pcmc students
    def plotter(event=""):
        plt.style.use('_mpl-gallery')
        a = []
        with open(Record,"r") as file:
            b = csv.reader(file)
            for i in b:
                a.append(i)
        num = 0
        with open(Recordplotter, "w", newline="\n") as filewrite:
            write = csv.writer(filewrite)
            for i in a:
                
                if a[0] != i:
                    num += 1
                    write.writerow((num, i[1], i[len(i)-1]))
        pos = []
        val = []
        nl = []
        myxticks = []
        with open(Recordplotter,"r") as file:
            read = csv.reader(file)
            for i in read:
                nl.append(i)
        for i in nl:
            pos.append(i[0])
            myxticks.append(i[1])
            val.append(i[2])
        npos = []
        nval = []
        for i in pos:
            npos.append(eval(i))
        for i in val:
            nval.append(eval(i))


        x = np.array(npos)
        y = np.array(nval)
        plt.figure(figsize=(20,5))
        plt.xticks(x, myxticks)
        plt.bar(x,y, align = CENTER)
        plt.xlabel("Names")
        plt.ylabel("Total marks")
        plt.xticks(rotation = 50)
        plt.tight_layout()
        plt.show()
    over.bind("<Control_L><g>", plotter)
    over.bind("<Control_R><g>", plotter)
    def leave():
        over.destroy()
        over.update()
        mainwin(course, name)
        
    data_frame = Frame(over, bg=BG, relief=SUNKEN, bd=5)
    data_frame.pack(fill=BOTH, expand=True)
    # for adding title to the notebook
    graphlabel = Label(data_frame, text= "  Graph for all students  ", bg="blue", anchor=CENTER)
    graphlabel.grid(row=0,column=0)
    graphlabel.configure(font=("Comic Sans MS", 38, "bold"))
    graphlabel.place(relx=0.33, rely=0.10)
    graphbutton = Button(data_frame, text= "  Create  ", cursor="hand2", command = plotter, width=10)
    graphbutton.grid(row=0,column=0)
    graphbutton.configure(font=("Comic Sans MS", 20, "bold"))
    graphbutton.place(relx=.45, rely=.40)
    graphbutton = Button(data_frame, text= "  Exit  ", cursor="hand2", command = leave)
    graphbutton.grid(row=0,column=0)
    graphbutton.configure(font=("Comic Sans MS", 20, "bold"))
    graphbutton.place(relx=.46, rely=.60)
    over.mainloop()

#------------------------------------main window for course
def mainwin(coursetype, name = "admin"):
    try:
        teacherpage.destroy()
        teacherpage.update()
    except:
        try:
            staffpage.destroy()
            staffpage.update()
        except:
            pass
    global teachmain
    teachmain = CTk()
    teachmain.geometry("950x350")
    teachmain.resizable(width=False, height=False)
    teachmain.config(bg=BG)
    teachmain.title("Title Selection")

    # top Navigation bar:
    topFrame = Frame(teachmain, bg=color["orange"])
    topFrame.pack(side="top", fill=X)

    # Header label text:
    homeLabel = Label(topFrame, text=f"{coursetype.capitalize()} - Term selection", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
    homeLabel.pack(side="top")

    # Main label text:
    framemain = Frame(teachmain, bg= "gray17", width=1450, height = 600)
    framemain.pack(anchor = CENTER)
    #-----------------------------------------------------
    title = CTkLabel(framemain, text="Select Term",text_color="white", width=74, height=75,font=titlefont)
    title.place(relx=0.5, rely=0.10, anchor=CENTER)
    options = StringVar(framemain)
    options.set(terms[0])
    menu = CTkOptionMenu(framemain, values=terms, variable = options ,button_color="white", button_hover_color="grey",font=menuFont_tuple, bg_color="#0566b5", width=180)
    menu.grid()
    menu.place(relx=0.40, rely=0.20)
    menu.set(terms[len(terms)-1])
    str_out= StringVar(framemain)
    str_out.set("Output")
    def my_show(*args):
        str_out.set(menu.get())
    options.trace_add('write',my_show)
    def optionmenu_callback():
        teachmain.destroy()
        teachmain.update()
        if menu.get() == "Periodic 1":
            per1(coursetype.lower(), name)
        elif menu.get() == "Mid Term":
            Midterm(coursetype.lower(), name)
        elif menu.get() == "Periodic 2":
            per2(coursetype.lower(), name)
        elif menu.get() == "Anual Exam":
            Final(coursetype.lower(), name)
        elif menu.get() == "Overall":
            Overall(coursetype.lower(), name)
    student_record = CTkButton(framemain, command=optionmenu_callback, text="Open Record",text_color="black", width=74, height=75,font=("",23), border_width=5)
    student_record.grid(row=5,column=2)
    student_record.place(relx=0.5, rely=0.54, anchor=CENTER)
    def leave():
        teachmain.destroy()
        teachmain.update()
        if name == "admin":
            teacher()
        else:
            staff(name)

    leaver = CTkButton(framemain, command=leave, text="Main Menu",text_color="black",font=("",16), border_width=5)
    leaver.grid(row=5,column=2)
    leaver.place(relx=1, rely=1, anchor=SE)
    #------
    teachmain.mainloop()

#------------------------------------calling the main page function to start the app
Main(BG, text_color, adder_Font_tuple, login)
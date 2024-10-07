import pickle
from tkinter import *
from tkinter import filedialog
from PIL import Image,  ImageTk
root=Tk()
root.geometry('500x520')
#global dashboard
def notification():
    global send_empid 
    #global delete_tex, delete_tex2
    def search_empid():
        pass
        send_empid1=send_empid.get()
        if send_empid1.isdigit() !=True:
            
            canvas_noti.create_rectangle(200,20,400,60, fill='green', outline='green')

            
            delete_tex=canvas_noti.create_text(300,40, text='EmpID in invalid format.', fill='red')
        if send_empid1.isdigit()==True:
            canvas_noti.create_rectangle(200,20,400, 60, fill='green', outline='green')

            with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_empid.dat",'rb') as f:
                import pickle
                try:
                    while True:
                        emp_idsearch=pickle.load(f)
                        print(emp_idsearch)
                        nam=emp_idsearch[1]
                        emp_idsear=emp_idsearch[0]
                        if int(send_empid1)==emp_idsear:
                            global send_me
                            send_me=int(send_empid1)
                            canvas_noti.create_rectangle(200,20,400, 60, fill='green', outline='green')

                            emp_id_found=1
                            canvas_noti.create_text(300,40, text='EmpID found'+' Name: '+ nam, )
                            canvas_noti.create_window(200, 300, window=send_button)
                            break

                        
                except EOFError:
                    pass
                try:
                    emp_id_found
                except NameError:
                    canvas_noti.create_rectangle(200,20,400, 60, fill='green', outline='green')
                    canvas_noti.create_text(300,40, text='EmpID in invalid format.', fill='red')
                try:
                    send_button 
                    canvas_noti.delete(send_button)
                    canvas_noti.delete(send_button)
                except NameError:
                    pass

                if  emp_id_found==1:
                    canvas_noti.create_rectangle(200,20,400, 60, fill='green', outline='green')
                    canvas_noti.create_text(300,40, text='EmpID found'+' Name: '+ nam, )

    noti_window=Toplevel()
    canvas_noti=Canvas(noti_window, height=400, width=400, bg='green')
    canvas_noti.grid(row=0,column=0)
    canvas_noti.create_text(80,15, text='Send messages', font=('Lucida Calligraphy', 15)) 
    noti_window.lift()
    canvas_noti.create_text(50, 40, text='Send to: ', font=('Arial Narrow', 15))
    send_empid=Entry(noti_window)
    send_empid_button=Button(noti_window, command=search_empid, text='Search')
    send_empid_message=Text(noti_window, height=10, width=45)
    canvas_noti.create_text(70, 95, text='Type message:', font=('joker', 13))
    canvas_noti.create_window(200, 200, window=send_empid_message )
    canvas_noti.create_window(150, 67, window=send_empid_button)
    canvas_noti.create_window(150, 40, window=send_empid)
    def send_message():
        str_temp='from'+str(super_id)+'to'+str(send_me)
        print(str_temp)
        str_path='C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\'+str_temp
        with open(str_path, 'ab') as file:
            pickle.dump(str(super_id)+'('+str(super_name)+'):\n'+send_empid_message.get(1.0, END), file)
        str_path2='C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\'+'to'+str(send_me)

        with open(str_path2, 'rb') as file:
            try:
                set_1=pickle.load(file)
            except:
                pass
            if ('set_1' in locals())==True or 'set_1' in globals()==True:
                print(type(set_1))
                if type(set_1) ==set:
                    set_1.add(int(super_id))
                    print(2)
                else:
                    print(3)
                    set_1=set() 
            else:
                set_1=set()
                set_1.add(int(super_id))
                print(1)
        with open(str_path2, 'wb') as file:

            pickle.dump(set_1, file)
        
    send_button=Button(noti_window, text='Send', command=send_message)
#notification()
def recieve_notification():
    list_seen=[]
    global d_notification
    #d_notification=dict()
    recieve_window=Toplevel()
    recieve_window.geometry('500x600')
    frame_short=Frame(recieve_window, height=500, width=100)
    scrollbar_1=Scrollbar(frame_short)
    frame_chat=Frame(recieve_window, height=500, width=400)
    frame_chat.grid(row=0, column=1)
    #my_list=Listbox(frame_short, yscrollcommand=scrollbar_1.set)
    scrollbar_1.pack(side=RIGHT, fill=Y)
    #scrollbar_2=Scrollbar(frame_chat)
    #scrollbar_2.pack(side=RIGHT, fill=Y)


    frame_short.grid(row=0, column=0)
    list_widget=[]
    seventh_canvas=Canvas(recieve_window, width=300, height=30, bg='red')

    seventh_canvas.grid(row=1,column=0, columnspan=2)
    def back():
        list_4=[]
        recieve_window.destroy()
        dashboard.state(newstate='normal')
        if os.path.exists('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\to'+str(super_id)):
            with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\to'+str(super_id), 'rb') as file:
                sender_1=pickle.load(file)
                for i in sender_1:
                    if 'emp_seen_times'+str(i) in globals():

                        if globals()['emp_seen_times'+str(i)]>=1:
                            print(globals()['emp_seen_times'+str(i)])
                            list_4.append(i)
                            with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\from'+str(i)+'to'+ str(super_id), 'wb') as file2:
                                pass
            with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\to'+str(super_id), 'wb') as file3:
                for i in list_4:
                    sender_1.discard(i)
                pickle.dump(sender_1, file3)
                pass
                        


    g_button=Button(recieve_window, text='back', command=back)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
    seventh_canvas.create_window(150,15, window=g_button)

    #canvas_recieve=Canvas(recieve_window, height= 400, width= 400, bg='green')
    #canvas_recieve.grid(row=0, column=0)
    global get_last_text
    import os
    if os.path.exists('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\to'+str(super_id)):
        #global uni_id
        def get_text():
            try:
                frame_chat.destroy()
            except:
                pass
            frame_chat=Frame(recieve_window, height=500, width=400)
            frame_chat.grid(row=0, column=1)

            #global uni_id
            print(uni_id)


                
            #emp=but.cget('text')
            #emp=emp[:4]
            #print(emp)

            get_last_text=''
            print(type(get_last_text))
            with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\from'+uni_id+'to'+str(super_id),'rb') as file:
                
                try:
                    while True:
                        hmm=pickle.load(file)
                        get_last_text+=hmm
                except EOFError:
                    pass
            print(get_last_text)
            
            message=Label(frame_chat)
            message.config(text=get_last_text)
            message.place(relx=0.35, rely=0.3, anchor=CENTER)
            def close():
                message.destroy()
                #recieve_window.state(newstate='normal')

            #Button(frame_chat, text='close', command=close).pack(side=BOTTOM)

            



        with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\to'+str(super_id), 'rb') as file:

            try:
                #while True
                sender_set=pickle.load(file)
                f=0
                for i in sender_set:
                    sender=i

                    with open('C:\\Users\\Aayush\\Desktop\\cs project\\notifications\\from'+str(sender)+'to'+str(super_id), 'rb') as fil:
                       # pass
                        message_glimpse=pickle.load(fil)
                        globals()['emp_'+str(sender)]=str(sender)
                        if len(message_glimpse)<30:
                            message_glimpse1=message_glimpse
                            pass
                        if len(message_glimpse)>=30:

                            
                            message_glimpse1=message_glimpse[0:30]+'.....'
                        def id():
                            global id2
                            id2=message_glimpse[:4]
                            pass
                        #global but
                        #hi=get_text(f)

                        globals()['button_emp_'+str(sender)]=Button(frame_short,  text = message_glimpse1,  command= get_text,  borderwidth=0, height=5,width=20)
                        globals()['button_emp_'+str(sender)].pack()
                        list_widget.append(globals()['button_emp_'+str(sender)])
                        #global uni_id

                        #d_notification.update({Button(recieve_window, command= lambda: [get_text(), uni_id:=(Button.cget())[:4]],text=message_glimpse1,textvariable=(uni_id:=message_glimpse[:4]),  borderwidth=0, height=5,width=20): message_glimpse[:4] })
                    f+=1

                        
   
                        #but=Button(recieve_window, command=lambda: [get_text()], text=message_glimpse1, borderwidth=0, height=5,width=20)
                        #but.pack()
            except EOFError:
                pass
            def get_widget(event):
                for button in list_widget:
                    print('hello')
                    if button is event.widget:
                        print('hell')
                        global uni_id
                        uni_id=(button['text'])[:4]
                        if 'emp_seen_times'+uni_id not in globals():
                            globals()['emp_seen_times'+uni_id]=0
                        else:
                            globals()['emp_seen_times'+uni_id]=0
                        globals()['emp_seen_times'+uni_id]+=1
                        print(globals()['emp_seen_times'+uni_id])

                        print(uni_id)
                        list_seen.append(uni_id)
                pass
            for buttons in list_widget:

                buttons.bind('<Button-1>', get_widget)
            #my_list.pack(side=LEFT, fill=BOTH)
        #print(d_notification)
        #for i in d_notification:
           # i.pack()
            #print(d_notification[i])
           # pass
def add_employee():
        dashboard.state(newstate='iconic')
        from tkinter import messagebox
        
        from random import randint
        up=Toplevel()
        up.geometry('300x530')

        second_canvas=Canvas(up, height=500 , width=300 ,bg="cyan")
        seventh_canvas=Canvas(up, width=300, height=30, bg='red')

        seventh_canvas.grid(row=1,column=0)
        def back():
            up.destroy()
            dashboard.state(newstate='normal')

        g_button=Button(up, text='back', command=back)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
        seventh_canvas.create_window(150,15, window=g_button)
        def ran():
            global z
            z=randint(1000,9999)
            import pickle
            l1=[]
            with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:
                    try:
                        while True:
                            d2=pickle.load(file)
                            l1.append(d2)
                            
                    except:
                        print('exception')
            for i in l1:
                if z in i:
                    ran()
                else:
                    second_canvas.create_text(110, 50 , text='New employee id is '+str(z)+".", font=('Lucida Calligraphy', 12))
                    
                    
        second_canvas.create_text(90,20,text='Add A Employee' ,font=('Showcard Gothic', 15))
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
        entry_name=Entry(up)
        salary_entry=Entry(up)
        click=StringVar()
        click.set("Employee")
        designation_entry=OptionMenu(up, click, 'Employee', 'Manager')
        age_entry=Entry(up)
        def get_image():
            import os
            global my_photo, filepath
            my_photo=filedialog.askopenfile(title='Select an image', filetypes=(('png files', '*.png'),))
            if my_photo:
                filepath = os.path.abspath(my_photo.name)
            my_photo=Image.open(filepath)
            my_photo= my_photo.resize((100, 100))
            my_photo= ImageTk.PhotoImage(my_photo)
            second_canvas.create_image(170, 270, image=my_photo)
            second_canvas.create_text(170, 330, text='(Preview)',fill='red')

            pass
        image_dialog=Button(up, text='Chose image', command=get_image)
        second_canvas.create_text(50, 200, text='Select your',font=('Castellar', 8) )
        second_canvas.create_text(50, 215, text='Photo',font=('Castellar', 8) )

        second_canvas.create_window(170, 200, window=image_dialog)

        ran()
#Aayush Singh
#class-XII-A
#Roll No:-1(one)

        def add_final():
                    if (age_entry.get()).isdigit() ==True and (salary_entry.get()).isdigit() ==True:
                        second_canvas.create_rectangle(0,400, 500,500, fill='cyan', outline='cyan')
                        response=messagebox.askokcancel("INFORMATION" , "Employee added.")
                        #root.state(newstate='normal')
                        up.lift()
                        if response==1:
                            global z
                            emp_id=z
                            name=entry_name.get()
                            designation=click.get()
                            global super_id
                            super_id1=super_id
                            if designation=='Manager':
                                import random
                                password=str()
                                l1=['a','b','c','q','w','e','r','t','y','u','i','o','p','1','2','3','4','5','6']
                                for z in range(7):
                                    y=random.choice(l1)
                                    password+=y
                                
                                super_id1=None
                            else:
                                    password=None



                            salary=salary_entry.get()
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                            age=age_entry.get()
                            d1={emp_id: [name,designation, int(salary), int(age), super_id1,password, filepath]}
                            with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'ab') as file:
                                pickle.dump(d1, file)
                            with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_empid.dat",'ab') as file:
                                pickle.dump((emp_id, name), file)
                            up.destroy()
                            dashboard.state(newstate='normal')

                        
                        
                        else:
                            pass
                    else:
                        second_canvas.create_rectangle(0,220,500,500 , fill='cyan', outline='cyan')
                        second_canvas.create_text(150, 470, text='There seems to be some problem in Age/Salary ', fill='red', anchor=CENTER)
                        second_canvas.create_text(150, 490, text='Input valid Salary / Age', fill='red', anchor=CENTER)

        button_save=Button(up,text="ADD", command= add_final)
        second_canvas.create_text(50,80, text="Name", font=('Castellar', 10))
        second_canvas.create_text(50,110, text="Designation", font=('Castellar', 10))
        second_canvas.create_text(50,140, text="Salary", font=('Castellar', 10))
        second_canvas.create_text(50,170, text="Age", font=('Castellar', 10))

        second_canvas.create_window( 170, 80, window= entry_name)
        second_canvas.create_window( 170, 110, window= designation_entry)
        second_canvas.create_window( 170,140 , window= salary_entry)
        second_canvas.create_window(170 , 170, window= age_entry)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
        second_canvas.create_window( 170, 360, window= button_save)
        second_canvas.grid(row=0)

        

def update_record():
    dashboard.state(newstate='iconic')

    up=Toplevel()
    up.geometry('405x437')
    third_canvas=Canvas(up,height=400, width=400, bg='yellow')
    third_canvas.grid(row=0,column=0)
    def delete_rec():
                    b=Entry(up)
                    third_canvas.create_text(330, 70 , text='Input Emp. ID')
                    third_canvas.create_window(330,90,window=b)
                    #b.grid(row=3)
                    def delete_ro():
                        random_number=0
                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:
                            l2=[]
                            try:
                                print(1)
                                while True:
                                        d1=pickle.load(file)
                                        
  #                                      print(1)
 #                                       print(b.get())
                                        if int(b.get()) not in d1:
                                            print(b.get())
                                            l2.append(d1)
                                        if int(b.get())  in d1:
                                            if int(b.get()) != 1000 :
                                                    if d1[int(b.get())][1]=='Manager':
                                                        l2.append(d1)
                                                        third_canvas.create_rectangle(0,200,400,400, fill='yellow',outline='yellow')
                                                        third_canvas.create_text(200,390, text='You are not authorised to remove details of this Employee', fill='red')
                                                        random_number+=2
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                                    else:
                                                        random_number+=1
                                            if int(b.get()) == 1000 :
                                                    random_number+=1
                                            
                            except EOFError:           
                                pass
                            if random_number==1:
                                third_canvas.create_rectangle(0,200,400,400, fill='yellow',outline='yellow')
                                third_canvas.create_text(200,390, text='Employee Details removed.', fill='red')
                            elif random_number==0:
                                third_canvas.create_rectangle(0,200,400,400, fill='yellow',outline='yellow')
                                third_canvas.create_text(200,390,text='Employee ID not found.', fill='red')
                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'wb') as file:
                                                    for dict in l2:
                                                        pickle.dump(dict, file)
                    with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as f:
                        try:
                            while True:
                                print(pickle.load(f))
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                        except:
                            pass      
                    del_but=Button(up,text="DELETE", command=delete_ro)
                    third_canvas.create_window(330,120,window=del_but)
    with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as f:
        try:
            while True:
                print(pickle.load(f))
        except:
            pass

    def update_rec():
                v=Entry(up)
                third_canvas.create_text(65,75, text='Search emp._id', font=('Ariel Narrow', 10))
                third_canvas.create_window(70, 100, window=v)
                #v.grid(row=4)

                def search():
                    with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:
                        l1=[]
                        rno=0
                        try:
                            while True:
                                d2=pickle.load(file)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                l1.append(d2)
                                for i in d2:
                                    print(int(v.get()))
                                    
                                    if int(v.get())==i:
                                        rno+=1
                                        global empid,empname,designation,salary,age, super_id
                                        empid,empname,designation,salary,age, super_id=i,d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]
                                                             
                                    
                                        print(100)
                                        value=StringVar()
                                        value.set('Salary')
                                        Label(up, text="What you want to modify?: "   )
                                        third_canvas.create_text(78,152,text='What you want to modify?: ')
                            
                                        d=OptionMenu(up, value, 'Name', 'Designation', 'Salary', 'Age')
                                        global delete_window4
                                        delete_window4=third_canvas.create_window(70,180,window=d)
                                        #d.grid(row=8,column=0)
                                        print("hello")
                                        Label(up, text='Choose option you want to update')
                                        def option_get():
                                            option=value.get()
                                        # d=d.get()
                                            global delete_window1, delete_window2
                                            if option=='Name':
                                                    x=Entry(up)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                                    
                                                    delete_window1=third_canvas.create_window(70,245,window=x)
                                                    #x.grid(row=9)
                                                    def change():
                                                        last_val=x.get()
                                                        #d2[int(v.get())][0]=last_val
                                                        
                                                        for d4 in l1:
                                                            if int(v.get()) in d4:
                                                                d4[int(v.get())][0] = last_val
                                                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'wb') as file:
                                                            for i in l1:
                                                                pickle.dump(i, file)

                                                        print("changes made")  
                                                    change_but=Button(up,text="change", command=change)
                                                    
                                                    delete_window2=third_canvas.create_window(70,278,window=change_but)
                                                    #Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                            elif option=="Designation":
                                                    x=Entry(up)
                                                    
                                                    delete_window1=third_canvas.create_window(70,245,window=x)
                                                    #x.grid(row=9)
                                                    def change():
                                                        last_val=x.get()
                                                        #d2[int(v.get())][0]=last_val
                                                        
                                                        for d4 in l1:
                                                            if int(v.get()) in d4:
                                                                d4[int(v.get())][1] = last_val
                                                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'wb') as file:
                                                            for i in l1:
                                                                pickle.dump(i, file)

                                                        print("changes made")  
                                                    change_but=Button(up,text="change", command=change)
                                                    
                                                    delete_window2=third_canvas.create_window(70,278,window=change_but)
                                            elif option=="Salary":
                                                    x=Entry(up)
                                                    delete_window1=third_canvas.create_window(70,245,window=x)
                                                    #x.grid(row=9)
                                                    #Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                                    def change():
                                                        last_val=x.get()
                                                        #d2[int(v.get())][0]=last_val
                                                        for d4 in l1:
                                                            if int(v.get()) in d4:
                                                                d4[int(v.get())][2] = last_val
                                                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'wb') as file:
                                                            for i in l1:
                                                                pickle.dump(i, file)
                                                        print("changes made")  
                                                    change_but=Button(up,text="change", command=change)
                                                    
                                                    delete_window2=third_canvas.create_window(70,278,window=change_but)
                                            elif option=="Age":
                                                    x=Entry(up)
                                                    
                                                    delete_window1=third_canvas.create_window(70,245,window=x)
                                                    #x.grid(row=9)
                                                    def change():
                                                        last_val=x.get()
                                                        #d2[int(v.get())][0]=last_val
                                                        
                                                        for d4 in l1:
                                                            if int(v.get()) in d4:
                                                                d4[int(v.get())][3] = last_val
                                                        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'wb') as file:
                                                            for i in l1:
                                                                pickle.dump(i, file)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                                        print("changes made")  
                                                    change_but=Button(up,text="change", command=change)
                                                    change_but=Button(up,text="change", command=change)
                                                    
                                                    delete_window2=third_canvas.create_window(70,278,window=change_but)
                                                    
                                        get_but=Button(up,text='select',command=option_get)
                                        global delete_window3
                                        delete_window3=third_canvas.create_window(70,215,window=get_but)
                                                    
                                    #elif int(v.get()) not in d2:
                                                
                                               # Label(up, text="EMPLOYEE ID not found in the database")
                                    
                        except : 
                                print('exception')
                                if rno==0:
                                        third_canvas.create_rectangle(0,142,300,400, fill='yellow',outline='yellow')
                                        third_canvas.create_text(200,390,text="EMP.  ID NOT FOUND IN DATABASE.", fill='red')
                                        try:
                                            while True:

                                                third_canvas.delete(delete_window4,  delete_window3)
                                        except:
                                            pass
                                        try:
                                            while True:
                                                #Aayush Singh
#class-XII-A
#Roll No:-1(one)

                                                third_canvas.delete( delete_window1, delete_window2)
                                        except:
                                            pass
                                elif rno==1:

                                        third_canvas.create_rectangle(100,172,300,400, fill='yellow',outline='yellow')
                                        third_canvas.create_text(200,330, text="EMP. ID found!", fill='red')
                                        third_canvas.create_text(200,345, text='Name: '+empname)
                                        third_canvas.create_text(200, 360, text='Designation: '+ designation)
                                        third_canvas.create_text(200, 375, text='Salary: '+ str(salary))
                                        third_canvas.create_text(200,390, text='Age: '+ str(age))

                search_but=Button(up, text="Search", command=search)
                third_canvas.create_window(70, 130 , window=search_but)

    third_canvas.create_text(130, 20, text='What you want to do?', font=('Showcard Gothic', 15))
    delete_button=Button(up, text='DELETE A RECORD', command=delete_rec, font=('Forte', 10))
    third_canvas.create_window(330,50,window=delete_button)
    update_button=Button(up, text='UPDATE A RECORD', command=update_rec, font=('Forte', 10))
    seventh_canvas=Canvas(up, width=400, height=30, bg='red')
    third_canvas.create_window(70,50,window=update_button)

    seventh_canvas.grid(row=1,column=0)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
    def back():
        up.destroy()
        dashboard.state(newstate='normal')

    g_button=Button(up, text='back', command=back)

    seventh_canvas.create_window(200,15, window=g_button)
def view_database():
    new2=Toplevel()
    dashboard.state(newstate='iconic')

    new2.geometry('727x635')
    def terminal_record_table():
        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:

  
            try:
                print(" "*30,"_"*88)     
                print(" "*30,"|  emp._id  |      Name      |      Designation     |    Salary  |   Age  |  super_id  |") 
                while True:
                    d2=pickle.load(file)
                    
                    for i in d2:
                        if d2[i][4]== super_id:
                            empid,empname,designation,salary,age, uper_id=i,d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]
                            t4=tuple()
                            t5=tuple(empname)
                            print(" "*30,"|",i," "*(8-len(tuple(str(empid)))),"|",empname," "*(13-len(t5)),"|",designation," "*(19-len(tuple(str((designation))))),"|",salary," "*(9-len(tuple(str(salary)))),"|",age," "*(5-len(tuple(str(age)))),"|",uper_id," "*(9-len(tuple(str(uper_id)))), '|')
            
            except EOFError:
                
                pass
            except TypeError:
                pass
        print(" "*30,"‾"*88)
    def gui_record_table():
        from tkinter import ttk
        
        my_tree= ttk.Treeview(new2)



        my_tree['columns']= ("Emp. ID", 'Name', 'Designation','Salary', 'Age', 'Super_ID')
        my_tree.column('#0', width=0, stretch=NO)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
        my_tree.column("Emp. ID", width=120, anchor=W)
        my_tree.column('Name', width=120, anchor=W)
        my_tree.column('Designation', width=120, anchor=W)
        my_tree.column('Salary', width=120, anchor=W)
        my_tree.column('Age', width=120, anchor=W)
        my_tree.column('Super_ID', width=120, anchor=W)
        my_tree.heading('#0', text="Label", anchor=W)
        my_tree.heading('Emp. ID', text='Emp_id', anchor=W)
        my_tree.heading('Name', text='Name', anchor=W)
        my_tree.heading('Designation', text='Designation', anchor=W)
        my_tree.heading('Salary', text='Salary', anchor=W)
        my_tree.heading('Age', text='Age', anchor=W)
        my_tree.heading('Super_ID', text='Super_ID', anchor=W)
        with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as f:
                u=0
                #l1=[]
                try:
                    while True:
                        d2=pickle.load(f)
                        #l1.append(d2)
                        print(d2)
                        
                        for i in d2:
                            if d2[i][4]== super_id:
                                my_tree.insert(parent='', index='end', iid=u, text='', values=(i,d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]))
                                
                                u+=1
                                print(u)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                except EOFError:
                    print(None)
        eleventh_canvas=Canvas(new2, width=725, height=50, bg='navy blue')
        eleventh_canvas.grid(row=3,sticky='ew')
        eleventh_canvas.create_text(362.5, 25, text='The details are as follows :-', font=('Lucida Calligraphy', 15), fill='white' )
        #Label(new2, text='The details are as follows :-', font=('Lucida Calligraphy', 15))#####         
        my_tree.grid(row=4,column=0)
    eighth_canvas=Canvas(new2, height=30, width=725, bg='red')
    def back():
        new2.destroy()
        dashboard.state(newstate='normal')

    back_buton=Button(new2, text='Back', command=back)
    no=eighth_canvas.create_window(362.5,5, window=back_buton, anchor=NW)
#   no.place(150,15,sticky='we')
    eighth_canvas.grid(row=0, sticky='we')
    tenth_canvas=Canvas(new2, height=300,width= 725,bg='purple')
    tenth_canvas.grid(row=1,sticky='we')

    but_1=Button(new2, text='VIEW DETAILS IN TERMINAL', command=terminal_record_table, font=('Algerian', 20))
    #.grid(row=1,padx=20,pady=20)
    but_2=Button(new2, text='VIEW DETAILS IN A GUI', command=gui_record_table , font=('Algerian', 20))
    #buid(row=2,padx=20,pady=20)
    tenth_canvas.create_window(362.5,90, window=but_1)
    tenth_canvas.create_window(362.5, 210, window=but_2)
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
def logout():
    dashboard.destroy()
    hum=Toplevel()
    Label(hum, text='Thank you for using this Programe!\nHave a good day.\nMade by: Aayush Singh\n RollNo.: 1(one)\n Class: XII-A', font=('Ariel Narroww', 20)).pack()
    def close():
        hum.destroy()
        root.state(newstate='normal')
        entry_name.delete(0, END)
        entry_password.delete(0, END)
        #root.lift()
        try:
            canvas.delete(delete_window5)
        except:
            pass
        try:
            canvas.delete(delete_window6)
        except:
            pass
    Button(hum, text='close', command=close).pack()
    #root.lift()
    #hum.mainloop()

def part_database():
    new=Toplevel()
    dashboard.state(newstate='iconic')

    fourth_canvas=Canvas(new, height=500,width=300,bg='orange')
    fourth_canvas.grid(row=0)
    fourth_canvas.create_text(80,10, text='Input Emp. ID.', font=('Showcard Gothic', 15))
    def search():
            c=ask.get()
            with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:
                num=0
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
                try:
                    while True:
                        d2=pickle.load(file)

                        if int(c) in d2:
                           # print(d2[int(c)][4])
                            if d2[int(c)][4]==super_id:
                                num+=1
                                fourth_canvas.create_rectangle(0,80,500,500, fill='orange', outline='orange')
 #Aayush Singh
#class-XII-A
#Roll No:-1(one)                             
                                global  filepath2
                                my_photograph=r'{}'.format(d2[int(c)][6])
                                filepath2=''
                                for i in my_photograph:
                                    if i=="\\":
                                        filepath2+='\\\\'
                                    else:
                                        filepath2+=i
                                my_photograph=Image.open(filepath2)
                                global resize_photo, last_img
                                resize_photo=my_photograph.resize((100, 100))
                                last_img=ImageTk.PhotoImage(resize_photo)
                                fourth_canvas.create_image(150, 140, image= last_img)
                                #fourth_canvas.create_image
                                fourth_canvas.create_text(150, 210,text='Emp. ID: '+str(c), font=('LUCIDA Calligraphy', 12))
                                fourth_canvas.create_text(150,230,text='Name: '+str(d2[int(c)][0]), font=('LUCIDA Calligraphy', 12))
                                fourth_canvas.create_text(150,250, text='Designation :'+str(d2[int(c)][1]), font=('LUCIDA Calligraphy', 12))
                                fourth_canvas.create_text(150,270, text='Salary :'+str(d2[int(c)][2]), font=('LUCIDA Calligraphy', 12))
                                fourth_canvas.create_text(150,290,text='Age :'+ str(d2[int(c)][3]), font=('LUCIDA Calligraphy', 12))
                                #Label(new, text= c).pack()
                                #Label(new, text='Name :'+str(d2[int(c)][0])).pack()
                                #Label(new, text='Designation :'+str(d2[int(c)][1])).pack()
                                #Label(new, text='Salary :'+str(d2[int(c)][2])).pack()
                                #Label(new, text='Age :'+ str(d2[int(c)][3])).pack()
                            else:
                                #Aayush Singh
#class-XII-A
#Roll No:-1(one)
                                num+=1
                                fourth_canvas.create_rectangle(0,80,300,300, fill='orange', outline='orange')
                                fourth_canvas.create_text(150,270, text='This Employee doesn\'t work under you!', fill='red')
                                fourth_canvas.create_text(150, 290, text='You are not authorised to view details of this employee', fill='red')

                except EOFError:
                    pass
                if num==0:
                    fourth_canvas.create_rectangle(0,80,300,300, fill='orange', outline='orange')
                    fourth_canvas.create_text(150, 280, text='Employee id not found in database.', fill='red')
                    #print("Employee id not found in database.")
                del num
    ask=Entry(new)
    fourth_canvas.create_window(72,40,window=ask)
    seventh_canvas=Canvas(new, width=300, height=30, bg='red')
    seventh_canvas.grid(row=1,column=0)
    def back():
        new.destroy()
        dashboard.state(newstate='normal')

    g_button=Button(new, text='back', command=back)
    seventh_canvas.create_window(150,15, window=g_button)



    #ask.pack()
    search_but=Button(new, text="SEARCH",command=search)
    fourth_canvas.create_window(72,70, window=search_but)

    

def login():
    global password_dict
    password_dict={}
    with open("C:\\Users\\Aayush\\Desktop\\cs project\\database_final.dat",'rb') as file:
        #Aayush Singh
#class-XII-A
#Roll No:-1(one)
        try:
            while True:
                d1=pickle.load(file)
                for i in d1:
                    if d1[i][1].capitalize()=='Manager':
                        d_te={i : (d1[i][5],d1[i][1])}
                        password_dict.update(d_te)
                        print(password_dict)
        except:
            pass
    if int(entry_name.get()) in password_dict:
        if password_dict[int(entry_name.get())][0]==entry_password.get():
            global super_id, super_name
            super_id=int(entry_name.get())
            super_name=password_dict[int(entry_name.get())][1]
            dash=canvas.create_rectangle(0,510, 100, 520, fill='green', outline='green')
            for kat in range(4):
                if (canvas.coords(dash))[0]== 500:
                    
                    canvas.move(dash, -500,0)
                    root.update()
                    import time
                    time.sleep(0.01)
                if (canvas.coords(dash))[0]!= 500:
                    for j in range(25):
                        canvas.move(dash, 20, 0)
                        root.update()
                        import time
                        time.sleep(0.01)
            root.iconify()
            global dashboard
            dashboard=Toplevel()
            #dashboard.bind('<Enter>', on_enter)
            #dashboard.bind('<Leave>', on_leave)
            dashboard.geometry("418x500")
            global add_Button, update_Button, view_button, view_particular, quit_button
            Label(dashboard,text='  HELLO THERE!     ', font=('Castellar', 30), fg='yellow', bg='green', ).grid(row=0,column=0)
            Label(dashboard,text=  '  What you want to perform today?    ', font=('Lucida Calligraphy', 15), fg='yellow', bg='green',).grid(row=1,column=0)
            add_Button=Button(dashboard, text="      ADD EMPLOYEE DETAILS      ", command=add_employee, font=('Algerian', 20), activebackground='cyan', width=24)
            add_Button.grid(row=2,column=0)
            update_Button=Button(dashboard, text='  UPDATE/ DELETE EMPLOYEE   \nDetails', command=update_record, font=('Algerian', 20), anchor=CENTER, activebackground='yellow',  width=24)
            update_Button.grid(row=3,column=0)
            view_button=Button(dashboard, text='     VIEW EMPLOYEE DETAILS      ', command=view_database, font=('Algerian', 20), activebackground='purple', width=24)
            view_button.grid(row=4,column=0)
            view_particular=Button(dashboard, text=' VIEW PARTICULAR EMPLOYEE  \n  DETAIL ',command=part_database, font=('Algerian', 20), anchor=CENTER, activebackground='orange', width=24)
            view_particular.grid(row=5,column=0,columnspan=1)
            quit_button=Button(dashboard, text='LOGOUT',command=logout, font=('Algerian', 20), activebackground='red', highlightbackground='red', width=24 )
            quit_button.grid(row=8,column=0, columnspan=2)
            global notification_button, recieve_button
            notification_button=Button(dashboard, text='notify',command=notification, font=('Algerian', 20), activebackground='red', highlightbackground='red', width=24)
            notification_button.grid(row=6,)
            recieve_button=Button(dashboard, text='notification',command=recieve_notification ,font=('Algerian', 20), activebackground='red', highlightbackground='red',  width=24)
            recieve_button.grid(row=7)


            add_Button.bind('<Enter>', on_enter)
            add_Button.bind('<Leave>', on_leave)
            view_button.bind('<Enter>', on_enter2)
            view_button.bind('<Leave>', on_leave2)
            update_Button.bind('<Enter>', on_enter1)
            update_Button.bind('<Leave>', on_leave1)
            view_particular.bind('<Enter>', on_enter3)
            view_particular.bind('<Leave>', on_leave3)
            quit_button.bind('<Enter>', on_enter4)
            quit_button.bind('<Leave>', on_leave4)
            notification_button.bind('<Enter>', on_enter7)
            notification_button.bind('<Leave>', on_leave7)
            recieve_button.bind('<Enter>', on_enter6)
            recieve_button.bind('<Leave>', on_leave6)




            return super_id
        
        else:
            global delete_window5,delete_window6
            try:
                canvas.delete(delete_window6)
            except:
                pass

            delete_window5=canvas.create_text(250,400 , text='WRONG PASSWORD.', fill='red',font=('Castellar', 10))
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
    else:
        try:
            canvas.delete(delete_window5)
        except:
            pass
        delete_window6=canvas.create_text(250,400 , text='Invalid Login ID', fill='red',font=('Castellar', 10))
        
background_image=ImageTk.PhotoImage(Image.open(r"C:\Users\Aayush\Desktop\canvas picture.png"))

canvas =Canvas(root, height=700, width=500)
canvas.pack(fill='both', expand=True, )
canvas.create_image(0,0, image=background_image, anchor= 'nw')
increament=0
global x
x=163
#rectan=canvas.create_rectangle(x,95,x+5, 100, fill='green' )

while True:
    welcome_image=Image.open(r"C:\Users\Aayush\Desktop\welcome_image.png")

    #print(1)
    try:
        canvas.delete(welcome_image)
        

    except:
        pass
    increament+=1
    
    x=163-increament

    welcome_image1=welcome_image.resize((334, 72))
    welcome_image1= welcome_image1.crop((167-increament, 0, 167+increament, 72))
    welcome_image1=ImageTk.PhotoImage(welcome_image1)
    canvas.create_image(250, 100, image=welcome_image1)
    #print(1)
    #l1=canvas.coords(rectan)

    #print(l1)
 ##   while (canvas.coords(rectan))[0]>=0:
#        try:
 #           canvas.move(rectan, -1, 0)
 #           root.update()
 #           import time
 #           time.sleep(0.01)
 #       except:
  #          pass
        
#        if (canvas.coords(rectan))[0]==0:
#
        #print((canvas.coords(rectan))[0])
           # break
    #print(1)
    
    import time
    time.sleep(0.01)
    root.update()
    #print(increament)
    if increament>=167:
        break

#canvas.create_text(250,100,text='Welcome!', font=('Jokerman', 50), fill='cyan')
#canvas.create_line(0,100, 700,100)
entry_name=Entry(root,width=30)
entry_password=Entry(root,width=30,show="*")
canvas.create_text(160,270,text='User ID', font=('Algerian', 15), fill='white')
#Aayush Singh
#class-XII-A
#Roll No:-1(one)
canvas.create_text(155,300,text='Password', font=('Algerian', 15), fill='white')
canvas.create_window(300, 270,window=entry_name)
canvas.create_window(300, 300,window=entry_password)
login_green=ImageTk.PhotoImage(Image.open(r"C:\Users\Aayush\Desktop\loginicon2.png"))
label_green=Label(root,image=login_green)
login_button=Button(root,text="           Login              ",command=login,overrelief=SUNKEN,borderwidth=0, font=('Algerian', 15))

canvas.create_window(250,350, window=login_button )
def on_enter(e):
   add_Button.config(background='cyan', foreground= "white")
   #Button.config(background='OrangeRed3', foreground= "white")
def on_enter1(e):
   update_Button.config(background='yellow', foreground= "red")
def on_enter2(e):
   view_button.config(background='purple', foreground= "white")
def on_enter3(e):
   view_particular.config(background='orange', foreground= "white")
def on_enter4(e):
   quit_button.config(background='red', foreground= "white")
def on_enter5(e):
   login_button.config(background='green', foreground= "white")
def on_enter6(e):
   recieve_button.config(background='violet', foreground= "white")
def on_enter7(e):
   notification_button.config(background='violet', foreground= "white")

def on_leave(e):
   add_Button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave1(e):
   update_Button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave2(e):
   view_button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave3(e):
   view_particular.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave4(e):
   quit_button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave5(e):
   login_button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave6(e):
   recieve_button.config(background= 'SystemButtonFace', foreground= 'black')
def on_leave7(e):
   notification_button.config(background= 'SystemButtonFace', foreground= 'black')
login_button.bind('<Enter>', on_enter5)
login_button.bind('<Leave>', on_leave5)



#Create a Button
#button= Button(win, text= "Click Me", font= ('Helvetica 13 bold'))
#button.pack(pady= 20)

#Bind the Enter and Leave Events to the Button

root.mainloop()
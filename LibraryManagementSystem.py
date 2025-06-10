from tkinter import * 
from tkinter import StringVar
from tkinter import ttk
from termcolor import colored
from tabulate import tabulate
from tkinter import filedialog
from PIL import Image ,  ImageTk 
import cv2
from cv2 import destroyAllWindows



def on_entry_focus_in(event):

    if EmailEntry.get() == placeholder_text:
        EmailEntry.delete(0 , END)
        EmailEntry.configure(show="")
        EmailEntry.configure(fg = "#000000")

    if DoiEntry.get() == doitext:
        DoiEntry.delete(0 , END)
        DoiEntry.configure(show="")
        DoiEntry.configure(fg="#000000")

    if DorEntry.get() == dortext:
        DorEntry.delete(0 , END)
        DorEntry.configure(show="")
        DorEntry.configure(fg="#000000")

    
   

def on_entry_focus_out(event):
     if EmailEntry.get() == "":
        EmailEntry.insert(0, placeholder_text)
        EmailEntry.configure(fg="#000000")
     
     if DoiEntry.get() == "":
        DoiEntry.insert(0 , doitext)
        DoiEntry.configure(fg="#000000")

     if DorEntry.get() == "":
         DorEntry.insert(0 , dortext)
         DorEntry.configure(fg = "#000000")

def upload():


    

    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])

    if image_path:

        image = Image.open(image_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        
        img_label = Label(window, image=photo)
        img_label.image = photo  
        img_label.pack()

        
        
        

    


def submit():

    
    
    

   

   
    new_window = Tk()

    new_window.title("Student table")
    new_window.geometry("500x500")


    

    frame4 = Frame(new_window , width=500 , height=500)
    frame4.pack(expand = True , fill ="both")
    
    
    

    frame4.grid_rowconfigure(0 , weight = 1)
    frame4.grid_columnconfigure(0 , weight = 1)

    student_details = ttk.Treeview(frame4)
    student_details['columns'] = ( 'Name' , 'Email' , 'Phone' ,'PRN' , 'Book' , 'Occupation' , 'Date of issue' , 'Date of returning' , 'Image',)


# Define column properties
    student_details.column("#0", width=0, stretch=NO)
    student_details.column("Name", anchor=CENTER, width=120)
    student_details.column("Email", anchor=CENTER, width=120)
    student_details.column("Phone", anchor=CENTER, width=120)
    student_details.column("PRN", anchor=CENTER, width=80)
    student_details.column("Book", anchor=CENTER, width=80)
    student_details.column("Occupation", anchor=CENTER, width=80)
    student_details.column("Date of issue", anchor=CENTER, width=80)
    student_details.column("Date of returning", anchor=CENTER, width=80)
    student_details.column("Image" , anchor=CENTER , width= 150)

# Set column headings
    student_details.heading("#0", text="", anchor=CENTER)
    student_details.heading("Name", text="Name", anchor=CENTER)
    student_details.heading("Email", text="Email", anchor=CENTER)
    student_details.heading("Phone", text="Phone", anchor=CENTER)
    student_details.heading("PRN", text="PRN", anchor=CENTER)
    student_details.heading("Book", text="Book", anchor=CENTER)
    student_details.heading("Occupation", text="Occupation", anchor=CENTER)
    student_details.heading("Date of issue", text="Date of issue", anchor=CENTER)
    student_details.heading("Date of returning", text="Date of returning" , anchor=CENTER)
    student_details.heading("Image" , text="Image" , anchor=CENTER)

    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    prn = prn_var.get()
    book = bookName_var.get()
    occupation = occupation_var.get()
    doi = doi_var.get()
    dor = dor_var.get()

      
    student_details.insert(parent='', index='end', iid=0, text='', values=(name, email , phone  , prn , book ,  occupation , doi , dor ))

    
 

    student_details.grid(row=0, column=0, sticky='nsew')


    uploadbutton = Button(frame4, 
                      text="Upload" , 
                      font=("Arial" , 10),
                      width=10 , 
                      bg = "#3CCB40" , 
                      fg="#ffffff",
                      activeforeground="#ffffff",
                      activebackground="#3CCB40",
                      command=upload)
    
    
    uploadbutton.grid(row=1, column=0, padx=5 , sticky="nsew")
    

   #new_window.mainloop()
    window.destroy()

  

def search():
    
    search_term = search_var.get().lower()  # Get the search term and convert to lowercase
    for row in student_details.get_children():
        item = student_details.item(row)
        values = [str(v).lower() for v in item['values']]  # Convert each value to lowercase for case-insensitive matching
        if search_term in values:
            student_details.see(row)  # Ensure the matching row is visible
            student_details.selection_set(row)  # Optionally, select the row
        else:
            student_details.selection_remove(row)  
            
  

def delete():
    pass

def select():
    pass
                
def photo():
    cam = cv2.VideoCapture(0)

    #cv2.namedWindow("Image of student")

    img_counter = 0

    while True:
        ret , frame = cam.read()

        if not ret:
            print("Failed to grab images")
            break
        cv2.imshow("Student image" , frame)

        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Escape key is hit")
            break

        if k%256 == 32:
            img_name =  "D:\\python\\practice\\student_image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name , frame)
            print("screenshot taken")
            img_counter += 1


    
    
    

    cam.release()
    cv2.destroyAllWindows()  


window = Tk()
window.title("Library Management System")
window.geometry("900x900")



#----------------------------------------frame 1 --------------------------------------------------------------------------------------------



frame1 = Frame(window, width = 200 , height=200, bg ="#55BAD9" , bd=10 , relief=SUNKEN)
frame1.pack_propagate(False) # Prevent frame 
frame1.pack()

'''uploadbutton = Button(frame1 , 
                      text="Upload" , 
                      font=("Arial" , 10),
                      width=10 , 
                      bg = "#3CCB40" , 
                      fg="#ffffff",
                      activeforeground="#ffffff",
                      activebackground="#3CCB40",
                      command=upload).place(relx = 1.0 , rely = 1.0 , x = 0 , y= 0 , anchor=SE)'''





photobutton = Button(frame1 , 
                      text="Photo" , 
                      font=("Arial" , 10),
                      width=10 , 
                      bg = "#3CCB40" , 
                      fg="#ffffff",
                      activeforeground="#ffffff",
                      activebackground="#3CCB40",
                      command=photo).pack(side=BOTTOM , anchor="sw")

#----------------------------------------frame 2 --------------------------------------------------------------------------------------------

frame2 = Frame(window , width=500 , height=500 , bg="#55BAD9")
frame2.pack()

name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
prn_var = StringVar()
bookName_var = StringVar()
occupation_var = StringVar()
doi_var = StringVar()
dor_var = StringVar()

NameLabel = Label(frame2 , text="Name: " , font=("MV Boli" , 25))
NameLabel.grid(row=0 , column=0 , padx=10 , pady=10)
NameEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#000000" , textvariable=name_var)
NameEntry.grid(row=0 , column=1 , padx=10 , pady=10)

EmailLabel = Label(frame2 , text="Email: " , font=("MV Boli" , 25))
EmailLabel.grid(row=1, column=0 , padx=10 , pady=10)
EmailEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#B3B3B3" , textvariable = email_var)

placeholder_text = "ABC123@gmail.com"
EmailEntry .insert(0, placeholder_text)
EmailEntry.bind("<FocusIn>", on_entry_focus_in)
EmailEntry .bind("<FocusOut>", on_entry_focus_out)

EmailEntry.grid(row=1 , column=1 , padx=10 , pady=10)



PhoneLabel = Label(frame2 , text="Phone number: " , font=("MV Boli" , 25))
PhoneLabel.grid(row=2, column=0 , padx=10 , pady=10)
PhoneEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#000000" , textvariable=phone_var)
PhoneEntry.insert(0 , "+91-")
PhoneEntry.grid(row=2 , column=1 , padx=10 , pady=10)

PrnLabel = Label(frame2 , text="PRN: " , font=("MV Boli" , 25))
PrnLabel.grid(row=3, column=0 , padx=10 , pady=10)
PrnEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#000000" , textvariable=prn_var)
PrnEntry.grid(row=3 , column=1 , padx=10 , pady=10)

BookNameLabel = Label(frame2 , text="Book Name: " , font=("Mv Boli",25))
BookNameLabel.grid(row=4, column=0 , padx=10 , pady=10)
BookNameEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#000000" , textvariable = bookName_var)
BookNameEntry.grid(row=4 , column=1 , padx=10 , pady=10)



OccupationLabel = Label(frame2 , text="Occupation: " , font=("MV Boli" , 25))
OccupationLabel.grid(row=5, column=0 , padx=10 , pady=10)
OccupationEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#000000" , textvariable = occupation_var)
OccupationEntry.grid(row=5 , column=1 , padx=10 , pady=10)


DoiLabel = Label(frame2 , text="Date of issue: " , font=("MV Boli" , 25))
DoiLabel.grid(row=6, column=0 , padx=10 , pady=10)
DoiEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#B3B3B3" ,textvariable=doi_var)

doitext = "dd/mm/yyyy"
DoiEntry.insert(0 , doitext)
DoiEntry.bind("<FocusIn>" , on_entry_focus_in)
DoiEntry.bind("<FocusOut>" , on_entry_focus_out)

DoiEntry.grid(row=6 , column=1 , padx=10 , pady=10)

DorLabel = Label(frame2 , text="Date of returning: " , font=("MV Boli" , 25))
DorLabel.grid(row=7, column=0 , padx=10 , pady=10)
DorEntry = Entry(frame2 , font=("Mv Boli" , 25) , fg="#B3B3B3" , textvariable=dor_var)

dortext = "dd/mm/yyyy"
DorEntry.insert(0 , doitext)
DorEntry.bind("<FocusIn>" , on_entry_focus_in)
DorEntry.bind("<FocusOut>" , on_entry_focus_out)

DorEntry.grid(row= 7 , column=1 , padx=10 , pady=10)

#----------------------------------------frame 3 --------------------------------------------------------------------------------------------

frame3 = Frame(window)
frame3.pack()

search_var = StringVar()
search_entry = Entry(frame3, textvariable=search_var)
search_entry.pack(side=LEFT)


searchButton =Button(frame3 , text="Search" , command= search)
searchButton.pack(side=LEFT)

deleteButton =Button(frame3 , text="Delete")
deleteButton.pack(side=LEFT)

selectButton =Button(frame3 , text="Select all")
selectButton.pack(side=LEFT)


submitButton =Button(frame3 , text="Submit" , command=submit)
submitButton.pack(side=LEFT, anchor="s")
frame4 = Frame(window, width=500, height=500)
frame4.pack(expand=True, fill="both")
frame4.grid_rowconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)

# Treeview for displaying student details
student_details = ttk.Treeview(frame4, columns=("Name", "Email", "Phone", "PRN", "Book", "Occupation", "DOI", "DOR"))
student_details.heading('#0', text='', anchor='w')
student_details.heading('Name', text='Name', anchor='w')
student_details.heading('Email', text='Email', anchor='w')
student_details.heading('Phone', text='Phone', anchor='w')
student_details.heading('PRN', text='PRN', anchor='w')
student_details.heading('Book', text='Book', anchor='w')
student_details.heading('Occupation', text='Occupation', anchor='w')
student_details.heading('DOI', text='Date of Issue', anchor='w')
student_details.heading('DOR', text='Date of Return', anchor='w')
student_details.column('#0', width=0, stretch=NO)
student_details.column('Name', width=100)
student_details.column('Email', width=100)
student_details.column('Phone', width=100)
student_details.column('PRN', width=100)
student_details.column('Book', width=100)
student_details.column('Occupation', width=100)
student_details.column('DOI', width=100)
student_details.column('DOR', width=100)
student_details.pack(expand=True, fill='both')








window.mainloop()
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import smtplib
import os,sys

#EmailClient class is defined
class Emailclient(object):
    def __init__(self):
        """
        Email Client class
        Locked under username and password
        Able to compose, open, delete, and send Emails
        Emails will be automatically encrypted and decrypted
        """
        #creates a GUI window to be used
        self.window = Tk()
        self.window.title("E-mail Client")
        self.window.geometry("400x500")

        #welcome message pasted to top
        self.labelText1 = StringVar()
        self.labelText1.set("Welcome to the e-mail client.")
        self.label1 = Label(self.window, textvariable=self.labelText1, height=4)
        self.label1.pack()

        #sign to tell user where to input username
        self.labelText2 = StringVar()
        self.labelText2.set("Username:")
        self.label2 = Label(self.window, textvariable=self.labelText2, height=4)
        self.label2.pack()

        #textbox to grab user input
        self.username = StringVar()
        self.enter_username = Entry(self.window, textvariable=self.username)
        self.enter_username.pack()

        #sign to tell user where to input password
        self.labelText3 = StringVar()
        self.labelText3.set("Password:")
        self.label3 = Label(self.window, textvariable=self.labelText3, height=4)
        self.label3.pack()

        #textbox to grab user input
        self.password = StringVar()
        self.enter_password = Entry(self.window, show="*",textvariable=self.password)
        self.enter_password.pack()

        #login button, will bring to main window
        self.buttonL = Button(self.window, text="Login", width=20,command=self.loginbutton)
        self.buttonL.pack(side="bottom",padx=15,pady=15)

        #buttons to select which email server to use
        self.button_hotmail = Button(self.window, text="Hotmail", width=20,command=self.hotmail)
        self.button_hotmail.pack(side="bottom",padx=15,pady=15)

        self.button_yahoo = Button(self.window, text="Yahoo!", width=20,command=self.yahoo)
        self.button_yahoo.pack(side="bottom",padx=15,pady=15)

        self.button_gmail = Button(self.window, text="Gmail", width=20,command=self.gmail)
        self.button_gmail.pack(side="bottom",padx=15,pady=15)

        self.cleannumber=1

        self.window.mainloop()

    def hotmail(self):
        #changes server to hotmail
        self.email_server="smtp-mail.outlook.com"
        tkMessageBox.showinfo("Success!","E-mail server changed to HOTMAIL")

    def yahoo(self):
        #changes server to yahoo
        self.email_server="smtp.mail.yahoo.com"
        tkMessageBox.showinfo("Success","E-mail server changed to YAHOO!")

    #PyScripter has a security issue with the Gmail server, thus not allowing connections or logins
    #into Gmail.
    def gmail(self):
        #An error popup is presented to the user when they click on the Gmail button.
        tkMessageBox.showerror("Error", "At this time, Gmail is not supported due to security issues with Python Scripter.")

    def loginbutton(self):
        """
        Button for Login screen
        """
        #logs in to email with selected server (This feature has been commented out due to security issues with PyScripter, since connections are now refused).
##        try:
##            s = smtplib.SMTP()
##            s.connect(self.email_server, 587)
##            s.ehlo()
##            s.starttls()
##            s.login(self.username.get(),self.password.get())
##            s.ehlo()
##            s.close()
##            #brings to main screen
##            self.mainscreen()
##        except:
##            tkMessageBox.showerror("Error","You have entered an incorrect username or password.")
        if (self.username.get() == "radu@yahoo.ca" and self.password.get()=="123"):
            self.mainscreen()
        else:
            tkMessageBox.showerror("Error","You have entered an incorrect username or password.")


    def mainscreen(self):
        """
        Main menu screen
        """
        #refreshes screen
        self.button_hotmail.pack_forget()
        self.button_yahoo.pack_forget()
        self.code_cleaner(self.cleannumber)
        self.window.title("E-Mail Client")
        self.window.geometry("560x460")
        menu = Menu(self.window)
        self.window.config(menu=menu)

        # Add a menu
        selectmenu = Menu(menu)
        #add drop down menu
        menu.add_cascade(label="Menu", menu=selectmenu)

        selectmenu.add_command(label="Compose", command=self.compose)
        selectmenu.add_command(label="Open", command=self.select_mail)
        selectmenu.add_command(label="Delete", command=self.delete_mail)

    def compose(self):
        """
        Screen to alow you to create an email
        Email will be encrypted before sending
        """
        #refreshes screen
        self.code_cleaner(self.cleannumber)

        self.send_button = Button(self.window, text="Send", width=20,command=self.send_mail)
        #message to tell user where to input recipiant email
        recipient_1 = StringVar()
        recipient_1.set("To:")
        self.recipientlabel = Label(self.window,textvariable=recipient_1, height=2)
        #message to tell user where to input email title
        subject_label = StringVar()
        subject_label.set("Subject:")
        self.subject_label_l = Label(self.window,textvariable=subject_label,height=2)
        #textbox to grab user input
        self.subject_1 = StringVar()
        self.enter_subject = Entry(self.window, textvariable = self.subject_1)
        #textbox to grab user input
        self.recipient = StringVar()
        self.enter_recipient = Entry(self.window, textvariable=self.recipient)
        #textbox to grab user input
        self.textinfo = Text(self.window,height = 14)
        #inserts text and textboxes to screen
        self.recipientlabel.pack(side="top")
        self.enter_recipient.pack()
        self.subject_label_l.pack()
        self.enter_subject.pack()
        self.textinfo.pack(side="top",padx=15,pady=15)
        self.send_button.pack(side="bottom",padx=15,pady=15)


        self.cleannumber=2
    def open_mail(self):
        """
        Open Selected Mail
        """
        #grabs title of textfile
        title=self.enter_title.get()
        self.code_cleaner(self.cleannumber)
        #creates a textbox widget
        self.text_screen=Text(self.window)

        try:
            #detects whether text is ecnrypted or not
            if title+".txt"=="ENCRYPTED.txt":
                #decrypts text
                decrypt=Encryption("ENCRYPTED.txt")
                decrypt.decrypt()
                text=open("DECRYTPED.txt", "r")
            else:
                text=open(title+".txt", "r")
        except IOError:
            tkMessageBox.showerror("Error", "No file found")

        screentext=text.read()
        #inserts text to screen
        self.text_screen.insert(INSERT, screentext)
        self.text_screen.pack()
        self.cleannumber=4

    def delete_mail(self):
        """
        Askes to Delete saved emails
        """
        self.code_cleaner(self.cleannumber)

        #button to delete file
        self.find_delete=Button(self.window, text="Find", width=20,command=self.Delete_file)
        #message to tell user where to input email title
        title_label = StringVar()
        title_label.set("Mail Title:")
        self.title_label_l = Label(self.window,textvariable=title_label,height=2)
        #textbox to grab user input
        enter_title = StringVar()
        self.enter_title = Entry(self.window, textvariable = enter_title)
        #inserts text and textboxes to screen
        self.title_label_l.pack(side="top")
        self.enter_title.pack()
        self.find_delete.pack(side="bottom",padx=15,pady=15)

        self.cleannumber=5

    def Delete_file(self):
        """
        Deletes selected files
        """
        try:
            #deletes file
            os.remove(self.enter_title.get())
            tkMessageBox.showinfo("Sucessfully deleted the email","Deleted!")
        except WindowsError:
            tkMessageBox.showerror("I/O ERROR","The e-mail you are looking for doesn't exist!")
    def send_mail(self):
        """
        Sends email to recipiant
        """
        self.code_cleaner(self.cleannumber)
        #opens new textfile
        savefile=open(self.subject_1.get()+".txt", "w")
        #writes text to file
        savefile.writelines(self.textinfo.get(1.0,END))
        #recipiants email adress
        text_send = open(self.subject_1.get()+".txt", "r")
        tosend = self.textinfo.get(1.0,END)
        #connects to email server
        s = smtplib.SMTP()
        s.connect(self.email_server, 587)
        s.ehlo()
        s.starttls()
        #login to email
        s.login(self.username.get(), self.password.get())
        s.ehlo()
        #creates email
        toaddr = self.recipient.get()
        fromaddr = self.username.get()
        message = 'Subject: %s\n\n%s' % (self.subject_1.get(), tosend)
        #sens email
        s.sendmail(fromaddr, toaddr, message)
        s.close()

        tkMessageBox.showinfo("Successfully sent email.","You e-mail has been sent to it recipient.")

    def select_mail(self):
        """
        Window to select mail
        Select by text file name
        """
        self.code_cleaner(self.cleannumber)

        self.find_mail_button=Button(self.window, text="Find", width=20,command=self.open_mail)
        #message to tell user where to input email title
        title_label = StringVar()
        title_label.set("Mail Title:")
        self.title_label_l = Label(self.window,textvariable=title_label,height=2)
        #textbox to grab user input
        enter_title = StringVar()
        self.enter_title = Entry(self.window, textvariable = enter_title)
        #inserts text and textboxes to screen
        self.title_label_l.pack(side="top")
        self.enter_title.pack()
        self.find_mail_button.pack(side="bottom",padx=15,pady=15)

        self.cleannumber=3

    def code_cleaner(self, number):
        """
        Clears screen before refreshing it
        """
        if self.cleannumber==1:
            self.label1.pack_forget()
            self.label2.pack_forget()
            self.label3.pack_forget()
            self.enter_username.pack_forget()
            self.enter_password.pack_forget()
            self.buttonL.pack_forget()
            self.button_gmail.pack_forget()
            self.button_yahoo.pack_forget()
            self.button_hotmail.pack_forget()
        if self.cleannumber==2:
            self.recipientlabel.pack_forget()
            self.enter_recipient.pack_forget()
            self.subject_label_l.pack_forget()
            self.enter_subject.pack_forget()
            self.textinfo.pack_forget()
            self.send_button.pack_forget()
        if self.cleannumber==3:
            self.title_label_l.pack_forget()
            self.enter_title.pack_forget()
            self.find_mail_button.pack_forget()
        if self.cleannumber==4:
            self.text_screen.pack_forget()
        if self.cleannumber==5:
            self.title_label_l.pack_forget()
            self.enter_title.pack_forget()
            self.find_delete.pack_forget()

Emailclient()
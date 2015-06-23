from Tkinter import *
from ttk import Button, Combobox
from PIL import Image, ImageTk
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import localtime, strftime
import smtplib
import win32com.client

class Window(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent, background = "grey")
            self.parent = parent
            self.centerWindow()
            self.initUI()
            self.output = ""

        def initUI(self):
            img = Image.open("welcomepage.jpg")
            img = img.resize((250, 450), Image.ANTIALIAS)
            WelcomeImage = ImageTk.PhotoImage(img)

            self.label1 = Label(self, image=WelcomeImage)
            self.label1.image = WelcomeImage
            self.label1.place (x = 10, y = 10)
            
            self.To = Entry(self)
            self.To.place(x = 300, y = 10)

            self.box_value = StringVar()
            self.box = Combobox(self, textvariable=self.box_value, state='readonly')
            self.box['values'] = ('Dad', 'Mom')
            self.box.current(0)
            self.box.place(x = 300, y = 35)

            lb = Listbox(self)
            lb.place(x = 300, y = 65)
            lb.bind("<<ListboxSelect>>", self.onSelect)

            with  open("recentEmails.txt", "r") as f:
                for line in f:
                    lb.insert(END, line)

            ScanButton = Button(self, text = "Scan Image", command = self.ScanClick)
            ScanButton.place (x = 275, y = 250)

            EmailButton = Button(self, text = "Email Bill", command = self.EmailClick)
            EmailButton.place(x = 375, y = 250)

        def centerWindow(self):
            self.parent.title("Bill Sender")
            self.pack(fill = BOTH, expand = 1)
            w = 500
            h = 500

            sw = self.parent.winfo_screenwidth()
            sh = self.parent.winfo_screenheight()

            x = (sw - w) / 2
            y = (sh - h) / 2
            self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        def ScanClick(self):
            wia = win32com.client.Dispatch("WIA.CommonDialog")
            img = wia.ShowAcquireImage(0,0,65536,"{B96B3CAE-0728-11D3-9D7B-0000F81EF32E}")

            fname = strftime("%I%M%S", localtime())
            self.output = fname + ".pdf"
            fname = fname + ".jpg"
            img.SaveFile(fname)

            ScanImg = Image.open(fname)
            ScanImg = ScanImg.resize((250, 450), Image.ANTIALIAS)
            ChangeImage = ImageTk.PhotoImage(ScanImg)

            self.label1.configure(image = ChangeImage)
            self.label1.image = ChangeImage

            ScanImg.save(self.output, "PDF", resolution = 100.0)

        def EmailClick(self):
            if self.box.get() == 'Dad':
                From = 'jprucool@gmail.com'
                UserName = 'jprucool@gmail.com'
                Password = 'pwd'
                Sub = 'Traditional Mechanical Service Invoice'
                Text = 'Please find invoice attached.'
            else:
                From = '4krealty@gmail.com'
                UserName = '4krealty@gmail.com'
                Password = 'pwd'
                Sub = '4k Realty Documents'
                Text = 'Please find attached files.'
                            
            To = self.To.get()
            
            if not To:
                return

            msg = MIMEMultipart()
            msg['Subject'] = Sub
            msg['From'] = From
            msg['To'] = To

            fp = open(self.output, 'rb')
            pdf = MIMEApplication(fp.read(), _subtype="pdf")
            fp.close()
            pdf.add_header('Content-Disposition', 'attachment', filename = self.output)

            msg.attach(pdf)

            Server = smtplib.SMTP('smtp.gmail.com:587')
            Server.ehlo()
            Server.starttls()
            Server.login(UserName, Password)
            Server.sendmail(From, To, msg.as_string())
            Server.quit()
            
        def onSelect(self, val):
            sender = val.widget
            idx = sender.curselection()
            value = sender.get(idx)
            self.To.delete(0, END)
            self.To.insert(0, value)

def main():

    root = Tk()
    root.resizable(0,0)
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()

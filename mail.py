import smtplib
def email_sending():
    try:
        emailid=input("enter the email id")
        f=open("bill.txt","a")
        f.write(f"\n{emailid}\n")
        message=(f.read("bill.txt"))
        s=smtplib.SMTP('SMTP.gmail.com',587)
        s.starttls()
        s.login("rasipriya959@gmail.com")
        s.sendmail("rasipriya959@gmail.com",message)
        s.quit()
        print("mail sent successfully")
    except:
        print("mail not sent")
email_sending()
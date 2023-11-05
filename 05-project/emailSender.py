import smtplib

recipentEmail = str(input("Enter the email of recipent: "))
recipentContent = str(input("Enter the email of content: "))

def sendEmail(recipentEmail, recipentContent):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehio()
    server.starttls()
    server.login('abdighanimd02@gmail.com', 'password')
    server.sendmail('abdighanimd02@gmail.com', recipentEmail, recipentContent)
    server.close()
    
sendEmail(recipentEmail, recipentContent) 
from email import message
import smtplib

my_address_mail = '***'



mailFrom = 'Your automation system'
mailTo = my_address_mail

mailSubject = 'Processing finished successfully'
mailBody = '''Hello

This mail confirms that processing has finished without problems,

Have a nice day'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = my_address_mail
password = '***'


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print("mail send, ok")

except Exception as e:
    print(e)

except:
    print('error sending email, not ok :( ')

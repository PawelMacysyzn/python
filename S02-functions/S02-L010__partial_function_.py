from email import message
import smtplib
import functools

my_address_mail = '*********************'
user = my_address_mail
password = '*************************'

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

def SendInfoMail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = '''From: {}
    Subject: {}

    {}
    '''.format(mailFrom, mailSubject, mailBody)

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


SendInfoEmailFromGmail = functools.partial(SendInfoMail, user, password, mailSubject = 'Execution alert')

SendInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailSubject = mailSubject, mailBody = mailBody)

# SendInfoMail(user, password, mailFrom, mailTo, mailSubject, mailBody)
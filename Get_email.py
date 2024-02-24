from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from email.header import Header

def get_email(receiver, content):
    host_server = '' #your email host,  example   smtp.gmail.com
    sender = '' # your email address
    pwd = '' # your email password
    receiver = receiver
    mail_title = 'llm助理发送的邮件' #email title
    mail_content = content #email content
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['To'] = receiver
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = SMTP(host_server, timeout=30, port='587')
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        message = '发送成功'
    except Exception as e:
        message = '发送失败' + e
    return message

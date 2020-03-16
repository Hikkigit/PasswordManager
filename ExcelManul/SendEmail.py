import smtplib #发送邮件库
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendemail(message):
    username='a1179712582@163.com'
    password='ZKTJCPGBXOWJMYWJ' #授权码
    sender = 'a1179712582@163.com'
    receiver = ('909855338@qq.com','1179712582@qq.com')

    Subject='python test'

    msg = MIMEMultipart('mixed')
    msg['Subject'] = Subject
    msg['From'] = sender
    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver)
    # msg['Date']='2012-3-16'
    text='Hello!\nThis is a remender email！\n'+message+'\nHave a nice day!'
    text_content=MIMEText(text,'plain','utf-8')
    msg.attach(text_content)

    html = """
    <html>  
      <head></head>  
      <body>  
        <p>Hi!<br>  
           How are you?<br>  
           Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
        </p> 
      </body>  
    </html>  
    """
    text_html = MIMEText(html, 'html', 'utf-8')
    text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
    msg.attach(text_html)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)
    smtp.login(username, password)

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功！")

    return
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_email(sent_str):
    msg_from = '748773880@qq.com'  # 发送方邮箱
    passwd = 'keffrbfnmokvbdii'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
    msg_to = ['748773880@qq.com']  # 收件人邮箱
    # msg_to = '616564099@qq.com'  # 收件人邮箱

    subject = "组合交易提醒"  # 主题
    content = sent_str
    # 生成一个MIMEText对象（还有一些其它参数）
    msg = MIMEText(content)
    # 放入邮件主题
    msg['Subject'] = subject
    # 也可以这样传参
    # msg['Subject'] = Header(subject, 'utf-8')
    # 放入发件人
    msg['From'] = msg_from
    # 放入收件人
    # msg['To'] = '616564099@qq.com'
    # msg['To'] = '发给你的邮件啊'
    try:
        # 通过ssl方式发送，服务器地址，端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录到邮箱
        s.login(msg_from, passwd)
        # 发送邮件：发送方，收件方，要发送的消息
        s.sendmail(msg_from, msg_to, msg.as_string())
        print('邮件发送成功')
    except s.SMTPException as e:
        print(e)
    finally:
        s.quit()
    return
import smtplib
from email.mime.text import MIMEText       #专门发送正文
from email.mime.multipart import MIMEMultipart   #发送多个部分
from email.mime.application import MIMEApplication    #发送附件包
#构造一个邮件体：正文，附件
class sendEmail:

    def sen_email(self,email_to,filepath):
        msg=MIMEMultipart()
        msg['Subject']='许寿龙的测试报告'
                    #邮件主题
        msg['From']='576388803@qq.com'
                    #发送人
        msg['To']=email_to
                    #接收人
        #构造邮件
        part_text=MIMEText('hell world #正文内容')
        msg.attach(part_text)
                #把正文加到邮件体里面去

        # 构建邮件附件
        part_attach=MIMEApplication(open(filepath,'rb+').read())
        part_attach.add_header('Content-Disposition','attachment',filename='test_report.html')
                        #格式声明
                        #filename附件的名字
        msg.attach(part_attach)
                        #把附件加到邮件体里面去

        #发送邮件   smtp
        s=smtplib.SMTP_SSL('smtp.qq.com',timeout=30)
                #链接服务
                #查看路径：设置---路径---SMTP服务---IMAP/SMTP服务(开启状态获取登陆授权码码)---设置IMAP服务
                #QQ邮箱需要添加_SSL
                #163邮箱不需要加_SSL

        s.login(user='576388803@qq.com',password='czkydfbkwkqubbfj')
                #登陆邮箱
        s.sendmail(msg['From'],msg['To'],msg.as_string())
                #发送
        s.close()   #关闭

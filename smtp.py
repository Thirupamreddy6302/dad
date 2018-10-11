import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("vadisenays@gmail.com","6302044819")
msg="hello"
s.sendmail("vadisenays@gmail.com","varshapn27@gmail.com",msg)
print('Sent')
s.quit()
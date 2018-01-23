from email.mime.multipart import MIMEMultipart

# Following functions can be used to draft

def Neha(me = "Aasif", HR = "HR_Name", gender = "Sir", company = "Company_Name", phone = "Tinson\r\n+91 9495097727", my_email = "myemail@mec.ac.in", alternate = "myalternate.email@gmail.com", adate = "31st June 2017", link = "https://somelink.com"):
    text = "Hi!\n<b>How are you?</b>\nHere is the link you wanted:\nhttps://www.modelengineering.college"
    html = """\
    <html>
    <head></head>
    <body>
        <p>Dear %(HR_name)s %(sex)s,</p>
        <p>Your Darft for %(comp)s<br></p>
        
        
        Regards,<br>
        <p><b>%(name)s</b><br><br>%(mail)s<br>%(alt)s<br>%(ph)s</p>
    </body>
    </html>
    """% dict(HR_name = HR, sex = gender, comp = company, date = adate, name = me, mail = my_email, alt = alternate, ph = phone)
    return text, html



# If you have some alternate draft for some type of companies specify that draft in the following function Amal using the above example

def Amal(me = "Aasif", HR = "HR_Name", gender="Sir", company = "Company_Name", phone = "Tinson\r\n+91 9495097727", my_email = "you@mec.ac.in", alternate = "you.alt@gmail.com", adate = "31st June 2017", link = "https://somelink.com"):
    text = "Hi!\n<b>How are you?</b>\nHere is the link you wanted:\nhttps://www.modelengineering.college"
    html = """\
 
    return text, html

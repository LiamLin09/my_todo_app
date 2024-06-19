import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = 'kyzohavdyvzgmxyi'
EMAIL_ADDRESS = 'liamlin5609@gmail.com'
RECEIVER = 'liamlin5609@gmail.com'


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!!!"
    email_message.set_content('Hey, we just saw a new customer!!')

    # read the image file in binary mode
    with open(image_path, 'rb') as file:
        content = file.read()
    # attach the image to the email
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    # connect to the gmail SMTP server and send the email
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_ADDRESS, PASSWORD)
    gmail.sendmail(EMAIL_ADDRESS, RECEIVER, email_message.as_string())
    gmail.quit()
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage


def sending_email(date, word, meaning):
    load_dotenv()
    user = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    recipient = os.getenv("MOI")

    plain_content = f'''\
    La palabra de hoy {date[-2:]}/{date[-5:-3]}/{date[:4]} es:\n
    {word.upper()}\n
    {meaning.capitalize()}\n
    Para mas información, Real Academia Española: https://dle.rae.es/{word}\n
    Esta palabra ha sido enviada con ❤️
    '''
    html_content = f'''\
    <!DOCTYPE html>
    <html>
        <body>
            <p>La palabra de hoy {date[-2:]}/{date[-5:-3]}/{date[:4]} es 📖📖📖📜📜📜📜📜</p>
            <h3 style="color: #2e6c80;">{word.upper()}</h3>
            <p>{meaning.capitalize()}</p>
            <p><br/>Para mas informaci&oacute;n:&nbsp;<a href="https://dle.rae.es/{word}" 
            target="_blank">https://dle.rae.es/{word}</a><br /><br />Real Academia Espa&ntilde;ola</p>
            <p>Esta palabra ha sido enviada con ❤️</p>
        </body>
    </html>
    '''

    msg = EmailMessage()
    msg["Subject"] = f"Tu palabra de hoy ya está aquí! - {word}"
    msg["From"] = user
    msg["To"] = recipient
    msg.set_content(plain_content)
    # msg.add_alternative(html_content, subtype='html')

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # setting server and port
    server.login(user, password)  # login to the account
    server.send_message(msg)  # sending email
    server.quit()  # ending connection
    print(f"Message sent to the following recipients: {recipient}")




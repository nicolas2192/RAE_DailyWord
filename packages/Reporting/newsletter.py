from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
import csv


def make_recipients_csv(rp_path: str):
    """
    :param rp_path: recipient.csv path. Here will be place the file with all recipients.
    :return: Creates the file with its header and two examples. Then it exits the script.
    """
    with open(rp_path, "w") as new_file:
        data_csv = [["Recipient"], ["new_recipient1@example.com"], ["new_recipient2@example.com"]]
        csv_writer = csv.writer(new_file)
        for line in data_csv:
            csv_writer.writerow(line)

        print(f"New recipients.csv file was added at the following path: {rp_path}\n"
              f"Please, add some recipients before running the main.py script again.")
        quit()


def recipients_list(rp_path: str):
    """
    :param rp_path: recipients.csv file
    :return: a list comprising all recipients in the recipients.csv file [rep, rep2, rep3 ...]
    """
    # if recipients.csv file does not exist, it will be created.
    if not os.path.exists(rp_path):
        make_recipients_csv(rp_path)
    else:
        with open(rp_path, "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            rp_list = [line[0] for line in csv_reader]
            f.close()
            # Checking if generic recipients.csv file was updated with true addresses
            if rp_list[0] == "new_recipient1@example.com":
                print("Please, update recipients.csv file with real addresses before running the script again.\n"
                      "Daily word was not sent.")
                quit()
            else:
                return rp_list


def sending_email(date, word, meaning, rp_csv):
    """
    :param date: Today's date, format: YYYY-MM-DD
    :param word: Daily word. one string word.
    :param meaning: Long string comprising whole meaning of the word.
    :param rp_csv: recipients.csv file path
    :return: Sends word and meaning to all email addresses in recipients.csv file
    """
    load_dotenv()
    user = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    # recipients = os.getenv("MOI")
    recipients = ", ".join(recipients_list(rp_csv))

    plain_content = f'''\
    La palabra de hoy {date[-2:]}/{date[-5:-3]}/{date[:4]} es:\n
    {word.upper()}\n
    {meaning.capitalize()}\n
    Para mas información, Real Academia Española: https://dle.rae.es/{word}\n\n

    Sent with ❤️ by Nico
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
    msg["To"] = "vendermercadolibrenico@gmail.com"
    msg["Bcc"] = recipients
    msg.set_content(plain_content)
    # msg.add_alternative(html_content, subtype='html')

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # setting server and port
    server.login(user, password)  # login to the account
    server.send_message(msg)  # sending email
    server.quit()  # ending connection
    print(f"Message sent to the following recipients: {recipients}")

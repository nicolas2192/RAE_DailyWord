import packages.Acquisition.scraper as aq
import packages.Acquisition.argparser as ap
import packages.Analyzing.analysis as an
import packages.Reporting.newsletter as nl
import os
from dotenv import load_dotenv


def main(rae_url: str = "https://dle.rae.es/",
         update_file: bool = True, csv_file="data/words.csv",
         send_email: bool = True, rp_csv="data/recipients.csv"):
    """
    :param rae_url: RAE url, https://dle.rae.es/
    :param update_file: True by default, adds new word to csv file. Parameter customizable from terminal
    :param csv_file: CSV file path where previous words are saved. Parameter customizable from terminal
    :param send_email: True by default, sends the word and its meaning by email. Parameter customizable from terminal
    :param rp_csv: recipients.csv file path. Parameter customizable from terminal
    :return: Scrapes RAE webpage, saves new word into a csv and sends it by email.
    """
    # Argparse
    args = ap.terminal_parser()

    # Acquisition
    word = aq.get_word(rae_url)
    meaning = aq.get_meaning(word)
    print(meaning)

    # Analyzing - Generating CSV file
    today = an.get_date()
    an.update_csv(today, word, meaning, csv_path=args.words_csv, update=ap.str2bool(args.update))

    # Reporting - Sending email
    load_dotenv()
    user = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    nl.sending_email(user, password, today, word, meaning, rp_csv=args.recps_csv, send_email=ap.str2bool(args.send))

# todo improve html email format
# todo put plain and html message apart. own function
# todo write readme file


if __name__ == "__main__":
    main()

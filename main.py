import packages.Acquisition.scraper as aq
import packages.Acquisition.argparser as ap
import packages.Analyzing.analysis as an
import packages.Reporting.newsletter as nl
import os
from dotenv import load_dotenv


def main(rae_url: str = "https://dle.rae.es/"):
    """
    :param rae_url: RAE url, https://dle.rae.es/
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
    if ap.str2bool(args.update):
        an.update_csv(today, word, meaning, csv_path=args.words_csv)
    else:
        print(f"update parameter 'update' was set as False. No changes were made to words.csv.")

    # Reporting - Sending email
    if ap.str2bool(args.send):
        load_dotenv()
        user = os.getenv("EMAIL")  # change this to your own email if there is not .env file
        password = os.getenv("PASSWORD")  # change this to your email password if there is not .env file
        nl.sending_email(user, password, today, word, meaning, rp_csv=args.recps_csv)
    else:
        print("send email parameter 'send' was set as False. Nothing was sent.")


if __name__ == "__main__":
    main()

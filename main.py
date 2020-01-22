import packages.WebScraping.scraper as ws
import packages.Analyzing.analysis as an
import packages.Reporting.newsletter as nl


def main(rae_url: str = "https://dle.rae.es/",
         update_file: bool = True, csv_file="data/words.csv",
         send_email: bool = True, rp_csv="data/recipients.csv"):
    """
    :param rae_url: RAE url, https://dle.rae.es/
    :param update_file: True by default, adds new word to csv file
    :param csv_file: CSV file path where previous words are saved
    :param send_email: True by default, sends the word and its meaning by email
    :param rp_csv: recipients.csv file path
    :return:
    """
    # WebScraping
    word = ws.get_word(rae_url)
    meaning = ws.get_meaning(word)
    print(meaning)

    # Analyzing - Generating CSV file
    today = an.get_date()
    if update_file:
        an.update_csv(today, word, meaning, csv_file, update=True)

    # Reporting - Sending email
    if send_email:
        nl.sending_email(today, word, meaning, rp_csv)


# todo # todo def create_csv(csv_path) in analysis if there is no words.csv file
# todo improve html email format
# todo put plain and html message apart. own function
# todo write readme file


if __name__ == "__main__":
    main()

import packages.WebScraping.scraper as ws
import packages.Analyzing.analysis as an
import packages.Reporting.newsletter as nl


def main(rae_url: str = "https://dle.rae.es/", csv_file="data/words.csv", send_email: bool = True):
    """
    :param rae_url: RAE url, https://dle.rae.es/
    :param csv_file: CSV file path where previous words are saved
    :param send_email: True by default, sends the word and its meaning by email
    :return:
    """
    # WebScraping
    word = ws.get_word(rae_url)
    meaning = ws.get_meaning(word)
    print(meaning)

    # Analyzing - Generating CSV file
    today = an.get_date()
    an.update_csv(today, word, meaning, csv_file, update=True)

    # Reporting - Sending email
    if send_email:
        nl.sending_email(today, word, meaning)

# todo create csv with recipients
# todo # todo def create_csv(csv_path) in analysis if there is no words.csv file
# todo # improve sending, add more than one recipient
# todo improve meaning variable, improve html email format
# todo put plain and html message apart. own function
# todo add requirements file
# todo write readme file

if __name__ == "__main__":
    main()

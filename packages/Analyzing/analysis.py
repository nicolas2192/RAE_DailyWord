import datetime
import pandas as pd
import os
import csv


def make_words_csv(csv_path: str):
    '''
    :param csv_path: words file, here will be saved all daily words.
    :return: Creates the file with its headers.
    '''
    with open(csv_path, "w") as new_file:
        data_csv = [["Date", "Word", "Meaning"]]
        csv_writer = csv.writer(new_file)
        for line in data_csv:
            csv_writer.writerow(line)

        print(f"New recipients.csv file was added at the following path: {csv_path}\n")
        quit()


def get_date():
    """
    :return: returns today's date in string format YYYY-MM-DD
    """
    today = datetime.date.today().strftime('%Y-%m-%d')
    return today


def update_csv(date, word, meaning, csv_path: str, update=True):
    """
    :param date: Today's date in string format YYYY-MM-DD
    :param word: Featured RAE word
    :param meaning: Featured word's definition
    :param csv_path: Path as string. CSV file storing all previous words
    :param update: True by default, updates CSV file.
    :return: updates words.csv file
    """

    # if words.csv file does not exist, it will be created.
    if not os.path.exists(csv_path):
        make_words_csv(csv_path)
    else:
        # Opens CSV file
        words_df = pd.read_csv(csv_path)

        # Temporary dataframe
        cols = words_df.columns.tolist()
        to_add = pd.DataFrame(data=[[date, word, meaning]], columns=cols)

        # Adding new word if yesterday and today's date don't match
        if words_df.iloc[len(words_df) - 1, 0] != date or words_df.iloc[len(words_df) - 1, 1] != word:
            words = words_df.append(to_add, ignore_index=True)
            words.to_csv(csv_path, index=False)
            print(f"CSV file updated, new word: {word}")
        else:
            print("Word already on file. No changes were made.")

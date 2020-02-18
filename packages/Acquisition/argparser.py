import argparse


def terminal_parser():
	parser = argparse.ArgumentParser(description="Sends today's RAE daily word to all emails in recipients.csv")
	parser.add_argument("-u", "--update", type=str, metavar="",
						default=True, help="If yes, saves word data into a csv file. Default: yes")
	parser.add_argument("-w", "--words_csv", type=str, metavar="",
						default="data/words.csv", help="File where words are saved. Default: data/words.csv")
	parser.add_argument("-s", "--send", type=str, metavar="",
						default=False, help="If yes, sends word by email. Default: no")
	parser.add_argument("-r", "--recps_csv", type=str, metavar="",
						default="data/recipients.csv", help="File with email recipients. Default: data/recipients.csv")
	return parser.parse_args()


def str2bool(val):
	if isinstance(val, bool):
		return val
	if val.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif val.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')

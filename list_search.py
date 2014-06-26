import argparse
from fuzzywuzzy import process

parser = argparse.ArgumentParser(description='Search for matches in two lists')
parser.add_argument('first_file', type=argparse.FileType('r'), nargs=1, help='First file to search')
parser.add_argument('second_file', type=argparse.FileType('r'), nargs=1, help='Second file to search')
parser.add_argument('-t', '--threshold', type=int, default=90)
args = parser.parse_args()

first_file = args.first_file[0]
second_file = args.second_file[0]
threshold = args.threshold

all_second = [line.rstrip('\n').upper() for line in second_file.readlines()]
for line in first_file.readlines():
	name = line.rstrip('\n').upper()
	results = [(score, match) for (match, score) in process.extract(name, all_second) if score >= threshold]
	if len(results) > 0:
		print("Found matches for %s" % name)
		for (score, name) in results:
			print("- %s (%d)" % (name, score))

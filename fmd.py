import argparse

parser = argparse.ArgumentParser(description='Give the files some meaning.')

parser.add_argument('-i', '--init', action='store_true', help='Initialise a File MetaData Repository')
parser.add_argument('-a', '--addtag', metavar='tagName', nargs='+', help='Add tags to the File MetaData Repository')

args = parser.parse_args()

if (args.init):
	from initialiser import init
	init()
elif (args.addtag):
	from tagAdder import addTag
	for tag in args.addtag:
		addTag(tag)

import sys
import html

path = sys.argv[1]
delim = sys.argv[2]

with open(path, 'r', errors = 'ignore') as infile:
	# Skip the headers
	infile.readline()
	with open(path + '.tidy', 'w') as outfile:
		for line in infile:
			# Remove special encodings (HTML escapes) from the datasets
			# and replace quoted fields
			line = html.unescape(line)
			line = line.replace('"', '')
			outfile.write(line)

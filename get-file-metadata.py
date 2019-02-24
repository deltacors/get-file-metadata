#!/usr/bin/python

import PyPDF2
import optparse

def printMetaData(file):
	pdf = open(file, 'rb')
	pdfObject = PyPDF2.PdfFileReader(pdf)
	info = pdfObject.getDocumentInfo()
	print('[*] document info for file ' + str(file))
	for i in info:
		print('[+] ' + i + ': ' + info[i])
		
def main():
	parser = optparse.OptionParser('usage %prog -F <PDF file name>')
	parser.add_option('-F', dest='file', type='string', help='specify PDF file name')
	(options, args) = parser.parse_args()
	file = options.file 
	if file == None:
		print(parser.usage)
		exit(0)
	else:
		printMetaData(file)

if __name__ == '__main__':
	main()
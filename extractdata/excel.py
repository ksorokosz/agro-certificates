import xlsxwriter
import sys, codecs, os

def main(filepath):

	# Create an new Excel file and add a worksheet.
	workbook = xlsxwriter.Workbook(filepath)
	worksheet = workbook.add_worksheet('data')

	# Add a bold format to use to highlight cells.
	header = workbook.add_format({'bold': True})
	normal = workbook.add_format({})

	sys.stdin = codecs.getreader('utf-8')(sys.stdin)
	for row, line in enumerate(sys.stdin):
		line = line.strip(os.linesep)
		columns = line.split("\t")
		for col, column in enumerate(columns):
			worksheet.write(row, col, column, normal)
	
	workbook.close()

if __name__ == "__main__":
	main("cobico.xlsx")
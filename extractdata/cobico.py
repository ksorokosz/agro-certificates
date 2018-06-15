import sys, time
import io, os, re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

# Convert PDF
# http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library
# https://github.com/timClicks/slate/issues/5
def convert_pdf(path):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	fp = file(path, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0
	caching = True
	pagenos=set()

	for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		interpreter.process_page(page)
	
	text = retstr.getvalue()

	fp.close()
	device.close()
	retstr.close()
	return text

def cobico():

	# For each pdf file
	for line in sys.stdin:
		
		line = line.strip()
		(name, url, pdffile) = line.split("\t"); # name for validation
		
		text = convert_pdf( pdffile )
		pdflines = iter(text.splitlines())
		
		name_address_field = "THE NAME AND ADDRESS OF THE PRODUCER";
		validity_field = "CERTIFICATE VALIDITY"
		products_field = ";"
		extracted_name, extracted_address, extracted_validity = "", [], []
		extracted_products = []
		name_start, address_start, validity_start  = 0, 0, 0
		for index, pdfline in enumerate(pdflines):
			
			pdfline = pdfline.strip("\n")
			# Address has 2 pieces
			if address_start == 1 or address_start == 2: 
				if pdfline:
					extracted_address.append(" ".join(pdfline.split()))
					address_start = address_start + 1
			
			# Read name (next will be address)
			if name_start == 1:
				if pdfline:
					extracted_name = " ".join(pdfline.split())
					name_start = name_start + 1
					address_start = 1
					
			if name_address_field in pdfline:
				name_start = 1
			
			# Read validity from and to (2 dates)
			if validity_start == 1 or validity_start == 2:
				if pdfline:
					p = re.compile('\d\d\d\d-\d\d-\d\d')
					if p.match(pdfline): # only dates
						extracted_validity.append(pdfline)
						validity_start = validity_start + 1
			
			if validity_field in pdfline:
				validity_start = 1	
						
			# Read products directly (the same line)
			if products_field in pdfline:
				
				items = pdfline.split(";")
				for item in items:
					p = re.compile("\d") # get number of item
					m = p.search(item)
					if m:
						product = item[:m.start()].strip()
						count = item[m.start():].strip()
					
					extracted_products.append({'product': product, 'count': count})
					
		for item in extracted_products:
			(name, surname) = extracted_name.rsplit(" ", 1);
			cert_id = os.path.splitext(os.path.basename(pdffile))[0];
			print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (name, surname, " ".join(extracted_address), "cobico", cert_id, 
                                                              extracted_validity[0], extracted_validity[1], item['product'], item['count']))

if __name__ == "__main__":
	cobico()
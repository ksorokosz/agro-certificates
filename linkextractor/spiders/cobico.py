import scrapy
from items import LinkExtractorItem
from tqdm import tqdm
import requests, os, codecs

class CobicoSpider(scrapy.Spider):
	name = "cobico"
	allowed_domains = ["cobico.pl"]
	start_urls = [
		"http://www.cobico.pl/Biuro_Certyfikacji/Certyfikaty/?CertificatesSearchForm=process&name=&number=&province=0&province_name=wybierz&certification_system=0&certification_system_name=wybierz",
	]

	def download_certificate(self, url, outputfile):
			
		response = requests.get(url, stream=True)

		with open(outputfile, "wb") as handle:
			for data in tqdm(response.iter_content()):
				handle.write(data)

	def parse(self, response):
		for subpage in response.xpath("//div[@class='cert_pages']/a[@class='paginator']/@href"):
			url = response.urljoin(subpage.extract())
			yield scrapy.Request(url, callback=self.parse_contents)

	def parse_contents(self, response):
		for certificates in response.xpath("//div[@id='certificates_search_results']"):
			item = LinkExtractorItem()
			hrefs = certificates.xpath("a[@class='certificate']/@href").extract()	
			names = certificates.xpath("table[@class='certificate_table']/tr/td[1]/text()").extract()
			for href, name in zip(hrefs, names):
				url = response.urljoin(href)
				filename = os.path.basename(url)
				outputdirectory = "certificates/cobico"
				if not os.path.exists(outputdirectory):
					os.makedirs(outputdirectory)
				outputfile = outputdirectory + "/" + filename
				item['name'], item['url'] = name, url
				
				# Only those files that not exists (are totally new)
				if not os.path.isfile(outputfile):
					self.download_certificate(url, outputfile)

					with codecs.open("certificates/cobico.tsv", "a", "utf-8") as file:

						file.write(name + "\t" + url + "\t" + outputfile + os.linesep)




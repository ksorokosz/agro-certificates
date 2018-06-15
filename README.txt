Instalacja:

pyinstaller -F download.py
 --hidden-import scrapy.spiderloader --hidden-import scrapy.statscollectors --hi
dden-import scrapy.logformatter --hidden-import scrapy.extensions.closespider --
hidden-import scrapy.extensions.memdebug --hidden-import scrapy.extensions.feede
xport --hidden-import scrapy.extensions.memusage --hidden-import scrapy.extensio
ns.logstats --hidden-import scrapy.extensions.telnet --hidden-import scrapy.exte
nsions.corestats --hidden-import scrapy.extensions.spiderstate --hidden-import s
crapy.extensions.throttle --hidden-import queue --hidden-import scrapy.core.sche
duler --hidden-import scrapy.core.downloader --hidden-import scrapy.downloadermi
ddlewares.robotstxt --hidden-import scrapy.downloadermiddlewares.httpauth --hidd
en-import scrapy.downloadermiddlewares.downloadtimeout --hidden-import scrapy.do
wnloadermiddlewares.defaultheaders --hidden-import scrapy.downloadermiddlewares.
useragent --hidden-import scrapy.downloadermiddlewares.retry --hidden-import scr
apy.downloadermiddlewares.ajaxcrawl --hidden-import scrapy.downloadermiddlewares
.redirect --hidden-import scrapy.downloadermiddlewares.httpcompression --hidden-
import scrapy.downloadermiddlewares.cookies --hidden-import scrapy.downloadermid
dlewares.httpproxy --hidden-import scrapy.downloadermiddlewares.chunked --hidden
-import scrapy.downloadermiddlewares.stats --hidden-import scrapy.downloadermidd
lewares.httpcache --hidden-import scrapy.spidermiddlewares.httperror --hidden-im
port scrapy.spidermiddlewares.offsite --hidden-import scrapy.spidermiddlewares.r
eferer --hidden-import scrapy.spidermiddlewares.urllength --hidden-import scrapy
.spidermiddlewares.depth --hidden-import scrapy.pipelines --hidden-import scrapy
.dupefilters --hidden-import scrapy.squeues --hidden-import queuelib --hidden-im
port scrapy.core.downloader.handlers.http --hidden-import scrapy.core.downloader.contextfactory


- uruchomiæ skrypt install.bat jako administrator

Uruchomienie:

1) Aby ¶ci±gn±æ certyfikaty cobico (zaktualizowaæ) nale¿y uruchomiæ aplikacjê download.exe
   Certyfikaty zostan± ¶ci±gniête do certificates/cobico

   ¶ci±ganie certyfikatów mo¿na przerwaæ wy³±czaj±c okno aplikacji. 

2) Aby stworzyæ plik XLSX z danymi z certyfikatów w formacie:
   Imiê | Nazwisko | Adres | Jednostka | Numer Certyfikatu | Data przyznania | Data wa¿no¶ci | Produkt | Ilo¶æ

   Uruchomiæ skrypt: extractdata.bat

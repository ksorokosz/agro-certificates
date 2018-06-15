# -*- mode: python -*-

block_cipher = None


a = Analysis(['download.py'],
             pathex=['C:\\Users\\Kamil\\Desktop\\agrocertificates\\linkextractor'],
             binaries=None,
             datas=None,
             hiddenimports=['scrapy.spiderloader', 'scrapy.statscollectors', 'scrapy.logformatter', 'scrapy.extensions.closespider', 'scrapy.extensions.memdebug', 'scrapy.extensions.feedexport', 'scrapy.extensions.memusage', 'scrapy.extensions.logstats', 'scrapy.extensions.telnet', 'scrapy.extensions.corestats', 'scrapy.extensions.spiderstate', 'scrapy.extensions.throttle', 'queue', 'scrapy.core.scheduler', 'scrapy.core.downloader', 'scrapy.downloadermiddlewares.robotstxt', 'scrapy.downloadermiddlewares.httpauth', 'scrapy.downloadermiddlewares.downloadtimeout', 'scrapy.downloadermiddlewares.defaultheaders', 'scrapy.downloadermiddlewares.useragent', 'scrapy.downloadermiddlewares.retry', 'scrapy.downloadermiddlewares.ajaxcrawl', 'scrapy.downloadermiddlewares.redirect', 'scrapy.downloadermiddlewares.httpcompression', 'scrapy.downloadermiddlewares.cookies', 'scrapy.downloadermiddlewares.httpproxy', 'scrapy.downloadermiddlewares.chunked', 'scrapy.downloadermiddlewares.stats', 'scrapy.downloadermiddlewares.httpcache', 'scrapy.spidermiddlewares.httperror', 'scrapy.spidermiddlewares.offsite', 'scrapy.spidermiddlewares.referer', 'scrapy.spidermiddlewares.urllength', 'scrapy.spidermiddlewares.depth', 'scrapy.pipelines', 'scrapy.dupefilters', 'scrapy.squeues', 'queuelib', 'scrapy.core.downloader.handlers.http', 'scrapy.core.downloader.contextfactory'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='download',
          debug=False,
          strip=False,
          upx=True,
          console=True )

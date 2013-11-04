#/usr/bin/env python
import os
import sys
import re
import lxml.html
import csv
from urllib2 import urlopen,HTTPError,URLError
from urlparse import urljoin,urlparse
#this helps take care of annoying encoding errors. Not sure how proper it is, but whatever.
reload(sys)
sys.setdefaultencoding('utf-8')
#sets some file path stuff.
path= os.path.dirname(__file__)
os.chdir(path)
file = open('ratings.txt','w')



ratingPage = urlopen('http://www.imdb.com/title/tt0804503/eprate?ref_=ttep_ql_3')
html = ratingPage.read()
xpathable = lxml.html.document_fromstring(html)
counter = 0
episodeNames = {}
episodeMetrics = []

episodeNumber = re.compile('[123456]\.[\d]{1,2}')
episodeRating = re.compile('[789]\.[\d]')
episodeTitle = re.compile('[A-Z][\w]+')

for episodeName in xpathable.xpath('//td/a/text()'):
	episodeNames[episodeName] = []
for item in xpathable.xpath('//tr/td//text()'):
	if episodeNumber.search(item):
		episodeMetrics.append(item[0:-1])
	if episodeRating.search(item) and episodeMetrics[-1] != item:
		episodeMetrics.append(item)
	if episodeTitle.search(item):
		episodeMetrics.append(item)
	
print episodeMetrics
print len(episodeNames)
# class lxmlspider():
	# viewedQueue = []
	# instQueue = []
	# printQueue = []
	
	# def getNextLink(self):
		# if self.instQueue == []:
			# return ''
		# else:
			# return self.instQueue.pop(0)
	# def loadUrl(self,path=''):
		# try:
				# page = urlopen(urljoin(url,path))
				# html = page.read()
			# return lxml.html.document_fromstring(html)
			# time.sleep(10)
		# except HTTPError,e:
			# print str(e.code),url,path
		# except URLError,e:
			# print str(e.reason),url,path
			
			
			
			
			
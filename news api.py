import urllib2
import json
datarqst = urllib2.Request('https://newsapi.org/v1/articles?source=techcrunch&apiKey=4887927831a64c9fbff993fe5909cb2d')
data = urllib2.urlopen(datarqst)
nws = json.loads(data.read())
#print nws
num = len(nws["articles"])
for i in range(0,num-1):
	print nws['articles'][i]['description']
	print "\n"


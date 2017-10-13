from urllib.request import urlopen

def getSrc(url, enc='utf-8'):
	f = urlopen(url)
	b = f.read().decode(enc)
	return b

#! /usr/bin/env python
import urllib2
import ConfigParser
import os

def download(url):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)
	
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break
	
	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,
	
	f.close()
	return file_size_dl, file_name

class Target:
	url = ""
	author = ""
	authorurl = ""
	name = ""
	date = ""
	desc = ""
	filesize = ""
	filename = ""
	valid_metadata = False
	def fillmetadata(urlpath):
		filesize, fn = download(urlpath)
		cfg = ConfigParser.ConfigParser()
		try:
			cfg.read(fn)
		except:
			print "unable to read metadata file"
			return		

		try:
			url = cfg.get("package", "url")
			author = cfg.get("package", "author")
			name = cfg.get("package", "name")
			authorurl = cfg.get("package", "author url")
			date = cfg.get("package", "date")
			filesize = cfg.get("package", "filesize")
			filename = cfg.get("package", "file name")
			desc = cfg.get("package", "description")
			valid_metadata = True
		except:
			print "unable to parse metadata file"
			return
		os.remove(fn)

def readPackageLists(url):
	filesize, fn = download(urlpath)
	pkglist = open(fn,"r")
	print "reading package directory contents\n"
	Target target
	for pkg in pkglist:
		target.fillmetadata(pkg)
		print "

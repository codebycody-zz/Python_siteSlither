import urllib.request
import os
url_page = input('Select your web page: ')
domain_name = url_page.partition('.')[0]
#! Needs a better way to check for http || https
if 'https://' not in url_page : url_page = 'https://%s' % url_page

req = urllib.request.Request(url_page)
response = urllib.request.urlopen(req)
the_page = response.read()
if not os.path.exists(domain_name):
	os.makedirs(domain_name)

#in the next round need to check the file name that browser gives.
output = open(domain_name + '\\' + 'index' + '.html','wb')
output.write(the_page)
output.close()


#needs to be made into a loop so it can be used for style and script tags
if not os.path.exists(domain_name + '\\' + 'css'):
	os.makedirs(domain_name + '\\' + 'css')

#in the next round need to check the file name that browser gives.
output = open(domain_name + '\\' + 'css' + '\\' + 'main' + '.css','wb')
output.write(the_page)
output.close()

#I really need to update this project!
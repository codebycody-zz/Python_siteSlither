import urllib.request
import os
url_page = input('Select your web page: ')
if 'https://' not in url_page : url_page = 'https://%s' % url_page
req = urllib.request.Request(url_page)
response = urllib.request.urlopen(req)
the_page = response.read()
domain_name = url_page.split('.')
domain_name = domain_name[0].split('https://')
if not os.path.exists(domain_name[1]):
    os.makedirs(domain_name[1])
output = open(domain_name[1] + '\\' + domain_name[1] + '.html','wb')
output.write(the_page)
output.close()
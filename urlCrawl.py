import urllib.request
url_page = input('Select your web page: ')
if 'https://' not in url_page : url_page = 'https://%s' % url_page
req = urllib.request.Request(url_page)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)
import urllib.request
import os
url_page = input('Select your web page: ')
domain_name = url_page.partition('.')[0]
site_folder = 'sites' + '\\' + domain_name
#! Needs a better way to check for http || https
if 'https://' not in url_page : url_page = 'https://%s' % url_page

req = urllib.request.Request(url_page)
response = urllib.request.urlopen(req)
the_page = response.read()


# check for the folder to put all the sites in if it doesn't exist make it
if not os.path.exists('sites'):
    os.makedirs('sites')


if not os.path.exists(site_folder):
	os.makedirs(site_folder)

#in the next round need to check the file name that browser gives.
output = open(site_folder + '\\' + 'index' + '.html','wb')
output.write(the_page)
output.close()


#needs to be made into a loop so it can be used for style and script tags
if not os.path.exists(site_folder + '\\' + 'css'):
	os.makedirs(site_folder + '\\' + 'css')

#in the next round need to check the file name that browser gives.
output = open(site_folder + '\\' + 'css' + '\\' + 'main' + '.css','wb')
output.write(the_page)
output.close()

#I really need to update this project!
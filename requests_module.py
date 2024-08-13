# requests is a module which is used to work with http sites.

import requests

r = requests.get("https://www.w3.org/TR/PNG/iso_8859-1.txt") # This will open the site given.
print(r.text) # This will print the content in the site.
print(r.status_code) # status_code is the code of the status of the site(this point is not much necessary).

# url = "www.some_website.com"
# data = {
#     "parameter1":4,
#     "parameter2":8
# }
# r2 = requests.post(url=url, data=data) # This is used to send data to a site.
# You can also login on a website using this method.

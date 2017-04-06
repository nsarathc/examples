#####
#   Using "requests" module from behind a http(s) proxy.
#
#   See discussion : http://stackoverflow.com/questions/8287628/proxies-with-python-requests-module
#
#   Found to be working with Python 2.7.13
#####

import requests as req

httpProxy = ""		## Specify HTTP proxy(:port)
httpsProxy = ""		## Specify HTTPS proxy(:port)

proxy_dict = {
        'http': httpProxy,
        'https': httpsProxy
}

payload = {
            'indexName': "NIFTY 50",
            'fromDate': "01-01-2015",
            'toDate': "30-12-2015",
            'yield4': "all"
}

resp = req.get("https://www.nseindia.com/products/dynaContent/equities/indices/historical_pepb.jsp",
               params=payload,
               proxies=proxy_dict)

# Prints the URL used in retrieving the resource.
print resp.request.url

# Prints the HTTP response code for the GET.
print resp.status_code

# Prints the actual text contained in the HTML document.
print resp.text

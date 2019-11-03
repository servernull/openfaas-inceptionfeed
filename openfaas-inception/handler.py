import os
import requests
import sys
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    urls = json.loads(req)

    resps = []
    for url in urls:
        try:
            r = requests.get("http://gateway.openfaas:8080/function/inception", data= url)
            if r.status_code != 200:
                resps.append("error with code "+r.status_code)
            else:
                urlObj = {}
                urlObj['url'] =  url
                urlObj['inception'] = json.loads(r.content.decode())
                resps.append(urlObj)
        except Exception as e:
            resps.append(str(e))

    return json.dumps(resps)
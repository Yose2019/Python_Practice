import requests 
from requests.exceptions import HTTPError

response = requests.get("https://github.com/Yose2019/Python_Practice")

if response.status_code == 200:
    print("Server responded successfully")

try:
    response2 = requests.get("https://github.com/Yose2019/Python_Practicing")
    raise response2.raise_for_status()
except HTTPError as http_err:
    print("HTTP error has pccured :",http_err)



    
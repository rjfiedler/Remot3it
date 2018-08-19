import requests, json

def GetProxy():
    APIKey = 'RDhEOTUyMTUtMDZGOC00NEQ5LThBMEYtMkU5NjBCOUFGQzVB'

    url = "https://api.remot3.it/apv/v23.5/user/login"

    payload = "{ \"username\" : \"fiedlerross94@gmail.com\", \"password\" : \"510Rf327!!\" }"
    headers = {
        'developerkey': APIKey,
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.post(url=url, data=payload, headers=headers)
    json_response = response.json()
    token = json_response["token"]

    # gets deviceaddress
    apiMethod = "https://"
    apiServer = "api.remot3.it"
    apiVersion = "/apv/v23.5"
    deviceListURL = apiMethod + apiServer + apiVersion + "/device/list/all"

    deviceHeaders = {
        'Content-Type': "application/json",
        'developerkey': APIKey,
        'token': token,
    }

    resp = requests.get(deviceListURL, headers=deviceHeaders)
    device_list = resp.json()
    Ross_Pi_001 = device_list["devices"][1]["deviceaddress"]

    # connects to RPi
    myip = requests.get('http://ip.42.pl/raw').text
    proxyconnectURL = apiMethod + apiServer + apiVersion + "/device/connect"
    connect_params = {'deviceaddress': Ross_Pi_001, "wait": 1, "hostip": myip}
    json_connect_params = json.dumps(connect_params)
    connection = False
    while not connection:
        connect_resp = requests.post(proxyconnectURL, headers=deviceHeaders, data=json_connect_params)
        connection = connect_resp.json()
    return connection['connection']['proxy']


proxy = GetProxy()
print(proxy)
import requests, json
import subprocess
import sys
import pandas as pd
from requests.structures import CaseInsensitiveDict


token_url = "https://connect2.pointclickcare.com/auth/token"
client_id = '1CUPpmGZ3GgMAitln0s8OhdgicaT2UO3'
client_secret = 'lc5be5JvPj8QJMPX'

data = {'grant_type': 'client_credentials'}

cert_file_path = "C:\certs\Fullchain.pem"
key_file_path  = "C:\certs\privkey.pem"

cert = (cert_file_path, key_file_path)

access_token_response = requests.post(token_url, data=data,cert=cert, auth=(client_id, client_secret))

#print("at:",access_token_response.headers)
#print(access_token_response.text)

tokens = json.loads(access_token_response.text)
#print("access token: ",tokens['access_token'])

call_url = "https://connect2.pointclickcare.com/api/public/preview1/orgs/4b796a12-6a8a-48f0-9457-cd65b42fe79d/allergyintolerances"
#https://connect2.pointclickcare.com/api/public/preview1/orgs/{orgUuid}//{patientId}

#https://connect2.pointclickcare.com/api/public/preview1/orgs/{orgUuid}/conditions
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = 'Bearer ' + tokens['access_token']
payload={"patientId":"57054"}

response = requests.get(call_url,headers=headers,params=payload, verify=False,cert=cert)
p_data = json.loads(response.text)
print("patients details:", p_data)

#facility_data = pd.DataFrame(facility_data['data'])

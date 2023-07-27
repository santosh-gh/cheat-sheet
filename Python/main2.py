import requests
import json
import msal

# Azure AD app credentials
client_id = '933d8a89-8fdb-41cc-b9d2-b7078cd02e2e'
client_secret = 'N0W8Q~CmpAWlghgL3xxTwCPBB1a4wyqIxTKY3cc9'
tenant_id = 'ec3ded2c-750b-415f-b382-96464321f3cf'

# Microsoft Graph API endpoints
graph_endpoint = 'https://graph.microsoft.com/v1.0'
users_endpoint = f'{graph_endpoint}/users'

# Get access token
authority_url = f'https://login.microsoftonline.com/{tenant_id}'
scopes = ['https://graph.microsoft.com/.default']

app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority_url
)

result = app.acquire_token_silent(scopes=scopes, account=None)

if not result:
    result = app.acquire_token_for_client(scopes=scopes)

if 'access_token' in result:
    access_token = result['access_token']

    # Prepare request headers
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Send GET request to list users
    response = requests.get(users_endpoint, headers=headers)
    if response.status_code == 200:
        users = response.json()['value']
        for user in users:
            print(f"User: {user['displayName']} ({user['userPrincipalName']})")
    else:
        print(f"Failed to list users. Error: {response.text}")
else:
    print(f"Failed to obtain access token. Error: {result.get('error')}")

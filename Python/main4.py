# Using EnvironmentCredential for demonstration purposes.
# There are many other options for getting an access token. See the following for more information.
# https://pypi.org/project/azure-identity/#async-credentials
from azure.identity.aio import EnvironmentCredential
# from msgraph_core.authentication import AzureIdentityAuthenticationProvider

from azure.identity import InteractiveBrowserCredential
from msgraph.core import GraphClient

client_id = '933d8a89-8fdb-41cc-b9d2-b7078cd02e2e'
client_secret = 'N0W8Q~CmpAWlghgL3xxTwCPBB1a4wyqIxTKY3cc9'
tenant_id = 'ec3ded2c-750b-415f-b382-96464321f3cf'

# credential=EnvironmentCredential()
# auth_provider = AzureIdentityAuthenticationProvider(credential)

# from msgraph_core import BaseGraphRequestAdapter
# adapter = BaseGraphRequestAdapter(auth_provider)

browser_credential = InteractiveBrowserCredential(client_id=client_id)

client = GraphClient(credential=browser_credential)

# result = client.get('/me')

result = client.get(
    '/users',
    params={
        '$select': 'displayName',
        '$top': '10'
    },
)

print(result.json())

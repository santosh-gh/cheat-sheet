import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient


client_id = '933d8a89-8fdb-41cc-b9d2-b7078cd02e2e'
client_secret = 'N0W8Q~CmpAWlghgL3xxTwCPBB1a4wyqIxTKY3cc9'
tenant_id = 'ec3ded2c-750b-415f-b382-96464321f3cf'

credential = ClientSecretCredential(
    tenant_id,
    client_id,
    client_secret
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET /users/{id | userPrincipalName}
# async def get_user():
#user = client.users.by_user_id('userPrincipalName').get()
#if user:
#print(user.display_name)
# asyncio.run(get_user())

from azure.identity.aio import EnvironmentCredential
from msgraph_core.authentication import AzureIdentityAuthenticationProvider

credential=EnvironmentCredential()
auth_provider = AzureIdentityAuthenticationProvider(credential)
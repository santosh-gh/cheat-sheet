# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import ResourceManagementClient
# from azure.mgmt.resource.resources.models import ResourceGroup

# # Azure subscription ID
# subscription_id = 'b798c28b-e334-4ecf-b338-ec314ced3616'

# # Resource group details
# resource_group_name = 'mynew-rg'
# location = 'southindia'

# # Instantiate the Azure credentials
# credentials = DefaultAzureCredential()

# # Instantiate the Resource Management client
# resource_client = ResourceManagementClient(credentials, subscription_id)

# # Create the resource group
# resource_group_params = ResourceGroup(location=location)
# resource_client.resource_groups.create_or_update(resource_group_name, resource_group_params)

import os, json
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
#from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials

# Set the Azure subscription ID and tenant ID
subscription_id = 'b798c28b-e334-4ecf-b338-ec314ced3616'
tenant_id = 'ec3ded2c-750b-415f-b382-96464321f3cf'

credential = ClientSecretCredential(
    tenant_id='ec3ded2c-750b-415f-b382-96464321f3cf',
    client_id='933d8a89-8fdb-41cc-b9d2-b7078cd02e2e',
    client_secret='N0W8Q~CmpAWlghgL3xxTwCPBB1a4wyqIxTKY3cc9'
)



resource_client = ResourceManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)
#network_client = NetworkManagementClient(credential, "subscription_id")


# Create an instance of the AuthorizationManagementClient using your credentials
auth_client = AuthorizationManagementClient(credential, subscription_id)


# Create an instance of the DefaultAzureCredential class to authenticate
# credential = DefaultAzureCredential()

# List all Virtual Machines in the specified subscription
def list_virtual_machines():
    for vm in compute_client.virtual_machines.list_all():
        print(vm.name)

list_virtual_machines()

for vm in compute_client.virtual_machines.list_all():
    print("\tVM: {}".format(vm.name))

# # Create an instance of the AuthorizationManagementClient using your credentials
# auth_client = AuthorizationManagementClient(credential, subscription_id)

# # Use the AuthorizationManagementClient to get the list of service principals
# service_principals = auth_client.service_principals.list()

# # Iterate over the service principals and print their details
# for sp in service_principals:
#     print("Service Principal Name:", sp.display_name)
#     print("Service Principal Object ID:", sp.object_id)
#     print("--------------------------------------")
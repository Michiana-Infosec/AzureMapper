from azure.mgmt.network import NetworkManagementClient
#from azure.common.credentials import ServicePrincipalCredentials #install msrestazure for this import
# ^ Removing this because azure-python-sdk updated
from azure.identity import DefaultAzureCredential
import adal

authority_uri = 'https://login.microsoftonline.com/' + "tenant-id"
context = adal.AuthenticationContext(authority_uri)

import os
os.environ["AZURE_CLIENT_ID"]=""
os.environ["AZURE_CLIENT_SECRET"] = ""
os.environ["AZURE_TENANT_ID"]=""

arm_credentials = DefaultAzureCredential()

client = NetworkManagementClient(arm_credentials, "subscription-id")
for i in client.network_security_groups.list_all():
    print(i)#.id.split('/')[-1])
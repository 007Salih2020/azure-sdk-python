# pip3 install azure-mgmt-resource
# pip3 install azure-identity
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Get creadentials from the CLI.
# only use for development.
credential = AzureCliCredential()

# subscripton
subscription_id = "c243c1ed-2977-4a89-bf0c-eaac5d86e2d0"

# a resource management client is needed to work with resource group and resources in Azure
resource_mgmt_client = ResourceManagementClient(credential, subscription_id)
resource_group_params = {'location':'westus', 'tags':{'hello': 'world', "test":"crazy"}}
resource_mgmt_client.resource_groups.create_or_update("rg-python", resource_group_params)

# print the list of all resource group names with their locations
resource_group_list = resource_mgmt_client.resource_groups.list()
for count, item in enumerate(resource_group_list):
    print(str(count+1) + ", " + item.name + ", " + item.location)
#
# # print all resources in a subscription with their name and location
resource_list = resource_mgmt_client.resources.list()
for count, resource in enumerate(resource_list):
     print(str(count+1) + ", " + resource.name + ", " + resource.location + ", " + resource.type)
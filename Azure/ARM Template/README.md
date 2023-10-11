https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template?tabs=azure-powershell


# Login
  Connect-AzAccount
  az login

# Create RG

  New-AzResourceGroup -Name myResourceGroup -Location "Central US"

  az group create --name myResourceGroup --location 'Central US'

# Deploy ARM Template 
    $templateFile = "path-to-the-template-file"
    New-AzResourceGroupDeployment `
    -Name blanktemplate `
    -ResourceGroupName myResourceGroup `
    -TemplateFile $templateFile


    $templateFile = "C:\cheat-sheet\Azure\ARM Template\storage.json"

    New-AzResourceGroupDeployment -Name mystoragetemplate -ResourceGroupName example-rg    -TemplateFile $templateFile



    az deployment group create --name azmystorage --resource-group example-rg --template-file $templateFile


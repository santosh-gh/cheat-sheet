# Install its respective plugins
    - Terraform extension (Microsoft DevLabs)
    - Replace Tokens (Guillaume Rouchon)

# Create Service Principal 
    $SubscriptionId = "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    az login
    az account set --subscription $subscriptionId
    az ad sp create-for-rbac --role="Contributor" --scopes="subscriptions/$subscriptionId" --name "id-terraformtest"

# Best practices for Terraform in Azure DevOps pipelines:
    Use a separate repository or branch for your Terraform configuration files to isolate changes and maintain version control.

    Store sensitive data such as credentials and API keys in Azure Key Vault or use environment variables in the 
    pipeline to avoid exposing them in the configuration files.

    Use Terraform workspaces to manage multiple environments (e.g., dev, staging, production) with 
    the same configuration files.

    Lock your Terraform state file during pipeline execution to prevent concurrent modifications.

    Review and approve changes using pull requests and require peer reviews for 
    critical infrastructure changes.

    Implement a CI/CD process with automated testing to validate your infrastructure 
    changes before applying them.
    
    Regularly update the Terraform extension and the Terraform binary to take advantage of new 
    features, bug fixes, and provider updates.


# ################

# CLI Login
  $ az login

  $ az account show
  $ az account list

  $ az account set --subscription="SUBSCRIPTION_ID"

# Service Principal
  $ az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/SUBSCRIPTION_ID"
  $ az ad sp create-for-rbac --name <SP_TEST> --role contributor --scopes /subscriptions/<SUBSCRIPTION_ID>

# Use Bash to set Environment Variables
  $ export ARM_CLIENT_ID="appId"
  $ export ARM_CLIENT_SECRET="password"
  $ export ARM_SUBSCRIPTION_ID="subscriptionId"
  $ export ARM_TENANT_ID="tenant"

# PowerShell
  $env:ARM_TENANT_ID = "tenantId"
  $env:ARM_SUBSCRIPTION_ID = "subscriptionId"
  $env:ARM_CLIENT_ID = "appId"
  $env:ARM_CLIENT_SECRET = "password"

# main.tf

  # Specify the Azure provider and version
  provider "azurerm" {
    features {}
  }

  # Configure the Azure provider
  terraform {
    required_providers {
      azurerm = {
        source  = "hashicorp/azurerm"
        version = "~> 3.0.2"
      }
    }

    required_version = ">= 1.1.0"
  }

  # Create a resource group
  resource "azurerm_resource_group" "rg" {
    name     = "example-resource-group"
    location = "West US"
  }

  # Create a virtual network
  resource "azurerm_virtual_network" "example" {
    name                = "example-vnet"
    address_space       = ["10.0.0.0/16"]
    location            = azurerm_resource_group.example.location
    resource_group_name = azurerm_resource_group.example.name
  }

  # Create a subnet within the virtual network
  resource "azurerm_subnet" "example" {
    name                 = "example-subnet"
    resource_group_name  = azurerm_resource_group.example.name
    virtual_network_name = azurerm_virtual_network.example.name
    address_prefixes     = ["10.0.1.0/24"]
  }
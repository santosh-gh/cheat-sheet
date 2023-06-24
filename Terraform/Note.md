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
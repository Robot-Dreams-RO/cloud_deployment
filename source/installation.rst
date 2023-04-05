###############
2. Installation
###############

=================
Install Azure CLI 
=================

.. note::

    azcli is a command-line tool for managing Azure resources.

Installation details can be found here https://learn.microsoft.com/en-us/cli/azure/install-azure-cli for WSL Ubuntu you can run ``curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash``

============
Install func
============

.. note::

    func is a command-line tool for managing Azure Functions. 

Installation details can be found here https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Clinux%2Ccsharp%2Cportal%2Cbash for WSL Ubuntu:

.. code-block::

    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

    sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg

    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'

    sudo apt-get update

    sudo apt-get install azure-functions-core-tools-4

=================
Install Terraform
=================

You can download the latest version of Terraform from the official website: https://www.terraform.io/downloads.html for WSL Ubuntu

.. code-block::

    wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

    sudo apt update && sudo apt install terraform


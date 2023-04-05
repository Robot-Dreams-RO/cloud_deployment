##################
4. Getting started
##################

An example of an Azure Function App that uses Flask and Swagger for API documentation.

Create a virtual environment and install the required packages:

.. code-block::
    
    python -m venv venv
    source venv/bin/activate
    pip install -r source_code/reqquirements.txt

Create a new Azure Functions project:

.. code-block::

    func init --worker-runtime python

Create a new Azure Functions HTTP Trigger:

.. code-block::

    func new --name robot_dreams --template "HTTP trigger"

Modify the ``requirements.txt`` file to include the required packages:

.. code-block::

    azure-functions
    fastapi


To test the function locally, start the Azure Functions Core Tools:

.. code-block::

    func start

Deploy the function in the previously created environment:

.. code-block::

    func azure functionapp publish func-robot-dreams-deploy

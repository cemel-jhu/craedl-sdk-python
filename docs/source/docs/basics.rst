The basics
==========

The Craedl Python SDK is, ultimately, a wrapper around the Craedl RESTful API, which is documented at `api.craedl.org <https://api.craedl.org>`_.
Through the RESTful API, you can do just about anything in code that you can do in the Craedl web site, as long as you don't mind composing commands like this one and then manually parsing the JSON response:

.. code-block:: bash

    curl -H "Authorization: Bearer RqjxUjHwuoov0LvVQV1bEuGLOftwEfOiLHXaGxzh" https://api.craedl.org/profile/whoami/

The Craedl Python SDK takes care of all of this messy HTTP request formatting and JSON parsing for you, replacing it with an intuitive Python module that you can use to easily script your Craedl usage.

The ability to script your Craedl usage can be beneficial if you commonly perform repetitive tasks like uploading the results of an experiment.
It can be mission-critical if you want to access Craedl through a computing resource that doesn't have a GUI (because then it's impossible to access Craedl through a web browser).

Follow these steps to get started using the Craedl Python SDK.

Obtain the Craedl Python SDK module
***********************************

Obtain the Craedl Python SDK from `PyPI <https://pypi.org/project/craedl/>`_:

.. code-block:: bash

    pip install craedl

You only have to perform this step once (on a particular computer and/or virtual environment).

Configure your authentication token
***********************************

Retrieve your API access token from your Craedl account by logging into `Craedl.org <https://craedl.org>`_ and clicking the key icon in the ``My Craedl`` card.
Generate a token and pass it to the following command when prompted:

.. code-block:: bash

    python -m craedl

As long as you don't revoke this token or generate a new one, you will only have to perform this step once every 28 days.
Should you have reason to worry that your token has been compromised, simply generate a new one in Craedl and re-run the command above to re-enable your Craedl Python SDK authentication.

Use the Craedl Python SDK
*************************

Now you're ready to write a Craedl Python script.
To begin, you must always import the Craedl Python SDK and get your profile:

.. code-block:: python

    import craedl
    profile = craedl.auth()

From here, you can put together the building blocks documented in :doc:`../core/index`.
If you're just getting started, you may find our :doc:`examples` helpful.

=============================
Python wrapper for Unimus API
=============================


.. image:: https://img.shields.io/pypi/v/pyunimus.svg
        :target: https://pypi.python.org/pypi/pyunimus

.. image:: https://img.shields.io/travis/smallsam/pyunimus.svg
        :target: https://travis-ci.com/smallsam/pyunimus


Python interface to the Unimus API. Useful to pull device information, retrieving configs and triggering config backups.


* Free software: MIT license


Features
--------

* List devices
* Trigger backup
* Get most recent backed up config (latest_backup)
* Get config from device (i.e. trigger backup and then download config)

Usage
-----

        import pyunimus
        logging.info("Connecting to Unimus...")
        u = pyunimus.Unimus(UNIMUS_HOST, UNIMUS_TOKEN)
        devices = u.devices()


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

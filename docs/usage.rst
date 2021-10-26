=====
Usage
=====

To use Python wrapper for Unimus API in a project::

    import pyunimus
    logging.info("Connecting to Unimus...")
    u = pyunimus.Unimus(UNIMUS_HOST, UNIMUS_TOKEN)
    devices = u.devices()

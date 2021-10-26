"""Main module."""

import requests
import base64
from datetime import datetime
from time import sleep
from urllib.parse import urljoin

class Unimus:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def _api_request(self, method, url, *args, **kwargs):
        url = urljoin("{}/api/v2/".format(self.url), url)
        if "headers" not in kwargs:
            kwargs["headers"] = {"Accept": "application/json", "Authorization": "Bearer {}".format(self.token)}

        r = requests.request(method, url, *args, **kwargs)
        r.raise_for_status()
        if kwargs.get("raw"):
            return r.content
        else:
            return r.json()

    def devices(self):
        return self._api_request("GET", "devices/").get("data")

    def backup_device(self,device_id):
        if int(device_id) == device_id:
            job = self._api_request("PATCH","jobs/backup?id={}".format(device_id))
            if job["data"]["accepted"] > 0:
                return True
        else:
            raise Exception("Need device_id")

    def get_latest_config(self, device_id):
        r = self._api_request("GET", "devices/{}/backups/latest".format(device_id))
        config = base64.b64decode(r["data"]["bytes"].encode('utf-8')).decode('utf-8')
        if r["data"]["validUntil"] is None:
            timestamp = datetime.fromtimestamp(r["data"]["validSince"])
        else:
            timestamp = datetime.fromtimestamp(max(r["data"]["validSince"],r["data"]["validUntil"]))
        age_seconds = (datetime.now() - timestamp).seconds
        return (config,age_seconds)

    def get_config_from_device(self, device_id):
        start_time = datetime.now()
        (_, initial_age) = self.get_latest_config(device_id)
        age = initial_age
        self.backup_device(device_id)
        while age >= initial_age:
            (config, age) = self.get_latest_config(device_id)
            sleep(0.5)
            if (datetime.now() - start_time).seconds > 60:
                raise Exception("Timed out waiting for new config")
        return config

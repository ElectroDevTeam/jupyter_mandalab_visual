import os

NOTEBOOK_RES_PATH = "/api/mandalab/res/"
LOCAL_RES_PATH = os.path.join(os.path.dirname(__file__), "res", "") # The last "" is for adding a slash at the end of the path.

COMPUTER_FILE_FORMAT = "{os}_{status}.jpg"

NETWORK_FILE = "network.jpg"
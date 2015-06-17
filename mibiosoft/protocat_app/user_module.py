__author__ = 'William, Ramanujamin@GitHub'

from os.path import expanduser
from stormpath.client import Client

client = Client(api_key_file_location=expanduser('/Users/William/api_keys/apiKey_stormpath_protocat.properties'))
application = client.applications.search('Protocat')[0]
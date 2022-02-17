
import json
import requests
import time
import pprint

from src.endpoint import Endpoint
from src.trafficPair import TrafficPair
from src.throughputTest import ThroughputTest
from src.attenuator import Attenuator
from src.device import Device
from src.pathLoss import PathLoss
from src.rotation import Rotation
from src.turntable import Turntable
from src.sniffer import Sniffer
from src.synchroSniffer import SynchroSniffer
from src.pal6Config import Pal6Config

# from src.fixId import fixId

# myhost = "169.254.100.4"
# myhost = "10.100.100.146"
myhost = "172.17.0.1"


class Octobox:

    def __init__(this, host=myhost, port=8084):
        this.host = host
        this.pp = pprint.PrettyPrinter(indent=1)
        this.uri = f'http://{host}:{port}'
        this.device = Device(this)
        this.endpoint = Endpoint(this)
        this.attenuator = Attenuator(this)
        this.trafficPair = TrafficPair(this)
        this.throughputTest = ThroughputTest(this)
        this.pathLoss = PathLoss(this)
        this.rotation = Rotation(this)
        this.turntable = Turntable(this)
        this.sniffer = Sniffer(this)
        this.synchroSniffer = SynchroSniffer(this)
        this.pal6Config = Pal6Config(this)

    def sleep(this, ms):
        """ Utility function - Sleep
            Program stops for set amount of time in miliseconds

            Paramaters
            ----------
            ms: int
                Time to sleep in miliseconds
        """
        time.sleep(ms / 1000)

    apiVersion = "0.0.2"

    def fetch(this, url, data):
        """
        Calling on GraphQL API

        Parameters
        ----------
        url : string
        data : dict

        Raises
        ----------
        Exception
            If GraphQL throws any errors exceptions are raised
            and apprioate error message is triggered

        Returns
        ----------
        data: dict
            Information regarding traffic pair, throughput test,
            endpoints and errors

        """
        resp = requests.post(url, data=data, timeout=120.0)
        text = json.loads(resp.text)
        # print("########################")
        # this.pp.pprint(resp.text)

        if 'errors' in text:
            errors = eval(text['errors'][0])
            text['errors'] = errors
            text['data'] = None
            # if('data' not in text):
        else:
            text['errors'] = None
        # this.pp.pprint(text)
        return text
        # raise Exception(errors)
        # elif 'data' in text:
        #     data = text['data']
        #     return data

    def myFetch(this, query="{viewer{version}}", variables={}):
        """
        Uses approriate query and variables to call fetch
        and reches GraphQL

        Parameters
        ----------
        query : string
        variables : dict

        Returns
        ----------
        fetch: dict
            GraphQL response information
        """
        data = {'query': query, 'variables': json.dumps(variables)}
        url = f'{this.uri}/graphql'
        return this.fetch(url=url, data=data)

    def serverVersion(this):
        """
        Get the current version of the octobox server


        Returns
        ----------
        version: string
            octobox server version

        """
        query = """
            {
          viewer {
            version
          }
        }
        """
        resp = this.myFetch(query=query)
        return resp['data']['viewer']['version']

class Sniffer:
    """
    Note
    -------
    Errors are no longer thrown and are now automatically returned
    with each method. Each API call returns an array with "data"
    as well as "errors". If there are no errors, "errors" will
    be null.
    """
    def __init__(this, octobox):
        this.octobox = octobox

    ##################################################################
    ##################################################################

    def discover(this, sniff):
        """
        Discover sniffer provided its address

        Parameters
        ----------
        dict
            sniffer dictionary containing a valid address key

        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing sniffer information keys

        Example
        ----------
        >>> octobox= Octobox()
        >>> octobox.sniffer.discover({'address': '169.254.20.9'})
        """

        if('address' not in sniff):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation FindSnifferMutation($input: FindSnifferInput!) {
                findSniffer(input: $input) {
                            sniffer {
                                   id
                                   address
                                   channelWidth
                                   probeID
                                   primaryChannel
                                   headersOnly
                                   secondaryChannel8080
                            }
                          }
                        }"""
        inputs = {}
        for k, v in sniff.items():
            if (k == "address"):
                inputs[k] = v

        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['findSniffer']['sniffer']
            resp['data'] = data
        # else:
        #     data = resp['data']['findSniffer']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def createSniffer(this, sniff):
        """
        Creates new sniffer. Generally used in conjunction with
        output from the discover method. It is recommended to use the
        create method which wraps both discover and createSniffer.

        Parameters
        ----------
        dict
            dictionary containing the keys:
                - id
                - address
                - channelWidth
                - probeID
                - primaryChannel
                - headersOnly
                - secondaryChannel8080



        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing sniffer information keys

        Example
        ----------
        >>> octobox = Octobox()
        #Find Sniffer
        >>> sniffAddr = {'address': '169.254.20.9'}
        >>> sniffInput, errors = octobox.sniffer.discover(sniffAddr)
        # Create Sniffer record
        >>> sniffer, errors = octobox.sniffer.createSniffer(sniffInput)
        """
        query = """mutation CreateSnifferMutation($input: CreateSnifferInput!) {
                  createSniffer(input: $input) {
                    snifferEdge {
                      node {
                         id
                         address
                         channelWidth
                         probeID
                         primaryChannel
                         headersOnly
                         secondaryChannel8080
                      }
                    }
                  }
                }"""
        inputs = {}
        for k, v in sniff.items():
            if (k == "address" or k == "channelWidth" or k == "primaryChannel"
                    or k == "probeID" or k == "headersOnly"or k == "secondaryChannel8080"):
                inputs[k] = v

        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['createSniffer']['snifferEdge']['node']
            resp['data'] = data
        # else:
        #     data = resp['data']['createSniffer']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def create(this, sniff):
        """
        Discovers and creates new sniffer by calling findSniffer
        and createSniffer methods. A sniffer can be created
        simply by calling this method with a valid sniffer address

        Parameters
        ----------
        dict
            dictonary with valid sniffer address key


        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing sniffer information


        Example
        ----------
        >>> octobox = Octobox()
        >>> sniffer, errors = octobox.sniffer.create({'address':'169.254.26.4'})
        """

        if('address' not in sniff):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        fSniff, errors = this.discover(sniff)

        if (errors is not None):
            return (fSniff, errors)

        for k, v in sniff.items():
            if (k == "id" or k == "address" or k == "channelWidth" or k == "probeID" or k == "primaryChannel" or k == "headersOnly" or k == "secondaryChannel8080"):
                fSniff[k] = v

        return this.createSniffer(fSniff)

    ##################################################################
    ##################################################################

    def update(this, sniff):
        """
        Update an attenuator given its id or address

        Parameters
        ----------
        dict
            attenuator dictionary with valid id or address key


        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing updated sniffer information keys


        Example
        ----------
        >>> octobox = Octobox()
        # Update with ID
        >>> updatedKeys = {'id':snifferId,
                            "channelWidth": "80+80",
                            "probeID": "custom-tag",
                            "primaryChannel": "48",
                            "secondaryChannel8080": "106",
                            "headersOnly": false
                         }
        >>> updatedSniffer, errors = octobox.sniffer.update(updatedKeys)
        # Update with Address
        >>> updatedKeys = {'address': "160.254.26.25",
                            'channelWidth': "90",
                            'probeID': 'updatedByAddr'}
        >>> updatedSniffer, errors = octobox.sniffer.update(updatedKeys)

        """

        if('id' not in sniff and 'address' not in sniff):
            resp = {"errors": [
                {"message": "Must provide either an id or an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangSnifferMutation($input: ChangeSnifferInput!) {
                  changeSniffer(input: $input) {
                    sniffer{
                        id
                        address
                        channelWidth
                        probeID
                        primaryChannel
                        headersOnly
                        secondaryChannel8080

                    }
                  }
                }"""
        inputs = {}
        for k, v in sniff.items():
            if (k == "address" or k == "channelWidth" or k == "primaryChannel"
                    or k == "probeID" or k == "id" or k == "headersOnly" or k == "secondaryChannel8080"):
                inputs[k] = v

        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['changeSniffer']['sniffer']
            resp['data'] = data
        # else:
        #     data = resp['data']['changeSniffer']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def delete(this, sniff):
        """
        Remove a sniffer given its id or address

        Parameters
        ----------
        dict
            sniffer dictionary with valid id or address key

        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing id of removed sniffer


        Example
        ----------
        >>> octobox = Octobox()

        >>> ##Address provided
        >>> sniff = {'address':'1.2.3.4'}
        >>> removed, errors = octobox.sniffer.delete(sniff)

        >>> ##ID provided
        >>> sniff ={ 'id':'VGhyb3VnaHB1dFRlc3Q6NWI0Y2ZkZWRjNWQ3M2QwMWZkYzVjY2Ni'}
        >>> removed, errors = octobox.sniffer.delete(sniff)

        """

        if('id' not in sniff and 'address' not in sniff):
            resp = {"errors": [
                {"message": "Must provide either an id or an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('id' in sniff):
            qType = ["removeSniffer", "RemoveSnifferInput"]
        else:
            qType = ["removeSnifferByAddress", "RemoveSnifferByAddressInput"]

        query = """mutation {0}($input:{1}!) {{
                {0}(input: $input) {{
                deletedSnifferId
                    }}
                }}""".format(*qType)
        inputs = {}
        for k, v in sniff.items():
            if (k == "address" or k == "id"):
                inputs[k] = v

        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            if('id' in sniff):
                data = resp['data']['removeSniffer']['deletedSnifferId']
                resp['data'] = data
            else:
                data = resp['data']['removeSnifferByAddress']['deletedSnifferId']
                resp['data'] = data
        # else:
        #     data = resp['data']['changeSniffer']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def deleteAll(this):
        """
        Deletes all sniffers in database

        Returns
        ----------
        array
            an array containing any errors as well as an array
            containing deleted sniffer ids

        Example
        ----------
        >>> octobox = Octobox()
        >>> octobox.sniffer.deleteAll()

        """
        query = """ mutation{ removeSniffers(input:{}){
                  deletedSnifferIds
                }
              }"""
        variables = {}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeSniffers']['deletedSnifferIds']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def readAll(this):
        """
        Get an array of all sniffers from database

        Returns
        ----------
        array
            an array containing any errors as well as an array
            containing all rotations and information

        Example
        ----------
        >>> octobox = Octobox()
        >>> octobox.sniffer.readAll()
        """
        query = """{
                  viewer {
                    sniffers {
                      edges {
                        node {
                              id
                              address
                              channelWidth
                              probeID
                              primaryChannel
                              headersOnly
                              secondaryChannel8080
                        }
                      }
                    }
                  } }"""
        variables = {}

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['sniffers']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def read(this, sniff):
        """
        Get a sniffer given its id or address (at least one required)

        Parameters
        ----------
        dict
            sniffer dictionary containing address or id keys

        Returns
        ----------
        array
            an array containing any errors as well as a dictionary
            containing sniffer information

        Example
        ----------
        >>> octobox = Octobox()

        >>> ##Address provided
        >>> sniff = {'address':'1.2.3.4'}
        >>> sniff, errors = octobox.sniffer.read(sniff)

        >>> ##ID provided
        >>> sniff ={ 'id':'VGhyb3VnaHB1dFRlc3Q6NWI0Y2ZkZWRjNWQ3M2QwMWZkYzVjY2Ni'}
        >>> sniff, errors = octobox.sniffer.read(sniff)

        """
        if('id' not in sniff and 'address' not in sniff):
            resp = {"errors": [
                {"message": "Must provide either an id or an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('id' in sniff):
            query = """query ($id: ID!) {
                      node(id: $id) {
                        ... on Sniffer {
                          id
                          address
                          channelWidth
                          probeID
                          primaryChannel
                          headersOnly
                          secondaryChannel8080
                        }
                      }
                    }"""

        else:
            query = """ query($address:String!) {
                    viewer {
                      snifferByAddr(address: $address) {
                            id
                            address
                            channelWidth
                            probeID
                            primaryChannel
                            headersOnly
                            secondaryChannel8080
                    }
                  }
                }"""

        # print("QUERY", query)
        inputs = {}
        for k, v in sniff.items():
            if (k == "address" or k == "id"):
                inputs[k] = v
        variables = inputs

        resp = this.octobox.myFetch(
            query,
            variables
        )

        if (resp['errors'] is None):
            if('id' in sniff):
                data = resp['data']['node']
                resp['data'] = data
            else:
                data = resp['data']['viewer']['snifferByAddr']
                resp['data'] = data
        # else:
        #     data = resp['data']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

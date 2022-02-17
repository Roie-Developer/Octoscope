class Endpoint:
   
    def __init__(this, octobox):
        this.octobox = octobox

    ##################################################################
    ##################################################################

    def findEndpoint(this, ep):
       
        ep.setdefault('legacy', False)
        ep.setdefault('localEP', False)

        if('address' not in ep):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """
            mutation FindEndpointMutation($input: FindEndpointInput!) {
              findEndpoint(input: $input) {
                endpoint {
                      id
                      address
                      legacy
                      legacyPort
                      localEP
                      managementAddr
                      name
                      version
                      status
                      serial
                      type
                      model
                      endpointType

                    }
                  }
                }
                """
        inputs = {}
        for k, v in ep.items():
            if (k == "address" or k == "legacy" or
                k == "legacyPort" or
                    k == "managementAddr" or k == "model"):
                inputs[k] = v

        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)
        # print("#####find response", resp)
        if (resp['errors'] is None):
            data = resp['data']['findEndpoint']['endpoint']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def createEndpoint(this, ep):
       

        if('address' not in ep):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """
        mutation CreateEndpointMutation($input: CreateEndpointInput!) {
            createEndpoint(input: $input) {
                endpointEdge {
                  __typename
                  cursor
                  node {
                     id
                     address
                     legacy
                     legacyPort
                     localEP
                     managementAddr
                     name
                     version
                     status
                     serial
                     type
                     model
                     endpointType
                     endpointMode
                     palRadio
                  }
                }
              }
            }"""

        ep.setdefault('endpointMode', 'endpoint')

        inputs = {}
        for k, v in ep.items():
            if (k == "address" or k == "legacy" or k == "legacyPort" or k == "localEP" or
                k == "managementAddr" or k == "name" or k == "serial" or k == "status" or
                k == "type" or k == "version" or k == "model"or k == "endpointMode"or k == "endpointType"
                    or k == "palRadio"):
                inputs[k] = v

        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)
        # print("#####create response", resp)
        if (resp['errors'] is None):
            data = resp['data']['createEndpoint']['endpointEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def create(this, ep):
       
        if('address' not in ep):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        ep.setdefault('legacy', False)

        fep, errors = this.findEndpoint(ep)
        # print("fep out",fep)
        if (errors is not None):
            return (fep, errors)

        inputs = {}
        for k, v in fep.items():
            if (k == "id" or k == "address" or k == "legacy" or k == "legacyPort" or k == "localEP" or
                k == "managementAddr" or k == "name" or k == "serial" or k == "status" or
                    k == "type" or k == "version" or k == "model" or k == "endpointType"or k == "endpointMode" or k == "palRadio"):
                inputs[k] = v

        for k, v in ep.items():
            if (k == "id" or k == "address" or k == "legacy" or k == "legacyPort" or
                k == "managementAddr" or k == "name" or k == "serial" or k == "status" or
                    k == "type" or k == "version" or k == "endpointMode" or k == "endpointType" or k == "palRadio"):
                inputs[k] = v

        return this.createEndpoint(inputs)
    ##################################################################
    ##################################################################

    def update(this, ep):
        
        if('id' not in ep):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """
                    mutation ChangeEndpointMutation($input: ChangeEndpointInput!) {
                  changeEndpoint(input: $input) {
                    endpoint {
                      id
                      address
                      legacy
                      legacyPort
                      localEP
                      managementAddr
                      name
                      version
                      status
                      serial
                      type
                      model
                      endpointType
                      endpointMode
                      palRadio
                    }
                  }
                }
            """

        inputs = {}
        for k, v in ep.items():
            if (k == "id" or k == "address" or k == "legacy" or k == "legacyPort" or k == "localEP" or
                k == "managementAddr" or k == "name" or k == "serial" or k == "status" or
                k == "type" or k == "version" or k == "model"or k == "endpointMode"or k == "endpointType"
                    or k == "palRadio"):
                inputs[k] = v

        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)
        # print("#####create response", resp)
        if (resp['errors'] is None):
            data = resp['data']['changeEndpoint']['endpoint']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##################################################################
    ##################################################################

    def readByAddress(this, address):

        if(address is None):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """
            query($address: String!) {
            viewer {
                endpointByAddr(address: $address) {
                    id
                    address
                    legacy
                    legacyPort
                    localEP
                    managementAddr
                    name
                    version
                    status
                    serial
                    type
                    endpointMode
                    endpointType
                }
            }
        }
        """
        variables = {
            'address': address
        }
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['endpointByAddr']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]


##################################################################
##################################################################


    def read(this, id):

        query = """
            query ($id: ID!) {
                node(id: $id) {
                    ...on Endpoint {
                    id
                    address
                    legacy
                    legacyPort
                    localEP
                    managementAddr
                    name
                    version
                    status
                    serial
                    type
                    endpointType
                    endpointMode
                }
              }
            }
        """
        variables = {
            'id': id
        }
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            node = resp['data']['node']
            resp['data'] = node
        return [resp[k] for k in ('data', 'errors')]

##################################################################
##################################################################

    def readAll(this):
        query = """
            {
            viewer {
                endpoints {
                    edges {
                        node {
                            id
                            address
                            legacy
                            legacyPort
                            localEP
                            managementAddr
                            name
                            version
                            status
                            serial
                            type
                            endpointType
                        }
                    }
                }
            }
        }
        """
        variables = {}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['endpoints']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]


##################################################################
##################################################################


    def delete(this, ep):

        if('id' not in ep and 'address' not in ep):
            resp = {"errors": [
                {"message": "Must provide either an id or an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if 'id' not in ep:
            query = """
                mutation removeEndpointByAddress($input: RemoveEndpointByAddressInput!) {
                    removeEndpointByAddress(input: $input) {
                        deletedEndpointId
                    }
                }
                """
            inputs = {}
            for k, v in ep.items():
                if (k == "address" or k == "managementAddr"):
                    inputs[k] = v
            variables = {
                'input': inputs
            }
            resp = this.octobox.myFetch(
                query,
                variables
            )
            if (resp['errors'] is None):
                data = resp['data']['removeEndpointByAddress']['deletedEndpointId']
                resp['data'] = data

            return [resp[k] for k in ('data', 'errors')]
        else:
            query = """
                mutation removeEndpoint($input: RemoveEndpointInput!) {
                    removeEndpoint(input: $input) {
                        deletedEndpointId
                    }
                }
                """
            inputs = {}
            for k, v in ep.items():
                if (k == "id"):
                    inputs[k] = v
            variables = {
                'input': inputs
            }
            resp = this.octobox.myFetch(
                query,
                variables
            )
            if (resp['errors'] is None):
                data = resp['data']['removeEndpoint']['deletedEndpointId']
                resp['data'] = data

            return [resp[k] for k in ('data', 'errors')]

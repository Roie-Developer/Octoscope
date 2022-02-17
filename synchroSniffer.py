class SynchroSniffer:
 
    def __init__(this, octobox):
        this.octobox = octobox

    ##############################################################
    ##############################################################

    def create(this, sSniff):

        if('testId' not in sSniff):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation CreateSynchroSnifferMutation($input: CreateSynchroSnifferInput!) {
            createSynchroSniffer(input: $input) {
              synchroSnifferEdge {
                __typename
                cursor
                node {
              id
              endpoint
              probeID
              channelWidth
              primaryChannel
              secondaryChannel8080
              headersOnly
              managementOnly
              palRadio

                }
              }
            }
          }"""
        sSniff['id'] = sSniff['testId']

        inputs = {}
        for k, v in sSniff.items():
            if (k == "id" or k == "endpoint" or k == "channelWidth" or k == "primaryChannel"or k == "secondaryChannel8080"
                or k == "probeID" or k == "palRadio"
                    or k == "headersOnly" or k == "managementOnly"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createSynchroSniffer']['synchroSnifferEdge']['node']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def remove(this, sSniff):
        
        if('id' not in sSniff):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveSynchroSnifferMutation($input: RemoveSynchroSnifferInput!) {
            removeSynchroSniffer(input: $input) {
              deletedSynchroSnifferId
            }
          }"""

        inputs = {}
        for k, v in sSniff.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeSynchroSniffer']['deletedSynchroSnifferId']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def removeAll(this, testId):
        
        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide a tesId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveSynchroSnifferMutation($input: RemoveSynchroSniffersInput!) {
            removeSynchroSniffers(input: $input) {
              deletedSynchroSnifferIds
            }
          }"""

        variables = {'input': {'id': testId}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeSynchroSniffers']['deletedSynchroSnifferIds']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def readAll(this, testId):

        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide a tesId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query ($id: ID!) {
            viewer {
            synchroSniffers(id: $id) {
            edges {
              node {
                  id
                  endpoint
                  probeID
                  channelWidth
                  primaryChannel
                  secondaryChannel8080
                  headersOnly
                  managementOnly


                    }
                }
              }
            }
        }"""

        variables = {'id': testId}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['synchroSniffers']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def update(this, sSniff):

        if('id' not in sSniff):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeSynchroSnifferMutation($input: ChangeSynchroSnifferInput!) {
          changeSynchroSniffer(input: $input) {
            synchroSniffer {
              id
              endpoint
              probeID
              channelWidth
              primaryChannel
              secondaryChannel8080
              headersOnly
              managementOnly
              palRadio

            }
          }
        }"""
        inputs = {}
        for k, v in sSniff.items():
            if (k == "id" or k == "endpoint"or k == "channelWidth" or k == "primaryChannel"or k == "secondaryChannel8080"
                    or k == "probeID" or k == "managementOnly" or k == "headersOnly" or k == "palRadio"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeSynchroSniffer']['synchroSniffer']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

        ##############################################################
        ##############################################################

    def push(this, sSniff):

        if('id' not in sSniff):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation PushSynchroSnifferConfigOneMutation ($input: PushSynchroSnifferOneInput!) {
          pushSynchroSnifferOne(input: $input) {
            synchroSniffer {
            id

            }
          }
        }"""
        inputs = {}
        for k, v in sSniff.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)
        # print("resp###############", resp)

        if (resp['errors'] is None):
            data = resp['data']['pushSynchroSnifferOne']['synchroSniffer']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

        ##############################################################
        ##############################################################

    def start(this, testId):

        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide a test id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation SynchroSnifferToggle($input: SynchroSnifferToggleInput!) {
          synchroSnifferToggle(input: $input) {
               clientMutationId
                }
        }"""
        inputs = {"id": testId}
        variables = {"input": inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['synchroSnifferToggle']['clientMutationId']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

        ##############################################################
        ##############################################################

    def stop(this, testId):

        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide a test id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation SynchroSnifferToggle($input: SynchroSnifferToggleInput!) {
          synchroSnifferToggle(input: $input) {
               clientMutationId
                }
        }"""
        inputs = {"id": testId}
        variables = {"input": inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['synchroSnifferToggle']['clientMutationId']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

        ##############################################################
        ##############################################################

    def createWsHost(this, wireSharkHost):

        if('address' not in wireSharkHost or "name" not in wireSharkHost):
            resp = {"errors": [
                {"message": "Must provide both an address and host name for wireshark host"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation CreateWiresharkHostMutation($input: CreateWiresharkHostInput!) {
        createWiresharkHost(input: $input) {
				wiresharkHostEdge{
                              node{
                              id
                              address
                              }
                            }}}"""

        variables = {
            'input': {'name': wireSharkHost['name'], 'address': wireSharkHost['address']}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createWiresharkHost']['wiresharkHostEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

        ##############################################################
        ##############################################################

    def createWsSelection(this, wiresharkSelection):

        if('testId' not in wiresharkSelection):
            resp = {"errors": [
                {"message": "Must provide an id of a test for the wireShark selection"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        wiresharkSelection['id'] = wiresharkSelection['testId']

        query = """mutation CreateWiresharkSelectionMutation($input: CreateWiresharkSelectionInput!) {
            createWiresharkSelection(input: $input) {
    			wiresharkSelectionEdge{
            node{
              id
              wiresharkHost
            }
          }
              }}"""

        inputs = {}

        for k, v in wiresharkSelection.items():
            if (k == "id" or k == "wiresharkHost"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createWiresharkSelection']['wiresharkSelectionEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]
    ##############################################################
    ##############################################################

    def createWireshark(this, wireShark):
       
        if('testId' not in wireShark):
            resp = {"errors": [
                {"message": "Must provide an id of a test for the wireShark selection"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        inputs = {'testId': wireShark['testId']}

        host, errors = this.createWsHost(wireShark)
        if (errors is not None):
            return (host, errors)
        inputs['wiresharkHost'] = host['id']

        return this.createWsSelection(inputs)

    ##############################################################
    ##############################################################

    def updateWsHost(this, wiresharkHost):

        if('id' not in wiresharkHost):
            resp = {"errors": [
                {"message": "Must provide a wireshark id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeWiresharkHostMutation($input: ChangeWiresharkHostInput!) {
            changeWiresharkHost(input:$input){
                    wiresharkHost{
                   	  name
                      id
                      address
                    }
                    }
                  }


        """
        inputs = {}

        for k, v in wiresharkHost.items():
            if (k == "id" or k == "name" or k == "address"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeWiresharkHost']['wiresharkHost']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def readAllWsHosts(this):
       
        query = """query{
            viewer {
                wiresharkHosts{
                  edges{
                    node{
                      name
                      address
                      id
                    }
                  }

                }
            }
        }"""

        inputs = {}

        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            edges = resp['data']['viewer']['wiresharkHosts']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes

        return [resp[k] for k in ('data', 'errors')]
    ##############################################################
    ##############################################################

    def removeWsHostbyAddr(this, address):
       
        if(address is None):
            resp = {"errors": [
                {"message": "Must provide a wireshark host address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation removeWiresharkHostByAddress($input: RemoveWiresharkHostByAddressInput!) {
                      removeWiresharkHostByAddress(input: $input) {
                        deletedWiresharkHostId
                      }
                    }"""
        variables = {'input': {'address': address}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeWiresharkHostByAddress']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def removeAllWsHosts(this):

        query = """mutation RemoveWiresharkHostsMutation($input: RemoveWiresharkHostsInput!) {
              removeWiresharkHosts(input: $input) {
                deletedWiresharkHostIds
              }
            }"""
        variables = {'input': {}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeWiresharkHosts']['deletedWiresharkHostIds']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def updateWsSelection(this, wsSelection):

        if('id' not in wsSelection):
            resp = {"errors": [
                {"message": "Must provide a wireshark selection id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """mutation ChangeWiresharkSelectionMutation($input: ChangeWiresharkSelectionInput!) {
                      changeWiresharkSelection(input: $input) {
                        wiresharkSelection {
                        id
                        wiresharkHost
                        }
                      }
                    }
                    """
        inputs = {}

        for k, v in wsSelection.items():
            if (k == "id" or k == "wiresharkHost"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeWiresharkSelection']['wiresharkSelection']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def removeWsSelection(this, id):

        if(id is None):
            resp = {"errors": [
                {"message": "Must provide a wireshark selection id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveWiresharkSelectionsMutation($input:RemoveWiresharkSelectionInput!) {
            		removeWiresharkSelection(input:$input){
                  deletedWiresharkSelectionId
                }}"""

        variables = {'input': {'id': id}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeWiresharkSelection']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def removeAllWsSelections(this, testId):
    
        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide a valid testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveWiresharkSelectionsMutation($input:RemoveWiresharkSelectionsInput!) {
            		removeWiresharkSelections(input:$input){
                  deletedWiresharkSelectionIds
                }}"""

        variables = {'input': {'id': testId}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeWiresharkSelections']['deletedWiresharkSelectionIds']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

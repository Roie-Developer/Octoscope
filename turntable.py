class Turntable:

    def __init__(this, octobox):
        this.octobox = octobox

    ##############################################################
    ##############################################################

    def findTurntable(this, turn):

        if('address' not in turn):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation FindTurntableMutation($input: FindTurntableInput!) {
            findTurntable(input: $input) {
              turntable {
                id
                address
                devName
                devSerial
                devType
                etherMac
                gateway
                subnet
                versionFirmware
              }
            }
          }"""

        inputs = {}
        for k, v in turn.items():
            if (k == "address"):
                inputs[k] = v

        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['findTurntable']['turntable']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def createTurntable(this, turn):

        query = """mutation CreateTurntableMutation($input: CreateTurntableInput!) {
          createTurntable(input: $input) {
            turntableEdge {
              __typename
              cursor
              node {
                id
                address
                devName
                devSerial
                devType
                etherMac
                gateway
                subnet
                versionFirmware
              }
            }
          }
        }"""

        inputs = {}
        for k, v in turn.items():
            if (k == "address" or k == "devName" or k == "devSerial" or k == "devType" or k == "etherMac"
                    or k == "gateway"or k == "subnet"or k == "versionFirmware"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createTurntable']['turntableEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def create(this, turn):

        fTurn, errors = this.findTurntable(turn)

        if (errors is not None):
            return (fTurn, errors)

        for k, v in turn.items():
            if (k == "address" or k == "devName" or k == "devSerial" or k == "devType" or k == "etherMac"
                    or k == "gateway"or k == "subnet"or k == "versionFirmware"):
                fTurn[k] = v

        return this.createTurntable(fTurn)

    ##############################################################
    ##############################################################

    def update(this, turn):

        if('id' not in turn):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """mutation ChangeTurntableMutation($input: ChangeTurntableInput!) {
                changeTurntable(input: $input) {
                turntable{
                    id
                    address
                    devName
                    devSerial
                    devType
                    etherMac
                    gateway
                    subnet
                    versionFirmware
                  }
                }
              }"""
        inputs = {}
        for k, v in turn.items():
            if (k == "id" or k == "address" or k == "devName" or k == "devSerial" or k == "devType" or k == "etherMac"
                    or k == "gateway"or k == "subnet"or k == "versionFirmware"):
                inputs[k] = v

        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeTurntable']['turntable']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


##############################################################
##############################################################


    def readAll(this):

        query = """{
              viewer {
                turntables{
                  edges {
                    node {
                      id
                      address
                      devName
                      devSerial
                      devType
                      etherMac
                      gateway
                      subnet
                      versionFirmware

                    }
                  }
                }
              }
            }"""
        variables = {}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['turntables']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]
##############################################################
##############################################################

    def delete(this, turn):

        if('address' not in turn and 'id' not in turn):
            resp = {"errors": [
                {"message": "Must provide either an id or address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """
            mutation removeTurntable($input: RemoveTurntableInput!) {
                removeTurntable(input: $input) {
                    deletedTurntableId
                }
            }
            """

        inputs = {}
        for k, v in turn.items():
            if (k == "id" or k == "address"):
                inputs[k] = v

        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeTurntable']['deletedTurntableId']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def readByAddr(this, turn):

        if('address' not in turn):
            resp = {"errors": [
                {"message": "Must provide either an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($address: String!) {
            viewer {
                turntableByAddr(address: $address) {
                id
                address
                gateway
                subnet
                devName
                devSerial
                devType
                etherMac
                versionFirmware


                }
            }
        }"""
        inputs = {}
        for k, v in turn.items():
            if (k == "address"):
                inputs[k] = v

        variables = inputs

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['turntableByAddr']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

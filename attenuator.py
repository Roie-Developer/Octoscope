
class Attenuator:

    def __init__(this, octobox):
        this.octobox = octobox

    def create(this, obj):
       

        if('address' not in obj):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        disc, errors = this.discover(obj)
        if (errors is not None):
            return (disc, errors)

        for k, v in obj.items():
            if (k == "id" or k == "address" or k == "gateway" or k == "subnet" or k == "devName"
                or k == "devSerial" or k == "devType" or k == "etherMac" or k == "versionFirmware"
                    or k == "usedById" or k == "dbMax" or k == "rfCount"):
                disc[k] = v

        return this.createAttenuator(disc)

###############################################################################
##############################################################################

    def delete(this, obj):

        if('address' not in obj and 'id' not in obj):
            resp = {"errors": [
                {"message": "Must provide either an id or address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveAttenuatorMutation($input: RemoveAttenuatorInput!) {
          removeAttenuator(input: $input) {
            deletedAttenuatorId
          }
        }"""

        inputs = {}
        for k, v in obj.items():
            if (k == "id" or k == "address"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeAttenuator']['deletedAttenuatorId']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def createAttenuator(this, obj):
        query = """mutation CreateAttenuatorMutation($input: CreateAttenuatorInput!) {
        createAttenuator(input: $input) {
        attenuatorEdge {
            __typename
            cursor
            node {
            id
            devName
            address
            gateway
            subnet
            devSerial
            devType
            etherMac
            versionFirmware
            usedById
            dbMax
            rfCount
            }
        }
        }
        }"""

        inputs = {}

        for k, v in obj.items():
            if (k == "devName" or k == "address"
                or k == "gateway" or k == "subnet"or k == "devSerial"
                or k == "devType" or k == "etherMac" or k == "versionFirmware"
                    or k == "usedById" or k == "dbMax" or k == "rfCount"):
                inputs[k] = v
        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createAttenuator']['attenuatorEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def update(this, obj):

        if('id' not in obj):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeAttenuatorMutation(
            $input: ChangeAttenuatorInput!
          ) {
            changeAttenuator(input: $input) {
              attenuator {
                id
                devName
                address
                gateway
                subnet
                devSerial
                devType
                etherMac
                versionFirmware
                usedById
                dbMax
                rfCount
              }
            }
          }"""
        inputs = {}
        for k, v in obj.items():
            if (k == "id" or k == "devName" or k == "address"
                or k == "gateway" or k == "subnet"or k == "devSerial"
                or k == "devType" or k == "etherMac" or k == "versionFirmware"
                    or k == "usedById" or k == "dbMax" or k == "rfCount"):
                inputs[k] = v
        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeAttenuator']['attenuator']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def readAll(this):

        query = """{
            viewer {
            attenuators {
                edges {
                node {
                    id
                    devName
                    address
                    gateway
                    subnet
                    devSerial
                    devType
                    etherMac
                    versionFirmware
                    usedById
                    dbMax
                    rfCount
                }
                }
            }
            }
        }"""

        variables = {}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['attenuators']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def read(this, obj):
       
        if('address' not in obj and 'id' not in obj):
            resp = {"errors": [
                {"message": "Must provide either an id or address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('id' in obj):
            qType = ['id', 'ID', '']
        else:
            qType = ['address', 'String', 'ByAddr']

        query = """query (${0}: {1}!) {{
            viewer {{
              attenuator{2}({0}: ${0}) {{
                id
                devName
                address
                gateway
                subnet
                devSerial
                devType
                etherMac
                versionFirmware
                usedById
                dbMax
                rfCount
            }}
          }}
        }}""".format(*qType)
        inputs = {}
        for k, v in obj.items():
            if (k == "id" or k == "address"):
                inputs[k] = v

        variables = inputs

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            if('id' not in obj):
                data = resp['data']['viewer']['attenuatorByAddr']
                resp['data'] = data
            else:
                data = resp['data']['viewer']['attenuator']
                resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def discover(this, obj):
      
        if('address' not in obj):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation FindAttenuatorMutation($input: FindAttenuatorInput!) {
          findAttenuator(input: $input) {
            attenuator {
              devName
              devType
              devSerial
              address
              subnet
              gateway
              dbMax
              rfCount
              etherMac
              versionFirmware
            }
          }
        }"""

        inputs = {}
        for k, v in obj.items():
            if (k == "address"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['findAttenuator']['attenuator']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def updateAttenuator(this, obj):
        
        if('address' not in obj):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query (
                      $address: String!,
                      $atten: [Float],
                      $atten1: Float,
                      $atten2: Float,
                      $atten3: Float,
                      $atten4: Float,
                      $byPass: Boolean,
                      $byPass1: Boolean,
                      $byPass2: Boolean,
                      $byPass3: Boolean,
                      $byPass4: Boolean,
                      $streamDelay: Int,
                      $streamLoopback: Int,
                      $streamRun: Int)
                      {
          viewer {
            attenuatorDeviceUpdate(
              address: $address,
              atten: $atten,
              atten1: $atten1,
              atten2: $atten2,
              atten3: $atten3,
              atten4: $atten4
              byPass: $byPass,
              byPass1: $byPass1,
              byPass2: $byPass2,
              byPass3: $byPass3,
              byPass4: $byPass4,
              streamDelay: $streamDelay,
              streamLoopback: $streamLoopback,
              streamRun: $streamRun)
            }
          }"""

        inputs = {}
        for k, v in obj.items():
            if (k == "address" or k == "atten1" or k == "atten2"
                or k == "atten3" or k == "atten4"or k == "atten"
                    or k == "streamDelay" or k == "streamLoopback" or k == "streamRun"):
                inputs[k] = v

        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, inputs)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['attenuatorDeviceUpdate']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def status(this, obj):
       
        if('address' not in obj):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query ($address: String!) {
          viewer {
            attenuatorStatus(address: $address) {
            atten
              atten1
              atten2
              atten3
              atten4
              byPass1
              byPass2
              byPass3
              byPass4
              streamRun
              streamDelay
              streamLoopback
              streamBufFree
              streamBufCount
            }
          }
        }"""

        inputs = {}
        for k, v in obj.items():
            if (k == "address"):
                inputs[k] = v
        resp = this.octobox.myFetch(query, inputs)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['attenuatorStatus']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def close(this, obj):
      
        if('address' not in obj):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query ($address: String!) {
              viewer {
                attenuatorClose(address: $address)
              }
            }"""
        inputs = {}
        for k, v in obj.items():
            if (k == "address"):
                inputs[k] = v
        resp = this.octobox.myFetch(query, inputs)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['attenuatorClose']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

class Device:

    def __init__(this, octobox):
        this.octobox = octobox

    def delete(this, device): 

        if('id' not in device):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveDeviceMutation($input: RemoveDeviceInput!) {
              removeDevice(input: $input) {
                deletedDeviceId
              }
            }"""

        inputs = {}
        for k, v in device.items():
            if (k == "id"):
                inputs[k] = v
        variables = {
            'input': inputs
        }
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['removeDevice']['deletedDeviceId']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def create(this, device):
        
        inputs = {}
        for k, v in device.items():
            if (k == "devName" or k == "address"
                or k == "gateway" or k == "subnet"or k == "devSerial"
                or k == "devType" or k == "etherMac" or k == "versionFirmware"
                    or k == "usedById"):
                inputs[k] = v
        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['createDevice']['deviceEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def update(this, device):
        
        if('id' not in device):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeDeviceMutation(
            $input: ChangeDeviceInput!
          ) {
            changeDevice(input: $input) {
              device {
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
              }
            }
          }"""

        inputs = {}
        for k, v in device.items():
            if (k == "id" or k == "devName" or k == "address"
                or k == "gateway" or k == "subnet"or k == "devSerial"
                or k == "devType" or k == "etherMac" or k == "versionFirmware"
                    or k == "usedById"):
                inputs[k] = v
        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['changeDevice']['device']
            resp['data'] = data
        else:
            data = resp['data']['changeDevice']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def readAll(this):

        query = """{
           viewer {
             devices {
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
                 }
               }
             }
           }
         }"""
        variables = {}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            edges = resp['data']['viewer']['devices']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def read(this, device):
       
        if('address' not in device and 'id' not in device):
            resp = {"errors": [
                {"message": "Must provide either an id or address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('id' in device):
            qType = ['id', 'ID', '']
        else:
            qType = ['address', 'String', 'ByAddr']

        query = """query (${0}: {1}!) {{
              viewer {{
                device{2}({0}: ${0}) {{
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
              }}
            }}
          }}""".format(*qType)

        inputs = {}
        for k, v in device.items():
            if (k == "id" or k == "address"):
                inputs[k] = v
        variables = inputs

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            if('id' not in device):
                data = resp['data']['viewer']['deviceByAddr']
                resp['data'] = data
            else:
                data = resp['data']['viewer']['device']
                resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def discover(this, device):
        
        if('address' not in device):
            resp = {"errors": [
                {"message": "Must provide an address"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation FindDeviceMutation($input: FindDeviceInput!) {
              findDevice(input: $input) {
                device {
                      devName
                      address
                      gateway
                      subnet
                      devSerial
                      devType
                      etherMac
                      versionFirmware
                    }
                  }
                }"""
        inputs = {}
        for k, v in device.items():
            if (k == "address"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['findDevice']['device']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

class PathLoss:

    def __init__(this, octobox):
        this.octobox = octobox
    ###############################################################################
    ##############################################################################

    def create(this, pl):

        query = """mutation CreatePathLossMutation($input: CreatePathLossInput!) {
          createPathLoss(input: $input) {
            pathLossEdge {
              __typename
              cursor
              node {
                id
                attenuator
                attenuation {
                  value
                }
                mode
                mpe{byPassValue}
              }
            }
          }
        }
        """
        if "testId" in pl:
            id = pl['testId']
            pl['id'] = id

        pl.setdefault('attenuator', None)
        pl.setdefault('mode', 'fixed')
        pl.setdefault('attenuation', {'value': 0})
        pl.setdefault('mpe', {'byPassValue': 0})

        inputs = {}
        for k, v in pl.items():
            if (k == "id" or k == "attenuator" or k == "attenuation"
                    or k == "mpe" or k == "mode"):
                inputs[k] = v

        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createPathLoss']['pathLossEdge']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


############################################################################
############################################################################

    def delete(this, pl):

        if('id' not in pl):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemovePathLossMutation($input: RemovePathLossInput!) {
            removePathLoss(input: $input) {
              deletedPathLossId
            }
          }"""

        inputs = {}
        for k, v in pl.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removePathLoss']['deletedPathLossId']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

############################################################################
############################################################################

    def deleteAll(this, pl):
       
        query = """mutation RemovePathLossesMutation($input: RemovePathLossesInput!) {
          removePathLosses(input: $input) {
            deletedPathLossIds
          }
        }"""

        pl.setdefault('mode', 'fixed')

        inputs = {}
        for k, v in pl.items():
            if (k == "id" or k == "mode"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removePathLosses']['deletedPathLossIds']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def readAll(this, testId):
       

        query = """query ($id: ID!) {
            viewer {
              pathLosses(id: $id) {
                edges {
                  node {
                    id
                    attenuator
                    attenuation {
                      value
                    }
                    mode
                    mpe{byPassValue}
                  }
                }
              }
            }
          }"""

        variables = {'id': testId}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['pathLosses']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

############################################################################
############################################################################

    def update(this, pl):

        if('id' not in pl):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangePathLossMutation($input: ChangePathLossInput!) {
                changePathLoss(input: $input) {
                pathLoss{
                    id
                    attenuator
                  	attenuation{value}
                  	mpe{byPassValue}
                  	mode

                  }
                }
              }"""

        inputs = {}

        for k, v in pl.items():
            if (k == "id" or k == "attenuator" or k == "attenuation"
                    or k == "mpe" or k == "mode"):
                inputs[k] = v

        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changePathLoss']['pathLoss']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

############################################################################
############################################################################

    def read(this, id):

        if('id' is None):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($id: ID!) {
              node(id: $id) {
                ...on PathLoss {
                  id
                  attenuator
                  attenuation{value}
                  mpe{byPassValue}
                  mode
                }
              }
            }"""

        variables = {'id': id}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['node']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

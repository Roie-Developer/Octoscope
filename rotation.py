class Rotation:

    def __init__(this, octobox):
        this.octobox = octobox

    ##############################################################
    ##############################################################

    def create(this, rot):
       
        query = """mutation CreateRotationMutation($input: CreateRotationInput!) {
            createRotation(input: $input) {
              rotationEdge {
                __typename
                cursor
                node {
                  id
                  start
                  stop
                  step
                  trainingInterval
                }
              }
            }
          }"""

        inputs = {}
        for k, v in rot.items():
            if (k == "id" or k == "start" or k == "stop" or k == "step" or k == "trainingInterval" or k == "turntable"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createRotation']['rotationEdge']['node']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def delete(this, rot):

        query = """mutation RemoveRotationMutation($input: RemoveRotationInput!) {
            removeRotation(input: $input) {
              deletedRotationId
            }
          }"""
        inputs = {}
        for k, v in rot.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeRotation']['deletedRotationId']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def deleteAll(this, testId):

        query = """mutation RemoveRotationMutation($input: RemoveRotationsInput!) {
            removeRotations(input: $input) {
              deletedRotationIds
            }
          }"""

        variables = {'input': {'id': testId}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeRotations']['deletedRotationIds']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def readAll(this, testId):
        
        query = """query ($id: ID!) {
            viewer {
            rotations(id: $id) {
            edges {
              node {
                id
                start
                stop
                step
                trainingInterval
                    }
                }
              }
            }
        }"""

        variables = {'id': testId}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['rotations']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def update(this, rot):
        
        query = """mutation ChangeRotationMutation($input: ChangeRotationInput!) {
          changeRotation(input: $input) {
            rotation {
              id
              turntable
              start
              stop
              step
              trainingInterval
            }
          }
        }"""
        inputs = {}
        for k, v in rot.items():
            if (k == "id" or k == "turntable" or k == "start" or k == "stop" or k == "step" or k == "trainingInterval"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeRotation']['rotation']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

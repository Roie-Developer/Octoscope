from src.endpoint import Endpoint


class TrafficPair:
   
    def __init__(this, octobox):
        this.octobox = octobox

    def create(this, tp):

        tp.setdefault('collapse', True)
        tp.setdefault('active', True)

        if('testId' not in tp):
            resp = {"errors": [
                {"message": "Must provide a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation CreateTrafficPairMutation($input: CreateTrafficPairInput!) {
            createTrafficPair(input: $input) {
              trafficPairEdge {
                __typename
                cursor
                node {
                  id
                  active
                  bitrate
                  blockcount
                  bytes
                  connTimeout
                  collapse
                  dscp
                  from
                  to
                  interval
                  length
                  name
                  noDelay
                  parallel
                  setMss
                  udp
                  udpCounters64bit
                  window
                  zerocopy
                  ping
                  pingPayload
                }
              }
            }
          }"""

        tp['id'] = tp.pop('testId')

        variables = {
            'input': tp
        }
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createTrafficPair']['trafficPairEdge']['node']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def update(this, tp):

        if('id' not in tp):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeTrafficPairMutation(
            $input: ChangeTrafficPairInput!
          ) {
            changeTrafficPair(input: $input) {
              trafficPair {
                id
                active
                advanced
                bitrate
                blockcount
                bytes
                collapse
                connTimeout
                dscp
                from
                to
                interval
                length
                name
                noDelay
                parallel
                setMss
                udp
                udpCounters64bit
                window
                zerocopy
                ping
                pingPayload
              }
            }
          }"""
        variables = {'input': tp}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeTrafficPair']['trafficPair']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################

    def restart(this, tp):

        if('id' not in tp):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """mutation TrafficPairRestartMutation($input: TrafficPairRestartInput!) {
          trafficPairRestart(input: $input) {
            trafficPair {
              id
              active
              bitrate
              blockcount
              bytes
              connTimeout
              dscp
              from
              to
              interval
              length
              name
              noDelay
              parallel
              setMss
              udp
              udpCounters64bit
              window
              zerocopy
              ping
              pingPayload
            }
          }
        }"""
        inputs = {}
        for k, v in tp.items():
            if (k == "id"):
                inputs[k] = v

        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['trafficPairRestart']['trafficPair']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def delete(this, tp):

        if('id' not in tp):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveTrafficPairMutation($input: RemoveTrafficPairInput!) {
          removeTrafficPair(input: $input) {
            deletedTrafficPairId
              }
            }"""

        inputs = {}
        for k, v in tp.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['removeTrafficPair']['deletedTrafficPairId']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def read(this, tp):

        if('id' not in tp):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """query ($id: ID!) {
            viewer {
             trafficPair(id:$id) {
                 id
                  active
                  bitrate
                  blockcount
                  bytes
                  connTimeout
                  collapse
                  dscp
                  from
                  to
                  length
                  name
                  noDelay
                  parallel
                  setMss
                  udp
                  udpCounters64bit
                  window
                  zerocopy
                  ping
                  pingPayload

          }
            }}"""

        for k, v in tp.items():
            if (k == "id"):
                id = v

        variables = {'id': id}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['trafficPair']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def readAll(this, testId):

        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query ($id: ID!) {
          viewer {
            trafficPairs(id: $id) {
              edges {
                node {
                  id
                  active
                  advanced
                  collapse
                  from
                  to
                  name
                  bitrate
                  blockcount
                  bytes
                  connTimeout
                  interval
                  parallel
                  length
                  dscp
                  setMss
                  window
                  udp
                  udpCounters64bit
                  noDelay
                  zerocopy
                  version4
                  version6
                  ping
                  pingPayload
                }
              }
            }
          }
        }"""

        variables = {'id': testId}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['trafficPairs']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

###############################################################################
##############################################################################

    def deleteAll(this, testId):

        if(testId is None):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveTrafficPairsMutation($input: RemoveTrafficPairsInput!) {
                removeTrafficPairs(input: $input) {
                 deletedTrafficPairIds
                }
             }"""
        variables = {'input': {
            'id': testId}}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removeTrafficPairs']['deletedTrafficPairIds']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]


###############################################################################
##############################################################################


    def swapEndpoints(this, tp):

        if('id' not in tp):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('from' not in tp):
            resp = {"errors": [
                {"message": "Must provide a from endpoint"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('to' not in tp):
            resp = {"errors": [
                {"message": "Must provide a to endpoint"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        up, errors = this.read(tp)

        hold = up['from']

        up['from'] = up['to']

        up['to'] = hold

        return this.update(up)

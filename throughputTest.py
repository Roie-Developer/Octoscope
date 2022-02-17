class ThroughputTest:

    def __init__(this, octobox):

        this.octobox = octobox

################################################################################
################################################################################

    def create(this, tt):

        if('name' not in tt):
            resp = {"errors": [
                {"message": "Must provide a name"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation CreateThroughputTestMutation($input: CreateThroughputTestInput!) {
          createThroughputTest(input: $input) {
            throughputTestEdge {
              __typename
              cursor
              node {
                description
                id
                reportingInterval
                model
                name
                revision
                testDuration
                settlingTime
                stepDuration
                rvrMode
                quadAttenStart
                quadAttenStep
                quadAttenStop
                trainingInterval
              }
            }
          }
        }"""
        variables = {
            'input': tt
        }

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createThroughputTest']['throughputTestEdge']['node']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

################################################################################
################################################################################

    def changeTestRunning(this, tt):

        if('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeTestRunningMutation($input: ChangeTestRunningInput!) {
            changeTestRunning(input: $input) {
            throughputTest {
              id
              testRunning
                }
              }
            }"""

        variables = {
            'input': {'id': tt['id'], 'testRunning': tt['testRunning']}
        }
        resp = this.octobox.myFetch(query, variables)
        # print("response", resp)
        if (resp['errors'] is None):
            data = resp['data']['changeTestRunning']['throughputTest']['testRunning']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

################################################################################
################################################################################

    def start(this, id):

        if(id is None):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        inputs = {'id': id, 'testRunning': True}

        return this.changeTestRunning(inputs)

################################################################################
################################################################################

    def stop(this, id):

        if(id is None):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        inputs = {'id': id, 'testRunning': False}

        return this.changeTestRunning(inputs)

################################################################################
################################################################################

    def update(this, tt):

        if('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeThroughputTestMutation($input: ChangeThroughputTestInput!) {
              changeThroughputTest(input: $input) {
                throughputTest {
                      description
                      id
                      reportingInterval
                      model
                      name
                      revision
                      testDuration
                      settlingTime
                      stepDuration
                      rvrMode
                      quadAttenStart
                      quadAttenStep
                      quadAttenStop
                      trainingInterval
                }
              }
            }"""
        inputs = {}
        for k, v in tt.items():
            if (k == "id" or k == "reportingInterval"
                    or k == "testDuration" or k == "rvrMode"
                     or k == "quadAttenStart" or k == "settlingTime"
                     or k == "quadAttenStep" or k == "quadAttenStop" or k == "stepDuration"):
                inputs[k] = v
        variables = {
            'input': inputs
        }

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeThroughputTest']['throughputTest']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def read(this, tt):

        if('name' not in tt and 'id' not in tt):
            resp = {"errors": [
                {"message": "Must provide either an id or name"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        if('id' in tt):
            qType = ['id', 'ID', '']
            query = """query(${0}: {1}!) {{
                    viewer {{
                      throughputTest{2}({0}: ${0}) {{
                                id
                                name
                                model
                                revision
                                description
                                reportingInterval
                                settlingTime
                                testDuration
                                csvFilename
                                pdfFilename
                                testRunning
                                testDuration
                                stepDuration
                                rvrMode
                                quadAttenStart
                                quadAttenStep
                                quadAttenStop
                                timeLeft
                                trainingInterval
                                computedDuration
                      }}
                    }}
                }}""".format(*qType)
        else:
            query = """query ($name: String!, $model: String!, $revision: String!) {
                  viewer {
                    throughputTestByName(name: $name, model: $model, revision: $revision) {
                      id
                      name
                      model
                      revision
                      description
                      reportingInterval
                      settlingTime
                      testDuration
                      csvFilename
                      pdfFilename
                      testRunning
                      testDuration
                      stepDuration
                      rvrMode
                      quadAttenStart
                      quadAttenStep
                      quadAttenStop
                      timeLeft
                      trainingInterval
                      computedDuration
                    }
                  }
                }"""

        inputs = {}
        for k, v in tt.items():
            if (k == "name" or k == "id" or k == "revision" or k == "model"):
                inputs[k] = v
        variables = inputs
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            if('id' not in tt):
                data = resp['data']['viewer']['throughputTestByName']
                resp['data'] = data
            else:
                data = resp['data']['viewer']['throughputTest']
                resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def delete(this, tt):

        if('id' not in tt and 'name' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id or name"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation RemoveThroughputTestMutation($input: RemoveThroughputTestInput!) {
            removeThroughputTest(input: $input) {
                deletedThroughputTestId
                }
            }"""

        inputs = {}
        for k, v in tt.items():
            if (k == "id" or k == "name" or k == "model" or k == "revision"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)
        # print("resp", resp)

        if (resp['errors'] is None):
            data = resp['data']['removeThroughputTest']['deletedThroughputTestId']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def readAll(this):

        query = """{
              viewer {
                throughputTests {
                  edges {
                    node {
                    id
                    name
                    model
                    revision
                    description
                    reportingInterval
                    settlingTime
                    testDuration
                    csvFilename
                    pdfFilename
                    testRunning
                    testDuration
                    stepDuration
                    rvrMode
                    quadAttenStart
                    quadAttenStep
                    quadAttenStop
                    timeLeft
                    trainingInterval
                    computedDuration
                    }
                  }
                }
              }
            }"""
        variables = {}
        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            edges = resp['data']['viewer']['throughputTests']['edges']
            nodes = []
            for edge in edges:
                nodes.append(edge['node'])
            resp['data'] = nodes
        return [resp[k] for k in ('data', 'errors')]

################################################################################
################################################################################

    def getData(this, bothIds):

        if('throughputTestId' not in bothIds or 'trafficPairId' not in bothIds):
            resp = {"errors": [
                {"message": 'Must provided both throughputTestId and trafficPairId.'}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($throughputTestId: ID!, $trafficPairId: ID!) {
              viewer {
                throughputData(throughputTestId: $throughputTestId, trafficPairId: $trafficPairId) {
                  timeStamp
                  throughput
                }
              }
            }"""
        throughputTestId = bothIds['throughputTestId']
        trafficPairId = bothIds['trafficPairId']
        variables = {'throughputTestId': throughputTestId,
                     'trafficPairId': trafficPairId}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['throughputData']
            resp['data'] = data
        # else:
        #     data = resp['data']['viewer']
        #     resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def getRvrData(this, tt):

        if('testId' not in tt):
            resp = {"errors": [
                {"message": "Must provide a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($testId: ID!) {
          viewer {
            rvrData(testId: $testId) {
              pairName
              pairId
              avg
              atten
              allAttens
              index
            }
          }
        }"""
        # print("tt input", tt)
        inputs = {}
        for k, v in tt.items():
            if (k == "testId"):
                inputs[k] = v

        variables = inputs
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['rvrData']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def getRvrvoData(this, tt):

        if('testId' not in tt):
            resp = {"errors": [
                {"message": "Must provide a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]
        query = """query($testId: ID!) {
          viewer {
            rvrvoData(testId: $testId) {
              pairName
              pairId
              avg
              atten
              allAttens
              position
              index
            }
          }
        }"""
        inputs = {}
        for k, v in tt.items():
            if (k == "testId"):
                inputs[k] = v

        variables = inputs
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['rvrvoData']
            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

################################################################################
################################################################################

    def getCSV(this, tt):

        if('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeGenCSVMutation($input: ChangeGenCSVInput!) {
          changeGenCSV(input: $input) {
            throughputTest {
              id
              csvFilename
            }
          }
        }"""

        uri = this.octobox.uri
        id = tt['id']
        variables = {'input': {'id': id, 'clearCsvFilename': False}}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeGenCSV']['throughputTest']
            ready, errors = this.isCSVReady(tt)
            while(ready is False):
                this.octobox.sleep(5000)
                ready, errors = this.isCSVReady(tt)
            # if(ready is True):
            #     print("csv ready")

            data['href'] = '{}/csv/{}'.format(
                uri, data['csvFilename'])

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def getPDF(this, tt):

        if ('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangeGenPDFMutation($input: ChangeGenPDFInput!) {
          changeGenPDF(input: $input) {
            throughputTest {
              id
              pdfFilename
            }
          }
        }"""

        uri = this.octobox.uri
        id = tt['id']
        variables = {'input': {'id': id, 'clearPdfFilename': False}}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changeGenPDF']['throughputTest']
            ready, errors = this.isPDFReady(tt)
            while (ready is False):
                this.octobox.sleep(5000)
                ready, errors = this.isPDFReady(tt)
            # if(ready is True):
            #     print("pdf ready")

            data['href'] = '{}/csv/{}'.format(uri, data['pdfFilename'])

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def isTestRunning(this, tt):

        if('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($id: ID!) {
            viewer {
                throughputTest(id: $id) {
                id
                testRunning
                    }
                }
            }"""
        id = tt['id']

        variables = {'id': id}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['viewer']['throughputTest']['testRunning']
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def allTestRunnings(this):
 
        tests, errors = this.readAll()
        runningList = []
        for x in range(len(tests)):
            id = tests[x]['id']
            run, errors = this.isTestRunning({'id': id})
            if(run is True):
                runningList.append(tests[x])

        return runningList, errors

    ############################################################################
    ############################################################################

    def isCSVReady(this, tt):

        if('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($id: ID!) {
            viewer {
              throughputTest(id: $id) {
                id
                csvFilename
              }
            }
        }"""
        id = tt['id']
        variables = {'id': id}

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['throughputTest']

            data = bool(data['csvFilename'])
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

    ############################################################################
    ############################################################################

    def isPDFReady(this, tt):

        if ('id' not in tt):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($id: ID!) {
            viewer {
              throughputTest(id: $id) {
                id
                pdfFilename
              }
            }
        }"""
        id = tt['id']
        variables = {'id': id}

        resp = this.octobox.myFetch(query, variables)
        if (resp['errors'] is None):
            data = resp['data']['viewer']['throughputTest']

            data = bool(data['pdfFilename'])
            resp['data'] = data
        return [resp[k] for k in ('data', 'errors')]

################################################################################
################################################################################

    def testProgress(this, tt):
        
        if('id' not in tt and 'name' not in tt):
            resp = {"errors": [
                {"message": "Must provide either an id or name"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        test, errors = this.read(tt)
        return test['timeLeft']

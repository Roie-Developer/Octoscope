class Pal6Config:

    def __init__(this, octobox):
        this.octobox = octobox

    ##############################################################
    ##############################################################

    def create(this, pal6):

        if('testId' not in pal6):
            resp = {"errors": [
                {"message": "Must provide a test id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation createPal6ConfigByEp($input: CreatePal6ConfigInput!) {
                  createPal6Config(input: $input) {
                    pal6ConfigEdge {
                      node {
                        id
                        testId
                        endpoint
                        apStaMode
                        bandwidth
                        beaconInterval
                        beamformeeMUEnable
                        beamformeeSUEnable
                        beamformerMUEnable
                        beamformerSUEnable
                        bridgeEnable
                        bssid
                        bssidMode
                        captureEnable
                        chainRXMask
                        chainTXMask
                        channelScanList
                        channelScanMode
                        ctsRtsThreshold
                        dfsEnable
                        filterHeadersOnly
                        filterManagementOnly
                        fragmentationThreshold
                        guardInterval
                        interface_
                        ipAddress
                        ipGateway
                        ipMode
                        ipNetmask
                        kBeaconReportActiveEnable
                        kBeaconReportPassiveEnable
                        kBeaconReportTableEnable
                        kChannelReportEnable
                        kEnable
                        kLinkMeasEnable
                        kLogging
                        kNeighborEnable
                        maxAMPDUFrameSize
                        netcatPort
                        ofdmaDLEnable
                        ofdmaULEnable
                        palRadio
                        password
                        primaryChannel
                        priority
                        probeID
                        rate
                        rEnable
                        rFastTransitionEnable
                        rLogging
                        rMode
                        roamTargetThreshold
                        roamThreshold
                        secondaryChannel_8080
                        security
                        ssid
                        streams
                        triggerOutMode
                        triggerOutPacketFilterMask
                        triggerOutScriptCmd
                        txAtten
                        uApsdDtimInterval
                        uApsdEnable
                        vEnable
                        vLogging
                        vstaCount
                        vTransitionMgtEnable
                      }
                    }
                  }
                }

                        """
        pal6.setdefault('palRadio', "RADIO_24")
        pal6.setdefault('apStaMode', "MODE_AP")
        pal6.setdefault('beaconInterval', 100)
        pal6.setdefault('bridgeEnable', False)
        pal6.setdefault('ctsRtsThreshold', 2347)
        pal6.setdefault('dfsEnable', True)
        pal6.setdefault('fragmentationThreshold', 2346)
        pal6.setdefault('ofdmaDLEnable', False)
        pal6.setdefault('ofdmaULEnable', False)
        pal6.setdefault('roamTargetThreshold', -95)
        pal6.setdefault('roamThreshold', -95)
        pal6.setdefault('interface_', "INTERFACE_AX")
        pal6.setdefault('ipAddress', pal6['ipAddress'])
        pal6.setdefault('ipMode', "IP_STATIC")
        pal6.setdefault('ssid', " ")
        pal6.setdefault('streams', 4)
        pal6.setdefault('captureEnable', False)
        pal6.setdefault('guardInterval', "GUARD_0_8US")
        pal6.setdefault('ipNetmask', "255.255.255.0")
        pal6.setdefault('rate', 1)
        pal6.setdefault('primaryChannel', 36)
        pal6.setdefault('bandwidth', "BANDWIDTH_40_ADAPT")
        pal6.setdefault('priority', "PRIORITY_BESTEFFORT")
        pal6.setdefault('security', 'SECURITY_NONE')
        pal6.setdefault('password', "")
        pal6.setdefault('triggerOutMode', 'TMODE_DISABLE')

        pal6['id'] = pal6['testId']

        inputs = {}
        for k, v in pal6.items():
            if (k == "id" or k == "endpoint" or k == "apStaMode"
                or k == "primaryChannel"or k == "secondaryChannel_8080" or k == "bandwidth"
                or k == "interface_" or k == "beamformeeMUEnable" or k == "beamformeeMUEnable"
                or k == "beamformeeSUEnable" or k == "beamformerMUEnable" or k == "beamformerSUEnable"
                or k == "bridgeEnable" or k == "chainRXMask" or k == "chainTXMask"
                or k == "ctsRtsThreshold" or k == "dfsEnable" or k == "fragmentationThreshold"
                or k == "guardInterval" or k == "ipAddress" or k == "ipMode"
                or k == "ipNetmask" or k == "kBeaconReportActiveEnable" or k == "kBeaconReportPassiveEnable"
                or k == "kBeaconReportTableEnable" or k == "kChannelReportEnable" or k == "kEnable" or k == "kLinkMeasEnable"
                or k == "kLogging" or k == "kNeighborEnable" or k == "maxAMPDUFrameSize" or k == "ofdmaDLEnable"
                or k == "ofdmaULEnable" or k == "password" or k == "priority" or k == "rate"
                or k == "rEnable" or k == "rLogging" or k == "rMode" or k == "security"
                or k == "ssid" or k == "streams" or k == "txAtten" or k == "uApsdEnable"
                or k == "vEnable" or k == "vLogging" or k == "vTransitionMgtEnable" or k == "beaconInterval"
                or k == "uApsdDtimInterval" or k == "bssid" or k == "bssidMode" or k == "channelScanList"
                or k == "channelScanMode" or k == "roamTargetThreshold" or k == "roamThreshold" or k == "vstaCount" or k == "captureEnable"
                or k == "filterManagementOnly" or k == "filterHeadersOnly" or k == "probeID" or k == "netcatPort"
                or k == "triggerOutMode" or k == "triggerOutPacketFilterMask" or k == "triggerOutScriptCmd"
                    or k == "palRadio" or k == "rFastTransitionEnable" or k == "ipGateway"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['createPal6Config']['pal6ConfigEdge']['node']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def update(this, pal6):
        if('id' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangePal6Config($input:ChangePal6ConfigInput!){
                  changePal6Config(input:$input){
                    pal6Config{
                     id
                     testId
                     endpoint
                     apStaMode
                     bandwidth
                     beaconInterval
                     beamformeeMUEnable
                     beamformeeSUEnable
                     beamformerMUEnable
                     beamformerSUEnable
                     bridgeEnable
                     bssid
                     bssidMode
                     captureEnable
                     chainRXMask
                     chainTXMask
                     channelScanList
                     channelScanMode
                     ctsRtsThreshold
                     dfsEnable
                     filterHeadersOnly
                     filterManagementOnly
                     fragmentationThreshold
                     guardInterval
                     interface_
                     ipAddress
                     ipGateway
                     ipMode
                     ipNetmask
                     kBeaconReportActiveEnable
                     kBeaconReportPassiveEnable
                     kBeaconReportTableEnable
                     kChannelReportEnable
                     kEnable
                     kLinkMeasEnable
                     kLogging
                     kNeighborEnable
                     maxAMPDUFrameSize
                     netcatPort
                     ofdmaDLEnable
                     ofdmaULEnable
                     palRadio
                     password
                     primaryChannel
                     priority
                     probeID
                     rate
                     rEnable
                     rFastTransitionEnable
                     rLogging
                     rMode
                     roamTargetThreshold
                     roamThreshold
                     secondaryChannel_8080
                     security
                     ssid
                     streams
                     triggerOutMode
                     triggerOutPacketFilterMask
                     triggerOutScriptCmd
                     txAtten
                     uApsdDtimInterval
                     uApsdEnable
                     vEnable
                     vLogging
                     vstaCount
                     vTransitionMgtEnable
                    }
                  }

                }"""
        inputs = {}
        for k, v in pal6.items():
            if (k == "id" or k == "endpoint" or k == "apStaMode" or k == "testId"
                or k == "primaryChannel"or k == "secondaryChannel_8080" or k == "bandwidth"
                or k == "interface_" or k == "beamformeeMUEnable" or k == "beamformeeMUEnable"
                or k == "beamformeeSUEnable" or k == "beamformerMUEnable" or k == "beamformerSUEnable"
                or k == "bridgeEnable" or k == "chainRXMask" or k == "chainTXMask"
                or k == "ctsRtsThreshold" or k == "dfsEnable" or k == "fragmentationThreshold"
                or k == "guardInterval" or k == "ipAddress" or k == "ipMode"
                or k == "ipNetmask" or k == "kBeaconReportActiveEnable" or k == "kBeaconReportPassiveEnable"
                or k == "kBeaconReportTableEnable" or k == "kChannelReportEnable" or k == "kEnable" or k == "kLinkMeasEnable"
                or k == "kLogging" or k == "kNeighborEnable" or k == "maxAMPDUFrameSize" or k == "ofdmaDLEnable"
                or k == "ofdmaULEnable" or k == "password" or k == "priority" or k == "rate"
                or k == "rEnable" or k == "rLogging" or k == "rMode" or k == "security"
                or k == "ssid" or k == "streams" or k == "txAtten" or k == "uApsdEnable"
                or k == "vEnable" or k == "vLogging" or k == "vTransitionMgtEnable" or k == "beaconInterval"
                or k == "uApsdDtimInterval" or k == "bssid" or k == "bssidMode" or k == "channelScanList"
                or k == "channelScanMode" or k == "roamTargetThreshold" or k == "roamThreshold" or k == "vstaCount" or k == "captureEnable"
                or k == "filterManagementOnly" or k == "filterHeadersOnly" or k == "probeID" or k == "netcatPort"
                    or k == "triggerOutMode" or k == "triggerOutPacketFilterMask" or k == "triggerOutScriptCmd" or k == "palRadio" or k == "rFastTransitionEnable" or k == "ipGateway"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)
        # print("resp", resp)

        if (resp['errors'] is None):
            data = resp['data']['changePal6Config']['pal6Config']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def updateByEP(this, pal6):
        if('endpoint' not in pal6 or 'testId' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an endpoint id as well as a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation ChangePal6ConfigByEp($input:ChangePal6ConfigByEpInput!){
                  changePal6ConfigByEp(input:$input){
                    pal6Config{
                     id
                     testId
                     endpoint
                     apStaMode
                     bandwidth
                     beaconInterval
                     beamformeeMUEnable
                     beamformeeSUEnable
                     beamformerMUEnable
                     beamformerSUEnable
                     bridgeEnable
                     bssid
                     bssidMode
                     captureEnable
                     chainRXMask
                     chainTXMask
                     channelScanList
                     channelScanMode
                     ctsRtsThreshold
                     dfsEnable
                     filterHeadersOnly
                     filterManagementOnly
                     fragmentationThreshold
                     guardInterval
                     interface_
                     ipAddress
                     ipGateway
                     ipMode
                     ipNetmask
                     kBeaconReportActiveEnable
                     kBeaconReportPassiveEnable
                     kBeaconReportTableEnable
                     kChannelReportEnable
                     kEnable
                     kLinkMeasEnable
                     kLogging
                     kNeighborEnable
                     maxAMPDUFrameSize
                     netcatPort
                     ofdmaDLEnable
                     ofdmaULEnable
                     palRadio
                     password
                     primaryChannel
                     priority
                     probeID
                     rate
                     rEnable
                     rFastTransitionEnable
                     rLogging
                     rMode
                     roamTargetThreshold
                     roamThreshold
                     secondaryChannel_8080
                     security
                     ssid
                     streams
                     triggerOutMode
                     triggerOutPacketFilterMask
                     triggerOutScriptCmd
                     txAtten
                     uApsdDtimInterval
                     uApsdEnable
                     vEnable
                     vLogging
                     vstaCount
                     vTransitionMgtEnable
                    }
                  }

                }"""
        inputs = {}
        for k, v in pal6.items():
            if (k == "id" or k == "endpoint" or k == "apStaMode" or k == "testId"
                or k == "primaryChannel"or k == "secondaryChannel_8080" or k == "bandwidth"
                or k == "interface_" or k == "beamformeeMUEnable" or k == "beamformeeMUEnable"
                or k == "beamformeeSUEnable" or k == "beamformerMUEnable" or k == "beamformerSUEnable"
                or k == "bridgeEnable" or k == "chainRXMask" or k == "chainTXMask"
                or k == "ctsRtsThreshold" or k == "dfsEnable" or k == "fragmentationThreshold"
                or k == "guardInterval" or k == "ipAddress" or k == "ipMode"
                or k == "ipNetmask" or k == "kBeaconReportActiveEnable" or k == "kBeaconReportPassiveEnable"
                or k == "kBeaconReportTableEnable" or k == "kChannelReportEnable" or k == "kEnable" or k == "kLinkMeasEnable"
                or k == "kLogging" or k == "kNeighborEnable" or k == "maxAMPDUFrameSize" or k == "ofdmaDLEnable"
                or k == "ofdmaULEnable" or k == "password" or k == "priority" or k == "rate"
                or k == "rEnable" or k == "rLogging" or k == "rMode" or k == "security"
                or k == "ssid" or k == "streams" or k == "txAtten" or k == "uApsdEnable"
                or k == "vEnable" or k == "vLogging" or k == "vTransitionMgtEnable" or k == "beaconInterval"
                or k == "uApsdDtimInterval" or k == "bssid" or k == "bssidMode" or k == "channelScanList"
                or k == "channelScanMode" or k == "roamTargetThreshold" or k == "roamThreshold" or k == "vstaCount" or k == "captureEnable"
                or k == "filterManagementOnly" or k == "filterHeadersOnly" or k == "probeID" or k == "netcatPort"
                    or k == "triggerOutMode" or k == "triggerOutPacketFilterMask" or k == "triggerOutScriptCmd" or k == "palRadio"
                    or k == "rFastTransitionEnable" or k == "ipGateway"):
                inputs[k] = v
        variables = {'input': inputs}
        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['changePal6ConfigByEp']['pal6Config']

            resp['data'] = data

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def remove(this, pal6):

        if('id' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """ mutation RemovePal6Config($input:RemovePal6ConfigInput!){
                        removePal6Config(input:$input){
                        deletedPal6ConfigId
                        }
                    }
                    """
        inputs = {}
        for k, v in pal6.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removePal6Config']['deletedPal6ConfigId']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def read(this, pal6):

        if('id' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """query($id: ID!) {
              node(id: $id) {
                ...on Pal6Config {
                    id
                     endpoint
                     apStaMode
                     bandwidth
                     beaconInterval
                     beamformeeMUEnable
                     beamformeeSUEnable
                     beamformerMUEnable
                     beamformerSUEnable
                     bridgeEnable
                     bssid
                     bssidMode
                     captureEnable
                     chainRXMask
                     chainTXMask
                     channelScanList
                     channelScanMode
                     ctsRtsThreshold
                     dfsEnable
                     filterHeadersOnly
                     filterManagementOnly
                     fragmentationThreshold
                     guardInterval
                     interface_
                     ipAddress
                     ipGateway
                     ipMode
                     ipNetmask
                     kBeaconReportActiveEnable
                     kBeaconReportPassiveEnable
                     kBeaconReportTableEnable
                     kChannelReportEnable
                     kEnable
                     kLinkMeasEnable
                     kLogging
                     kNeighborEnable
                     maxAMPDUFrameSize
                     netcatPort
                     ofdmaDLEnable
                     ofdmaULEnable
                     palRadio
                     password
                     primaryChannel
                     priority
                     probeID
                     rate
                     rEnable
                     rFastTransitionEnable
                     rLogging
                     rMode
                     roamTargetThreshold
                     roamThreshold
                     secondaryChannel_8080
                     security
                     ssid
                     streams
                     triggerOutMode
                     triggerOutPacketFilterMask
                     triggerOutScriptCmd
                     txAtten
                     uApsdDtimInterval
                     uApsdEnable
                     vEnable
                     vLogging
                     vstaCount
                     vTransitionMgtEnable

                }
              }
            }"""

        for k, v in pal6.items():
            if (k == "id"):
                id = v
        variables = {'id': id}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['node']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    def pushOne(this, pal6):

        if('id' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation PushPal6ConfigOneMutation($input: PushPal6ConfigOneInput!) {
            pushPal6ConfigOne(input: $input) {
              pal6Config {
                id
              }
            }
          }"""

        inputs = {}

        for k, v in pal6.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['pushPal6ConfigOne']['pal6Config']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################

    def pushAll(this, pal6):

        if('testId' not in pal6):
            resp = {"errors": [
                {"message": "Must provide a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """mutation PushPal6ConfigAllMutation($input: PushPal6ConfigAllInput!) {
            pushPal6ConfigAll(input: $input) {
              pushedPal6ConfigIds
            }
          }"""
        inputs = {}
        pal6['id'] = pal6['testId']
        for k, v in pal6.items():
            if (k == "id"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['pushPal6ConfigAll']['pushedPal6ConfigIds']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################

    def removeAll(this, testId):

        if('testId' is None):
            resp = {"errors": [
                {"message": "Must provide a testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """ mutation RemovePal6Configs($input:RemovePal6ConfigsInput!){
                        removePal6Configs(input:$input){
                        deletedPal6ConfigIds
                        }
                    }
                    """

        variables = {'input': {'id': testId}}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removePal6Configs']['deletedPal6ConfigIds']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def removeByEp(this, pal6):

        if('testId' not in pal6 or 'endpoint' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an endpoint and testId"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """ mutation RemovePal6ConfigByEp($input:RemovePal6ConfigByEpInput!){
                        removePal6ConfigByEp(input:$input){
                        deletedPal6ConfigId
                        }
                    }
                    """
        inputs = {}
        for k, v in pal6.items():
            if (k == "testId" or k == "endpoint"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['removePal6ConfigByEp']['deletedPal6ConfigId']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]



    ##############################################################
    ##############################################################

    def updateBandConfig(this, pal6):

        if('id' not in pal6 or 'bandConfig' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id and bandConfig"}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """ mutation UpdateBandConfig($input: UpdateBandConfigInput!) {
                    updateBandConfig(input: $input) {
                        
                        bandConfig
                        
                    }
                    }

                    """
        inputs = {}
        for k, v in pal6.items():
            if (k == "id" or k == "bandConfig"):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['updateBandConfig']
            resp['data'] = data
        # else:
        #     resp['data'] = None

        return [resp[k] for k in ('data', 'errors')]

    ##############################################################
    ##############################################################

    def readBandConfg(this, pal6):

        if('id' not in pal6):
            resp = {"errors": [
                {"message": "Must provide an id "}], "data": None}
            return [resp[k] for k in ('data', 'errors')]

        query = """ mutation ReadBandConfig($input: ReadBandConfigInput!) {
            readBandConfig(input: $input) {
    				bandConfig
              
            }
          }
                    """
        inputs = {}
        for k, v in pal6.items():
            if (k == "id" ):
                inputs[k] = v
        variables = {'input': inputs}

        resp = this.octobox.myFetch(query, variables)

        if (resp['errors'] is None):
            data = resp['data']['readBandConfig']
            resp['data'] = data
        # else:
        #     resp['data'] = None
        return [resp[k] for k in ('data', 'errors')]

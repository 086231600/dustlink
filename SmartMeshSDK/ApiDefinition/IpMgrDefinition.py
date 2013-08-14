#!/usr/bin/python

import ApiDefinition
import ByteArraySerializer

class IpMgrDefinition(ApiDefinition.ApiDefinition):
    '''
    \ingroup ApiDefinition
    \brief API definition for the IP manager.
   
    \note This class inherits from ApiDefinition. It redefines the attributes of
          its parents class, but inherits the methods.
    '''
    
    STRING    = ApiDefinition.FieldFormats.STRING
    BOOL      = ApiDefinition.FieldFormats.BOOL
    INT       = ApiDefinition.FieldFormats.INT
    INTS      = ApiDefinition.FieldFormats.INTS
    HEXDATA   = ApiDefinition.FieldFormats.HEXDATA
    RC        = ApiDefinition.ApiDefinition.RC
    SUBID1    = ApiDefinition.ApiDefinition.SUBID1
    SUBID2    = ApiDefinition.ApiDefinition.SUBID2
    RC_OK     = ApiDefinition.ApiDefinition.RC_OK
    
    def __init__(self):
        self.serializer = ByteArraySerializer.ByteArraySerializer(self)
    
    def default_serializer(self,commandArray,fieldsToFill):
        '''
        \brief IpMgrDefinition-specific implementation of default serializer
       
        \param commandArray   An array of the form [commandName, subCommandname]
                              The array can be of any length, and is of length 1
                              if no subcommands are used.
        \param fieldsToFill   The list of fields to send, organized as a
                              dictionary of the form
                              <tt>fieldname:fieldvalue</tt>.
       
        \returns id,byteString where id is the command ID and byteArray an array
                               of bytes
        '''
        return self.serializer.serialize(commandArray,fieldsToFill)
    
    def deserialize(self,type,cmdId,byteArray):
        '''
        \brief IpMgrDefinition-specific implementation of deserializer
        '''
        return self.serializer.deserialize(type,cmdId,byteArray)
    
    # We redefine this attribute inherited from ApiDefinition. See
    # ApiDefinition for a full description of the structure of this field.
    fieldOptions = {
        # 'notificationTypes' : [
        #     [ 1,   'event',                 'Event notification'],
        #     [ 2,   'log',                   'Log notification'],
        #     [ 4,   'data',                  'Data payload notification'],
        #     [ 5,   'ipData',                '6lowpan packet notification'],
        #     [ 6,   'healthReport',          'Health report notification'],
        # ],
        # 'eventTypes' : [
        #     [ 0,   'moteReset',             'A mote reset'],
        #     [ 1,   'networkReset',          'The network was reset'],
        #     [ 2,   'commandFinish ',        'A command has completed execution'],
        #     [ 3,   'moteJoin',              'A mote joined the network'],
        #     [ 4,   'moteOperational',       'A new mote was configured and is now operational'],
        #     [ 5,   'moteLost',              'A mote is no longer communicating in the network'],
        #     [ 6,   'netTime',               'Contains the network uptime (in response to a getTime command)'],
        #     [ 7,   'pingResponse',          'A reply was received from a mote ping'],
        #     [10,   'pathCreate',            'A path was created'],
        #     [11,   'pathDelete',            'A path was deleted'],
        #     [12,   'packetSent',            'A packet was sent'],
        #     [13,   'moteCreate',            'A mote was created'],
        #     [14,   'moteDelete',            'A mote was deleted'],
        # ],
        RC : [
            [ 0,   'OK',                    'The application layer has processed the command correctly'],
            [ 1,   'RC_INVALID_COMMAND',    'Invalid command'],
            [ 2,   'RC_INVALID_ARGUMENT',   'Invalid argument'],
            [ 3,   'INVALID_AUTHENTICATION','Invalid Authentication (MUX)'],
            [ 4,   'INVALID_API_VERSION',   'Invalid API version (MUX)'],
            [ 5,   'comd_timeout',          'command timeout (MUX)'],
            [11,   'RC_END_OF_LIST',        'End of list is returned when an iteration reaches the end of the list of objects'],
            [12,   'RC_NO_RESOURCES',       'Reached maximum number of items'],
            [13,   'RC_IN_PROGRESS',        'Operation is in progress'],
            [14,   'RC_NACK',               'Negative acknowledgment'],
            [15,   'RC_WRITE_ERROR',        'Flash write failed'],
            [16,   'RC_VALIDATION_ERROR',   'Parameter validation error'],
        ],
        'frameProfile' : [
            [ 1,   'Profile_01',            'Fast network build, medium speed network operation'],
        ],
        'advertisementState' : [
            [ 0,   'on',                    'Advertisement is on'],
            [ 1,   'off',                   'Advertisement is off'],
        ],
        'downstreamFrameMode' : [
            [ 0,   'normal',                'Normal downstream bandwidth'],
            [ 1,   'fast',                  'Fast downstream bandwidth'],
        ],
        'locationMode' : [
            [ 0,   'off',                   'No Location capability'],
            [ 1,   'onDemand',              'On Demand Location Awareness'],
        ],
        'networkState' : [
            [ 0,   'operational',           'Network is operating normally'],
            [ 1,   'radiotest',             'Manager is in radiotest mode'],
            [ 2,   'notStarted',            'Waiting for startNetwork API command'],
            [ 3,   'errorStartup',          'Unexpected error occurred at startup'],
            [ 4,   'errorConfig',           'Invalid or not licensed configuration found at startup'],
            [ 5,   'errorLicense',          'Invalid license file found at startup'],
        ],
        'moteState' : [
            [ 0,   'lost',                  'Mote is not currently part of the network'],
            [ 1,   'negotiating',           'Mote is in the process of joining the network'],
            [ 4,   'operational',           'Mote is operational'],
        ],
        'resetType' : [
            [ 0,   'resetSystem',           'Reset the system'],
            [ 1,   'resetNetwork',          'Reset the network'],
            [ 2,   'resetMote',             'Reset the mote'],
        ],
        'backboneFrameMode' : [
            [ 0,   'off',                   'Backbone frame is off'],
            [ 1,   'upstream',              'Backbone frame is activated for upstream frames'],
            [ 2,   'bidirectional',         'Backbone frame is activated for both upstream and downstream frames'],
        ],
        'pathFilter' : [
            [ 0,   'all',                   'All paths'],
            [ 1,   'upstream',              'Upstream paths'],
        ],
        'pathDirection' : [
            [ 0,   'none',                  'No path'],
            [ 1,   'unused',                'Path is not used'],
            [ 2,   'upstream',              'Upstream path'],
            [ 3,   'downstream',            'Downstream path'],
        ],
        'packetPriority': [
            [0,    'Low',                   'Default packet priority'],
            [1,    'Medium',                'Higher packet priority'],
            [2,    'High',                  'Highest packet priority'],
        ],
        'commandFinishedResult': [
            [0,    'OK',                    'Command completed successfully'],
            [1,    'nack',                  'Command not acknowledged'],
            [2,    'commandTimeout',        'Command timed out'],
        ],
        'ccaMode': [
            [0,    'off',                   'CCA disabled'],
            [1,    'energy',                'Energy detect'],
            [2,    'carrier',               'Carrier detect'],
            [3,    'both',                  'Energy detect and Carrier detect'],
        ],
        #==================== misc ============================================
        'successCode' : [
            [ 0,   'success',               ''],
            [ 1,   'unsupported_version',   ''],
            [ 2,   'invalid_mode',          ''],
        ],
        'mode' : [
            [ 0,   'legacy',                ''],
        ],
        'userRole' : [
            [ 0,   'viewer',                ''],
            [ 1,   'admin',                 ''],
        ],
    }
    
    # We redefine this attribute inherited from ApiDefinition. See
    # ApiDefinition for a full description of the structure of this field.
    commands = [
        # command 'hello' (commandID 1) is handled by the Hdlc module
        # command 'hello_response' (commandID 2) is handled by the Hdlc module
        {
            'id'         :  1,
            'name'       :  'mux_hello',
            'description':  'Sent by the manager to initiate a new session with a client.',
            'request'    : [
                ['version',                 INT,      1,   None],
                ['secret',                  HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['version',             INT,      1,   None],
                ],
            },
        },
        {
            'id'         :  1,
            'name'       :  'hello',
            'description':  '',
            'request'    : [
                ['version',                 INT,      1,   None],
                ['cliSeqNo',                INT,      1,   None],
                ['mode',                    INT,      1,   True],
            ],
        },
        {
            'id'         : 2,
            'name'       : 'hello_response',
            'description': '',
            'request'    : [], # there is no request
            'response'   : {
                'FIELDS':  [
                    ['successCode',         INT,      1,   True],
                    ['version',             INT,      1,   None],
                    ['mgrSeqNo',            INT,      1,   None],
                    ['cliSeqNo',            INT,      1,   None],
                    ['mode',                INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 21,
            'name'       : 'reset',
            'description': 'The reset command is used to reset various objects. The command argument is an object type, and if the object is a mote the MAC address must be specified (otherwise that argument is ignored).',
            'request'    : [
                ['type',                    INT,      1,   'resetType'],
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                ],
            },
        },
        {
            'id'         : 22,
            'name'       : 'subscribe',
            'description': 'The subscribe command indicates that the manager should send the external application the specified notifications. The notification filter is a bitmask of flags indicating the types of notifications that the client wants to receive.\n\nThe unackFilter allows client to select whether each notification-type should be sent acknowledged or not. If a notification is sent as \'acknowledged\', the subsequent notification packets will be queued while waiting for response.\n\nEach subscription request overwrites the previous one. If an application is subscribed to data and then decides he also wants events he should send a subscribe command with both the data and event flags set. To clear all subscriptions, the client should send a subscribe command with the filter set to zero. When a session is initiated between the manager and a client, the subscription filter is initialized to zero.\n\nThe subscribe bitmap uses the values of the notification type enumeration. Some values are unused to provide backwards compatibility with earlier APIs. ',
            'request' : [
                ['filter',                  HEXDATA,  4,   None],
                ['unackFilter',             HEXDATA,  4,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 23,
            'name'       : 'getTime',
            'description': 'The getTime command returns the current manager UTC time and current absolute slot number (ASN). The time values returned by this command are delayed by queuing and transfer time over the serial connection. For additional precision, an external application should trigger the networkTime notification using the Time pin.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['uptime',              INT,      4,   None],
                    ['utcSecs',             INT,      8,   None],
                    ['utcUsecs',            INT,      4,   None],
                    ['asn',                 HEXDATA,  5,   None],
                    ['asnOffset',           INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 26,
            'name'       : 'setNetworkConfig',
            'description': 'The setNetworkConfig command changes network configuration parameters. The response code indicates whether the changes were successfully applied. Generally, changes to network configuration will take effect when the manager reboots. Exceptions are detailed below:\n\n-Max Motes: The new maxMotes value is used as soon as new motes try to join the network, but motes are not removed from the network if the value is set to a number lower than numMotes.\n-Base Bandwidth: Changing baseBandwidth while the network is running does not reallocate bandwidth to Operational motes.',
            'request'    :  [
                ['networkId',               INT,      2,   None],
                ['apTxPower',               INTS,     1,   None],
                ['frameProfile',            INT,      1,   True],
                ['maxMotes',                INT,      2,   None],
                ['baseBandwidth',           INT,      2,   None],
                ['downFrameMultVal',        INT,      1,   None],
                ['numParents',              INT,      1,   None],
                ['ccaMode',                 INT,      1,   True],
                ['channelList',             INT,      2,   None],
                ['autoStartNetwork',        INT,      1,   None],
                ['locMode',                 INT,      1,   'locationMode'],
                ['bbMode',                  INT,      1,   'backboneFrameMode'],
                ['bbSize',                  INT,      1,   None],
                ['isRadioTest',             INT,      1,   None],
                ['bwMult',                  INT,      2,   None],
                ['oneChannel',              INT,      1,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 31,
            'name'       : 'clearStatistics',
            'description': 'The clearStatistics command clears the accumulated network statistics. The command does not clear path quality or mote statistics.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 33,
            'name'       : 'exchangeMoteJoinKey',
            'description': 'The exchangeMoteJoinKey command triggers the manager to send a new join key to the specified mote and update the manager\'s ACL entry for the mote. The response contains a callbackId. A commandFinished notification with the callbackId will be sent when the operation is complete.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['key',                     HEXDATA,  16,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 34,
            'name'       : 'exchangeNetworkId',
            'description': 'The exchangeNetworkId command triggers the manager to distribute a new network ID to all the motes in the network. A callbackId is returned in the response. A commandFinished notification with the callbackId will be sent when the operation is complete.',
            'request'    : [
                ['id',                      INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 35,
            'name'       : 'radiotestTx',
            'description': 'The radiotestTx command allows the user to initiate a radio transmission test. It may only be executed if the manager has been booted up in radioTest mode (see setNetworkConfig command). Three types of transmission tests are supported:\n\n-Packet transmission\n-Continuous modulation\n-Continuous wave (unmodulated signal)\n\nIn a packet transmission test, the device generates a repeatCnt number of packet sequences. Each sequence consists of up to 10 packets with configurable size and delays. Each packet consists of payload of up to 125 bytes, and a 2-byte 802.15.4 CRC at the end. Bytes 0 and 1 contain the packet number (in big-endian format) that increments with every packet transmitted. Bytes 2..N contain a counter (from 0..N-2) that increments with every byte inside payload. Transmissions occur on the set of channels defined by chanMask, selected in pseudo-random order.\n\nIn a continuous modulation test, the device generates continuous pseudo-random modulated signal, centered at the specified channel. The test is stopped by resetting the device.\n\nIn a continuous wave test, the device generates an unmodulated tone, centered at the specified channel. The test tone is stopped by resetting the device.\n\nNote: Channel numbering is 0-14, corresponding to IEEE 2.4 GHz channels 11-25.',
            'request'    : [
                ['testType',                INT,      1,   None],
                ['chanMask',                INT,      2,   None],
                ['repeatCnt',               INT,      2,   None],
                ['txPower',                 INTS,     1,   None],
                ['seqSize',                 INT,      1,   None],
                ['pkSize1',                 INT,      1,   None],
                ['gap1',                    INT,      2,   None],
                ['pkSize2',                 INT,      1,   None],
                ['gap2',                    INT,      2,   None],
                ['pkSize3',                 INT,      1,   None],
                ['gap3',                    INT,      2,   None],
                ['pkSize4',                 INT,      1,   None],
                ['gap4',                    INT,      2,   None],
                ['pkSize5',                 INT,      1,   None],
                ['gap5',                    INT,      2,   None],
                ['pkSize6',                 INT,      1,   None],
                ['gap6',                    INT,      2,   None],
                ['pkSize7',                 INT,      1,   None],
                ['gap7',                    INT,      2,   None],
                ['pkSize8',                 INT,      1,   None],
                ['gap8',                    INT,      2,   None],
                ['pkSize9',                 INT,      1,   None],
                ['gap9',                    INT,      2,   None],
                ['pkSize10',                INT,      1,   None],
                ['gap10',                   INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 37,
            'name'       : 'radiotestRx',
            'description': 'The radiotestRx command clears all previously collected statistics and initiates radio reception on the specified channel.  It may only be executed if the manager has been booted up in radioTest mode (see setNetworkConfig command). During the test, the device keeps statistics about the number of packets received (with and without error). The test results may be retrieved using the getRadiotestStatistics command.\n\nNote: Channel numbering is 0-14, corresponding to IEEE 2.4 GHz channels 11-25.',
            'request'    : [
                ['mask',                    INT,      2,   None],
                ['duration',                INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 38,
            'name'       : 'getRadiotestStatistics',
            'description': 'This command retrieves statistics from a previously run radiotestRx command.  It may only be executed if the manager has been booted up in radioTest mode (see setNetworkConfig command). ',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['rxOk',                INT,      2,   None],
                    ['rxFail',              INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 39,
            'name'       : 'setACLEntry',
            'description': 'The setACLEntry command adds a new entry or updates an existing entry in the access control list (ACL).',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['joinKey',                 HEXDATA,  16,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 40,
            'name'       : 'getNextACLEntry',
            'description': 'The getNextACLEntry command returns information about next mote entry in the access control list (ACL). To begin a search (find the first mote in ACL), a zero MAC address (0000000000000000) should be sent.\n\nThere is no mechanism for reading the ACL entry of a specific mote. This call is an iterator. If you call getNextACLEntry with mote A as the argument, your response is the ACL entry for mote B, where B is the next mote in the ACL.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                    ['joinKey',             HEXDATA,  16,  None],
                ],
            },
        },
        {
            'id'         : 41,
            'name'       : 'deleteACLEntry',
            'description': 'The deleteACLEntry command deletes the specified mote from the access control list (ACL). If the macAddress parameter is set to all 0xFFs, the entire ACL is cleared.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 42,
            'name'       : 'pingMote',
            'description': 'The pingMote command sends a ping (echo request) to the mote specified by MAC address. A unique callbackId is generated and returned with the response. When a ping response is received from the mote, the manager generates a ping notification with the measured round trip delay and several other parameters.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 43,
            'name'       : 'getLog',
            'description': 'The getLog command retrieves diagnostic logs from the manager or a mote specified by MAC address.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 44,
            'name'       : 'sendData',
            'description': 'The sendData command sends a packet to a mote in the network. The response contains a callbackId. When the manager injects the packet into the network, it will generate a packetSent notification. It is the application layer\'s responsibility send a response from the mote, and to timeout if no response is received.\n\nThe sendData command should be used by applications that communicate directly with the manager. If end-to-end (application to mote) IP connectivity is required, the application should use the sendIP command. For a more comprehensive discussion of the distinction, see the SmartMesh IP Network User Guide.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['priority',                INT,      1,   'packetPriority'],
                ['srcPort',                 INT,      2,   None],
                ['dstPort',                 INT,      2,   None],
                ['options',                 INT,      1,   None],
                ['data',                    HEXDATA,  None,None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 45,
            'name'       : 'startNetwork',
            'description': 'The startNetwork command tells the manager to allow the network to start forming (begin accepting join requests from devices). The external application must issue the startNetwork command if the autoStartNetwork flag is not set (see setNetworkConfig).',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 46,
            'name'       : 'getSystemInfo',
            'description': 'The getSystemInfo command returns system-level information about the hardware and software versions.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                    ['hwModel',             INT,      1,   None],
                    ['hwRev',               INT,      1,   None],
                    ['swMajor',             INT,      1,   None],
                    ['swMinor',             INT,      1,   None],
                    ['swPatch',             INT,      1,   None],
                    ['swBuild',             INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 47,
            'name'       : 'getMoteConfig',
            'description': 'The getMoteConfig command returns a single mote description as the response. The command takes two arguments, a MAC Address and a flag indicating whether the MAC Address refers to the requested mote or to the next mote in manager\'s memory. This command may be used to iterate through all motes known by the manager by starting with the macAddress parameter set to 0 and next set to true, and then using the MAC Address of that response as the input to the next call.\n\nThe mote MAC address is used in all query commands, but space constraints require the neighbor health reports to use the moteId for identification. Therefore, both identifiers are present in the mote structure.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['next',                    BOOL,     1,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                    ['moteId',              INT,      2,   None],
                    ['isAP',                INT,      1,   None],
                    ['state',               INT,      1,   'moteState'],
                    ['reserved',            INT,      1,   None],
                    ['isRouting',           BOOL,     1,   None],
                ],
            },
        },
        {
            'id'         : 48,
            'name'       : 'getPathInfo',
            'description': 'The getPathInfo command returns parameters of requested path.',
            'request'    : [
                ['source',                  HEXDATA,  8,   None],
                ['dest',                    HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['source',              HEXDATA,  8,   None],
                    ['dest',                HEXDATA,  8,   None],
                    ['direction',           INT,      1,   'pathDirection'],
                    ['numLinks',            INT,      1,   None],
                    ['quality',             INT,      1,   None],
                    ['rssiSrcDest',         INTS,     1,   None],
                    ['rssiDestSrc',         INTS,     1,   None],
                ],
            },
        },
        {
            'id'         : 49,
            'name'       : 'getNextPathInfo',
            'description': 'The getNextPathInfo command allows iteration across paths connected to a particular mote. The pathId parameter indicates the previous value in the iteration. Setting pathId to 0 returns the first path. A pathId can not be used as a unique identifier for a path. It is only valid when associated with a particular mote.',
            'request'    : [
                ['mac',                     HEXDATA,  8,   None],
                ['filter',                  INT,      1,   'pathFilter'],
                ['pathId',                  INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['pathId',              INT,      2,   None],
                    ['source',              HEXDATA,  8,   None],
                    ['dest',                HEXDATA,  8,   None],
                    ['direction',           INT,      1,   'pathDirection'],
                    ['numLinks',            INT,      1,   None],
                    ['quality',             INT,      1,   None],
                    ['rssiSrcDest',         INTS,     1,   None],
                    ['rssiDestSrc',         INTS,     1,   None],
                ],
            },
        },
        {
            'id'         : 50,
            'name'       : 'setAdvertising',
            'description': 'The setAdvertising command tells the manager to activate or deactivate advertising. The response is a callbackId. A commandFinished notification with the callbackId is generated when the command propagation is complete.',
            'request'    : [
                ['activate',                INT,      1,   'advertisementState'],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 51,
            'name'       : 'setDownstreamFrameMode',
            'description': 'The setDownstreaFrame Mode command tells the manager to shorten or extend the downstream frame. Once this command is executed, the manager switches to manual mode and no longer changes frame size automatically. The response is a callbackId. A commandFinished notification with the callbackId is generated when the command propagation is complete.',
            'request'    : [
                ['frameMode',               INT,      1,   'downstreamFrameMode'],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 53,
            'name'       : 'getManagerStatistics',
            'description': 'The getManagerStatistics command returns dynamic information and statistics about the manager API. The statistics counts are cleared together with all current statistics using clearStatistics.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['serTxCnt',            INT,      2,   None],
                    ['serRxCnt',            INT,      2,   None],
                    ['serRxCRCErr',         INT,      2,   None],
                    ['serRxOverruns',       INT,      2,   None],
                    ['apiEstabConn',        INT,      2,   None],
                    ['apiDropppedConn',     INT,      2,   None],
                    ['apiTxOk',             INT,      2,   None],
                    ['apiTxErr',            INT,      2,   None],
                    ['apiTxFail',           INT,      2,   None],
                    ['apiRxOk',             INT,      2,   None],
                    ['apiRxProtErr',        INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 54,
            'name'       : 'setTime',
            'description': 'The setTime command sets the UTC time on the manager. This command may only be executed when the network is not running. If the trigger flag is false, the manager sets the specified time as soon as it receives the setTime command. When the manager receives a Time pin trigger, it temporarily stores the current time. If a setTime request is received within a short period of time following the trigger, the manager calculates the delay since the trigger and adjust the time such that the trigger was received at the specified time value.',
            'request'    : [
                ['trigger',                 INT,      1,   None],
                ['utcSecs',                 INT,      8,   None],
                ['utcUsecs',                INT,      4,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 55,
            'name'       : 'getLicense',
            'description': 'The getLicense command returns the current license key.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['license',             HEXDATA,  13,  None],
                ],
            },
        },
        {
            'id'         : 56,
            'name'       : 'setLicense',
            'description': 'The setLicense command validates and updates the software license key stored in flash. Features enabled or disabled by the license key change will take effect after the device is restarted. If the license parameter is set to all 0x0s, the manager restores the default license.',
            'request'    : [
                ['license',                 HEXDATA,  13,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 58,
            'name'       : 'setUser',
            'description': 'The setUser command sets the password that must be used to log into the command line for a particular user role.',
            'request'    : [
                ['role',                    INT,      1,   'userRole'],
                ['password',                HEXDATA,  16,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 59,
            'name'       : 'sendIP',
            'description': 'The sendIP command sends an 6LowPAN packet to a mote in the network. The response contains a callbackId. When the manager injects the packet into the network, it will generate a packetSent notification. It is the application layer\'s responsibility send a response from the mote, and to timeout if no response is received. The application is responsible for constructing a valid 6LoWPAN packet.\n\nThe sendIP command should be used by applications that require end-to-end IP connectivity. For applications that do not require end-to-end IP connectivity, the sendData command provides a simpler interface without requiring the application to understand 6LoWPAN encapsulation. For a more comprehensive discussion of the distinction, see the SmartMesh IP Network User Guide.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['priority',                INT,      1,   'packetPriority'],
                ['options',                 INT,      1,   None],
                ['encryptedOffset',         INT,      1,   None],
                ['data',                    HEXDATA,  None,None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 60,
            'name'       : 'startLocation',
            'description': 'The startLocation command sends a request to a set of motes to generate distance measurements to a mobile mote. The manager sends a series of commands to the specified motes active the location links for enough time to perform the requested measurements. More than one startLocation request may be queued up by the manager, but the queue size is limited. The caller must be able to handle a queue full error and retry. The startLocation request contains a variable number of fixed motes. The manager determines the number of fixedMotes provided by the caller by checking the length of the request.\n\nThe startLocation call returns a callbackId that is used to inform the caller of the progress of the distance measurement (see Event Notifications). Location events are similar to commandFinished events. The distance measurements are returned as ipData notifications from the fixed motes. The structure of distance measurements is defined in the \'Dust mote command spec\'.\n\nThe startLocation command is only allowed if the license allows it.',
            'request'    : [
                ['numMeasurements',         INT,      1,   None],
                ['mobileMote',              HEXDATA,  8,   None],
                ['fixedMotes',              HEXDATA,  None,None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['callbackId',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 61,
            'name'       : 'restoreFactoryDefaults',
            'description': 'The restoreFactoryDefaults command restores the default configuration and clears the ACL. This command does not affect the license.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 62,
            'name'       : 'getMoteInfo',
            'description': 'The getMoteInfo command returns dynamic information for the specified mote.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                    ['state',               INT,      1,   'moteState'],
                    ['numNbrs',             INT,      1,   None],
                    ['numGoodNbrs',         INT,      1,   None],
                    ['requestedBw',         INT,      4,   None],
                    ['totalNeededBw',       INT,      4,   None],
                    ['assignedBw',          INT,      4,   None],
                    ['packetsReceived',     INT,      4,   None],
                    ['packetsLost',         INT,      4,   None],
                    ['avgLatency',          INT,      4,   None],
                ],
            },
        },
        {
            'id'         : 63,
            'name'       : 'getNetworkConfig',
            'description': 'The getNetworkConfig command returns general network configuration parameters, including the network ID, bandwidth parameters and number of motes.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['networkId',           INT,      2,   None],
                    ['apTxPower',           INT,      1,   None],
                    ['frameProfile',        INT,      1,   True],
                    ['maxMotes',            INT,      2,   None],
                    ['baseBandwidth',       INT,      2,   None],
                    ['downFrameMultVal',    INT,      1,   None],
                    ['numParents',          INT,      1,   None],
                    ['enableCCA',           INT,      1,   None],
                    ['channelList',         INT,      2,   None],
                    ['autoStartNetwork',    INT,      1,   None],
                    ['locMode',             INT,      1,   'locationMode'],
                    ['bbMode',              INT,      1,   'backboneFrameMode'],
                    ['bbSize',              INT,      1,   None],
                    ['isRadioTest',         INT,      1,   None],
                    ['bwMult',              INT,      2,   None],
                    ['oneChannel',          INT,      1,   None],
                ],
            },
        },
        {
            'id'         : 64,
            'name'       : 'getNetworkInfo',
            'description': 'The getNetworkInfo command returns dynamic network information and statistics.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['numMotes',            INT,      2,   None],
                    ['asnSize',             INT,      2,   None],
                    ['advertisementState',  INT,      1,   True],
                    ['downFrameState',      INT,      1,   'downstreamFrameMode'],
                    ['netReliability',      INT,      1,   None],
                    ['netPathStability',    INT,      1,   None],
                    ['netLatency',          INT,      4,   None],
                    ['netState',            INT,      1,   'networkState'],
                    ['ip6addr',             HEXDATA,  16,  None],
                ],
            },
        },
        {
            'id'         : 65,
            'name'       : 'getMoteConfigById',
            'description': 'The getMoteConfigById command returns a single mote description as the response. The command takes one argument, the Short Address of a mote (mote ID). The command returns the same response structure as the getMoteConfig command.',
            'request'    : [
                    ['moteId',              INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['macAddress',          HEXDATA,  8,   None],
                    ['moteId',              INT,      2,   None],
                    ['isAP',                INT,      1,   None],
                    ['state',               INT,      1,   None],
                    ['reserved',            INT,      1,   None],
                    ['isRouting',           BOOL,     1,   None],
                ],
            },
        },
        {
            'id'         : 66,
            'name'       : 'setCommonJoinKey',
            'description': 'The setCommonJoinKey command will set a new value for the common join key. The common join key is used to decrypt join messages only if the ACL is empty.',
            'request'    : [
                ['key',                     HEXDATA,  16,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 67,
            'name'       : 'getIPConfig',
            'description': 'The getIPConfig command returns the manager\'s IP configuration parameters, including the IPv6 address and mask.',
            'request'    : [
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['ipv6Address',         HEXDATA,  16,  None],
                    ['mask',                HEXDATA,  16,  None],
                ],
            },
        },
        {
            'id'         : 68,
            'name'       : 'setIPConfig',
            'description': 'The setIPConfig command sets the manager\'s IP configuration parameters, including the IPv6 address and mask.',
            'request'    : [
                ['ip6addr',                 HEXDATA,  16,  None],
                ['mask',                    HEXDATA,  16,  None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 69,
            'name'       : 'deleteMote',
            'description': 'The deleteMote command deletes a mote from the manager\'s list. A mote can only be deleted if it in the Lost or Unknown states.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                ],
            },
        },
        {
            'id'         : 70,
            'name'       : 'getMoteLinks',
            'description': 'The getMoteLinks command returns information about links assigned to the mote. The response contains a list of links starting with Nth link on the mote, where N is supplied as \'idx\' parameter in the request. To retrieve all links on the device the user can call this command with idx that increments by number of links returned with prior response,  until the command returns RC_END_OF_LIST response code. Note that links assigned to a mote may change between API calls.',
            'request'    : [
                ['macAddress',              HEXDATA,  8,   None],
                ['idx',                     INT,      2,   None],
            ],
            'response'   : {
                'FIELDS':  [
                    [RC,                    INT,      1,   True],
                    ['idx',                 INT,      2,   None],
                    ['utilization',         INT,      1,   None],
                    ['numLinks',            INT,      1,   None],
                    ['frameId1',            INT,      1,   None],  # 1
                    ['slot1',               INT,      4,   None],
                    ['channelOffset1',      INT,      1,   None],
                    ['moteId1',             INT,      2,   None],
                    ['flags1',              INT,      1,   None],
                    ['frameId2',            INT,      1,   None],  # 2
                    ['slot2',               INT,      4,   None],
                    ['channelOffset2',      INT,      1,   None],
                    ['moteId2',             INT,      2,   None],
                    ['flags2',              INT,      1,   None],
                    ['frameId3',            INT,      1,   None],  # 3
                    ['slot3',               INT,      4,   None],
                    ['channelOffset3',      INT,      1,   None],
                    ['moteId3',             INT,      2,   None],
                    ['flags3',              INT,      1,   None],
                    ['frameId4',            INT,      1,   None],  # 4
                    ['slot4',               INT,      4,   None],
                    ['channelOffset4',      INT,      1,   None],
                    ['moteId4',             INT,      2,   None],
                    ['flags4',              INT,      1,   None],
                    ['frameId5',            INT,      1,   None],  # 5
                    ['slot5',               INT,      4,   None],
                    ['channelOffset5',      INT,      1,   None],
                    ['moteId5',             INT,      2,   None],
                    ['flags5',              INT,      1,   None],
                    ['frameId6',            INT,      1,   None],  # 6
                    ['slot6',               INT,      4,   None],
                    ['channelOffset6',      INT,      1,   None],
                    ['moteId6',             INT,      2,   None],
                    ['flags6',              INT,      1,   None],
                    ['frameId7',            INT,      1,   None],  # 7
                    ['slot7',               INT,      4,   None],
                    ['channelOffset7',      INT,      1,   None],
                    ['moteId7',             INT,      2,   None],
                    ['flags7',              INT,      1,   None],
                    ['frameId8',            INT,      1,   None],  # 8
                    ['slot8',               INT,      4,   None],
                    ['channelOffset8',      INT,      1,   None],
                    ['moteId8',             INT,      2,   None],
                    ['flags8',              INT,      1,   None],
                    ['frameId9',            INT,      1,   None],  # 9
                    ['slot9',               INT,      4,   None],
                    ['channelOffset9',      INT,      1,   None],
                    ['moteId9',             INT,      2,   None],
                    ['flags9',              INT,      1,   None],
                    ['frameId10',           INT,      1,   None],  # 10
                    ['slot10',              INT,      4,   None],
                    ['channelOffset10',     INT,      1,   None],
                    ['moteId10',            INT,      2,   None],
                    ['flags10',             INT,      1,   None],
                ],
            },
        },
    ]
    
    subCommandsEvents = [
        {
            'id'         : 0,
            'name'       : 'eventMoteReset',
            'description': 'This notification is sent when a user-initiated reset is executed by the manager.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',         HEXDATA,  8,   None],
                ],
            },
        },
        {
            'id'         : 1,
            'name'       : 'eventNetworkReset',
            'description': 'This notification is sent when the manager starts the network. This event has no eventData fields.',
            'response'   : {
                'FIELDS':  [
                ],
            },
        },
        {
            'id'         : 2,
            'name'       : 'eventCommandFinish',
            'description': 'The commandFinished notification is used when a reliable command response is received.',
            'response'   : {
                'FIELDS':  [
                    ['callbackId',          HEXDATA,  4,   None],
                    ['rc',                  INT,      1,   'commandFinishedResult'],
                ],
            },
        },
        {
            'id'         : 3,
            'name'       : 'eventMoteJoin',
            'description': 'This notification is sent when a mote joins the network.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',         HEXDATA,  8,   None],
                ],
            },
        },
        {
            'id'         : 4,
            'name'       : 'eventMoteOperational',
            'description': 'This notification is sent when a mote that joins the network becomes operational.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',         HEXDATA,  8,   None],
                ],
            },
        },
        {
            'id'         : 5,
            'name'       : 'eventMoteLost',
            'description': 'This notification is sent when a mote\'s state changes to "Lost," which may occur when a mote becomes unreachable through the network.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',         HEXDATA,  8,   None],
                ],
            },
        },
        {
            'id'         : 6,
            'name'       : 'eventNetTime',
            'description': 'The time notification is triggered by the client asserting the TIME pin or by calling the getTime command. This notification contains the time when the TIME pin was asserted (or the getTime command was processed) expressed as:\n\n- ASN--The absolute slot number (the number of timeslots since 20:00:00 UTC July 2,2002 if UTC is set on manager, otherwise since Jan 1, 1970)\n- Uptime--The number of seconds since the device was booted\n-- Unix time--The number of seconds and microseconds since Jan 1, 1970 in UTC',
            'response'   : {
                'FIELDS':  [
                    ['uptime',             INT,      4,   None],
                    ['utcSecs',            INT,      8,   None],
                    ['utcUsecs',           INT,      4,   None],
                    ['asn',                HEXDATA,  5,   None],
                    ['asnOffset',          INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 7,
            'name'       : 'eventPingResponse',
            'description': 'This notification is sent when a reply is received from a mote ping.',
            'response'   : {
                'FIELDS':  [
                    ['callbackId',         INT,      4,   None],
                    ['macAddress',         HEXDATA,  8,   None],
                    ['delay',              INT,      4,   None],
                    ['voltage',            INT,      2,   None],
                    ['temperature',        INT,      1,   None],
                ],
            },
        },
        {
            'id'         : 10,
            'name'       : 'eventPathCreate',
            'description': 'This notification is sent when the manager creates a connection (path) between two motes.',
            'response'   : {
                'FIELDS':  [
                    ['source',             HEXDATA,  8,   None],
                    ['dest',               HEXDATA,  8,   None],
                    ['direction',          INT,      1,   'pathDirection'],
                ],
            },
        },
        {
            'id'         : 11,
            'name'       : 'eventPathDelete',
            'description': 'This notification is sent when the manager removes a connection (path) between two motes.',
            'response'   : {
                'FIELDS':  [
                    ['source',             HEXDATA,  8,   None],
                    ['dest',               HEXDATA,  8,   None],
                    ['direction',          INT,      1,   'pathDirection'],
                ],
            },
        },
        {
            'id'         : 12,
            'name'       : 'eventPacketSent',
            'description': 'The packetSent notification is generated when client\'s packet is removed from manager\'s queue and sent into the wireless network.',
            'response'   : {
                'FIELDS':  [
                    ['callbackId',         INT,      4,   None],
                    ['rc',                 INT,      1,   None],
                ],
            },
        },
        {
            'id'         : 13,
            'name'       : 'eventMoteCreate',
            'description': 'This event is sent when a mote joins the manager for the first time.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',        HEXDATA,  8,   None],
                    ['moteId',             INT,      2,   None],
                ],
            },
        },
        {
            'id'         : 14,
            'name'       : 'eventMoteDelete',
            'description': 'This notification is sent when a mote is deleted as a result of moteDelete command.',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',        HEXDATA,  8,   None],
                    ['moteId',             INT,      2,   None],
                ],
            },
        },
    ]
    
    subCommandsNotification = [
        {
            'id'         : 1,
            'name'       : 'notifEvent',
            'description': 'Event notification',
            'response'   : {
                'FIELDS':  [
                    ['eventId',            INT,      4,   None],
                    [SUBID2,               INT,      1,   None],
                ],
            },
            'subCommands': subCommandsEvents,
        },
        {
            'id'         : 2,
            'name'       : 'notifLog',
            'description': 'Log notification',
            'response'   : {
                'FIELDS':  [
                    ['macAddress',         HEXDATA,  8,   None],
                    ['logMsg',             HEXDATA,  None,None],
                ],
            },
        },
        {
            'id'         : 4,
            'name'       : 'notifData',
            'description': 'Data payload notification',
            'response'   : {
                'FIELDS':  [
                    ['utcSecs',            INT,      8,   None],
                    ['utcUsecs',           INT,      4,   None],
                    ['macAddress',         HEXDATA,  8,   None],
                    ['srcPort',            INT,      2,   None],
                    ['dstPort',            INT,      2,   None],
                    ['data',               HEXDATA,  None,None],
                ],
            },
        },
        {
            'id'         : 5,
            'name'       : 'notifIpData',
            'description': '6lowpan packet notification',
            'response'   : {
                'System':  [
                    ['utcSecs',            INT,      8,   None],
                    ['utcUsecs',           INT,      4,   None],
                    ['macAddress',         HEXDATA,  8,   None],
                    ['data',               HEXDATA,  None,None],
                ],
            },
        },
        {
            'id'         : 6,
            'name'       : 'notifHealthReport',
            'description': 'Health report notification',
            'response'   : {
                'System':  [
                    ['macAddress',         HEXDATA,  8,   None],
                    ['payload',            HEXDATA,  None,None],
                ],
            },
        },
    ]
    
    # We redefine this attribute inherited from ApiDefinition. See
    # ApiDefinition for a full description of the structure of this field.
    notifications = [
        {
            'id'         : 3,
            'name'       : 'manager_hello',
            'description': 'Sent by the manager to a initiate new session with a client.',
            'response'   : {
                'FIELDS':  [
                    ['version',             INT,      1,   None],
                    ['mode',                INT,      1,   None],
                ],
            },
        },
        {
            'id'         : 20,
            'name'       : 'notification',
            'description': '',
            'response'   : {
                'FIELDS':  [
                    [SUBID1,                INT,      1,   None],
                ]
            },
            'subCommands': subCommandsNotification,
        },
    ]
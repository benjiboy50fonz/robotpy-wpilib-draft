#
# Everything in here should be usable on all implementations of the HAL
#

#############################################################################
# HAL
#############################################################################

kHALAllianceStationID_red1 = 0
kHALAllianceStationID_red2 = 1
kHALAllianceStationID_red3 = 2
kHALAllianceStationID_blue1 = 3
kHALAllianceStationID_blue2 = 4
kHALAllianceStationID_blue3 = 5

kMaxJoystickAxes = 12
kMaxJoystickPOVs = 12

class HALUsageReporting:
    # enum tResourceType
    kResourceType_Controller = 0
    kResourceType_Module = 1
    kResourceType_Language = 2
    kResourceType_CANPlugin = 3
    kResourceType_Accelerometer = 4
    kResourceType_ADXL345 = 5
    kResourceType_AnalogChannel = 6
    kResourceType_AnalogTrigger = 7
    kResourceType_AnalogTriggerOutput = 8
    kResourceType_CANJaguar = 9
    kResourceType_Compressor = 10
    kResourceType_Counter = 11
    kResourceType_Dashboard = 12
    kResourceType_DigitalInput = 13
    kResourceType_DigitalOutput = 14
    kResourceType_DriverStationCIO = 15
    kResourceType_DriverStationEIO = 16
    kResourceType_DriverStationLCD = 17
    kResourceType_Encoder = 18
    kResourceType_GearTooth = 19
    kResourceType_Gyro = 20
    kResourceType_I2C = 21
    kResourceType_Framework = 22
    kResourceType_Jaguar = 23
    kResourceType_Joystick = 24
    kResourceType_Kinect = 25
    kResourceType_KinectStick = 26
    kResourceType_PIDController = 27
    kResourceType_Preferences = 28
    kResourceType_PWM = 29
    kResourceType_Relay = 30
    kResourceType_RobotDrive = 31
    kResourceType_SerialPort = 32
    kResourceType_Servo = 33
    kResourceType_Solenoid = 34
    kResourceType_SPI = 35
    kResourceType_Task = 36
    kResourceType_Ultrasonic = 37
    kResourceType_Victor = 38
    kResourceType_Button = 39
    kResourceType_Command = 40
    kResourceType_AxisCamera = 41
    kResourceType_PCVideoServer = 42
    kResourceType_SmartDashboard = 43
    kResourceType_Talon = 44
    kResourceType_HiTechnicColorSensor = 45
    kResourceType_HiTechnicAccel = 46
    kResourceType_HiTechnicCompass = 47
    kResourceType_SRF08 = 48

    # enum tInstances
    kLanguage_LabVIEW = 1
    kLanguage_CPlusPlus = 2
    kLanguage_Java = 3
    kLanguage_Python = 4

    kCANPlugin_BlackJagBridge = 1
    kCANPlugin_2CAN = 2

    kFramework_Iterative = 1
    kFramework_Simple = 2

    kRobotDrive_ArcadeStandard = 1
    kRobotDrive_ArcadeButtonSpin = 2
    kRobotDrive_ArcadeRatioCurve = 3
    kRobotDrive_Tank = 4
    kRobotDrive_MecanumPolar = 5
    kRobotDrive_MecanumCartesian = 6

    kDriverStationCIO_Analog = 1
    kDriverStationCIO_DigitalIn = 2
    kDriverStationCIO_DigitalOut = 3

    kDriverStationEIO_Acceleration = 1
    kDriverStationEIO_AnalogIn = 2
    kDriverStationEIO_AnalogOut = 3
    kDriverStationEIO_Button = 4
    kDriverStationEIO_LED = 5
    kDriverStationEIO_DigitalIn = 6
    kDriverStationEIO_DigitalOut = 7
    kDriverStationEIO_FixedDigitalOut = 8
    kDriverStationEIO_PWM = 9
    kDriverStationEIO_Encoder = 10
    kDriverStationEIO_TouchSlider = 11

    kADXL345_SPI = 1
    kADXL345_I2C = 2

    kCommand_Scheduler = 1

    kSmartDashboard_Instance = 1

#############################################################################
# Accelerometer
#############################################################################

class AccelerometerRange:
    kRange_2G = 0
    kRange_4G = 1
    kRange_8G = 2

#############################################################################
# Analog
#############################################################################

class AnalogTriggerType:
    kInWindow = 0
    kState = 1
    kRisingPulse = 2
    kFallingPulse = 3

#############################################################################
# Digital
#############################################################################

class Mode:
    kTwoPulse = 0
    kSemiperiod = 1
    kPulseLength = 2
    kExternalDirection = 3


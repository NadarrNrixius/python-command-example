import wpilib
import commands2
import ctre



class AmmoSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        self._front_motor = ctre.WPI_VictorSPX(7)
        self._rear_motor = ctre.WPI_VictorSPX(6)

        self._front_sensor = wpilib.DigitalInput(4)
        self._rear_sensor = wpilib.DigitalInput(3)

        self._rear_motor.setInverted(True)

        self._front_motor.set(0.5)
        self._rear_motor.set(0.5)
    
    def startFrontMotor(self):
        self._front_motor.set(0.5)

    def startRearMotor(self):
        self._rear_motor.set(0.5)

    def stopFrontMotor(self):
        self._front_motor.set(0.0)
    
    def stopRearMotor(self):
        self._rear_motor.set(0.0)
    
    def isFrontSensorTriggered(self) -> bool:
        return self._front_sensor.get()
    
    def isRearSensorTriggered(self) -> bool:
        return self._rear_sensor.get()
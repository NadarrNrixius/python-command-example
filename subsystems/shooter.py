import wpilib
import commands2

import rev

class ShooterSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        self._shoot_wheel = rev.CANSparkMax(8, rev.CANSparkMax.MotorType.kBrushless)

    def startShootWheel(self):
        self._shoot_wheel.set(0.5)

    def stopShootWheel(self):
        self._shoot_wheel.set(0.0)
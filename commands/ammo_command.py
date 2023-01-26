import wpilib
import commands2

from subsystems.ammo import AmmoSubsystem

class AmmoCommand(commands2.CommandBase):
    def __init__(self, subsystem: AmmoSubsystem):
        super().__init__()

        self.ammo_subsystem = subsystem

        self.addRequirements(self.ammo_subsystem)

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        if self.ammo_subsystem.isRearSensorTriggered():
            self.ammo_subsystem.stopRearMotor()
        else:
            self.ammo_subsystem.startRearMotor()
        if self.ammo_subsystem.isFrontSensorTriggered() and self.ammo_subsystem.isRearSensorTriggered():
            self.ammo_subsystem.stopFrontMotor()
        else:
            self.ammo_subsystem.startFrontMotor()
    
    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False
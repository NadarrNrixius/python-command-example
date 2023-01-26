import wpilib
import commands2
import time

from subsystems.shooter import ShooterSubsystem
from subsystems.ammo import AmmoSubsystem

class ShooterCommand(commands2.CommandBase):
    def __init__(self, shooter_subsystem: ShooterSubsystem, ammo_subsystem: AmmoSubsystem):
        super().__init__()

        self.shooter_subsystem = shooter_subsystem
        self.ammo_subsystem = ammo_subsystem

        self.addRequirements(self.shooter_subsystem)

    def initialize(self) -> None:
        self.shooter_subsystem.startShootWheel()
        self.ammo_subsystem.startRearMotor()
        time.sleep(1)
    
    def execute(self) -> None:
        pass

    def end(self, interrupted: bool) -> None:
        self.shooter_subsystem.stopShootWheel()
        self.ammo_subsystem.stopRearMotor()
    
    def isFinished(self) -> bool:
        return True
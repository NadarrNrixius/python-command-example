import wpilib
import commands2
import time

from subsystems.shooter import ShooterSubsystem

class ShooterCommand(commands2.CommandBase):
    def __init__(self, subsystem: ShooterSubsystem):
        super().__init__()

        self.shooter_subsystem = subsystem

        self.addRequirements(self.shooter_subsystem)

    def initialize(self) -> None:
        self.shooter_subsystem.startShootWheel()
        time.sleep(1)
    
    def execute(self) -> None:
        pass

    def end(self, interrupted: bool) -> None:
        self.shooter_subsystem.stopShootWheel()
    
    def isFinished(self) -> bool:
        return True
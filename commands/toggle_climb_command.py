import wpilib
import commands2

from subsystems.climb import ClimbSubsystem

class ToggleClimbCommand(commands2.CommandBase):
    def __init__(self, subsystem: ClimbSubsystem):
        super().__init__()

        self.climb_subsystem = subsystem

        self.addRequirements(self.climb_subsystem)
    
    def initialize(self):
        self.climb_subsystem.togglePistons()

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def isFinished(self):
        return True
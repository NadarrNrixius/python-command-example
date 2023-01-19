import wpilib
import commands2

from subsystems.snatch import SnatchSubsystem

class ToggleSnatchCommand(commands2.CommandBase):

    def __init__(self, subsystem: SnatchSubsystem):

        super().__init__()

        self.snatch_subsystem = subsystem

        self.addRequirements(self.snatch_subsystem)

    def initialize(self):
        self.snatch_subsystem.togglePistons()

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def isFinished(self):
        return True
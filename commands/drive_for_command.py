import wpilib
import commands2

from subsystems.drive import DriveSubsystem

class DriveForCommand(commands2.CommandBase):
    def __init__(self, subsystem: DriveSubsystem, drive_time: float):
        super().__init__()

        self.drive_subsystem = subsystem

        self.drive_time = drive_time

        self.timer = wpilib.Timer()

        self.addRequirements(self.drive_subsystem)

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()
    
    def execute(self) -> None:
        self.drive_subsystem.drive(0.0, 0.2, 0.0)
    
    def end(self, interrupted: bool) -> None:
        self.drive_subsystem.fullstop()
        self.timer.stop()
    
    def isFinished(self) -> bool:
        if self.timer.hasElapsed(self.drive_time):
            return True
        else:
            return False
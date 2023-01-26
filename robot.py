import wpilib
import commands2.button as button

import commands2

from subsystems.drive import DriveSubsystem
from subsystems.snatch import SnatchSubsystem
from subsystems.climb import ClimbSubsystem
from subsystems.ammo import AmmoSubsystem
from subsystems.shooter import ShooterSubsystem
from commands import DriveCommand, TurnCommand, ToggleSnatchCommand, ToggleClimbCommand, AmmoCommand, ShooterCommand, DriveForCommand

# This is the main robot class.
class RobotDriveDemo(wpilib.TimedRobot):
    drive: DriveSubsystem
    controller: button.CommandXboxController

    def robotInit(self) -> None:
        # Here we instantiate all of our subsystems, controllers, and any necessary commands.
        # Ideally, all of these will wrap all of the hardware on the robot, and we won't need
        # to declare anything else here (however, there could be a reason, just probably not a good one).
        self.drive = DriveSubsystem(4, 2, 1, 3)
        self.snatch = SnatchSubsystem()
        self.climb = ClimbSubsystem()
        self.ammo = AmmoSubsystem()
        self.shooter = ShooterSubsystem()

        self.controller = button.CommandXboxController(0)

        self.drive.setDefaultCommand(DriveCommand(self.drive, self.controller))
        #self.ammo.setDefaultCommand(AmmoCommand(self.ammo))
        
        self.controller.X().onTrue(TurnCommand(self.drive, 90))
        self.controller.leftBumper().onTrue(ToggleSnatchCommand(self.snatch))
        self.controller.rightBumper().onTrue(ToggleClimbCommand(self.climb))
        self.controller.rightTrigger().onTrue(ShooterCommand(self.shooter, self.ammo))
        self.controller.leftTrigger().onTrue(DriveForCommand(self.drive, 2.0))

        self.autonomous_commands = commands2.SequentialCommandGroup()

    def robotPeriodic(self) -> None:
        # This is what allows us to actually run the commands. You will almost 
        # never need to write this line yourself.
        commands2.CommandScheduler.getInstance().run()
        # You may sometimes use this to update values on the dashboard.
        pass

    def autonomousInit(self) -> None:
        # We'll use this to set the autonomous command on the actual robot.

        self.autonomous_commands = commands2.SequentialCommandGroup(commands=[
            #TurnCommand(self.drive, 90),
            ToggleSnatchCommand(self.snatch),
            DriveForCommand(self.drive, 2.5),
            ToggleSnatchCommand(self.snatch),
            #TurnCommand(self.drive, 180),
            ShooterCommand(self.shooter, self.ammo)
        ])

        self.autonomous_commands.schedule()

    def autonomousPeriodic(self) -> None:
        # We rarely do anything with this function.
        pass

    def teleopInit(self) -> None:
        # Mostly used to stop the autonomous command, if it's still running.
        self.autonomous_commands.cancel()

    def teleopPeriodic(self) -> None:
        # You'll never use this. All TeleOp behaviours should be registered 
        # as commands.
        pass


# This is what runs the actual robot. You will need to write this as often as you write
# the command scheduler. This handles literally everything to do with running the robot.
# If your code fails to even deploy, but doesn't look wrong otherwise, you forgot this.
if __name__ == "__main__":
    wpilib.run(RobotDriveDemo)
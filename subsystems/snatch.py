import wpilib
import commands2
from wpilib import DoubleSolenoid

class SnatchSubsystem(commands2.SubsystemBase):
    
    def __init__(self):

        super().__init__()

        self._pistons = DoubleSolenoid(moduleType=wpilib.PneumaticsModuleType.CTREPCM,forwardChannel=3, reverseChannel=4)
        
        self.extended = False

        self._pistons.set(DoubleSolenoid.Value.kReverse)

    def togglePistons(self):

        if self.extended:
            self._pistons.set(DoubleSolenoid.Value.kReverse)
            self.extended = False
        else:
            self._pistons.set(DoubleSolenoid.Value.kForward)
            self.extended = True
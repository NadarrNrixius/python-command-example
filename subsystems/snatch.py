import wpilib
import commands2
from wpilib import DoubleSolenoid

class SnatchSubsystem(commands2.SubsystemBase):
    
    def __init__(self):

        super().__init__()

        self._pistons = DoubleSolenoid(moduleType=wpilib.PneumaticsModuleType.CTREPCM,forwardChannel=3, reverseChannel=4)
        
        self.toggle_state = False

        self._pistons.set(DoubleSolenoid.Value.kReverse)

    def lowerPistons(self):
        
        self._pistons.set(DoubleSolenoid.Value.kForward)

    def raisePistons(self):
        
        self._pistons.set(DoubleSolenoid.Value.kReverse)
    
    def togglePistons(self):

        if self.toggle_state:
            self._pistons.set(DoubleSolenoid.Value.kReverse)
            self.toggle_state = False
        else:
            self._pistons.set(DoubleSolenoid.Value.kForward)
            self.toggle_state = True
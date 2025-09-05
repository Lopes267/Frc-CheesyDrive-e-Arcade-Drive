import wpilib
import rev
import wpilib.drive


class Climber():
    def __init__(self):
         self.climber_right_motor = rev.SparkMax(5, rev.SparkMaxLowLevel.MotorType.kBrushed)
         self.climber_left_motor = rev.SparkMax(6, rev.SparkMaxLowLevel.MotorType.kBrushed)
         self.climber_right_motor.setInverted(True)
         self.climber_motors = wpilib.MotorControllerGroup(self.climber_right_motor, self.climber_left_motor)
    def climber_motor(self,speed):
         self.climber_motors.set(speed)
    
class Climber():
    def __init__(self):
         self.climber_right_motor = CANSparkMax(5, CANSparkMaxLowLevel.MotorType.kBrushed)
         self.climber_left_motor = CANSparkMax(6, CANSparkMaxLowLevel.MotorType.kBrushed)
         self.climber_right_motor.setInverted(True)
         self.climber_motors = wpilib.MotorControllerGroup(self.climber_right_motor, self.climber_left_motor)
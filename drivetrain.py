import wpilib
import wpilib.drive
from rev import CANSparkMax, CANSparkMaxLowLevel

class DriveTrain():
    def __init__(self):
        self.left_front_motor = CANSparkMax(1, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.left_back_motor = CANSparkMax(2, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.right_front_motor = CANSparkMax(3, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.right_back_motor = CANSparkMax(4, CANSparkMaxLowLevel.MotorType.kBrushed)

        # Climber motors
        self.climber_right_motor = CANSparkMax(5, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.climber_left_motor = CANSparkMax(6, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.climber_right_motor.setInverted(True)
        self.climber_motors = wpilib.MotorControllerGroup(self.climber_right_motor, self.climber_left_motor)

        #Drive Motors
        self.left_motors = wpilib.MotorControllerGroup(self.left_front_motor, self.left_back_motor)
        self.right_motors = wpilib.MotorControllerGroup(self.right_front_motor, self.right_back_motor)
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    def arcadeDrive(self, speed, rotation):
        self.drivetrain.arcadeDrive(speed, rotation)
        

        
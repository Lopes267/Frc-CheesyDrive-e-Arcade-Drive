import wpilib
import wpilib.drive
import rev

class DriveTrain():
    def __init__(self):
        self.left_front_motor = rev.SparkMax(1, rev.SparkMaxLowLevel.MotorType.kBrushed)
        self.left_back_motor = rev.SparkMax(2, rev.SparkMaxLowLevel.MotorType.kBrushed)
        self.right_front_motor = rev.SparkMax(3, rev.SparkMaxLowLevel.MotorType.kBrushed)
        self.right_back_motor = rev.SparkMax(4, rev.SparkMaxLowLevel.MotorType.kBrushed)

    
        

        #Drive Motors
        self.left_motors = wpilib.MotorControllerGroup(self.left_front_motor, self.left_back_motor)
        self.right_motors = wpilib.MotorControllerGroup(self.right_front_motor, self.right_back_motor)
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    def arcadeDrive(self, speed, rotation):
        self.drivetrain.arcadeDrive(speed, rotation)
        

        
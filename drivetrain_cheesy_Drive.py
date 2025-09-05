import wpilib
import wpilib.drive
from rev import CANSparkMax, CANSparkMaxLowLevel

class DriveTrain_cheesy_Drive():
    def __init__(self):
        self.left_front_motor = CANSparkMax(1, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.left_back_motor = CANSparkMax(2, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.right_front_motor = CANSparkMax(3, CANSparkMaxLowLevel.MotorType.kBrushed)
        self.right_back_motor = CANSparkMax(4, CANSparkMaxLowLevel.MotorType.kBrushed)

        
        # Drive motors
        self.left_motors = wpilib.MotorControllerGroup(self.left_front_motor, self.left_back_motor)
        self.right_motors = wpilib.MotorControllerGroup(self.right_front_motor, self.right_back_motor)

        self.right_motors.setInverted(True)
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    def cheesyDrive(self, speed: float, rotation: float, quickTurn: bool):
        self.drivetrain.curvatureDrive(speed, rotation, quickTurn)

      


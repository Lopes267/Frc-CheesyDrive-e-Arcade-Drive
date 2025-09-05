import wpilib
import wpilib.drive
import rev
from drivetrain import DriveTrain
from drivetrain_cheesy_Drive import DriveTrain_cheesy_Drive
from climber_motors import Climber

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = DriveTrain()
        self.joystick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.drive = DriveTrain_cheesy_Drive()
        self.climber = Climber

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        rotation = self.joystick.getRawAxis(2)
        speed = -self.joystick.getRawAxis(1)
        quickTurn = self.joystick.getRawButton(1)
        self.drive.cheesyDrive(speed, rotation, quickTurn)

        if self.joystick.getRawButton(3):
            self.drive.climber_motors.set(0.5)
        elif self.joystick.getRawButton(2):
            self.drive.climber_motors.set(-0.5)
        else: 
            self.drive.climber_motors.set(0)

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()
        self.autonomous_duration = 15.0
    def autonomousPeriodic(self):
        if self.timer.get() <= 7.5:
            self.drive.arcadeDrive (0.5, 0)
        elif 7.6 <= self.timer.get() <= 9.0:
            self.drive.climber_motors.set(0.5)
        elif 9.0 < self.timer.get() <= self.autonomous_duration:
            self.drive.arcadeDrive(-0.5, 0)
        else:
            self.drive.arcadeDrive(0, 0)
            self.drive.climber_motors.set(0)

    

            
    




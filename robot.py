import commands2
import wpilib
import wpilib.drive
import rev
from drivetrain import DriveTrain
from climber_motors import Climber
from wpilib import SlewRateLimiter


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = DriveTrain()
        self.joystick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.climber = Climber()
        self.slew_limiter = SlewRateLimiter(2) 
        

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        
        raw_speed = -self.joystick.getRawAxis(1)
        rotation = self.joystick.getRawAxis(2)
        current = self.slew_limiter.lastValue 
        if raw_speed > current:             #calcula para que se tenha uma aceleracao suave
            speed = self.slew_limiter.calculate(raw_speed) 
        else:                               #Freada Rapida
            speed = raw_speed
            self.slew_limiter.reset(raw_speed)
        self.drive.arcadeDrive(speed, rotation)
        

        if self.joystick.getRawButton(1):
            self.climber.climber_motor(0.5)
        elif self.joystick.getRawButton(2):
            self.climber.climber_motor(-0.5)
        else: 
            self.climber.climber_motor(0)

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()
        self.autonomous_duration = 15.0
    def autonomousPeriodic(self):
        if self.timer.get() <= 7.5:
            self.drive.arcadeDrive (0.5, 0)
        elif 7.6 <= self.timer.get() <= 9.0:
            self.climber.climber_motor(0.5)
        elif 9.0 < self.timer.get() <= self.autonomous_duration:
            self.drive.arcadeDrive(-0.5, 0)
        else:
            self.drive.arcadeDrive(0, 0)
            self.climber.climber_motor(0)
    




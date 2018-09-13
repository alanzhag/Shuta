class ShooterService:

    def __init__(self, arduino):
        self.arduino = arduino

    def shoot(self, shots):
        for shot in shots:
            shot.shot_by(self)

    def fire(self, shot):
        self.arduino.send_command(shot.COMMAND)

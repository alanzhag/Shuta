class Shot:

    COMMAND = ""

    def shot_by(self, shooter):
        print("About to shoot some type", self.COMMAND)
        shooter.fire(self)

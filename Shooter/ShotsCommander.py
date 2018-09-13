class ShotsCommander:
    def __init__(self, shooter_service, shots_resolver):
        self.shooter_service = shooter_service
        self.shots_resolver = shots_resolver

    def shoot_shots(self, previous_health, actual_health):
        shots_to_fire = self.shots_resolver.resolve(previous_health, actual_health)
        self.shooter_service.shoot(shots_to_fire)

from Shooter.ShotResolvers.ShotsResolver import ShotsResolver
from Shooter.Shots.AutoShot import AutoShot
from Shooter.Shots.BurstShot import BurstShot
from Shooter.Shots.SingleShot import SingleShot


class LinearHealthShotsResolver(ShotsResolver):
    delta_shot_mapping = {0.3: SingleShot(),
                          0.7: BurstShot(),
                          1: AutoShot()}

    def resolve(self, previous_health, actual_health):
        calculated_delta = self._calculate_delta(previous_health, actual_health)
        for delta_bound in self.delta_shot_mapping.keys():
            if calculated_delta < delta_bound:
                return [self.delta_shot_mapping[delta_bound]]

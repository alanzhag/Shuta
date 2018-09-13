class ShotsResolver:

    def resolve(self, previous_health, actual_health):
        pass

    @staticmethod
    def _calculate_delta(previous, actual):
        return (previous - actual) / previous

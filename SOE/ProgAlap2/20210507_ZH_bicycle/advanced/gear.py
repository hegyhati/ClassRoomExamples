class Gear:

    def __init__(self, teeth_counts: tuple):
        self._teeths = teeth_counts
        self._current_gear = 0

    def shift_up(self):
        if self._current_gear + 1 < len(self._teeths):
            self._current_gear += 1

    def shift_down(self):
        if self._current_gear > 0:
            self._current_gear -= 1

    def current_teeths(self) -> int:
        return self._teeths[self._current_gear]

    def current_gear(self) -> int:
        return self._current_gear + 1


class Bike:

    def __init__(self, wheel_radius_in_cm: float, front_teeths: tuple, rear_teeths: tuple):
        self._wheel_circumference = 2 * wheel_radius_in_cm * 3.141521 / 100  # in m
        self._chainring = Gear(front_teeths)
        self._cassette = Gear(rear_teeths)

    def shift_front_up(self):
        self._chainring.shift_up()

    def shift_front_down(self):
        self._chainring.shift_down()

    def shift_rear_up(self):
        self._cassette.shift_up()

    def shift_rear_down(self):
        self._cassette.shift_down()

    def get_front_gear(self) -> int:
        return self._chainring.current_gear()

    def get_rear_gear(self) -> int:
        return self._cassette.current_gear()

    def get_speed(self, cadence: float) -> float:  # from rounds/min to km/h
        return cadence * 60 * self._chainring.current_teeths() / self._cassette.current_teeths() * self._wheel_circumference / 1000

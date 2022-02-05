from math import pi, isclose

import pytest

from models.function.function import cos_power_series


class TestFunction:

    @pytest.mark.parametrize("test_input, expected",
                             [(0, 1),
                              (pi / 2, 0),
                              (pi, -1),
                              (-pi / 2, 0),
                              (-pi, -1),
                              (2 * pi, 1),
                              (-2 * pi, 1)
                              ])
    def test_dumb_cases(self, test_input, expected):
        assert cos_power_series(test_input) == pytest.approx(expected, 0.001)

    @pytest.mark.parametrize("test_input, expected",
                             [
                                 (0.10, 0.99500),
                                 (0.20, 0.98006),
                                 (0.66, 0.78999),
                                 (5.00, 0.28366)
                             ])
    def test_float_cases(self, test_input, expected):
        assert cos_power_series(test_input) == pytest.approx(expected, 0.001)

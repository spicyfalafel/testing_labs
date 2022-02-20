from math import pi, isclose

import pytest

from models.function.function import sin_power_series


class TestFunction:

    @pytest.mark.parametrize("test_input, expected",
                             [(0, 0),
                              (pi / 2, 1),
                              (pi, 0),
                              (2 * pi, 0)
                              ])
    def test_dumb_cases(self, test_input, expected):
        assert sin_power_series(test_input) == pytest.approx(expected, 0.001)
        assert sin_power_series(-test_input) == pytest.approx(-expected, 0.001)

    @pytest.mark.parametrize("test_input, expected",
                             [
                                 (0.10, 0.09983),
                                 (0.20, 0.19866),
                                 (0.66, 0.61311),
                                 (5.00, -0.95892)
                             ])
    def test_float_cases(self, test_input, expected):
        assert sin_power_series(test_input) == pytest.approx(expected, 0.001)

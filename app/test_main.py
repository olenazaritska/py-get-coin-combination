import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should have correct num of pennies"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should have correct num of pennies and nickels"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should have correct num of pennies, nickels and dimes"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should have correct num of pennies, nickels, "
                   "dimes and quarters"
            )
        ]
    )
    def test_correct_split_into_coins(
            self,
            cents: int,
            expected_combination: list
    ) -> None:
        assert get_coin_combination(cents) == expected_combination

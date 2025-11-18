from bip32 import HARDENED_INDEX

__all__ = ("COIN_PATHS",)


def coin_path_by_index(index: int = 0) -> tuple[int, int]:
    # Full list is at https://github.com/satoshilabs/slips/blob/master/slip-0044.md#registered-coin-types
    return (44 + HARDENED_INDEX, index + HARDENED_INDEX)


COIN_PATHS = {
    "BTC": coin_path_by_index(),
    "TESTNET": coin_path_by_index(1),
    "LTC": coin_path_by_index(2),
    "DOGE": coin_path_by_index(3),
    "ETH": coin_path_by_index(60),
    "ETC": coin_path_by_index(61),
    "XRP": coin_path_by_index(144),
    "DOT": coin_path_by_index(354),
    "SOL": coin_path_by_index(501),
    "APT": coin_path_by_index(637),
    "SUI": coin_path_by_index(784),
    "SDN": coin_path_by_index(809),
    "ASTR": coin_path_by_index(810),
    "ADA": coin_path_by_index(1815),
    "STRK": coin_path_by_index(9004),
}

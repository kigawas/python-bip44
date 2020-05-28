from typing import Tuple, List, Iterable
from bip32 import BIP32, HARDENED_INDEX
from mnemonic import Mnemonic

from bip44.utils import parse_path

COIN_PATHS = {
    "BTC": (44 + HARDENED_INDEX, HARDENED_INDEX),
    "ETH": (44 + HARDENED_INDEX, 60 + HARDENED_INDEX),
}

_Mnemonic = Mnemonic("english")


class Wallet:
    def __init__(self, mnemonic: str):
        self._mnemonic = mnemonic
        self._seed = _Mnemonic.to_seed(mnemonic)
        self._bip32 = BIP32.from_seed(self._seed)

    def _derive_secret(self, path: Iterable[int]) -> bytes:
        return self._bip32.get_privkey_from_path(path)

    def _derive_public(self, path: Iterable[int]) -> bytes:
        return self._bip32.get_pubkey_from_path(path)

    def derive_secret_key(self, path: str) -> bytes:
        return self._derive_secret(parse_path(path))

    def derive_public_key(self, path: str) -> bytes:
        return self._derive_public(parse_path(path))

    def derive_account(
        self, coin: str, account: int = 0, change: int = 0, address_index: int = 0
    ) -> Tuple[bytes, bytes]:
        coin_path = COIN_PATHS[coin.upper()]
        account_path = (account + HARDENED_INDEX, change, address_index)
        path = coin_path + account_path
        return (self._derive_secret(path), self._derive_public(path))

from typing import Tuple, Iterable, Union

from bip32 import BIP32, HARDENED_INDEX
from mnemonic import Mnemonic


COIN_PATHS = {
    "BTC": (44 + HARDENED_INDEX, HARDENED_INDEX),
    "ETH": (44 + HARDENED_INDEX, 60 + HARDENED_INDEX),
}

_Mnemonic = Mnemonic("english")

__all__ = ("Wallet",)


class Wallet:
    def __init__(self, mnemonic: str):
        """
        :param mnemonic (str): The master mnemonic to derive keys
        """
        self._mnemonic = mnemonic
        self._seed = _Mnemonic.to_seed(mnemonic)
        self._bip32 = BIP32.from_seed(self._seed)

    def _derive_secret(self, path: Union[str, Iterable[int]]) -> bytes:
        return self._bip32.get_privkey_from_path(path)

    def _derive_public(self, path: Union[str, Iterable[int]]) -> bytes:
        return self._bip32.get_pubkey_from_path(path)

    def derive_secret_key(self, path: str) -> bytes:
        return self._derive_secret(path)

    def derive_public_key(self, path: str) -> bytes:
        return self._derive_public(path)

    def derive_account(
        self, coin: str, account: int = 0, change: int = 0, address_index: int = 0
    ) -> Tuple[bytes, bytes]:
        # m / purpose' / coin_type' / account' / change / address_index
        coin_path = COIN_PATHS[coin.upper()]
        account_path = (account + HARDENED_INDEX, change, address_index)
        path = coin_path + account_path
        return (self._derive_secret(path), self._derive_public(path))

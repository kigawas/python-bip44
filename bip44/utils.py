from typing import List

from bip32 import HARDENED_INDEX
from coincurve import PublicKey
from sha3 import keccak_256 as _keccak_256

__all__ = ("keccak_256", "get_eth_addr")


def keccak_256(b: bytes) -> bytes:
    h = _keccak_256()
    h.update(b)
    return h.digest()


def get_eth_addr(pk: bytes) -> str:
    if len(pk) != 64:
        pk = PublicKey(pk).format(False)[1:]
    return f"0x{keccak_256(pk)[-20:].hex()}"

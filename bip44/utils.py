from typing import Union

from coincurve import PublicKey
from sha3 import keccak_256 as _keccak_256

__all__ = ("keccak_256", "get_eth_addr")


def keccak_256(b: bytes) -> bytes:
    """Get keccak 256 hash from a bytes input."""
    h = _keccak_256()
    h.update(b)
    return h.digest()


def get_eth_addr(pk: Union[str, bytes]) -> str:
    """Get ETH address from a public key."""

    pk_bytes = bytes.fromhex(pk) if isinstance(pk, str) else pk

    if len(pk_bytes) != 64:
        pk_bytes = PublicKey(pk_bytes).format(False)[1:]

    return f"0x{keccak_256(pk_bytes)[-20:].hex()}"

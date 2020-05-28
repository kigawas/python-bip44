from typing import List
from bip32 import HARDENED_INDEX
from coincurve import PublicKey
from sha3 import keccak_256 as _keccak_256


def keccak_256(b: bytes) -> bytes:
    h = _keccak_256()
    h.update(b)
    return h.digest()


def parse_path(s: str) -> List[int]:
    """
    m / purpose' / coin_type' / account' / change / address_index
    """
    args = s.split("/")
    res = []
    for arg in args:
        if arg == "m":
            continue
        elif arg.endswith("'") or arg.endswith("H") or arg.endswith("h"):
            res.append(int(arg[:-1]) + HARDENED_INDEX)
        else:
            res.append(int(arg))

    return res


def get_eth_addr(pk: bytes) -> str:
    if len(pk) != 64:
        pk = PublicKey(pk).format(False)[1:]
    return f"0x{keccak_256(pk)[-20:].hex()}"

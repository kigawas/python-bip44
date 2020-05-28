from coincurve import PublicKey

from bip44.wallet import Wallet
from bip44.utils import get_eth_addr, keccak_256

MNEMONIC = "purity tunnel grid error scout long fruit false embody caught skin gate"


def test_eth_wallet():
    w = Wallet(MNEMONIC)

    sk, pk = w.derive_account("eth")

    assert sk == bytes.fromhex(
        "ac54f0dc80f38b824c666572a0730ea340d63b2581c41a563e624a41074770df"
    )
    assert pk == bytes.fromhex(
        "02d9ed78008e7b6c4bdc2beea13230fb3ccb8072728c0986894a3d544485e9b727"  # short format
    )

    pk_64bytes = PublicKey(pk).format(False)[1:]
    assert (
        get_eth_addr(pk_64bytes) == "0x7aD23D6eD9a1D98E240988BED0d78e8C81Ec296C".lower()
    )


def test_btc_wallet():
    w = Wallet(MNEMONIC)

    sk, pk = w.derive_account("btc")
    expected_sk = bytes.fromhex(
        "18a4ff856a9fcb2ccc599f9fa4aadef57117122b644669523a992296e68c216a"
    )
    expected_pk = bytes.fromhex(
        "03bbaf7f964e5f07471c931e04479b1787427d14d47f0679601438cca53cadc65b"
    )

    assert sk == expected_sk
    assert pk == expected_pk
    assert pk == PublicKey.from_secret(expected_pk).format()

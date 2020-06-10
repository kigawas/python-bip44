from coincurve import PublicKey

from bip44.wallet import Wallet
from bip44.utils import get_eth_addr, to_checksum_addr

MNEMONIC = "purity tunnel grid error scout long fruit false embody caught skin gate"
MNEMONIC_JA = "なみだ　むろん　しひょう　こうつう　はかい　たいうん　さほう　ことり　げんき　おでかけ　ひこく　ざんしょ"


def test_utils():
    pk = "02d9ed78008e7b6c4bdc2beea13230fb3ccb8072728c0986894a3d544485e9b727"
    addr = "0x7aD23D6eD9a1D98E240988BED0d78e8C81Ec296C"
    assert get_eth_addr(pk) == get_eth_addr(bytes.fromhex(pk))
    assert get_eth_addr(pk) == addr
    assert to_checksum_addr(addr.lower()) == addr

    addr = "0x0Fd60495d705F4Fb86e1b36Be396757689FbE8B3"
    assert to_checksum_addr(addr.lower()) == addr


def test_eth_wallet():
    w = Wallet(MNEMONIC)

    sk, pk = w.derive_account("eth")

    assert sk == bytes.fromhex(
        "ac54f0dc80f38b824c666572a0730ea340d63b2581c41a563e624a41074770df"
    )
    # compressed format pk
    assert pk == bytes.fromhex(
        "02d9ed78008e7b6c4bdc2beea13230fb3ccb8072728c0986894a3d544485e9b727"
    )

    assert sk == w.derive_secret_key("m/44'/60'/0'/0/0")
    assert pk == w.derive_public_key("m/44'/60'/0'/0/0")

    expected_addr = "0x7aD23D6eD9a1D98E240988BED0d78e8C81Ec296C"
    pk_64bytes = PublicKey(pk).format(False)[1:]
    assert get_eth_addr(pk_64bytes) == expected_addr
    assert get_eth_addr(pk) == expected_addr
    assert get_eth_addr(bytes.fromhex(pk_64bytes.hex())) == expected_addr


def test_btc_wallet():
    w = Wallet(MNEMONIC_JA, language="japanese")

    sk, pk = w.derive_account("btc")
    expected_sk = bytes.fromhex(
        "b9a012b6b7a483cd31dee2cf3c6734b7f5c043657f3b7068e3ca806c3b5d7ef1"
    )
    expected_pk = bytes.fromhex(
        "02e5552d6999ce4f43c2b519c3b5d541585a6980dca3f3c5a96ce1b482824dd713"
    )

    assert sk == expected_sk
    assert pk == expected_pk
    assert pk == PublicKey.from_secret(expected_sk).format()

    sk, pk = w.derive_account(1)  # testnet
    expected_pk = bytes.fromhex(
        "02c0dc81e9753524f3303881ab026d27b3a614ce4de93dbe7d2b115aba103d19b5"
    )
    assert pk == expected_pk


def test_passphrase():
    w = Wallet(MNEMONIC, passphrase="@@@@")

    sk, pk = w.derive_account("btc")
    expected_sk = bytes.fromhex(
        "63c7cf13220c7e2d81a7edf88cef431da1f7a323b8cfc9125be4311651aa6b43"
    )
    expected_pk = bytes.fromhex(
        "03fcd9a4f6abc4a0548e57fae133c47de5715372cfc5ea44e2b5f7ab4a3997d344"
    )

    assert sk == expected_sk
    assert pk == expected_pk
    assert pk == PublicKey.from_secret(expected_sk).format()

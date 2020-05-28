# python-bip44

Simple python bip44 implementation. Mnemonic + bip32.

## Quickstart
```python
>>> from coincurve import PrivateKey
>>> from bip44.wallet import Wallet
>>> from bip44.utils import get_eth_addr
>>> mnemonic = "purity tunnel grid error scout long fruit false embody caught skin gate"
>>> w = Wallet(mnemonic)
>>> sk, pk = w.derive_account("eth", account=0)
>>> sk = PrivateKey(sk)
>>> sk.public_key.format() == pk
True
>>> get_eth_addr(pk)
'0x7ad23d6ed9a1d98e240988bed0d78e8c81ec296c'
```

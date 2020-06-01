# python-bip44

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4e4aa71f4a234dca809d014b0b214220)](https://www.codacy.com/manual/kigawas/python-bip44)
[![CI](https://github.com/kigawas/python-bip44/workflows/Build%20and%20test/badge.svg)](https://github.com/kigawas/python-bip44/actions)
[![Codecov](https://img.shields.io/codecov/c/github/kigawas/python-bip44.svg)](https://codecov.io/gh/kigawas/python-bip44)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bip44.svg)](https://pypi.org/project/bip44/)
[![PyPI](https://img.shields.io/pypi/v/bip44.svg)](https://pypi.org/project/bip44/)
[![License](https://img.shields.io/github/license/kigawas/python-bip44.svg)](https://github.com/kigawas/python-bip44)

Simple Python [bip44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) implementation. [Mnemonic](https://github.com/trezor/python-mnemonic) + [bip32](https://github.com/darosior/python-bip32).

## Install

`pip install bip44`

## Quick Start

```python
>>> from coincurve import PrivateKey
>>> from bip44 import Wallet
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

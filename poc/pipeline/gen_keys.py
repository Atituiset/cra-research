#!/usr/bin/env python3
"""Generate the dev-only ed25519 signing keypair in poc/keys/.

DEVELOPMENT ONLY — see keys/README.md. Production would use KMS/HSM-backed
signers (securesystemslib supports cloud KMS via signer URIs).
"""
import json
import os
import sys

from cryptography.hazmat.primitives import serialization
from securesystemslib.signer import CryptoSigner

KEYS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "keys")
PRIV = os.path.join(KEYS_DIR, "dev-ed25519.pem")
PUB = os.path.join(KEYS_DIR, "dev-ed25519.pub.json")


def main():
    os.makedirs(KEYS_DIR, exist_ok=True)
    if os.path.exists(PRIV) and os.path.exists(PUB):
        print(f"keys already exist ({PRIV}); keeping")
        return
    signer = CryptoSigner.generate_ed25519()
    with open(PRIV, "wb") as f:
        f.write(signer.private_bytes)
    os.chmod(PRIV, 0o600)
    pub = signer.public_key
    with open(PUB, "w") as f:
        json.dump({"keyid": pub.keyid, **pub.to_dict()}, f, indent=2)
    print(f"generated ed25519 keypair: keyid={pub.keyid}")
    print(f"  private: {PRIV} (dev only!)")
    print(f"  public:  {PUB}")


if __name__ == "__main__":
    main()

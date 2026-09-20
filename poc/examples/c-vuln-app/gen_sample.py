#!/usr/bin/env python3
"""Generate sample.gz: a gzip stream whose header carries an FEXTRA field.

zlib <= 1.2.12 (CVE-2022-37434) mishandles the EXTRA state in inflate() when
the extra field is longer than the space reserved by inflateGetHeader().
This sample exercises that code path; it is the input that makes the
curated vuln->function mapping (inflate) reachable from main().
"""
import struct
import zlib

payload = b"hello cra poc\n"

# raw deflate stream
co = zlib.compressobj(9, zlib.DEFLATED, -15)
body = co.compress(payload) + co.flush()

extra_id = b"PO"
extra_data = b"cra-poc"
extra = extra_id + struct.pack("<H", len(extra_data)) + extra_data

hdr = (
    b"\x1f\x8b"          # magic
    b"\x08"              # CM = deflate
    b"\x04"              # FLG = FEXTRA
    + struct.pack("<I", 0)  # MTIME
    + b"\x00"            # XFL
    + b"\x03"            # OS = unix
    + struct.pack("<H", len(extra))
    + extra
)
trailer = struct.pack("<II", zlib.crc32(payload) & 0xFFFFFFFF, len(payload))

with open("sample.gz", "wb") as f:
    f.write(hdr + body + trailer)
print("wrote sample.gz", len(hdr + body + trailer), "bytes")

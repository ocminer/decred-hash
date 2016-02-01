# This is a Testcase for Decred, see https://wiki.decred.org/Block_Header_Specifications
#
# ocminer - admin AT suprnova.cc 16/02/01
#
# Teststart refers to the original block header bytes from the example given on the page
# The Hash must return df03ea8cb4a6f201c3e726f2f922a9249b39129bb59fa593ceb172e0f7c14d6e if your module is hashing correctly


import blake_hash
import weakref
import binascii
import StringIO

from binascii import unhexlify
from binascii import hexlify
#teststart = '000000ba5cae4648b1a2b823f84cc3424e5d96d7234b39c6bb42800b2c7639be';
teststart = '010000006fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d61900000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a00000000000000000000000000000000ffff001d0000000000000000000000000000000029ab5f49f3e00100000000000000000000000000000000000000000000000000000000000000000000000000'
testbin = unhexlify(teststart)
hash_bin = blake_hash.getPoWHash(testbin)
out = hexlify(hash_bin[::-1])
print(out)      # DEBUG


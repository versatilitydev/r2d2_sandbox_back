import hashlib

def sha256_hash(file):
    sha256_hash = hashlib.sha256()
    # Read the file in chunks and update the hash
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    file.close()
    return sha256_hash.hexdigest()



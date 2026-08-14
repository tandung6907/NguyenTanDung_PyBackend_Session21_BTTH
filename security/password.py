import bcrypt

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    # B1 encode the password to bytes
    bytes_password = password.encode('utf-8')
    # B2 hash the password with a salt
    hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
    # B3 decode the hashed password to a string
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash."""
    # B1 encode the password to bytes
    bytes_password = password.encode('utf-8')
    # B2 encode the hashed password to bytes
    bytes_hashed = hashed.encode('utf-8')
    # B3 check the password against the hash
    return bcrypt.checkpw(bytes_password, bytes_hashed)

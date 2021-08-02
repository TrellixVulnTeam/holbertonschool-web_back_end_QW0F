#!/usr/bin/env python3
"""hash_password module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns byte string"""

    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password matches the hashed password"""

    hashed_password = hash_password(password)
    if bcrypt.checkpw(password.encode('utf8'), hashed_password):
        return True
    else:
        return False

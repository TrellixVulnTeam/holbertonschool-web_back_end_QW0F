#!/usr/bin/env python3
"""auth module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return path, excluded_path, otherwise False"""
        return False

    def authorization_header(self, request=None) -> str:
        """return request, otherwise None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return request, otherwise None"""
        return None

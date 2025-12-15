"""Utility helpers for Nintendo Parental Controls."""

from __future__ import annotations

from pynintendoparental import Authenticator


def prepare_authenticator(authenticator: Authenticator) -> Authenticator:
    """Ensure authenticator exposes a public refresh method.

    The upstream library currently only exposes ``_perform_refresh`` which is
    used internally by the API client via ``perform_refresh``. Provide the
    expected attribute when it is missing so API requests can refresh tokens
    correctly.
    """

    if not hasattr(authenticator, "perform_refresh"):
        authenticator.perform_refresh = authenticator._perform_refresh  # type: ignore[attr-defined,assignment]

    return authenticator


# Copyright: (c) 2023 Jordan Borean (@jborean93) <jborean93@gmail.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import annotations

import sspic


def test_cred_no_user() -> None:
    cred = sspic.UserCredential()
    assert str(cred) == "CurrentUser - Negotiate"
    assert cred.username == "CurrentUser"


def test_cred_username_no_domain() -> None:
    cred = sspic.UserCredential("user")
    assert str(cred) == "user - Negotiate"
    assert cred.username == "user"


def test_cred_username_upn() -> None:
    cred = sspic.UserCredential("user@DOMAIN.COM")
    assert str(cred) == "user@DOMAIN.COM - Negotiate"
    assert cred.username == "user@DOMAIN.COM"


def test_cred_username_domain() -> None:
    cred = sspic.UserCredential("user", domain="domain")
    assert str(cred) == "domain\\user - Negotiate"
    assert cred.username == "domain\\user"

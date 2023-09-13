import sspi


def test_enumerate_security_packages() -> None:
    actual = sspi.enumerate_security_packages()
    assert isinstance(actual, list)
    for sec_pkg in actual:
        assert isinstance(sec_pkg, sspi.SecPkgInfo)
        assert isinstance(sec_pkg.capabilities, sspi.SecurityPackageCapability)
        assert isinstance(sec_pkg.name, str)
        assert sec_pkg.name
        assert isinstance(sec_pkg.comment, str)

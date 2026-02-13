"""Smoke tests for the Ever Gauzy Python SDK."""


def test_package_imports():
    """Test that the SDK package can be imported."""
    import ever_gauzy_sdk
    assert ever_gauzy_sdk is not None

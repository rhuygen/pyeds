
def test_module_load():
    from pyeds import fsm
    from pyeds import coordinator
    from pyeds import lib

def test_module_version():
    from pyeds import __version__
    # For python3 there is no more basestring. Python3 only uses str class.
    assert isinstance(__version__, str)


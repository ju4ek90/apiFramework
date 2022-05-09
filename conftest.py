def pytest_addoption(parser):
    """Method for defining parameter --browser, for the pytest call"""
    parser.addoption("--browser", action="store", help="Select parameter 'browser'")
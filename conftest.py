from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle

fixture = None
config_file = None


@pytest.fixture
def app(request):
    global fixture
    global config_file

    browser = request.config.getoption("--browser")

    if config_file is None:
        config_file_json = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        request.config.getoption("--target"))
        with open(config_file_json) as f:
            config_file = json.load(f)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config_file["baseUrl"])

    fixture.session.ensure_login(username=config_file["username"], password=config_file["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# parametri komandnoi ctroki
# hook function https://docs.pytest.org/en/latest/parametrize.html#basic-pytest-generate-tests-example
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


# sviazivaev dinamicheski testi i dannie
# hook function https://docs.pytest.org/en/latest/parametrize.html#basic-pytest-generate-tests-example
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

# zagruska dannih iz data/modile.py
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

# zagruska dannih iz data/modile.json
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

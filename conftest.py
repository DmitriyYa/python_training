from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
config_file = None


def load_config(file):
    global config_file
    if config_file is None:
        config_file_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file_json) as f:
            config_file = json.load(f)
    return config_file


@pytest.fixture
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])

    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


# fixtura dliya raboty s bd
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])

    def fin():
        pass  #dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# parametri komandnoi ctroki
# hook function https://docs.pytest.org/en/latest/parametrize.html#basic-pytest-generate-tests-example
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


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

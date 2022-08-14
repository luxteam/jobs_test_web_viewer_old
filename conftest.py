import pytest
import argparse
import os
import yaml

conf = None

def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="default name")

def pytest_configure(config):
    global conf
    with open(__file__ + "\\..\\Utils\\ConfigurationFiles\\" + config.option.domain + "Config.yaml", "r") as ymlfile:
        conf = yaml.load(ymlfile, Loader=yaml.FullLoader)

# Timeout for an induvidual test. Will terminate the entire run, if timeout is exceeded
def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.timeout(180))

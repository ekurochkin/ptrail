# coding: utf8

import py.test
# from testrail import APIClient as TestrailClient


def pytest_addoption(parser):
    parser.getgroup("reporting").addoption("--sync", action="store_true")
    parser.getgroup("reporting").addoption("--testrail", action="store_true")


def pytest_configure(config):
    config.pluginmanager.register(TestListener(config))


class TestListener(object):
    def __init__(self, config):
        self.config = config

    def _send_report(self, report, status=None):
        pass

    def pytest_runtest_logreport(self, report):
        print("My custom report", report.nodeid, report.when, report.outcome)

    def pytest_sessionfinish(self):
        print("End testing")

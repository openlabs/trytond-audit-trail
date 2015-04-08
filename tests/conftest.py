# -*- coding: utf-8 -*-
"""
    tests/conftest.py

    :copyright: (C) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import time
import pytest


@pytest.fixture(params=["sqlite"])
def install_module(request, monkeypatch):
    """Install tryton module in specified database.
    """
    if request.param == 'sqlite':
        monkeypatch.setenv('DB_NAME', ':memory:')
    else:
        monkeypatch.setenv('DB_NAME', 'test_' + str(int(time.time())))

    from trytond.tests import test_tryton
    test_tryton.install_module('audit_trail')


@pytest.yield_fixture()
def transaction(install_module):
    """Yields transaction with installed module.
    """
    from trytond.transaction import Transaction
    from trytond.tests.test_tryton import USER, CONTEXT, DB_NAME

    with Transaction().start(DB_NAME, USER, context=CONTEXT) as transaction:
        yield transaction

        transaction.cursor.rollback()

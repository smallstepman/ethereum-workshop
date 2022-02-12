#!/usr/bin/env python3

from brownie import SimpleStorage, accounts

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 5
    assert starting_value == expected

def test_updating_starage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    simple_storage.store(expected, {"from": account})
    assert expected == simple_storage.retrieve()

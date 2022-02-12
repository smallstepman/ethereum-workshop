#!/usr/bin/env python3

import time
from brownie import network
import pytest

from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, _ = deploy_and_create()
    time.sleep(60)
    assert advanced_collectible.tokenCounter() == 1

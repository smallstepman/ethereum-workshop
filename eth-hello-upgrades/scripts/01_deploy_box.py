#!/usr/bin/env python3

from scripts.utils import get_account
from brownie import network, Box, ProxyAdmin


def main():
    account = get_account()
    print(f"deploying to {network.show_active()}")
    box = Box.deploy({"from": account})

    proxy_admin = ProxyAdmin.deploy({"from": account})

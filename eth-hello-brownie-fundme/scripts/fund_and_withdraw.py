#!/usr/bin/env python3

from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    enterence_fee = fund_me.getEntarenceFee()
    print(enterence_fee)
    fund_me.fund({"from":account, "value":enterence_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw()
    fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()

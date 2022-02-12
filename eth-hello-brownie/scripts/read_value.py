#!/usr/bin/env python3

from brownie import SimpleStorage, accounts, config

def read_contract():
    ss= SimpleStorage[0]
    print(ss.retrieve())

def main():
    read_contract()

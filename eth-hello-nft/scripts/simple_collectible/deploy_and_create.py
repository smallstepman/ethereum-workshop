#!/usr/bin/env python3

from brownie import SimpleCollectible
from scripts.utils import get_account, OPENSEA_URL

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    print(account)
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    opensea_asset_url = OPENSEA_URL.format(
        simple_collectible.address, simple_collectible.tokenCounter() - 1
    )
    print(f"view your nft at {opensea_asset_url}")
    return simple_collectible


def main():
    deploy_and_create()

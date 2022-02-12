#!/usr/bin/env python3
from brownie import AdvancedCollectible, config, network
from scripts.utils import fund_with_link, get_account, OPENSEA_URL, get_contract

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    print(advanced_collectible)
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(5)
    print(advanced_collectible.tokenCounter())
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()

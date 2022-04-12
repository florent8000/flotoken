from scripts.helpful_scripts import get_account
from brownie import FLOToken, network, config
from web3 import Web3

initial_supply = Web3.toWei(1_000_000, "ether")


def deploy_token():
    account = get_account()
    flotoken = FLOToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed token!")
    return flotoken


def main():
    deploy_token()

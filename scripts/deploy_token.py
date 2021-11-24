from scripts.helpful_scripts import get_account
from brownie import ArtemToken, network, config
from web3 import Web3


def deploy_artem_token():
    account = get_account()
    artem_token = ArtemToken.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    # artem_token.wait(1)


def main():
    deploy_artem_token()

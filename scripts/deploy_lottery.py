from typing import List
from web3.main import Web3
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    fund_with_link,
)
from brownie import ArtemLottery, network, config
import time
from web3 import Web3
import yaml
import json
import os
import shutil


DEFAULT_ENTRANCE_FEE_USD = Web3.toWei(10, "ether")
DEFAULT_LOTTERY_LENGTH_IN_SECONDS = 60 * 60 * 24  # 24 hours


def deploy_lottery(front_end_update=False):
    account = get_account()
    lottery = ArtemLottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        DEFAULT_ENTRANCE_FEE_USD,
        DEFAULT_LOTTERY_LENGTH_IN_SECONDS,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery!")
    if front_end_update:
        update_front_end()
    return lottery


def start_lottery():
    account = get_account()
    lottery = ArtemLottery[-1]
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    print("The lottery is started!")


def enter_lottery():
    account = get_account()
    lottery = ArtemLottery[-1]
    value = lottery.getEntranceFee() + 100000000
    tx = lottery.enter({"from": account, "value": value})
    tx.wait(1)
    print("You entered the lottery!")


def end_lottery():
    account = get_account()
    lottery = ArtemLottery[-1]
    # fund the contract
    # then end the lottery
    tx = fund_with_link(lottery.address)
    tx.wait(1)
    ending_transaction = lottery.endLottery(False, {"from": account})
    ending_transaction.wait(1)
    print("endlottery requested")


def update_front_end():
    # Send the build folder
    copy_folders_to_front_end("./build", "./front_end/src/chain-info")

    # Sending the front end our config in JSON format
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./front_end/src/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Front end updated!")


def copy_folders_to_front_end(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main():
    lottery = deploy_lottery(front_end_update=True)

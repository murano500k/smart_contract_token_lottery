from typing import List
from web3.main import Web3
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    fund_with_link,
    listen_for_end_lottery_event,
)
from brownie import ArtemLottery, network, config
import time
from web3 import Web3


DEFAULT_ENTRANCE_FEE_USD = Web3.toWei(10, "ether")


def deploy_lottery():
    account = get_account()
    lottery = ArtemLottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        DEFAULT_ENTRANCE_FEE_USD,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery!")
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
    ending_transaction = lottery.endLottery({"from": account})
    ending_transaction.wait(1)
    print("endlottery requested")


def main():
    # lottery = ArtemLottery[-1]
    # if not lottery:
    lottery = deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
    listen_for_end_lottery_event(lottery)

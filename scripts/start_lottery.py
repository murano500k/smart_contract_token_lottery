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


def start_lottery():
    account = get_account()
    lottery = ArtemLottery[-1]
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    print("The lottery is started!")


def main():
    start_lottery()

from typing import List
from web3.main import Web3
from scripts.helpful_scripts import get_account
from brownie import ArtemLottery


def enter_lottery():
    account = get_account()
    lottery = ArtemLottery[-1]
    value = lottery.getEntranceFee() + 100000000
    tx = lottery.enter({"from": account, "value": value})
    tx.wait(1)
    print("You entered the lottery!")


def main():
    lottery = ArtemLottery[-1]
    enter_lottery()

from typing import List
from web3.main import Web3
from scripts.helpful_scripts import (
    fund_with_link,
)
from brownie import ArtemLottery


def main():
    lottery = ArtemLottery[-1]
    tx = fund_with_link(lottery.address)
    tx.wait(1)

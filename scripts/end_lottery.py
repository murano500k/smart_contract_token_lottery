from typing import List
from web3.main import Web3
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    fund_with_link,
    listen_for_end_lottery_event,
)
from brownie import ArtemLottery


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


def main():
    lottery = ArtemLottery[-1]
    # if not lottery:
    #     lottery = deploy_lottery()
    # lottery = deploy_lottery()
    # start_lottery()
    end_lottery()
    listen_for_end_lottery_event(lottery)

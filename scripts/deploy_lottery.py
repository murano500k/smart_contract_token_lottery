from typing import List
from web3.main import Web3
from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from brownie import ArtemLottery, network, config
import time
import json
import asyncio
from web3 import Web3
import os


INFURA_PROJECT_ID = os.getenv("WEB3_INFURA_PROJECT_ID")
INFURA_URL_BASE = "https://rinkeby.infura.io/v3/"
infura_url = INFURA_URL_BASE + INFURA_PROJECT_ID
web3 = Web3(Web3.HTTPProvider(infura_url))


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


# define function to handle events and print to the console
def handle_event(event):
    print("handle event!")
    lottery = ArtemLottery[-1]
    print(f"lottery.winner={lottery.recentWinner()}")
    print(f"event={event}")
    return 1


async def log_loop(event_filter, poll_interval):
    counter = 0
    result = 0
    while not result:
        for event in event_filter.get_new_entries():
            result = handle_event(event)
        print(f"waiting... {counter}")
        counter += 2
        await asyncio.sleep(poll_interval)


def listen_for_end_lottery_event():
    lottery = ArtemLottery[-1]
    contract = web3.eth.contract(address=lottery.address, abi=ArtemLottery.abi)
    event_filter = contract.events.LotteryEnded.createFilter(fromBlock="latest")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(log_loop(event_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()


def main():
    lottery = ArtemLottery[-1]
    if not lottery:
        lottery = deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
    listen_for_end_lottery_event()

#!/usr/bin/python3
from brownie import ArtemLottery
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    keeper_contract = ArtemLottery[-1]
    upkeepNeeded, performData = keeper_contract.checkUpkeep.call(
        "",
        {"from": account},
    )
    print(f"The status of this upkeep is currently: {upkeepNeeded}")
    print(f"Here is the perform data: {performData}")

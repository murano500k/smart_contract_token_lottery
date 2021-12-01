from scripts.helpful_scripts import (
    get_account,
)
from brownie import ArtemLottery


def main():
    lottery = ArtemLottery[-1]
    account = get_account()
    print(f"{lottery}")
    state = lottery.lottery_state()
    print(f"state={state}")
    counter = lottery.lotteryCounter()
    print(f"counter={counter}")
    winner = lottery.recentWinner()
    print(f"winner={winner}")
    balance = lottery.balance()
    print(f"balance={balance}")
    lastTimeStamp = lottery.lastTimeStamp()
    print(f"lastTimeStamp={lastTimeStamp}")
    upkeepNeeded, performData = lottery.checkUpkeep.call(
        "",
        {"from": account},
    )
    print(f"The status of this upkeep is currently: {upkeepNeeded}")
    print(f"Here is the perform data: {performData}")

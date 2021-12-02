from brownie import network, ArtemLottery
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    fund_with_link,
)
from scripts.deploy_lottery import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery(False, {"from": account})

    time.sleep(200)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0


def test_lottery_finished_single_player():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # lottery = deploy_lottery()
    lottery = ArtemLottery[-1]
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.endLottery(False, {"from": account})

    time.sleep(20)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0


def test_events_emited():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # TODO: Add a test for async callback on rinkeby
    pass

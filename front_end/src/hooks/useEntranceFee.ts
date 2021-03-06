import { useEthers, useContractFunction, useContractCall } from "@usedapp/core"
import { constants, utils, BigNumber } from "ethers"
import ArtemLottery from "../chain-info/contracts/ArtemLottery.json"
import networkMapping from "../chain-info/deployments/map.json"
import { formatUnits } from "@ethersproject/units"


export const useEntranceFee = (): BigNumber | undefined => {
    const { chainId } = useEthers()
    const { abi } = ArtemLottery
    const artemLotteryAddress = chainId ? networkMapping[String(chainId)]["ArtemLottery"][0] : constants.AddressZero
    const artemLotteryInterface = new utils.Interface(abi)
    const [entranceFee]: any = useContractCall({
        abi: artemLotteryInterface,
        address: artemLotteryAddress,
        method: "getEntranceFee",
        args: [],
    }) ?? []

    return entranceFee;
}
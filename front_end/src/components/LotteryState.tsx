import { useLotteryState, useLotteryBalance, useLotteryTimeStamp, useLotteryCounter } from "../hooks"
import { makeStyles } from "@material-ui/core"
import { formatUnits } from "@ethersproject/units"



const useStyles = makeStyles((theme) => ({
    title: {
        color: theme.palette.common.white,
        textAlign: "center",
        padding: theme.spacing(4)
    }
}))

export const LotteryState = () => {
    const classes = useStyles()
    const lotteryState = useLotteryState()
    const balance = useLotteryBalance()

    const formattedBalance: number = balance?._hex
        ? parseFloat(formatUnits(balance._hex, 18))
        : -1
    const counter = useLotteryCounter()
    const timestamp = useLotteryTimeStamp()
    return (
        <>
            <h2 className={classes.title}> lottery_state = {lotteryState}</h2>
            <h2 className={classes.title}> formattedBalance = {formattedBalance}</h2>
            <h2 className={classes.title}> balance = {balance ? balance.toNumber() : -10}</h2>
            <h2 className={classes.title}> counter = {counter ? counter.toNumber() : -10}</h2>
            <h2 className={classes.title}> lastTimeStamp = {timestamp}</h2>

        </>)
}


import { useLotteryState, useLotteryBalance, useLotteryTimeStamp, useLotteryCounter } from "../hooks"
import { makeStyles } from "@material-ui/core"



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
    const counter = useLotteryCounter()
    const timestamp = useLotteryTimeStamp()
    return (
        <>
            <h2 className={classes.title}> Lottery is {lotteryState} now</h2>
            <h2 className={classes.title}> Lottery balance is {balance} ethers</h2>
            <h2 className={classes.title}> Lottery counter is {counter ? counter.toNumber() : -10}</h2>
            <h2 className={classes.title}> last updated {timestamp}</h2>

        </>)
}


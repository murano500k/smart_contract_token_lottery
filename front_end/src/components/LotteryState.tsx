import { useLotteryState, useLotteryBalance, useLotteryTimeStamp, useLotteryCounter, useRecentWinner } from "../hooks"
import { makeStyles } from "@material-ui/core"



const useStyles = makeStyles((theme) => ({
    title: {
        color: theme.palette.common.white,
        textAlign: "center",
        padding: theme.spacing(4)
    },
    subtitle: {
        color: theme.palette.common.white,
        textAlign: "center",
        padding: theme.spacing(1)
    },
}))

export const LotteryState = () => {
    const classes = useStyles()
    const lotteryState = useLotteryState()
    const balance = useLotteryBalance()
    const counter = useLotteryCounter()
    const timestamp = useLotteryTimeStamp()
    const recentWinner = useRecentWinner()
    return (
        <>
            <h2 className={classes.subtitle}> Lottery is {lotteryState} now</h2>
            <h2 className={classes.subtitle}> Lottery balance is {balance} ethers</h2>
            <h2 className={classes.subtitle}> Recent winner is {recentWinner}</h2>
            <h2 className={classes.subtitle}> Lottery counter is {counter ? counter.toNumber() : -10}</h2>
            <h2 className={classes.subtitle}> last updated {timestamp}</h2>

        </>)
}


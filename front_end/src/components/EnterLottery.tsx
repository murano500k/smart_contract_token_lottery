import React, { useEffect, useState } from "react"
import { makeStyles, Button, Input, CircularProgress, Snackbar } from "@material-ui/core"
import { useEnterLottery, useEntranceFee } from "../hooks"



const useStyles = makeStyles((theme) => ({
    root: {
        justifyContent: 'center'
    },
    text: {
        color: theme.palette.common.white,
    }
}))



export const EnterLottery = () => {
    const classes = useStyles()
    const { enterLotterySend, enterLotteryState } =
        useEnterLottery()

    const entranceFee = useEntranceFee()

    const handleEnterLottery = () => {
        return enterLotterySend({ value: entranceFee })
    }
    const isMining = enterLotteryState.status === "Mining"



    return (
        <>
            <Button
                color="primary"
                variant="contained"
                size="large"
                onClick={handleEnterLottery}
                disabled={isMining}>
                {isMining ? <CircularProgress size={26} /> : "Enter lottery"}
            </Button>
            <div>{entranceFee ? entranceFee.toNumber() : -1}</div>

        </>)
}


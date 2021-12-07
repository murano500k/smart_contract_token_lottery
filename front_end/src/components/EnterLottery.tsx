import { makeStyles, Button } from "@material-ui/core"



const useStyles = makeStyles((theme) => ({
    root: {
        justifyContent: 'center'
    },
    title: {
        color: theme.palette.common.white,
        textAlign: "center",
        padding: theme.spacing(4)
    }
}))

export const EnterLottery = () => {
    const classes = useStyles()
    return (
        <>
            <Button
                color="primary"
                variant="contained"
                size="large"
            >
                Enter lottery
            </Button>
        </>)
}


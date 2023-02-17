import React from 'react'
import Box from '@mui/material/Box';
import SpeedDial from '@mui/material/SpeedDial';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';
import SpeedDialAction from '@mui/material/SpeedDialAction';
import FileCopyIcon from '@mui/icons-material/FileCopyOutlined';
import SaveIcon from '@mui/icons-material/Save';
import PrintIcon from '@mui/icons-material/Print';
import ShareIcon from '@mui/icons-material/Share';
import { Button } from '@mui/material';
// import * as React from 'react';

const actions = [
    { icon: <FileCopyIcon />, name: 'Copy' },
    { icon: <SaveIcon />, name: 'Save' },
    { icon: <PrintIcon />, name: 'Print' },
    { icon: <ShareIcon />, name: 'Share' },
];

function Home() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const addBlog=()=>{
        console.log("button clicked")
    }
    return (
        <div className='homemain'>
            <h1>This is home page</h1>
            <h3>Here we will place blogs available to read</h3>
            
                <Box sx={{ height: 320, transform: 'translateZ(0px)', flexGrow: 1 }}>
                    <Button
                        sx={{ position: 'absolute', bottom: 16, right: 16 }}
                        onClick={addBlog}
                    >
                        Add
                    </Button>
                </Box>
            
        </div>
    )
}

export default Home

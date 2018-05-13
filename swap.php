
<?php
        if(!empty($_REQUEST['device'])) { // i used $_REQUEST because it receives the data from POST or GET.
            $device = $_REQUEST['device'];
            exec("python3 swap_state.py $device");
        } 
    ?>
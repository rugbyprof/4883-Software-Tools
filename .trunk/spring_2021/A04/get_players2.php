<?php

/**
 * This function is an example of running a sql query using php. The difference between this one
 * and the 1st one is this one simply returns our result as an array. If you want to get the data
 * from the result, you have to loop through the result set. Simply returning "$result" wouldn't
 * give you the data. You would still need to loop through it.  
 */
function getPlayers2(){
    global $mysqli; // this is how we access global vars

    // create a sql query
    $sql = 'SELECT * FROM players';

    // run the query
    $result = $mysqli->query($sql);

    // Create a return array:
    $data = [];

    // If we were successful
    if($result){

        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            // This "pushes" $row onto end of data array
            $data[] = $row;
        }
    }else{
        // Print the error :) 
        echo "{$mysqli->error}";
    }

    // If we were successful, then free the result
    if($result){
        $result->free();
    }

    // Return our data
    return $data;
}
?>
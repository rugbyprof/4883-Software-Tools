<?php
/**
 * This function is an example of running a sql query using php. The query returns ALL the players
 * in the "players" table. Each iteration of the while loop below prints an associative array
 * like this one:
 * Array
 * (
 *    [id]      => 00-0022927
 *    [name]    => K.Dansby
 *    [season]  => 2013
 *    [club]    => ARI
 * )
 * 
 */
function getPlayers1(){
    global $mysqli; // this is how we access global vars

    // create a sql query
    $sql = 'SELECT * FROM players';

    // run the query
    $result = $mysqli->query($sql);

    // If we were successful
    if($result){

        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            print_r($row);
        }
    }else{
        // Print the error :) 
        echo "{$mysqli->error}";
    }

    // If we were successful, then free the result
    if($result){
        $result->free();
    }
}
?>
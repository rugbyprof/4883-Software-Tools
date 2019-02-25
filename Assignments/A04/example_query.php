<?php

//Find the Team with the largest average interception returns by year.

//Connect to mysql
$host = "localhost";             // because we are ON the server
$user = "software_tools";        // user name

// Get username and password from slack
// The DB username and pass not the ones
// I sent you to log into the server.
$password = "******";         // password 
$database = "nfl_data";              // database 
$mysqli = mysqli_connect($host, $user, $password, $database);

if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


/**
 * This function runs a SQL query and returns the data in an associative array
 * that looks like:
 * $response [
 *      "success" => true or false
 *      "error" => contains error if success == false
 *      "result" => associative array of the result
 * ]
 *
 */
function runQuery($mysqli,$sql){
    $response = [];

    // run the query
    $result = $mysqli->query($sql);

    // If we were successful
    if($result){
        $response['success'] = true;
        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            $response['result'][] = $row;
        }
        $result->free();
    }else{
        $response['success'] = false;
        $response['error'] = $mysqli->error;
    }

    return $response;
}


$sql = "SELECT * 
        FROM `players_stats` 
        WHERE statid = '25'";


$response = runQuery($mysqli, $sql);

echo "<pre>";   // so whitespace matters

$stats = [];

if($response['success']){
    foreach($response['result'] as $row){
        $season = $row['season'];
        $club = $row['club'];
        $yards = $row['yards'];

        if(!array_key_exists($season,$stats)){
            $stats[$season] = [];
        }

        if(!array_key_exists($club,$stats[$season])){
            $stats[$season][$club] = [];
        }

        $stats[$season][$club][] = $yards;
        
    }
}

// for($i=2009;$i<=2018;$i++){
//     print_r($stats[$i]);
// }

$totals = [];

foreach($stats as $year => $yearly_stat){
    //echo"<h1>$year</h1>";
    foreach($yearly_stat as $team => $yards){
        //echo"<h3>$team</h3>"; 
        //print_r($yards);
        $totals[$year][$team] = array_sum($yards) / sizeof($yards);
    }
    arsort($totals[$year]);
}

foreach($totals as $year => $data){
    $key = key($data);
    $val = $data[$key];
    echo"$year $key => $val\n";
}

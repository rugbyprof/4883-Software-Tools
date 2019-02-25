<?php
/**
 * This file answers the following questions from A03. It uses SQL
 * as opposed to the comparitively painful processing of json.
 * 
 * 1. Find the player(s) that played for the most teams.
 * 2. Find the player(s) that played for multiple teams in one year.
 * 3. Find the player(s) that had the most yards rushed for a loss.
 * 4. Find the player(s) that had the most rushes for a loss.
 * 5. Find the player(s) with the most number of passes for a loss.
 * 6. Find the team with the most penalties.
 * 7. Find the team with the most yards in penalties.
 * 8. Find the correlation between most penalized teams and games won / lost.
 * 9. Average number of plays in a game.
 * 10. Longest field goal.
 * 11. Most field goals.
 * 12. Most missed field goals.
 * 13. Most dropped passes (Search for "pass" and "dropped" in play description, and stat-id 115).
 */

// Require the config file with credentials
<<<<<<< HEAD
//require("/Users/griffin/Code/1-Current_Courses/.config.php");

$host = 'cs2.mwsu.edu';
$user = 'software_tools';
$password = 'horseblanketdonkey';
$database = 'nfl_data';
=======
include("/Users/griffin/Code/1-Current_Courses/.config.php");
include("../4883_db_config.php");
>>>>>>> 1f125aed3043bba1c6427c4e098cb715dba0e894

//Connect to mysql
$mysqli = mysqli_connect($host, $user, $password, $database);

// Throw mysql error
if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

// Helper function to run sql
require "query_function.php";

function f(){
    ob_flush();
    flush();
}

/**
 * Pulls a player out of players table and returns:
 *     [name] => Player.Name
 * Params:
 *     playerId [string] : id of type => 00-000001234
 * Returns:
 *     name [string] : => T. Smith
 */
function getPlayer($playerId){
    global $mysqli;
    $sql = "SELECT `name` FROM players WHERE id = '{$playerId}' LIMIT 1";
    $response = runQuery($mysqli,$sql); 
    if(!array_key_exists('error',$response)){
        return $response['result'][0]['name'];
    }
    return null;
}

/**
 * Prints a question plus a border underneath
 * Params:
 *     question [string] : "Who ran the most yards in 2009?"
 *     pads [array] : [3,15,15,5] padding for each data field
 * Returns:
 *     header [string] : Question with border below
 */
function printHeader($question,$pads,$cols){
    if(strlen($question) > array_sum($pads)){
        $padding = strlen($question);
    }else{
        $padding = array_sum($pads);
    }
    $header = "\n<b>";
    $header .= "{$question}\n\n";
    for($i=0;$i<sizeof($cols);$i++){
        $header .= str_pad($cols[$i],$pads[$i]);
    }
    $header .= "\n".str_repeat("=",$padding);

    $header .= "</b>\n";

    return $header;
}

/**
 * formatRows:
 *    Prints each row with a specified padding for allignment
 * Params:
 *    $row [array] - array of multityped values to be printed
 *    $cols [array] - array of ints corresponding to each column size wanted
 * Example:
 *    
 *    $row = ['1','00-00000123','T. Smith','329']
 *    $pads = [4,14,20,5]
 */
function formatRows($row,$pads){
    $ouput = "";

    for($i=0;$i<sizeof($row);$i++){
        $output .= str_pad($row[$i],$pads[$i]);
    }
    return $output."\n";
}

/**
 * displayQuery: print question + sql result in a consistent and 
 *               formatted manner
 * Params: 
 *     question [string] : question text
 *     sql [string] : sql query
 *     cols [array] : column headers in array form
 *     pads [array] : padding size in ints for each column
 */
function displayQuery($question,$sql,$cols,$pads){
    global $mysqli;

    $parts = explode('.',$question);
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$cols);
    $response = runQuery($mysqli,$sql);

    if($response['success']){
        foreach($response['result'] as $id => $row){
            $id++;
            $row['id'] = $id;
            $row['name'] = getPlayer($row['playerid']);
            $row[0] = $row[$cols[0]];
            $row[1] = $row[$cols[1]];
            $row[2] = $row[$cols[2]];
            $row[3] = $row[$cols[3]];

            echo formatRows($row,$pads);
        }
    }
    echo"</pre>";
    f();
}

/**
 * Question 1
 */
$question = "1. Find the player(s) that played for the most teams.";
$pads = [3,12,17,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count FROM `players` group by id,name ORDER BY `count` DESC LIMIT 5";
$response = runQuery($mysqli,$sql);
$cols = ['id','name','count'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 2
 */
$question = "2. Find the player(s) that played for multiple teams in one year.";
$pads = [3,12,15,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count FROM `players` group by id,name,season ORDER BY `count` DESC LIMIT 20";
$response = runQuery($mysqli,$sql);
$cols = ['id','name','count'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 3
 */
$question = "3. Find the player(s) that had the most yards rushed for a loss.";
$pads = [3,12,18,5];
$sql = "SELECT `players_stats`.`playerid`,sum(`players_stats`.`yards`) as negative_yards 
        FROM `players_stats` 
        WHERE `players_stats`.`yards` < 0 and `players_stats`.`statid` = '10' 
        GROUP BY `players_stats`.`playerid` 
        ORDER BY negative_yards ASC
        LIMIT 5";
$cols = ['id','playerid','name','negative_yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 4
 */
$question = "4. Find the player(s) that had the most rushes for a loss.";
$pads = [3,12,18,5];
$sql = "SELECT `players_stats`.`playerid`,COUNT(`players_stats`.`yards`) as negative_carries 
        FROM `players_stats` 
        WHERE `players_stats`.`yards` < 0 and `players_stats`.`statid` = '10' 
        GROUP BY `players_stats`.`playerid`  
        ORDER BY `negative_carries`  DESC
        LIMIT 5";
$cols = ['id','playerid','name','negative_carries'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 5
 */
$question = "5. Find the player(s) with the most number of passes for a loss.";
$pads = [3,12,18,5];
$sql = "SELECT `players_stats`.`playerid`,COUNT(`players_stats`.`yards`) as negative_passes 
        FROM `players_stats` 
        WHERE `players_stats`.`yards` < 0 and `players_stats`.`statid` = '15' 
        GROUP BY `players_stats`.`playerid`  
        ORDER BY `negative_passes`  DESC
        LIMIT 5";
$cols = ['id','playerid','name','negative_passes'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 6
 */
$question = "6. Find the team with the most penalties.";
$pads = [3,5,5];
$sql = "SELECT club,sum(pen) as pen 
        FROM `game_totals` 
        GROUP BY club  
        ORDER BY `pen`  DESC
        LIMIT 5";
$cols = ['id','club','pen'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 7
 */
$question = "7. Find the team with the most yards in penalties.";
$pads = [3,5,5];
$sql = "SELECT club,sum(pyds) as `pyds`
        FROM `game_totals` 
        GROUP BY club  
        ORDER BY `pyds`  DESC
        LIMIT 5";
$cols = ['id','club','pyds'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 8
 */
$question = "8. Find the correlation between most penalized teams and games won / lost.";
$pads = [3,5,5];
echo printHeader($question,$pads);

/**
 * Question 9
 */
$question = "9. Average number of plays in a game.";
$pads = [3,5];
$sql = "SELECT AVG(count) as average_plays
FROM (
    SELECT count(distinct(playid)) as count FROM `players_stats` group by gameid
) as count";
$cols = ['id','average_plays'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 10
 */
$question = "10. Longest field goal.";
$pads = [3,12,15,5,5];
$sql = "SELECT * FROM `players_stats` 
        WHERE statid = '70' 
        ORDER BY `players_stats`.`yards` DESC
        LIMIT 5";
$cols = ['id','playerid','name','club','yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 11
 */
$question = "11. Most field goals.";
$pads = [3,12,15,5];
$sql1 = "SELECT `playerid`,COUNT(`statid`) AS `fieldgoals` 
        FROM `players_stats` 
        WHERE statid = '70' 
        GROUP BY playerid  
        ORDER BY `fieldgoals`  DESC
        LIMIT 5";
$cols = ['id','playerid','name','fieldgoals'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 12
 */
$question = "12. Most missed field goals.";
$pads = [3,12,15,5];
$sql = "SELECT `playerid`,COUNT(`statid`) AS `fieldgoals` 
        FROM `players_stats` 
        WHERE statid = '69' 
        GROUP BY playerid  
        ORDER BY `fieldgoals`  DESC
        LIMIT 5";
$cols = ['id','playerid','name','fieldgoals'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 13
 */
// $question = "13. Most dropped passes.";
// $pads = [3,12,15,5];
// $sql1 = "SELECT gameid,playid FROM `players_stats` WHERE statid LIKE '115'";
// $response1 = runQuery($mysqli,$sql1);

// if($response1['success']){
//     foreach($response1['result'] as $row){
//         $sql2 = "SELECT `gameid`,`description` FROM plays 
//                  WHERE `gameid` LIKE '{$row['gameid']}' 
//                  AND `playid` LIKE '{$row['playid']}'
//                  AND `description` LIKE '%dropped%'";
//         $response2 = runQuery($mysqli,$sql2);
        
//         print_r($response2['result']);
        
//     }
// }
// $cols = ['id','playerid','name','drops'];
// displayQuery($question,$sql,$cols,$pads);


    //SELECT * FROM `plays` where lower(description) like '%pass%' and lower(description) like '%dropped%'
    //SELECT * FROM players_stats WHERE playerid IN (SELECT playerid FROM `players_stats` WHERE statid LIKE '115')


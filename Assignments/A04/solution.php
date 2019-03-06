<?php
//Connect to mysql
require("/Users/griffin/Code/1-Current_Courses/.config.php");


$mysqli = mysqli_connect($host, $user, $password, $database);

if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

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


/**
 * Prints a question plus a border underneath
 * Params:
 *     question [string] : "Who ran the most yards in 2009?"
 *     pads [array] : [3,15,15,5] padding for each data field
 * Returns:
 *     header [string] : Question with border below
 */
function printHeader($question,$pads,$cols){
    if(strpos($question,"\n") > 0){
        $parts = explode("\n",$question);
        $qlen = strlen($parts[0]);
    }else{
        $qlen = strlen($question);
    }
    if($qlen > array_sum($pads)){
        $padding = $qlen ;
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
 *     data [array] : array of data, if null then SQL query must exist
 */
function displayQuery($question,$sql,$cols,$pads,$data=null){
    global $mysqli;

    $parts = explode('.',$question);
   
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$cols);

    if(!$data){
        $response = runQuery($mysqli,$sql);

        if($response['success']){
            $data = $response['result'];
        }
    }
    displayArray($data,$cols,$pads);
    
    echo"</pre>\n\n\n";
    f();
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
function displayArray($data,$cols,$pads){
    
    foreach($data as $id => $row){
        $id++;
        $row['id'] = $id;
        if(in_array('name',$cols)){
            $row['name'] = getPlayer($row['playerid']);
        }
        for($i=0;$i<sizeof($cols);$i++){
            $row[$i] = $row[$cols[$i]];
        }
        // $row[0] = $row[$cols[0]];
        // $row[1] = $row[$cols[1]];
        // $row[2] = $row[$cols[2]];
        // $row[3] = $row[$cols[3]];

        echo formatRows($row,$pads);
    }

}

/**
 * Question 1
 */
$question = "1. Count number of teams an individual player played for.";
$question .= "\nLimit your output to the top 10 players that played for the most teams.";
$pads = [3,18,17,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count 
        FROM `players` group by id,name 
        ORDER BY `count` DESC , substring(name,2) ASC LIMIT 10";
$cols = ['id','name','count'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 2
 */
$question = "2. Find the players with the highest total rushing yards by year, and limit the result to top 5.";
$question .= "\nThis means to sum up all players rushing yards per year, and list the top 5 (most yards) in your output.";
$pads = [3,18,17,7,5];
$sql = "SELECT playerid,season,sum(yards) as rushing 
        FROM `players_stats` WHERE statid like '10' 
        GROUP BY playerid,season 
        ORDER BY rushing DESC LIMIT 5";
$cols = ['id','playerid','name','season','rushing'];
displayQuery($question,$sql,$cols,$pads);


/**
 * Question 3
 */
$question = "3. Find the bottom 5 passing players per year.";
$question .= "\nThis is the similar to previous question, just change top to bottom, and most to least.";
$pads = [3,18,17,7,5];
$sql = "SELECT playerid,season,sum(yards) as passing 
        FROM `players_stats` WHERE statid like '15' 
        GROUP BY playerid,season 
        ORDER BY passing ASC LIMIT 5";
$cols = ['id','playerid','name','season','passing'];
displayQuery($question,$sql,$cols,$pads);


/**
 * Question 4
 */
$question = "4. Find the top 5 players that had the most rushes for a loss.";
$question .= "\nThis is not grouped by year, this is over a players career.";
$pads = [3,18,17,5];
$sql = "SELECT playerid,count(*) as rushes_for_loss 
        FROM `players_stats` 
        WHERE statid like '10' AND yards < 0
        GROUP BY playerid 
        ORDER BY rushes_for_loss DESC LIMIT 5";
$cols = ['id','playerid','name','rushes_for_loss'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 5
 */
$question = "5. Find the top 5 teams with the most penalties.";
$question .= "\nThis is not grouped by year, this is over a teams career.";
$pads = [3,18,15];
$sql = "SELECT `club`,`season`,count(*) as `penalties`
        FROM `players_stats` 
        WHERE `statid` like '93' 
        GROUP BY `club`,`season`
        ORDER BY `penalties` DESC
        LIMIT 5";
$cols = ['id','club','penalties'];
displayQuery($question,$sql,$cols,$pads);


/**
 * Question 6
 */
$question = "6. Find the average number of penalties per year.";
$question .= "\nAverage Penalties = Sum of all penalties per year / Total games played that year";
$pads = [3,7,10,18,15];
$cols = ['id','club','season','total_penalties','avg_penalties'];
$sql = "SELECT `club`,`season`,count(*) as `total_penalties` 
        FROM `players_stats` 
        WHERE `statid` like '93' 
        GROUP BY `club`,`season`
        ORDER BY `total_penalties` DESC";

$response = runQuery($mysqli,$sql);


if(in_array('result',$response)){
    $data = array_slice($response['result'],0,10);
}

for($i=0;$i<sizeof($data);$i++){
    $sql = "SELECT count(*) as games FROM `game_totals` WHERE `season` = '{$data[$i]['season']}' AND `club` = '{$data[$i]['club']}'";
    $response = runQuery($mysqli,$sql);
    if(in_array('result',$response)){
        $data2 = $response['result'];
        $data[$i]['avg_penalties'] = round($data[$i]['total_penalties'] / $data2[0]['games'],2);
    }
}

displayQuery($question,null,$cols,$pads,$data);


/**
 * Question 7
 * 
 * Obviously this should have been 1-2 sql queries only. Processing in php is not the right "tool" for the job.
 */

$question = "7. Find the Team with the least amount of average plays every year.";
$question .= "\nAverage Plays is by game.";
$question .= "\nTotal Plays is per year.";
$question .= "\nOutput: List the top 10 teams by lowest average number of plays.";
$pads = [3,7,10,18,15];
$cols = ['id','team','year','avg'];
$sql = "SELECT `clubid`, substring(`gameid`,1,4) AS `season`,substring(`gameid`,5,2) AS `month`,`gameid`, count(*) AS play_count 
        FROM `plays` 
        GROUP BY `clubid`,`season`,`gameid`  
        ORDER BY `clubid` ASC, `season` ASC , `play_count` DESC";

$response = runQuery($mysqli,$sql);

if(in_array('result',$response)){
    $data =$response['result'];
}

$summary = [];

for($i=0;$i<sizeof($data);$i++){

    if($data[$i]['month'] < 9){
        $data[$i]['season']--;
    }

    // put team into summary array
    if(!array_key_exists($data[$i]['clubid'],$summary)){
        $summary[$data[$i]['clubid']] = [];
    }

    // put season into team array
    if(!array_key_exists($data[$i]['season'],$summary[$data[$i]['clubid']])){
        $summary[$data[$i]['clubid']][$data[$i]['season']] = ['games'=>0,'total_plays'=>0];
    }

    // add counts 
    $summary[$data[$i]['clubid']][$data[$i]['season']]['total_plays'] += $data[$i]['play_count'];
    $summary[$data[$i]['clubid']][$data[$i]['season']]['games'] += 1;

}

$finally = [];

foreach($summary as $team => $seasons){
    foreach($seasons as $year => $totals){
        $avg = round($totals['total_plays'] / $totals['games'],2);
        $finally["{$avg}"] = ['team'=>$team,'year'=>$year];
    }
}

krsort($finally);
$data = [];
$i=0;
foreach($finally as $avg => $vals){
    $data[] = ['team'=>$vals['team'],'year'=>$vals['year'],'avg'=>$avg];
    $i++;
    if($i >= 10){
        break;
    }
}

displayQuery($question,null,$cols,$pads,$data);

/**
 * Question 8
 */
$question = "8. Find the top 5 players that had field goals over 40 yards.";
$pads = [3,18,17,15,12];
$sql = "SELECT `playerid`, count(*) as `attempts` 
        FROM `players_stats` 
        WHERE `statid` = '70' and `yards` > 40
        GROUP BY `playerid` 
        ORDER BY count(*) DESC
        LIMIT 5";
$cols = ['id','playerid','name','attempts'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 9A
 */
$question = "9A. Find the top 5 players with the shortest avg field goal length.";
$pads = [3,18,17,15,12];
$sql = "SELECT `playerid`, count(*) as `attempts` , avg(yards) as `avg_yards`
        FROM `players_stats` 
        WHERE `statid` = '70' 
        GROUP BY `playerid` 
        ORDER BY avg(yards) ASC
        LIMIT 5";
$cols = ['id','playerid','name','attempts','avg_yards'];
displayQuery($question,$sql,$cols,$pads);


/**
 * Question 9B
 */
$question = "9B. Find the top 5 players with the shortest avg field goal length AND more than 19 attempts.";
$pads = [3,18,17,15,12];
$sql = "SELECT * FROM (SELECT `playerid`, count(*) as `attempts` , avg(yards) as `avg_yards`
        FROM `players_stats` 
        WHERE `statid` = '70' 
        GROUP BY `playerid` 
        ORDER BY avg(yards) ASC) AS tmp
        WHERE `attempts` >= 20
        LIMIT 5";
$cols = ['id','playerid','name','attempts','avg_yards'];
displayQuery($question,$sql,$cols,$pads);


/**
 * Question 10
 */
$question = "10. Rank the NFL by win loss percentage (worst first).";
$pads = [3,18,17];
$cols = ['id','club','win_loss_pct'];
$sql = "SELECT distinct(`club`) FROM `game_totals`";
$response = runQuery($mysqli,$sql);

if(in_array('result',$response)){
    $teams = $response['result'];
}

$summary = [];

for($i=0;$i<sizeof($teams);$i++){

    $club = $teams[$i]['club'];

    $sql1 = "SELECT count(*) as `games` FROM `game_totals` WHERE `club` LIKE '{$club}'";
    $response1 = runQuery($mysqli,$sql1);

    if(in_array('result',$response1)){
        $games = $response1['result'][0]['games'];
    }

    $sql2 = "SELECT count(*) as `wins` FROM `game_totals` WHERE `club` LIKE '{$club}' AND `wonloss` LIKE 'won'";
    $response2 = runQuery($mysqli,$sql2);

    if(in_array('result',$response2)){
        $wins = $response2['result'][0]['wins'];
    }

    $summary[] = ['club'=>$club,'win_loss_pct'=>round($wins/$games,2)];
}

function cmp($a, $b)
{
    if ($a == $b) {
        return 0;
    }
    return ($a['win_loss_pct'] < $b['win_loss_pct']) ? -1 : 1;
}

usort($summary,'cmp');

displayQuery($question,null,$cols,$pads,$summary);

/**
 * Question 11
 */
$question = "11. Find the top 5 most common last names in the NFL.";
$pads = [3,18,17,15,12];
$sql = "SELECT * FROM (SELECT SUBSTRING_INDEX(name,'.',-1) as `last_name` ,count(SUBSTRING_INDEX(name,'.',-1)) as `name_count` 
        FROM `players` 
        GROUP BY SUBSTRING_INDEX(name,'.',-1)) as tmp 
        ORDER BY `name_count` DESC
        LIMIT 5";
$cols = ['id','last_name','name_count'];
displayQuery($question,$sql,$cols,$pads);



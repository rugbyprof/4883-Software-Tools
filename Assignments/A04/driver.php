<?php
//Connect to mysql
require(".config.php");


$mysqli = mysqli_connect($host, $user, $password, $database);

if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

// Helper function to run sql
require "query_function.php";

// Include my example functions
// "include" isn't as strong as "require" it won't error if file is missing
include "get_players1.php";
include "get_players2.php";
include "load_stat_codes.php";

// Which example you wanna run?
$choices = [
    'loadStats',
    'example1',
    'example2',
    'example3',
    'example4',
];

// choose 1-4
switch ($choices[2]) {
    case 'loadStats':
        // This won't run when running with 'software_tools' user. It doesn't have permissions
        // to insert data.
        $path = 'stat_codes.json';
        load_stat_codes($mysqli, $path);
        break;
    case 'example1':
        // Run getPlayers1
        getPlayers1();
        break;
    case 'example2':
        // Get data from getPlayers2
        $data = getPlayers2();
        // Dump array to stdout
        print_r($data);
        break;
    case 'example3':
        // Write a query
        $sql = "SELECT playerid,season,SUM(YARDS) as total_yards
                FROM `players_stats`
                WHERE `statid` = '10'
                GROUP BY playerid,season";
        // Send it to our runQuery function with our mysqli resource variable
        $response = runQuery($mysqli, $sql);

        // handle the response
        if ($response['success']) {
            // pull the data out of the result array
            $data = $response['result'];

            // print out the size
            echo sizeof($data) . "\n";

            // loop through our result array
            for ($i = 0; $i < sizeof($data); $i++) {
                echo "\t{$data[$i]['playerid']} \t{$data[$i]['total_yards']}\n";
            }
        }
	break;
    case 'example4':
        // This query finds all the player stats with the word "goal" in the stat name
        // and only returns the first 1000 results (so my console doesn't print over a million rows)
        // If you combine limit with an order by statement, you could return the top N results or 
        // bottom N results (like top 5 rushers for example)
        $sql = "SELECT `players_stats`.`playerid`,`players_stats`.`season`,`players_stats`.`club`,`players_stats`.`statid`,`stat_codes`.`name`,`players_stats`.`yards`
                FROM `players_stats`,`stat_codes`
                WHERE `players_stats`.`statid` = `stat_codes`.`id` AND `stat_codes`.`name` LIKE '%goal%'
                LIMIT 0,1000";

        // Send it to our runQuery function with our mysqli resource variable
        $response = runQuery($mysqli, $sql);


	print_r($response);
        // handle the response
        if ($response['success']) {
            // pull the data out of the result array
            $data = $response['result'];

            echo "playerid\tseason\tclub\tyards\t\tstatid\tname\n";
            foreach ($data as $row) {
                echo "{$row['playerid']}\t{$row['season']}\t{$row['club']}\t\t{$row['yards']}\t\t\t{$row['statid']}\t\t{$row['name']}\n";
            }
        }
}

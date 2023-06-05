<?php
$config = [
    'servername' => "localhost",
    'username' => "nfl_data",
    'password' => "***********",
    'dbname' => "nfl_data"
];

// pass in the number of seconds elapsed to get hours:minutes:seconds returned
function secondsToTime($s)
{
    $h = floor($s / 3600);
    $s -= $h * 3600;
    $m = floor($s / 60);
    $s -= $m * 60;
    return $h.':'.sprintf('%02d', $m).':'.sprintf('%02d', $s);
}


class NflTeamCode{
    function __construct(){
        $this->team_codes = json_decode(file_get_contents("./json_data/team_codes.json"),true);
    }

    function correctTeamCode($code){
        if(array_key_exists($code,$this->team_codes)){
            return $this->team_codes[$code];
        }
        return false;
    }
}

class NflDbHelper{
    function __construct(){
        global $config;
        // Create connection
        $this->conn = new mysqli($config['servername'], $config['username'], $config['password'], $config['dbname']);
        // Check connection
        if ($this->conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $this->codeFix = new NflTeamCode();
        $this->savePath = "./json_data/stat_data/";
        $this->currentGameId = "";
        $this->filePointer = fopen("/tmp/temp","w");
    }

    function createTables(){
        $queries = [
            [
            'sql' => "TRUNCATE `games`",
            'comment' => "TRUNCATING `games` table"
            ],
            [
            'sql' => "TRUNCATE `game_totals`",
            'comment' => "TRUNCATING `game_totals` table"
            ],
            [
            'sql' => "TRUNCATE `players`",
            'comment' => "TRUNCATING `players` table"
            ],
            [
            'sql' => "TRUNCATE `plays`",
            'comment' => "TRUNCATING `plays` table"
            ],
            [
            'sql' => "TRUNCATE `players_stats`",
            'comment' => "TRUNCATING `players_stats` table"
            ],
            [
                'sql' => "TRUNCATE `stat_codes`",
                'comment' => "TRUNCATING `players_stats` table"
            ],
            [
                'sql' => "CREATE TABLE IF NOT EXISTS `games` (
                        `gameid` varchar(32) NOT NULL,
                        `home_club` varchar(3) NOT NULL,
                        `away_club` varchar(3) NOT NULL,
                        `season` int(5) NOT NULL,
                        `home_score` int(3) NOT NULL,
                        `away_score` int(3) NOT NULL,
                        PRIMARY KEY (`gameid`,`home_club`,`away_club`));",
                'comment' => "Creating `games` table"
            ],
            [
            'sql' => "CREATE TABLE IF NOT EXISTS `game_totals` (
                `gameid` varchar(32) NOT NULL,
                `season` int(5) NOT NULL,
                `club` varchar(3) NOT NULL,
                `totfd` int(4) NOT NULL,
                `totyds` int(4) NOT NULL,
                `pyds` int(4) NOT NULL,
                `ryds` int(4) NOT NULL,
                `pen` int(4) NOT NULL,
                `penyds` int(4) NOT NULL,
                `trnovr` int(4) NOT NULL,
                `pt` int(4) NOT NULL,
                `ptyds` int(4) NOT NULL,
                `ptavg` int(4) NOT NULL,
                `top` varchar(6) NOT NULL,
                PRIMARY KEY (`gameid`,`club`))",
            'comment' => "Creating `game_totals` table"
            ],
            [
                'sql' => "CREATE TABLE IF NOT EXISTS `players` (
                    `id` varchar(32) NOT NULL,
                    `name` varchar(32) NOT NULL,
                    `season` int(4) NOT NULL,
                    `club` varchar(4) NOT NULL,
                    PRIMARY KEY (`id`,`name`,`season`,`club`))",
                'comment' => "Creating `players` table"
                ],
            [
                'sql' => "CREATE TABLE IF NOT EXISTS `plays` (
                    `gameid` varchar(32) NOT NULL,
                    `clubid` varchar(3) NOT NULL,
                    `playid` int(5) NOT NULL,
                    `sp` int(4) NOT NULL,
                    `qtr` int(4) NOT NULL,
                    `down` int(4) NOT NULL,
                    `time` varchar(6) NOT NULL,
                    `yrdln` varchar(12) NOT NULL,
                    `ydstogo` int(4) NOT NULL,
                    `ydsnet` int(4) NOT NULL,
                    `description` text NOT NULL,
                    `note` varchar(32) NOT NULL,
                    PRIMARY KEY (`gameid`,`clubid`,`playid`));",
                'comment' => "Creating `plays` table"
                ],
                [
                    'sql' => "CREATE TABLE IF NOT EXISTS `players_stats` (
                        `gameid` varchar(32) NOT NULL,
                        `playerid` varchar(32) NOT NULL,
                        `playid` int(4) NOT NULL,
                        `sequence` int(4) NOT NULL,
                        `season` int(4) NOT NULL,
                        `club` varchar(3) NOT NULL,
                        `statid` int(4) NOT NULL,
                        `yards` int(4) NOT NULL,
                        PRIMARY KEY (`gameid`,`playerid`,`playid`,`sequence`))",
                    'comment' => "Creating `player_stats` table"
                    ],
                [
                    'sql' => "CREATE TABLE `stat_codes` (
                        `id` int(4) NOT NULL,
                        `name` varchar(128) NOT NULL,
                        `comment` text NOT NULL,
                        PRIMARY KEY (`id`))",
                    'comment'=>"Creating `stat_codes` table"
                ]
        ];

        foreach($queries as $query){
            $sql = $query['sql'];
            $comment = $query['comment'];
            echo"{$comment} ";
            $result = $this->conn->query($sql);
        
            if ($result) {
                // output data of each row
                echo ".... success \n";
            } else {
                echo "..... ooops. Failed\n"; 
                printf("Errormessage: %s\n", $this->conn->error);
            }
        }
    }

    function addGame($gid,$h,$a,$s,$hs,$as){
        $sql = "INSERT INTO `games` VALUES('{$gid}','{$h}','{$a}','{$s}','{$hs}','{$as}')";
        $result = $this->conn->query($sql);
        
        if (!$result) {
            printf("Errormessage: %s\n", $this->conn->error);
        }
    }

    function addGameTotals($gameid,$season,$totals_data){
        $sql = "INSERT INTO `game_totals` VALUES ('{$gameid}','{$season}',";
        foreach($totals_data as $key => $value){
            $sql .= "'{$value}'";
            if($key != 'top'){
                $sql .= ',';
            }
        }
        $sql .= ")\n";
        //print($sql);
        $result = $this->conn->query($sql);
        


        if (!$result) {
            printf("Errormessage: %s\n", $this->conn->error);
        }
    }

    function addPlayerStat($gameid,$playerid,$playid,$season,$stat){
        $seq = $stat['sequence'];
        $club = $this->codeFix->correctTeamCode($stat['clubcode']);
        if(!$club){
            return;
        }
        $id = $stat['statId'];
        $yards = $stat['yards'];
        $name = $stat['playerName'];
        $sql = "INSERT INTO `players_stats` VALUES ('{$gameid}','{$playerid}','{$playid}','{$seq}','{$season}','{$club}','{$id}','{$yards}');";

        // if($gameid != $this->currentGameId){
        //     if (get_resource_type($this->filePointer ) == 'handle') { 
        //         fclose($this->filePointer);
        //     } 

        //     $this->currentGameId = $gameid;
            
        //     $this->filePointer = fopen($this->savePath.$this->currentGameId.".sql","w");
            
        // }
        
        // fwrite($this->filePointer,$sql."\n");

        $result = $this->conn->query($sql);
        $this->addPlayer($playerid,$name,$season,$club);
    }

    function addPlay($gameid,$playid,$play,$season){
        $team = $this->codeFix->correctTeamCode($play['posteam']);
        if(!$team){
            return;
        }
        $sp = $play['sp'];
        $qtr = $play['qtr'];
        $down = $play['down'];
        $time = $play['time'];
        $yrdln = $play['yrdln'];
        $ydstogo = $play['ydstogo'];
        $ydsnet = $play['ydsnet'];
        $desc = $play['desc'];
        $note = $play['note'];
        $sql = "INSERT INTO `plays` VALUES ('{$gameid}','{$team}','{$playid}','{$sp}','{$qtr}','{$down}','{$time}','{$yrdln}','{$ydstogo}','{$ydsnet}','{$desc}','{$note}')";
        $result = $this->conn->query($sql);

        foreach($play['players'] as $playerid => $stats){
            if(strpos($playerid,'-') > 0){
                foreach($stats as $stat){
                    $this->addPlayerStat($gameid,$playerid,$playid,$season,$stat);
                }
            }
        }
    }

    function addPlayer($id,$name,$season,$club){
        $sql = "INSERT INTO `players` VALUES ('{$id}','{$name}','{$season}','{$club}')";
        $result = $this->conn->query($sql);
    }

    function truncateTable($table){
        $sql = "TRUNCATE `{$table}`";
        $result = $this->conn->query($sql); 
    }

    function loadStatCodes(){

        $stats = json_decode(file_get_contents("./json_data/stat_codes.json"),true);
        foreach($stats as $id => $code){
            $n = addslashes ($code['Name']);
            $c = addslashes ($code['Comment']);
            $sql = "INSERT INTO `stat_codes` VALUES ('$id','{$n}','{$c}')";
            $result = $conn->query($sql);
            echo"$sql\n";
        }
    }

}

class processNflLiveData{
    function __construct($path){
        $this->path = $path;
        $this->files = [];     // json live update files array
        $this->home = [];
        $this->away = [];
        $this->codeFix = new NflTeamCode();
        $this->db = new NflDbHelper();
        $this->db->createTables();
        $this->readFileDirectory();
        $this->processJson();
        $this->db->loadStatCodes();
    }

    function loadStatCodes(){
        


    }

    function getSeason($gameid){
        $year = substr($gameid,0,4);
        $month = substr($gameid,4,2);
        if($month < 3){
            $year -= 1;
        }
        return $year;
    }


    // Load json filenames into array
    function readFileDirectory(){
        $this->files = scandir($this->path);
        array_shift($this->files);
        array_shift($this->files);
    }

    function addGames($gameid,$season,$data){
        $home = $data[$gameid]['home']['abbr'];
        $away = $data[$gameid]['away']['abbr'];
        $new_home = $this->codeFix->correctTeamCode($home);
        $new_away = $this->codeFix->correctTeamCode($away);
        if($new_home){
            $home = $new_home;
        }else{
            return;
        }
        if($new_away){
            $away = $new_away;
        }else{
            return;
        }

        $home_score = $data[$gameid]['home']['score']['T'];
        $away_score = $data[$gameid]['away']['score']['T'];
        
        $this->db->addGame($gameid,$home,$away,$season,$home_score,$away_score);
    }

    function addGameTotals($gameid,$season,$data){
        $code = $this->codeFix->correctTeamCode($data['abbr']);
        if(!$code){
            return;
        }
        $qData = [
            'club' => $code,
            'totfd' => $data['stats']['team']['totfd'],
            'totyds' => $data['stats']['team']['totyds'],
            'pyds' => $data['stats']['team']['pyds'],
            'ryds' => $data['stats']['team']['ryds'],
            'pen' => $data['stats']['team']['pen'],
            'penyds' => $data['stats']['team']['penyds'],
            'trnovr' => $data['stats']['team']['trnovr'],
            'pt' => $data['stats']['team']['pt'],
            'ptyds' => $data['stats']['team']['ptyds'],
            'ptavg' => $data['stats']['team']['ptavg'],
            'top' => $data['stats']['team']['top']
        ];
        
        $this->db->addGameTotals($gameid,$season,$qData);
    }

    function addPlays($gameid,$season,$drives){
        foreach($drives as $did => $drive){
            if($did != 'crntdrv'){
                foreach($drive["plays"] as $playid => $play){
                    $this->db->addPlay($gameid,$playid,$play,$season);
                }
            }
        }
    }

    // 
    function processJson(){
        // $this->db->truncateTable('games');
        // $this->db->truncateTable('game_totals');
        // $this->db->truncateTable('players');
        // $this->db->truncateTable('player_stats');
        // $this->db->truncateTable('plays');

        $starttime = microtime(true);
        foreach($this->files as $file){
            $filetime = microtime(true);
            $contents = file_get_contents($this->path."/".$file);
            $data = json_decode($contents,true);
            if(is_array($data)){
                list($gameid,$null) = array_keys($data);

                echo"$gameid\n";

                $season = $this->getSeason($gameid);

                $this->addGames($gameid,$season,$data);

                $gameTotalsStartTime = microtime(true);
                $this->addGameTotals($gameid,$season,$data[$gameid]['home']);
                $this->addGameTotals($gameid,$season,$data[$gameid]['away']);
                $gameTotalsStopTime = microtime(true);
                echo "Game Add Time: ".secondsToTime(microtime(true) - $filetime)."\n";

                $playsStartTime = microtime(true);
                if(is_array($data[$gameid]['drives'])){
                    $this->addPlays($gameid,$season,$data[$gameid]['drives']);
                }
                $playsEndTime = microtime(true);
                echo "Plays Add Time: ".secondsToTime(microtime(true) - $filetime)."\n";

            }
            
            echo "File  Process Time: ".secondsToTime(microtime(true) - $filetime)."\n";
            echo "Total Process Time: ".secondsToTime(microtime(true) - $starttime)."\n";
        }
    }
}

function getStatDefs(){

    $sql = "SELECT * FROM stat_codes";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            print_r($row);
        }
    } else {
        echo "0 results"; 
    }
}



$p = new processNflLiveData("./json_data/live_update_data");


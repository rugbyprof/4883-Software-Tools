<?php

function load_stat_codes($mysqli,$filename){

    // read contents of stats into file
    $data = file_get_contents($filename);

    // loads json and decodes it (true => associative array)
    $stat_codes = json_decode($data,true);

    foreach($stat_codes as $id => $code){
        $n = addslashes ($code['Name']);
        $c = addslashes ($code['Comment']);
        $sql = "INSERT INTO `stat_codes` VALUES ('$id','{$n}','{$c}')";
        $result = $mysqli->query($sql);
        if($result){
            echo"$sql\n";
        }else{
            echo $mysqli->error."\n";
        }
    }
}

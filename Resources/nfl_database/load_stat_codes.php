<?php
$config = [
    'servername' => "cs2.mwsu.edu",
    'username' => "software_tools",
    'password' => "horseblanketdonkey",
    'dbname' => "nfl_data"
];

// Create connection
$conn = new mysqli($config['servername'], $config['username'], $config['password'], $config['dbname']);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 



$stat_codes = json_decode(file_get_contents("stat_codes.json"),true);

foreach($stat_codes as $id => $code){
    $n = addslashes ($code['Name']);
    $c = addslashes ($code['Comment']);
    $sql = "INSERT INTO `stat_codes` VALUES ('$id','{$n}','{$c}')";
    $result = $conn->query($sql);
    echo"$sql\n";
}

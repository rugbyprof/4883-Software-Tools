## VSCode and SFTP - Connecting to remote server

## Overview

This will explain how to use VSCode to run code on a remote server. 

#### Explanation 

The reason we are putting our code on a remote server is because of the schools firewall not allowing `Mysql` (aka `MariadB`) to accept incoming connections.  When you connect to a database that is on the same machine as your code, you are connecting via `localhost` and your query does not need to be sent across a network. When you connect to a database that is NOT `localhost` you are sending your request to some other machine accepting requests. This is what we are doing when we connect via the wireless network on campus, and it is allowed becuase there is no `firewall` involved. A `firewall` is a part of the network that accepts or rejects network traffic based on a set of rules. One simple way to reject traffic is by port number. `Mysql` uses (default) port 3306. MSU's firewall tells packets headed for port 3306 to go screw themselves. So, you can't connect to `cs2.mwsu.edu:3306` because of the firewall (which actually is a good thing).

If we place our code on a server "inside" the firewall (aka cs2), we can run php code that connects to `localhost` and eliminate the firewall issues. So, how do we do that?

#### Getting Started 

- Install VSCode: https://code.visualstudio.com/
- Install SFTP

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/install_sftp.png" width="300">

- Create an `sftp` config file:
- From the Command Palette 
    - Windows: (Ctrl+Shift+P)
    - Mac (Cmd+Shift+P)

When you type "SFTP" into the command palette, you get filtered choices. Choose `SFTP:Config`.

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_config.png" width="250">


A file will appear that looks like:

```json
{
    "name": "My Server",
    "host": "localhost",
    "protocol": "sftp",
    "port": 22,
    "username": "username",
    "remotePath": "/",
    "uploadOnSave": true
}
```

Change it to look like the following, but replace:

- "username": "`yourusername`",
- "password":"`yourpassword`",
- "remotePath": "/home/`yourusername`/public_html/software_tools"

```json
{
    "name": "cs2 SoftwareTools",
    "host": "cs2.mwsu.edu",
    "protocol": "sftp",
    "port": 22,
    "username": "yourusername",
    "password":"yourpassword",
    "remotePath": "/home/yourusername/public_html/software_tools",
    "uploadOnSave": true,
    "ignore":[
        ".vscode",
        ".git",
        ".DS_Store"
    ]
}
```

>NOTE: This assumes you have a folder called `public_html` in your home folder. If you don't, you need to create one. If that is the case (probably because you already had a cs2 account and I didn't make a folder for you) log in to cs2 and make one. If you need help with that, slack me.

Once you have added the `SFTP` config file, try to add a file to cs2. Create a file called `index.html` and add the following to it:

```html
<h1>IT WORKED!</h1>
```

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_create_index.png" width="300">

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_upload_file.png" width="300">

If you then go to your own url, you should see: 

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_itworks.png" width="300">

What is your URL?? 

```
http://cs2.mwsu.edu/~yourusername/software_tools/
```

The `public_html` is assume by the server and doesn't need to be in the path.

You are now ready to add php code!

#### Adding Php

Create a php file in your new sftp connected folder. Call it `team_games.php`. Inside your new file, put the following code:

```php
<?php
//Connect to mysql
$host = "localhost";             // because we are ON the server
$user = "software_tools";        // user name

// Get username and password from slack
// The DB username and pass not the ones
// I sent you to log into the server.
$password = "************";         // password 
$database = "nfl_data"              // database 
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
        FROM `games` 
        WHERE (`home_club` = 'DAL' or `away_club` = 'DAL') 
        AND season = '2018'";

$response = runQuery($mysqli, $sql);

echo "<pre>";   // so whitespace matters

if($response['success']){
    foreach($response['result'] as $row){
        echo "{$row['away_club']} {$row['season']} {$row['home_score']} {$row['away_score']} {$row['winner']} {$row['win_type']} \n";
    }
}
```

Then goto `http://cs2.mwsu.edu/~yourusername/software_tools/team_games.php` and you should see:

```
DAL 2018 16 8 CAR home 
NYG 2018 20 13 DAL home 
DAL 2018 24 13 SEA home 
DET 2018 26 24 DAL home 
DAL 2018 19 16 HOU home 
JAX 2018 40 7 DAL home 
DAL 2018 20 17 WAS home 
TEN 2018 14 28 TEN away 
DAL 2018 20 27 DAL away 
DAL 2018 19 22 DAL away 
WAS 2018 31 23 DAL home 
NO 2018 13 10 DAL home 
PHI 2018 29 23 DAL home 
DAL 2018 23 0 IND home 
TB 2018 27 20 DAL home 
DAL 2018 35 36 DAL away 
SEA 2018 24 22 DAL home 
DAL 2018 30 22 LA home 
```
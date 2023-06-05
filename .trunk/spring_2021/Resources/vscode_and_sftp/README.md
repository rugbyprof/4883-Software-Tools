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



| Editing the file `index.html`   |
|:----:|
|<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_create_index.png" width="300"> |



| Upload it by right clicking on the file, and choose upload:   |
|:----:|
| <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_upload_file.png" width="300"> |
|   |

 


| If you then go to your own url, you should see:   |
|:----:|
| <img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/sftp_itworks.png" width="500"> |
|<sub>NOTE: This path is a little different because I created a user called `software_tools` and put my code directly into `public_html`.</sub>| 



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
        FROM `games` 
        WHERE (`home_club` = 'DAL' or `away_club` = 'DAL') 
        AND season = '2018'";

$response = runQuery($mysqli, $sql);

echo "<pre>";   // so whitespace matters

if($response['success']){
    foreach($response['result'] as $row){
        echo "{$row['season']} {$row['home_club']}:{$row['home_score']}  {$row['away_club']}:{$row['away_score']} {$row['winner']} {$row['win_type']} \n";
    }
}
```

Then goto `http://cs2.mwsu.edu/~yourusername/software_tools/team_games.php` and you should see:

```
2018 CAR:16  DAL:8 CAR home 
2018 DAL:20  NYG:13 DAL home 
2018 SEA:24  DAL:13 SEA home 
2018 DAL:26  DET:24 DAL home 
2018 HOU:19  DAL:16 HOU home 
2018 DAL:40  JAX:7 DAL home 
2018 WAS:20  DAL:17 WAS home 
2018 DAL:14  TEN:28 TEN away 
2018 PHI:20  DAL:27 DAL away 
2018 ATL:19  DAL:22 DAL away 
2018 DAL:31  WAS:23 DAL home 
2018 DAL:13  NO:10 DAL home 
2018 DAL:29  PHI:23 DAL home 
2018 IND:23  DAL:0 IND home 
2018 DAL:27  TB:20 DAL home 
2018 NYG:35  DAL:36 DAL away 
2018 DAL:24  SEA:22 DAL home 
2018 LA:30  DAL:22 LA home
```

## VSCode and SFTP - Connecting to remote server

## Overview

This will explain how to use VSCode to run code on a remote server. 

#### Explanation 

The reason we are putting our code on a remote server is because of the schools firewall not allowing `Mysql` (aka `MariadB`) to accept incoming connections.  When you connect to a database that is on the same machine as your code, you are connecting via `localhost` and your query does not need to be sent across a network. When you connect to a database that is NOT `localhost` you are sending your request to some other machine accepting requests. This is what we are doing when we connect via the wireless network on campus, and it is allowed becuase there is no `firewall` involved. A `firewall` is a part of the network that accepts or rejects network traffic based on a set of rules. One simple way to reject traffic is by port number. `Mysql` uses (default) port 3306. MSU's firewall tells packets headed for port 3306 to go screw themselves. So, you can't connect to `cs2.mwsu.edu:3306` because of the firewall (which actuall is a good thing).

If we place our code on a server "inside" the firewall (aka cs2), we can run php code that connects to `localhost` and eliminate the firewall issues. So, how do we do that?

#### Pre-Requisites 

- Install VSCode: https://code.visualstudio.com/
- Install SFTP

<img src="http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/install_sftp.png" width="300">


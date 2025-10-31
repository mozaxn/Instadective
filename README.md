# Instadective

Instadective is a simple command-line tool uses Instagram's API (using `instagrapi`) to gain various insights about your Instagram account along with changes to followers and following over time.

## Features

- Detects users you follow that don't follow you back on Instagram.
- Detects change in follower/following between two scans.
- Scans your account to store your followers and following locally which can be used later.
- Uses your Instagram `sessionid` to do so.
- Uses Instagram's official API via `instagrapi`.

## Installation

You can directly install `instadective` using `pip`:

```bash
pip install instadective
```

Also, you can clone the Github repo:

```bash
git clone https://github.com/mozaxn/Instadective.git
cd Instadective
pip install -r requirements.txt
```

## Usage

To display help, run:
```bash
instadective -h
```

This will show something similar to:
```bash
                             _________ _        _______ _________ _______                               
                             \__   __/( (    /|(  ____ \\__   __/(  ___  )                              
                                ) (   |  \  ( || (    \/   ) (   | (   ) |                              
                                | |   |   \ | || (_____    | |   | (___) |                              
                                | |   | (\ \) |(_____  )   | |   |  ___  |                              
                                | |   | | \   |      ) |   | |   | (   ) |                              
                             ___) (___| )  \  |/\____) |   | |   | )   ( |                              
                             \_______/|/    )_)\_______)   )_(   |/     \|                              
                                                                                                        
                     ______   _______  _______ __________________          _______                      
                    (  __  \ (  ____ \(  ____ \\__   __/\__   __/|\     /|(  ____ \                     
                    | (  \  )| (    \/| (    \/   ) (      ) (   | )   ( || (    \/                     
                    | |   ) || (__    | |         | |      | |   | |   | || (__                         
                    | |   | ||  __)   | |         | |      | |   ( (   ) )|  __)                        
                    | |   ) || (      | |         | |      | |    \ \_/ / | (                           
                    | (__/  )| (____/\| (____/\   | |   ___) (___  \   /  | (____/\                     
                    (______/ (_______/(_______/   )_(   \_______/   \_/   (_______/                     
                                                                                                        
                                             VERSION 1.0.0                                              
                                           DEVELOPED BY ZAXN                                            
                                         mozaxn@protonmail.com                                          



usage: instadective [-h] [-s SESSIONID] [--scan] [-o OUT] [-n] [-c SCAN1 SCAN2]

options:
  -h, --help            show this help message and exit
  -s, --sessionid SESSIONID
                        Your Instagram SESSION_ID
  --scan                Perform core scan. This displays your followers and following. Use with flag
                        -o to save the results to a file.
  -o, --out OUT         Save the output of a scan to a directory. Mention the directory without the
                        '/' at the end.
  -n, --non-follow      Identify accounts you follow but don't follow you back.
  -c, --compare SCAN1 SCAN2
                        Compare two core scans to identify changes in followers & following.

```

### Non-follower Scan

To perform the non-follower scan, run it directly from your terminal:

```bash
instadective -s SESSION_ID -n
```
or,
```bash
instadective --sessionid SESSION_ID --non-follow
```

### Core Scan

To perform core scan, run:

```bash
instadective -s SESSION_ID --scan
```

To output the scan to a JSON file:

```bash
instadective -s SESSION_ID --scan -o DEST_DIRECTORY
```

### Compare Scans

To compare two scans:

```bash
instadective -c SCAN_1 SCAN_2
```
or,
```bash
instadective --compare SCAN_1 SCAN_2
```

## License

Licensed under the **GPL-3.0 License** — see the [LICENSE](https://github.com/mozaxn/Instadective/blob/main/LICENSE) file for details.
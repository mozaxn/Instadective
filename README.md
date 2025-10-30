# Instadective

Instadective is a simple command-line tool uses Instagram's API (using `instagrapi`) to detect users you follow who **don't follow you back**.

## Features

- Detects users you follow that don't follow you back on Instagram.
- Uses your Instagram `sessionid` to do so.
- Uses Instagram's official API via `instagrapi`.

## Installation

You can clone the Github repo:

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
                                                                                                        
                                             VERSION 0.1.0                                              
                                           DEVELOPED BY ZAXN                                            
                                         mozaxn@protonmail.com                                          



usage: instadective [-h] -s SESSIONID

options:
  -h, --help            show this help message and exit
  -s, --sessionid SESSIONID
                        Instagram Session ID
```

To perform the non-follower scan, run it directly from your terminal:

```bash
instadective -s SESSION_ID
```
or,
```bash
instadective --sessionid SESSION_ID
```

## License

Licensed under the **GPL-3.0 License** — see the [LICENSE](https://github.com/mozaxn/Instadective/blob/main/LICENSE) file for details.
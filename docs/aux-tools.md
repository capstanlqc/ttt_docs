---
tags:
  - Audience꞉User
---

# Auxiliary tools

## AutoHotKey

AutoHotKey can be used to create global autotext macros. In particular, if you need to insert non-breaking spaces or other special characters, you might find this AutoHotKey script helpful.

1. Download and install [AutoHotKey](https://www.autohotkey.com/download/).

2. Press ++win+r++ on your keyboard and type `shell:startup` to open the Startup folder. Copy the path to that folder (e.g. `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `USER` would be your Windows user name).

3. Right click on [this link](files/ahk/insert_unicode_char.ahk), choose “Save link as” and paste the path to the Startup folder before the file name, to download the script file in that folder.

4. Right click the script file (`insert_unicode_char.ahk`) in the Startup folder and choose **Run script**.

This script will be run automatically the next time your machine starts.

# TMX Editor

## For Windows:

you will need 
- a Github account, log in to it in the default browser
- admin rights in your machine

install dependencies

- Insta JDK 17 from Temurin... add to PATH
- Run PowerShell as administrator
- Install Chocolatey, restart PS
- choco install git -y
- choco install gh -y
- choco install ant -y
- choco install nodejs-lts -y
- restart PS
- npm install typescript (or choco install typescript)
- optional: update npm
- check all versions: node -v, npm -v, ant -version, java -version
- restart PS as admin

- mkdir C:\Users\USER\Apps
- cd C:\Users\USER\Apps
- gh repo clone rmraya/TMXEditor
- cd TMXEditor
- ant
- npm install
- npm start


cultural shift -- in PM attitude 
judgement calls -- 

KS articles --- 

Tanya -- filter outlook


## For Linux and Mac

Just follow the documentation.
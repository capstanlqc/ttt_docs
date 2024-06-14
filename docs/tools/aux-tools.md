---
tags:
  - Audience꞉User
---

# Auxiliary tools (installation)

This page lists instructions about installing some tools that don't have a straight-foward installation process.

## AutoHotKey

AutoHotKey can be used to create global autotext macros. In particular, if you need to insert non-breaking spaces or other special characters, you might find this AutoHotKey script helpful.

1. Download and install [AutoHotKey](https://www.autohotkey.com/download/).

2. Press ++win+r++ on your keyboard and type `shell:startup` to open the Startup folder. Copy the path to that folder (e.g. `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `USER` would be your Windows user name).

3. Right click on [this link](files/ahk/insert_unicode_char.ahk), choose “Save link as” and paste the path to the Startup folder before the file name, to download the script file in that folder.

4. Right click the script file (`insert_unicode_char.ahk`) in the Startup folder and choose **Run script**.

This script will be run automatically the next time your machine starts.

## TMX Editor

### Unix-like systems (Linux or Mac)

Just RTD.

### Windows

You will need:

- a Github account (tip: log in to it in the default browser)
- admin rights in your machine

Install dependencies:

- Install JDK 21 from [Temurin](https://adoptium.net/temurin/releases/) (and add it to PATH).
- Run PowerShell as administrator.
- [Install Chocolatey](https://chocolatey.org/install).
- Restart PowerShell as admin and run:
    ```
    choco install git -y 
    choco install gh -y
    choco install ant -y
    choco install nodejs-lts -y
    ``` 
- Restart PowerShell as admin, and run `npm install typescript` (or `choco install typescript`).
- Optional: update npm
- Check all versions: `node -v`, `npm -v`, `ant -version`, `java -version`
- Restart PowerShell as admin, finally:
    ```
    mkdir C:\Users\USER\Apps
    cd C:\Users\USER\Apps
    gh repo clone rmraya/TMXEditor
    cd TMXEditor
    ant
    npm install
    ``` 

To run TMX Editor:

- `npm start`
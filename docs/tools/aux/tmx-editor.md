---
tags:
  - Audience꞉Tech
---

<!-- ## TMX Editor -->

## Unix-like systems (Linux or Mac)

Just RTD.

## Windows

You will need:

- a Github account (tip: log in to it in the default browser)
- admin rights in your machine

### Installing dependencies

Before installing TMX Editor you must:

- Install JDK 21 from [Temurin](https://adoptium.net/temurin/releases/) (and add it to PATH).
- Run PowerShell as administrator.
- [Install Chocolatey for Individual Use](https://chocolatey.org/install).
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

### Installing TMX Editor

- Restart PowerShell as admin, finally:
    ```
    mkdir C:\Users\USER\Apps
    cd C:\Users\USER\Apps
    gh repo clone rmraya/TMXEditor
    cd TMXEditor
    ant
    npm install
    ``` 

### Running TMX Editor

To run TMX Editor:

- `npm start`

### Desktop launcher

blabla <- Vale
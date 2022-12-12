# Auxiliary tools

## AutoHotKey

AutoHotKey can be used to create global autotext macros. In particular, if you need to insert non-breaking spaces or other special characters, you might find this AutoHotKey script helpful.

1. Download and install [AutoHotKey](https://www.autohotkey.com/download/).

2. Press `Win+R` on your keyboard and type `shell:startup` to open the Startup folder. Copy the path to that folder (e.g. `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `USER` is your Windows user name).

3. Right click on [this link](files/insert_unicode_char.ahk), choose “Save link as” and paste the path to the Startup folder, to download the script file in that folder.

4. Right click the script file (`insert_unicode_char.ahk`) in the Startup folder and choose **Run script**.

This script will be run automatically the next time your machine starts.

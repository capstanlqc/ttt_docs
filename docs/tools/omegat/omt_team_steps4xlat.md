# Working with OmegaT team projects

This document is addressed to linguists (translators, revisers, etc.).

Upper-cased names are used as placeholders in this document.

## File organization

File organization on your end is very important for the successful execution of your work. Here come some recommendations for a tidy organization.

1. Designate a working folder for the project in your machine, and use that same location for all related tasks. We would suggest a location at a very high level in the folder structure in your machine, e.g. one of the following

   - `C:\Work\CLIENT\PROJECT` or `C:\Users\USER\Work\CLIENT\PROJECT` (for Windows)
   -  `/Users/USER/Work/CLIENT/PROJECT` (for macOS)

2. Inside the `PROJECT`'s working folder above, create the following folder structure (or something similar that fits your purposes):

   ``` 
   ├── 00_Admin
   ├── 01_Instructions
   ├── 02_Tasks
   └── 03_Whatever
   ```

When you download a team project (see below), if the path to your local OmegaT project folder that OmegaT proposes is not suitable, you might want to replace it with the path to your `02_Tasks` folder (or a subfolder deeper inside), e.g. `C:\Users\Manolo\Work\cApStAn\Delta\02_Tasks`. 

The final path should look like `C:\Users\USER\Work\CLIENT\PROJECT\02_Tasks\OMT-PROJ-DIR` (where `OMT-PROJ-DIR` is (the name of) your local OmegaT project folder and everything else to the left of it is the path leading to your `02_Tasks` folder).

   > If you have already downloaded a team project to your designated location inside your `02_Tasks` folder, then the proposed path to the local project folder should be already fine.

## OmegaT 5.7.1

If you haven't done so, please follow our [installation and customization guide](https://slides.com/capstan/omegat5-installation-and-customization-guide) to get up and running with OmegaT 5.7.1.

If you were using OmegaT 4.2.0 until now to work in OmegaT for other projects, you are advised to uninstall that version first. If you would like to keep both versions, let us know and we can advise about the best way to do that.

## Downloading team projects

To start working on your project, proceed as follows.

1. If you don't have one, please [create a Github account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account). As credentials to work in OmegaT, you will need your Github username and a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token) (as password). 

	> For management purposes, it's better if your username identifies you clearly (e.g. for Manuel Souto Pico, something like `msoutopico` or `manuelsouto` or `msouto` etc. would be fine -- but something like `mnlstpc` would be a bit cryptic).

```
► @TODO: explain here how the token must be created... repo etc.
```

2. Send your username to your PM at cApStAn so that they can give you access to your project.

3. You will receive a URL to your OmegaT project repository. Copy it to your clipboard (e.g. select it and press `Ctrl+C`).

4. In OmegaT, go to **Project > Download team project**.

5. Click inside the **Repository URL** field and press `Ctrl+V` to paste the URL you have copied.

6. Click inside the **New Local Project Folder** field. 

7. If it's the first time you download this project, you may be asked for authentication. Please enter your Github user name in the **User** field and your personal access token in the **Password** field, then press **OK**.

8. Then, a path to your local OmegaT project folder will be proposed automatically in the **New Local Project Folder** field, which you can edit if not suitable (see our file organization tips above). 

9. Press **OK** . Your project will download and open in OmegaT.

## Stopping and resuming work

When you want to stop working on your project, go to **Project > Close** in OmegaT to close the project. 

> Please close the project if you're going to be away from your computer for some time. No need to close OmegaT, that's up to you.

When you want to resume working on that project, go to **Project > Open Recent Project** and select the project you want to open (probably the one at the top of the list).

> There's no need to download the project again if you have already done so once.

## Delivery

You can monitor your progress by looking at the status bar in the bottom right of the OmegaT main window. It will tell you the percentage of translated segments and the number of remaining (untranslated) segments, both in the current file iand in the whole OmegaT project.

When the status bar shows `100% (0 left)` and there are no more segments you must edit, then you can deliver. 

To deliver, go to **Project** > **Commit Target Files**.

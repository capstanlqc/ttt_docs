# Instructions for PISA 25 translators (testing in `fr`)

> NOTE for testing: During testing, please put yourself in the skin of a (clumsy) user (e.g. a translator, an NPM, a verifier, etc.) who knows nothing other than what is described in this guide. The purpose of testing is to find problems in the documentation as well as in the documented process, so please flag any issues you see in both.

## File organization

In this cycle of PISA we'll be using a new approach to handle translation projects, which will be more efficient but also potentially more challenging in some regards. File organization on your end is very important for the successful execution of this task. We strongly advise you that you follow these instructions to the letter.

1. Designate a working folder for PISA in your machine, and use that same location for all PISA-related tasks. We would suggest a location at a very high level in the folder structure in your machine, e.g. one of the following

   - `C:\Work\PISA2025` or `C:\Users\USER\Work\PISA2025` (for Windows)
   -  `/Users/USER/Work/PISA2025` (for macOS)

2. Create the following folder structure in the working folder above:

   ``` 
   ├── 00_Admin (tentative)
   ├── 01_Instructions (tentative)
   ├── 02_Projects
   └── 03_Whatever (tentative)

> NOTE for testing: Please ignore all folders above except `02_Projects`.

## OmegaT 5.7.1

If you haven't done so, please follow our [installation and customization guide](https://slides.com/capstan/omegat5-installation-and-customization-guide) to install and customize OmegaT 5.7.1.

> NOTE for testing: Make a copy of your user configuration folder: 1. press `Win+R` and run `%appdata%` (or go to **Options > User Configuration Folder** in OmegaT); 2. in the folder that will open, make a copy of the `omegat` folder (e.g. as `omegat_YYYYMMHH`).

> NOTE for testing: Install OmegaT 5.7.1 in `C:\Apps\OmegaT_5.7.1` so that it doesn't overwrite, or conflict with, your current installation of version 4.2.0. You can do this for any OmegaT versions you want to install in parallel.

## Downloading team projects

To start working on your project, proceed as follows.

1. If you don't have one, please [create a free Github account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account). As credentials to work in OmegaT, you will need your Github username and a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token). 

  Also, make sure your username follows the following patterns (where `{lang}` stands for your language code, e.g. `fra-BEL` for French (Belgium), etc.):

     - `TRA-{lang}-your-name` if you are a translator
     - `REC-{lang}-your-name` if you are a reconciler
     - `NPM-{lang}your-name` if you are an NPM (or an NPM and a reconciler or an NPM and a translator)
     - `VER-{lang}-your-name` if you are a verifier

   > NOTE for testing: You can disregard the pattern above, whatever user name you nave is fine.

  When you create your token, pay attention to the following points:

    - Make sure you select "repo" (and all its children) as scope
    - You're advised to select "no expiry date" (so that you don't need to do this again)
    - Please copy your token and keep it safe (but where you can find it whenever you need it)

2. Send your username to the [cApStAn PM](mailto:manuel.souto@capstan.be) to be added to the PISA team and have access to your project. You will receive an invitation to collaborate on the Github repository, which you need to accept (either by email or on your Github profile).

  > NOTE for testing: We might do this differently, e.g. create all usernames in a centralized way and then provide them to users rather than the other way round, but for testing, let's stick to this way. 

  > NOTE for testing: If you are `@vn342`or `@amathot`, you can disregard this step.

3. You will receive a URL to your OmegaT project. Select it and copy it (e.g. with `Ctrl+C`).

  > NOTE for testing: Use `https://github.com/capstanlqc/pisa25_trans_fr_omt.git` for testing the translation task and `https://github.com/capstanlqc/pisa25_verif_fr_omt.git`for testing the verification task. No testing for the reconciliation task is needed for the time being, as it is just a variation of the translation task.

4. In OmegaT, go to **Project > Download team project**.

5. Click inside the **Repository URL** field  and press `Ctrl+V` to paste the URL you have copied.

6. Click inside the **New Local Project Folder** field. 

7. If it's the first time you download this project, you will be asked for authentication. Please enter your Github user name in the **User** field and your personal access token in the **Password** field, then press **OK**.

8. Then, a local path will be proposed automatically in the **New Local Project Folder** field, where the last folder is the name of the project that will be created in your machine. You might need to replace the part of the path up to the last slash with the path to your `02_Projects` folder, e.g. `C:\Users\USER\Work\PISA2025\02_Projects`. The final path should look like `C:\Users\USER\Work\PISA2025\02_Projects\<PROJECT>` (where ` <PROJECT>` is the name of the project and everything else to the left of it is the path to your `02_Projects` folder).

   > If you have already downloaded a team project to your `02_Projects` folder for PISA 2025, then the proposed path to the local project folder might be already correct.

   > NOTE for testing: This step is potentially challenging, suggestions welcome as to how to make the instruction clearer.

9. Press **OK** . Your project will download and open in OmegaT.

   

## Stopping and resuming work

When you want to stop working on your project, go to **Project > Close** in OmegaT to close the project. 

>  NOTE: Please do not leave your project open for prolonged periods of absence from your computer.

When you want to resume working on that project, go to **Project > Open Recent Project** and select the project you want to open.

> NOTE: There's no need to download the project again if you have already done so once.

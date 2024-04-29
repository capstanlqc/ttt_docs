# ☆ OmegaT customization roadmap

*Estimated Reading Time: 15 min*

| Person           | Date         | Update     |
|:-----------------|:-------------|:-----------|
| Manuel           | 2019-08-19   | Creation   |

This document aims to give an overview about the evolution and the current situation of the OmegaT installation and customization process for all kinds of users in PISA and PIAAC. In general you can live without knowing all this, but perhaps this information can be useful to answer some questions you might have sometimes. I try to be brief and not too technical. 

I say ‘evolution’ because the approach has changed since the beginning of these respective cycles, even thought that evolution has not affected all users equally. 

Why is the customization needed? There are two main reasons: First and most important, the customization is necessary to be able to work with non-standard XLIFF files produced by ETS (or potentially, by other partners). Secondly, it is convenient to select automatically (i.e. without the user having to think or spend time or have the chance to overlook anything) a number of parameters in the OmegaT interface that will make the work of users easier and safer, and also because having homogeneous settings across different users makes it much easier for us (tech team) to train users and provide support to them. 

That second reason hasn’t changed since the initial approach and is unlikely to change, which means that some means to customize will always be *desirable* even if ETS or any other partner produce valid XLIFF files. At the moment, given the non-valid XLIFF files, customization is not only desirable but also *necessary*. 

Pros of each step below refer to the customization process only and are in relation to the previous approach. Cons refer to future improvements. You might want to think of those "pros" and "cons" as "improvements" and "remaining challenges".

## 1. Initial approach: OmegaT for PISA and OmegaTcp

We have abandoned the initial approach we had a few years ago where we provided the user with a complete bundle including the OmegaT standard installation files and specific configuration for one specific project or others (i.e. either PISA or other projects that were not PISA, through two kinds of installers: “OmegaT for PISA” and “OmegaTcp”, where “cp” means “cApStAn projects”, which means that we prepare files ourselves, properly). That specific configuration was indispensable to work with non-standard XLIFF files produced by ETS, but can be incompatible with other projects where we do have standards files. The main disadvantage of this approach was that updates were slow, as the 200~300 MB bundle took some time to download, and erased any user settings. Besides, the customization was Windows-specific (which means we were forcing Linux and Mac users to use Windows). 

In a nutshell:

  * One Windows-specific installer for PISA
  * OmegaTcp: Another Windows-specific installer for cApStAn projects

Pros:

  1. The custom installer for PISA allowed us to handle XLIFF files prepared by ETS

Cons:

  1. The user needed to download the full installer every time there was an update
  1. The custom files are saved in the default location in the installation folder and need writing permissions to run the customization utility
  1. A separate installation of OmegaT was needed to handle other projects

## 2. New approach: separate customization

We have now (2018-2019) moved towards an approach where, instead of providing a bundle that contains all needed files for the installation, we provide the original link to the OmegaT standard installer, and we provide the customization (to have that specific configuration) separately. 

### 2.1. OmegaT for participants: customization utility

For PISA and PIAAC participants, apart from the link to download OmegaT, we have thus provided a separate utility that would try to guess the default installation folders and user configuration folders and put custom files there as appropriate. This approach proved challenging, mostly because OmegaT’s default installation folders are often not writeable without the appropriate permissions, and because it wasn’t possible for the customization utility to guess where those folders were when the user had to use non-default folders, for whatever reason. We had expected a limitation due to lack of permissions, rightly noted by some PMs, but the process brought about too many unexpected situations and a lot of support requests from users. Another disadvantage of this approach is that every new update erases user settings, such as recent projects, which can be a problem for some users. 

In a nutshell:

  * Default OmegaT installer and one Windows-specific customization utility for PISA
  * OmegaTcp: (The installation for cApStAn projects hasn’t changed)

Pros:

  1. The user doesn’t need to download the full installer and re-install the whole of OmegaT whenever there’s an update in the custom files
  1. The user downloads the original OmegaT installer directly from the OmegaT website, minimizing any malware infection that could have happened during our manipulation and bundling

Cons:

  1. Some custom files are saved in the installation folder and the user doesn’t always have writing permissions to do the customization in that folder
  1. The customization utility erases user settings
  1. A separate installation of OmegaT is needed to handle other projects
  1. The customization is Windows-dependent 

We had a couple of fallback plans for when the default approach proved too challenging or for other operating systems other than Windows, and we kept looking for a better approach, which we found. However, since PISA/PIAAC participants (and their IT teams) had already been trained this way and made an effort to accommodate this customization process, we have kept this approach for PISA/PIAAC participants (translators, reconcilers, etc.) in general, and for most of them it is expected to be valid. For those who have issues, we had fallback plans before and we have a new approach now, which is:

### 2.2. OmegaT for verifiers and all users going forward: customization script

The new and current (2019.08.21) approach is very similar, but instead of downloading and running a separate executable utility outside OmegaT, the user should run a script from inside OmegaT. Another difference is that, to overcome potential limitations in permissions, we don’t use the default location for scripts and plugins any more (inside the installation folder), but we have moved scripts and plugins to the user configuration folder, which should always be writable for the user and therefore no rights issues are expected. The advantages of this are (i) that the script doesn’t have to guess the location of those folders, because OmegaT already knows and the script uses that knowledge; and (ii) that we can safely assume that the user has enough permissions to run the script; (iii) also, this approach does not erase user settings, such as shortcuts to recent projects. 

In a nutshell:

  * Default OmegaT installer and one platform-independent customization script for PISA/PIAAC
  * OmegaTcp: (The installation for cApStAn projects hasn’t changed)

Pros:

  1. Platform independent, i.e. the user can use the operating system of their preference
  1. Doesn’t erase user settings
  1. No separate program needs to be run, everything happens inside OmegaT 

Cons:

  1. A separate installation of OmegaT is needed to handle other projects

An effort was made to come up with this new approach and have it ready before the PISA/PIAAC verification seminar, and therefore it was the approach verifiers used to customize their installation. It should also be the default approach for any users going forward, except PISA/PIAAC participants that had no problems with the previous approach.

The platform-independent aspect of this approach is non-negligible. Users have the freedom to use the operating system of their choice, which means that we are not imposing a particular operating system (Windows). Some users might not be used to Windows or might struggle to install and use it. From the point of view of the user experience in OmegaT, it is certainly preferable to stay in an environment where the user is comfortable rather than having to use another machine or trying to install a virtual machine. From the support perspective, it also makes sense, too, since less issues are expected. 

## 3. Expected future developments

So far we are using this approach for PISA/PIAAC, but the idea is to use different customization bundles for different projects. That should allow the user to choose the right configuration depending on the project or task in which they have to work, either choosing among several configurations or customizing OmegaT ex-novo every time they have to work in a new project that requires a new configuration. At least two configurations are needed: one for ETS files (PISA/PIAAC), another for other projects (where XLIFF files are valid according to the XLIFF specification), and the differences between the two are very few, but important. The PM would have to ask the user to customize OmegaT (or choose the right configuration) according to the project or task they will be involved with. 

In a nutshell:

  * Default OmegaT installer and platform-independent customization scripts 
    * for PISA/PIAAC
    * for other projects (one for all, or one per project… as requested by PM)

Pros:

  1. Only one installation of OmegaT for all projects, less confusion when handling updates
  1. It is possible to customize OmegaT before the user is invited to upgrade to a new version (if any) – as not all custom files might be compatible with newer versions.

Cons:

  1. The user has to run a project-specific customization script before starting/resuming work on that project. If a user handles two or more projects simultaneously, customization should happen every time they are about to switch to a new project.

Suggestions are welcome. 

## Mini FAQ / discussion forum

If you have any question, please add it below.

- **Question**: It may happen that the same linguist works in two projects with different OmegaT configurations. Does this create a problem?
    + Answer: No problem, but the user needs to switch between two OmegaT settings. As explained above, at the moment we have PISA/PIAAC-customized OmegaT for PISA/PIAAC and OmegaTcp for other projects (cp = cApStAn Projects) – this is done through different desktop shorcut icons. Going forward, we might drop OmegaTcp and use different customizations for different projects (at least one for PISA/PIAAC and one for other projects) in the standard installation of OmegaT – this might be done by running the customizer with a specific URL (one URL specific for each project) or by using a launcher where the user chooses the appropriate profile (TBD).

- **Question**: If the user has originally installed the customizer using the separate customizer.exe file, can they just simply do it using the new method (i.e. within OmegaT) from here on? From above my understanding is that they do the same thing, but the new method helps circumvent some issues caused by user rights or deviating installation paths, is that correct?

    + Answer: Each user should follow the installation and customization guide that we have written for their *profile*. There are two profiles: (1) countries/participants (including NPM, translators and reconcilers) and (2) verifiers, and there are two customization modes and therefore two customization guides. At this stage, we are not unifying the two customization approaches in only one, therefore countries/participants are expected to follow the guide that has been written for them. For this cycle of PISA/PIAAC we don't want to re-train countries/participants to use another approach. Exceptionally we might use the customization script as yet another fallback plan for countries/participants who have issues with their default approach, but this is a decision that the tech team should take when providing support. Also, we keep track of what settings each user has and we need to refer to that information when providing support. In a nutshell, a PM should always ask the user (regardless of their profile) to refer to their installation and customization guide. 

- **Question**: Can we use the current PISA/PIAAC version for projects where target files are something other than .xlf, like Word or Excel files? I don't remember working on xliffs in any other project than PIAAC (and PISA), in other projects where we have used OmegaT it has been Word or Excel files. 

    + Answer: Yes, you can use the PISA/PIAAC-customized OmegaT for any other projects as long as the *source* files don't include XLIFF files.

### OmegaT tips and tricks newsletter

Subscribe to the [OmegaT Tips and Tricks newsletter](https://cat.capstan.be/) to receive updates and useful tips.


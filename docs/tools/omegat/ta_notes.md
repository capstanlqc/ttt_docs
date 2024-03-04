# T&A notes in OmegaT [Comments pane]

This document lists the steps you must take to create and use T&A notes directly in OmegaT.

## Installation

This functionality is enabled by a new plugin that is not included yet in our customized setup. Please proceed as follows:

1. Click [this link](https://github.com/t-cordonnier/TMX-Content-Provider/releases/download/prod-1.1/TmxCommentsProvider.jar) to download the plugin file, namely file `TmxCommentsProvider.jar`.
2. Go to **Options** > **Access Configuration Folder** in OmegaT to open your config folder, then open the `plugins` folder.
3. Move the plugin file to the `plugins` folder.
4. Restart OmegaT if it was running.

## Creating T&A notes

Steps for the PM:

1. Open the OmegaT project for which you want to create T&A notes
2. Make sure there are no translations in the project, all segments should be untranslated. 
3. For every segment you want to create a T&A note, enter the notes as the translation of the segment.
4. When you're done with all segments, press Ctrl+D to export the master TMs of the project (of the three that get created, you'll need the one with the `-omegat.tmx` suffix). 
5. Rename the master TM as you like (say: `PROJECT-omegat.tmx` -> `ta_note.tmx`).
6. Go to **Project** > **Access Project Contents** to open the project folder.
7. Create a new folder called `notes`.
8. Move the `ta_notes.tmx` filed to the `notes` folder of the project (or ask TT to add it to the project for all versions)

> If the project contains translations, you may remove them with script **Flush Working TM**. If any translations are coming from the `/tm/auto` or `/tm/enforce` folders, delete those folders or the TMX files inside them.

## Using the T&A notes

Steps for the user: 

1. Before translating or revising/verifying each segment, read the T&A note in the Comments pane. 

## Video demo

<iframe title="vimeo-player" src="https://player.vimeo.com/video/805050363?h=f102da30d1" width="745" height="420" frameborder="0"    allowfullscreen></iframe>

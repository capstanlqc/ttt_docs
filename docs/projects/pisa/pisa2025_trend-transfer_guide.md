# PISA 2025 -- trend translation transfer

Summarised steps: 

- Traverse the project with `Ctrl+U`
- Retrieve the trend translation from the trend TMs and populate every segment with it

## Cases

Possible cases: 

1. pre-translated segment
2. untranslated segment but a fuzzy match
3. untranslated segment and no fuzzy match

Relative actions for each case: 

| Case             | Action                   					|
|------------------|-----------------------------------------------|
| Exact match      | Nothing to do, the segment is pre-translated |
| Fuzzy match      | Insert and update if needed 					|
| No fuzzy match   | Concordance search, possibly insert fragments |

#### 1. Pre-translated segment with fuzzy match

When that's the case, the pre-translated segment will have a pink shade, and there's nothing to do at this stage. While moving through the project with `Ctrl+U` these pre-translated will be skipped. 

#### 2. Untranslated segment with fuzzy match(es)

In some cases, the segment will not be pre-translated but there will be one or more valid fuzzy match (with a high score (or high enough) so that it is displayed in the Matches pane. This is the easy case, unfortunately not that frequent. 

In those cases, press `Ctrl+I` to insert the match. 

Not likely, but it could happen that several matches (or parts of matches) need to be combined to translate a segment. If you need to insert different matches or different part of several matches, press `Ctrl+#` to select the match (where `#` is the match number) or double click the match before pressing `Ctrl+I`. If you want to insert part of a match only, select the fragment in the match with your mouse before pressing `Ctrl+I`.

> demo needed?

##### 2.1. Special cases

###### a) Exact match with only a difference in case

Steps: 

- Press `Ctrl+i` to insert the match
- Press `Ctrl+A` to select the whole target text
- Press `Shift+F3` to cycle through case options

#### 3. Untranslated segment with no useful fuzzy matches

In some cases, the Matches pane will not have any valid fuzzy match. In that case, after inspecting the matches pane and confirming that there's nothing there that you can use, you must search for the source text in the TMs to find the translation. 

To do that:

- Select the source text that you want to search in the TMs.

	> To select the source text in the segment without using your keyboard, press `F2` and then hold the `Shift` and press the upwards and leftwards arrows.

- Press `Ctrl+F` to launch the text search window. The previously selected source text will be filled in automatically. Press the **Search** button to get results. 

  > Make sure you've marked the right options: TMs, translated, source text, etc.

- Copy the target text or the relevant part in the search results and paste it as the translation of the relevant segment(s).

## Tips and tricks 

Let's see different strategies to deal with each case a bit more in detail.

### Split matches

It may be the case that a fuzzy match or a TM search result contains the translations for several segments, in which case you need to split the match in several parts. In other words, you will find the translation of the segment you’re looking for as part of a longer text chunk. 

That's typically the case when a TM contains the translation of a paragraph -- the translation found in the TM will have to be split among all the segments belonging to that paragraph.

> Tip: If you find the translation of a whole paragraph containing several segments, you might be handy to copy the translation of the whole paragraph from the search results once, and then use copy-paste to distribute the fragments in the segment they belong.

For example: 

  ![](https://capps.capstan.be/doc/images/trend-transfer-2-split-match-in-3-parts.gif)

Or here's a demo where every step is spelled out:


<iframe title="vimeo-player" src="https://player.vimeo.com/video/866401571?h=2e169af9ab" width="640" height="360" frameborder="0"    allowfullscreen></iframe>



### TM searches

If you cannot find a concordance, try searching for a smaller part or removing certain elements that might be preventing the match. For example:

![](https://capps.capstan.be/doc/images/trend-transfer-2-fine-tuning-searches.gif)

### Markup

Tags must be inserted as normal. The recommended approach to insert paired tags around formatted words or expressions is to use the auto-completer: 

1. Select the word or expression that must be formatted
2. Press `Ctrl+Space` to cycle through the auto-completer until you see the tags section
3. Press `Enter` to insert the tag pair. 

![](https://capps.capstan.be/doc/images/trend-transfer-apply-markup.gif)

Of course, `Ctrl+T` can also be used to insert individual tags.


<iframe title="vimeo-player" src="https://player.vimeo.com/video/866384726?h=3ba910e71f" width="640" height="360" frameborder="0"    allowfullscreen></iframe>

#### Legacy tags

There are two versions of each TM: one original version and one where markup has been removed. 

Legacy markup must be removed anyway (and replaced with new tags) and also lower the matching score, so it's better to insert the match or copy the translation without legacy tags. 

However, the original TMs including legacy markup are kept because legacy tags could be useful to give you an idea of what part of the text was formatted in the trend version.

#### Removing legacy tags 

If you happen to insert a match that contains legacy HTML tags (e.g. `<b>`) and you find it cumbersome or unreliable to remove them manually (e.g. because there are many of them), you can run script **6 - Strip HTML tags** (`Ctrl+Shift+6`).

![](https://capps.capstan.be/doc/images/trend-transfer-translate-strip-html-tags.gif)

### Replacements

If you find yourself making some edits repeatedly, it might be possible to batch process all instances at the end in one go.  

For example, if you're inserting a superscript 2 (i.e. ²) for every instance of square meters units, you could just leave "m2" and then search all instances "m2" and replace with "m²" in one go as a post-processing step when all segments are translated.

### Case

If you need to change the case of a translation (e.g. it is expected to be in Title Case but the match available comes in UPPER CASE), you can do with shortcut `Shift+F3`. Follow these steps: 

1. Insert the match or paste the translation
2. Select the part you want to change the case of
3. Press `Shift+F3` to cycle through case options.

You can choose upper case, lower case, all capitals or title case. 

### Glossary

To optimise the translation of certain segments where you need to assemble several fragments, you may find useful to add some fragments to the glossary if they are always the same. 

This is typically the case of the prompt "Refer to X on the right", where X is new every time but the rest is repeated for every unit. 

Demo:

<iframe title="vimeo-player" src="https://player.vimeo.com/video/866391559?h=cd8f40206d" width="640" height="360" frameborder="0"    allowfullscreen></iframe>

## References
- [cApStAn's OmegaT guides](https://capstanlqc.github.io/omegat-guides/)

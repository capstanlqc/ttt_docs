---
share: true
---

# Recency-based auto-population

### Title 

Recency-based auto-population, or matches from /tm/update folder overwrite if more recent.

### Summary

For each segment, OmegaT will find the most recent exact match in`/tm/update`, and it will compare its timestamp with the timestamp of the existing translation in the current segment and keep the translation that has the most recent timestamp: 

- If the match in `/tm/update` is more recent, then the current translation in the project will be ovewritten with it. 
- If the the current transaltion is more recent than the match in `/tm/update`, then nothing changes.

!!! info
    A translation's *timestamp* in this ticket referes to the `changedate` property if it exits, otherwise the `creationdate` property. If the entry has none of those two properties, then that translation will be considered as older than any other that does have a timestamp. 

In other words, `tm/update` provides a behaviour between `tm/auto` and `tm/enforce`: while the former never overwrittes an existing translation and the second always overwrites, an exact match from `tm/update` would overwrite if it is more recent than the existing translation.

If the segment is untranslated, then an exact match from `/tm/update` simply auto-populates the segment (just like in the other two auto-population cases).

Just as is the case with matches from `/tm/auto`, matches coming from `/tm/update` should be editable.

!!! warning
    From the above it can be inferred that the behaviour of matches from `/tm/update` and matches from `/tm/auto` are alike in most cases but not always. In particular, if there's an alternative translation in the project and an alternative translation in `/tm/auto`, the latter overwrites the former by default -- however the behaviour of a match from `/tm/update` should be different in this case: the newer alternative translation in the project should be prevail over the older alternative in `/tm/update`.

### Metadata properties

When OmegaT finds a (more recent) translation in a TMX file under /tm/update and uses that as the translation of a segment, it also adds an origin property `<prop type="x-auto">update</prop>` (or `<prop type="x-update">update</prop>`, whatever is appropriate) as a child node of the entry’s `<tu>` node.

A background color can be then assigned to translations with that property.

Also, if a match from `/tm/update` is selected and use, not only the translation is registered in the working TM, but also the metadata properties (`changeid` and `changedate`). 

For example, assuming this is the current translation in the working TM (`omegat/project_save.tmx`):

```xml
<tu>
  <tuv lang="en">
	<seg>foo</seg>
  </tuv>
  <tuv lang="es-ES" 
    changeid="souto" changedate="20201111T000000Z" 
    creationid="souto" creationdate="20201111T000000Z">
	<seg>bar</seg>
  </tuv>
</tu>
```

If a TMX file is added to `/tm/update` containing the following entry:

``` xml
<tu>
  <tuv lang="en">
	<seg>foo</seg>
  </tuv>
  <tuv lang="es-ES" 
    changeid="fulano" changedate="20232323T123456Z"
    creationid="fulano" creationdate="20232323T123456Z">
	<seg>QUX</seg>
  </tuv>
</tu>
```

Then the current translation changes to (see selected row) the following in the working TM:

``` xml hl_lines="7"
<tu>
  <prop type="x-auto">update</prop>
  <tuv lang="en">
	<seg>foo</seg>
  </tuv>
  <tuv lang="es-ES" 
    changeid="fulano" changedate="20232323T123456Z" 
    creationid="souto" creationdate="20201111T000000Z">
	<seg>QUX</seg>
  </tuv>
</tu>
```

### Interaction with match sorting criteria

This feature adds the notion of "recency" to the match sorting criteria (summarized [here](https://capstanlqc.github.io/ttt_docs/tools/omegat/match-sorting-specs/)). At this point those criteria are: similarity score, auto-population precedence, context binding, position of the file in the list of files and position of the match in the file.

Let's consider how recency interacts with each: 

#### Similarity score

Recency will only be considered for exact matches (100% score).

#### Auto-population precedence

OmegaT needs to decide when a match from `/tm/update` must be selected and used over a match from `/tm/auto` and `/tm/enforce` and when not. 

When comparing two default translations (with no context binding properties) or two alternative translations (that that have the same context binding properties), in other words, when context binding do not discriminate between the two:

- If the same identical match is found in both `/tm/update` and `/tm/enforce`, the latter prevails regardless of timestamps, and the translation will be locked as expected.
- If the same identical match is found in both `/tm/update` and `/tm/auto`, simply the most recent one prevails.

In cases when one match has context binding and the other doesnt:

- An alternative translation from `tm/update` will prevail over a default match from `tm/enforce` or `tm/auto`, regardless of timestamps.
- An alternative translation from `tm/enforce` or `tm/auto` will prevail over a default match from `tm/update`, regardless of timestamps.

See the next subsection for more details.

#### Context binding

Context binding will always have more weight than recency, i.e. an alternative translation should always prevail over a default translation, regardless of timestamps

Recency can determine selection when comparing two translations with context binding or two translations without context binding, i.e. a newer alternative translation will prevail over an older alternative translation, and a newer default translation will prevail over an older default translation.

In other words:

- new translation with context > old translation without context
- old translation with context > new translation without context
- new translation with context > old translation with context

The following examples show how context biding always wins (timestamps can be ignored if one translation is alternative and the other one is default) and how the most recent translation wins when context binding (or lack of it) is equal in both translations being compared:

- **A.** alternative in project > default in `/tm/update` (timestamps are ignored)
- **B.** default in project < alternative in `/tm/update` (timestamps are ignored)
- **C.** alternative in project < alternative in `/tm/update` (the most recent wins)
- **D.** default in project < default in `/tm/update` (the most recent wins)

!!! note
    The `>` symbol above means that the one to the left has more weight and "wins", and vice versa for `<`.

The table below shows all the possible combinations:

|#| Project | /tm/update  | Results 	| Reason | 
|-|:-------:|:-----------:|:-----------:|:--------------------------------------------------|
|1| def-old | **def-new** | UPDATE  	| the match is newer  |
|2| def-old | **alt-new** | UPDATE  	| the match is newer and is context-bound |
|3| alt-old | def-new     |         	| the translation is context-bound, even if it's older |
|4| alt-old | **alt-new** | UPDATE  	| the match is newer |
|5| def-new | def-old 	  |   		    | the match is not newer |
|6| def-new | **alt-old** | UPDATE  	| the match is context-bound, even if it's older |
|7| alt-new | def-old     |         	| the translation is context-bound and newer | 
|8| alt-new | alt-old     |   		    | the translation is context-bound and newer |

!!! note
    An option in the user preferences / project settings could be used to toggle the preference given to context binding over recency, e.g. `<content_binding_beats_recency>false</content_binding_beats_recency>` (true by default).

#### Position of the file in the list of files

A more recent match from `tm/update` will always prevail over other older matches that are ranked higher according to the file sorting logic (descending alphabetical order).

#### Position of the match in the file

A more recent match from `tm/update` will always prevail over other older matches that are ranked higher according to their position inside the TMX file (closer to the top).

### Match sorting 

To keep things simpler, recency will be used only to select and use a match from `/tm/update`, not to re-arrange match sorting in the **Matches** pane according to recency together with the other match sorting criteria.  

This goes against the current logic of match sorting and selection (see below), but the feature is really about which translation is used and not so much about in which position it appears in the set of matches.

!!! info
    Match sorting and selection: there are certain [criteria to rank/sort matches](https://rentry.org/omegat-match-ranking-specs) (and display them in the **Matches** pane), and the one that is selected to auto-populate the segment, if possible, is simply the one at the top. 

### Proof of concept

This [script](https://github.com/capstanlqc/omegat-scripts/blob/master/project_changed/set_latest_translations.groovy) provides the intended behaviour (looking for more recent translations in `tm/auto`) and has been tested in production for several months. 

That script does have, however, some issues that should be addressed in the built-in feature (e.g. using `ImportFomAutoTMX`, which keeps matches' `changeid` and `changedate`, etc.):

- the pre-populated translation carried over from `tm/auto` will get the current user's info (changeid and changedate) rather than keep the info it originally has in the TM
- it only handles default translations (alternative translations from `tm/auto` will always be used regardless of timestamp)
- the conflict resolution dialog might pop if the active segment has a transation that is older than a match coming from the TM


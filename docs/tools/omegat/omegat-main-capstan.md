---
tags:
  - Audience꞉Tech
---

# OmegaT main-capstan

We maintain our own fork of OmegaT, where we merge features/enhancements and bug fixes developed by Briac Pilpré and Thomas Cordonnier. 

We used version 5.7.2 in PISA 2025 FT and other projects, while we worked on patches to be included in 5.7.3 (to be released for PISA 2025 MS).

## Summary of what was done:

In our clone:
```
cd capstanlqc/omegat
git checkout releases/5.7.2-capstan
```

Created the new `main-capstan` branch based on the branch we used to create the 5.7.2 build:
```
git checkout releases/5.7.2-capstan -b main-capstan
```
Added Thomas' clone as remote (it needs to be done locally in any new clone of capstanlqc/omegat):
```
git remote add thomas https://github.com/t-cordonnier/omegat.git
```

Got all Thomas' current branches (it needs to be done to fetch updates in Thomas' code):
```
git fetch thomas
```

## To merge a feature branch

Check out the branch where to start merging feature branches:
```
git checkout main-capstan
```

To add feature branch, do `git pull thomas BRANCH`. For example, to add the functuality commit target files on close, it was done:

```
git pull thomas compile-on-close
```

Then, committed changes:
```
git push origin main-capstan
```

## Tags

We tagged the commit we used to create the 5.7.2 build:
```
git tag -a v5.7.2-capstan a978d82 -m "Version based on 5.7.1..." 
git push origin v5.7.2-capstan
```

The same thing will be done with next build, which will tagged as `v5.7.3-capstan`, and so on.

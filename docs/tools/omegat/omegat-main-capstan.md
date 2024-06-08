---
tags:
  - Audience꞉Tech
---

# OmegaT main-capstan

We maintain our own fork of OmegaT, where we merge features/enhancements and bug fixes developed by Thomas Cordonnier. 

We used version 5.7.2 in PISA 2025 FT, while we worked on patches to be included in 5.7.3.

## Summary of what was done:

In our clone:
```
cd capstanlqc/omegat
git checkout releases/5.7.2-capstan
```

Created the new main branch based on the branch we used to create the 5.7.2 build:
```
git checkout releases/5.7.2-capstan -b main-capstan
```

Added Thomas' clone as remote:
```
git remote add thomas https://github.com/t-cordonnier/omegat.git
```

Got all Thomas' current branches:
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

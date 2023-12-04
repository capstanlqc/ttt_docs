# Team projects

## Restoring translations

Have a look at the log to identify which commit deleted translations:

```git
git log --stat
```

Then, copy the commit hash of the previous commit, e.g. `03d9f5e`, and do:

```git
git checkout 03d9f5e
cp omegat/project_save.tmx ../03d9f5e.tmx
git checkout main
mkdir tm/auto/restored
mv ../03d9f5e.tmx tm/auto/restored 
git pull && git add . && git commit -m "Restored translations" && git push
```


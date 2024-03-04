---
tags:
  - Audience꞉ Tech
---

## Unable to read project file! Ref origin/HASH cannot be resolved

The user gets this error when opening the team project:

> Unable to read project file!
> org.eclipse.jgit.api.errors.RefNotFoundException: Ref origin/{hash} cannot be resolved

![](../_assets/img/455978.png)

Likely cause: The user has downloaded the team project in a sync'ed folder (under OneDrive, Dropbox, etc.).

## Unable to download team project! 

The user gets this error when downloading the team project:

> Unable to download team project!
> java.util.concurrent.ExecutionException: org.eclipse.jgit.api.errors.RefNotFoundException: Ref origin/master cannot be resolved

![](../_assets/img/6CiQ4C0.png)x

Likely cause: lack of support for `main` branches in git projects, it may happen with omegat versions below 5.5.

## Unable to download team project: authentication exception

The user gets this error when downloading the team project:

> Unable to download team project!
> java.util.concurrent.ExecutionException: org.tmatesoft.svn.core.SVNAuthenticationException: svn: E170001: OPTIONS of '{URL}': 403 Forbidden..

![](../_assets/img/zv8jiye.png)

Likely cause: Incorrect credentials.

## Unable to download team project: project file was not a file

The user gets this error when downloading the team project:

> Unable to download team project! 
> java.util.concurrent.ExecutionException: java.lang.IllegalArgumentException: Project file /path/to/project/omegat.project was not a file

![](../_assets/img/dHvNAfO.png)


Likely cause: The OmegaT project does not exist in that branch or is corrupted.

## Socket closed???

![](https://imgur.com/dpaPIIe.png)

---- 

https://imgur.com/v8MGPqd.png

![Alt text](https://mail.google.com/mail/u/2?ui=2&ik=5941e63073&attid=0.1&permmsgid=msg-a:r-2178763549435231894&th=18345ac19366c4e9&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ89GBvlButtVG9Ka84GJdAw5xQQcb_VSp38-shHYB4UJuvfAnNfj7NVJJktEHuCpXJSVzZmq6VW-5WtKAoUf9DRwTzZxfAgK_G0P2WKSynCm0nxlBsKZiOLldA&disp=emb&realattid=ii_l84aet1g0)

https://imgur.com/klbhChr.png

The error shows that OmegaT failed to upload with credential problem. The user may not have write permissions. 

TransportException =>  https authentication or communication error

git-upload-pack not permitted -> git service deny to accept upload command.

https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ae.html
https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ide-ec.html
https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html

--


https://imgur.com/2VeicWe.png
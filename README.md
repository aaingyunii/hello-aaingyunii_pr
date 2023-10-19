# hello-aaingyunii_pr

- The Python program I'm distributing for the first time

View at:

- https://pypi.org/project/hello-aaingyunii_pr

### INSTALL
`$ pip install hello-aaingyunii_pr`

### DEV

```bash
$ git clone ...
$ cd hello-aaingyunii_pr
$ pdm venv create
$ source .venv/bin/activate
(hello-aaingyunii_pr) $ pdm install
```
### DEPLOY
`$ pdm publish`

### Contributing

```bash
$ git branch 0.2.0/very-small-function

$ git checkout 0.2.0/very-small-function
Switched to branch '0.2.0/very-small-function'

$ vi pyproject.toml

$ git status
On branch 0.2.0/very-small-function
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   pyproject.toml

no changes added to commit (use "git add" and/or "git commit -a")

$ git add .
$ git status
On branch 0.2.0/very-small-function
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   pyproject.toml

$ git commit -m "start dev 0.2.0"
[0.2.0/very-small-function 4ed0751] start dev 0.2.0
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
fatal: The current branch 0.2.0/very-small-function has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin 0.2.0/very-small-function

$ git push --set-upstream origin 0.2.0/very-small-function
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for '0.2.0/very-small-function' on GitHub by visiting:
remote:      https://github.com/pySatellite/hello-pysatellite/pull/new/0.2.0/very-small-function
remote:
To github.com:pySatellite/hello-pysatellite.git
 * [new branch]      0.2.0/very-small-function -> 0.2.0/very-small-function
Branch '0.2.0/very-small-function' set up to track remote branch '0.2.0/very-small-function' from 'origin'.
```


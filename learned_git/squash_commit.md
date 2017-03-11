# 如何合併commit

使用指令 `git rebase -i (sha)`
	
>vim底下的sha，從上到下是舊到新。

或是先 `git stash` 暫存目前的變動，在 `git rest sha`，

還原到舊版本，再`git stash pop`。

遠端強制push的話是`git push -f` or `git push --force`。

想不用-f維持樹的整潔，在push前先fetch再rebase

	如
	git fetch origin master
	git rebase origin/master
	git push
		
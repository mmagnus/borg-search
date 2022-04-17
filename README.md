# borg-search

<b>The way that the borg documentation suggests to do the search is to mount archive and use search tool specific for you system [1]. However, in my case, because of not the best Internet connection (?), mounting often failed and I was not able to search for files on mounted drives. The tools here seem to work well without mounting your backups. There is something that looks way more versetile than my mini tools here, so take a look there as well [2].</b>

Two tools here search archive all repositories or make list for each repository and then use grep.

	./borg-search.py -h
	usage: borg-search.py [-h] [-v] [--only ONLY] search

	Search for phrase in all of your repos or in --only::

		python borg-search.py --only snapshot-2022-04-16 cCA

	positional arguments:
	  search

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --verbose  be verbose
	  --only ONLY    only this repo, like 'snapshot' or 'snapshot-2022-04'

-------------------------------------------------------------------------------
  
	./borg-index.py -h
	usage: borg-index.py [-h] [-v] [--only ONLY] search

	Search for phrase in all of your repos or in --only::

		  python borg-search.py --only snapshot-2022-04-16 cCA

	positional arguments:
	  search

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --verbose  be verbose
	  --only ONLY    only this repo, like 'snapshot' or 'snapshot-2022-04'

grep resulting from borg-index.py files:

	(base) ➜  mnt grep t3-3 *.txt | grep def
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4950526 Wed, 2022-03-16 16:20:53 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff    114210 Tue, 2022-04-12 18:19:44 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out.2.pdb
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff    114534 Tue, 2022-04-12 18:19:44 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out.1.pdb
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4955668 Thu, 2022-03-17 15:05:50 Users/magnus/Desktop/trx-farfar/t3-3/cAc/default.out
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4936946 Wed, 2022-03-16 15:27:04 Users/magnus/Desktop/trx-farfar/t3-3/aAg/default.out
	
extract:

	(base) ➜  mnt borg extract ::snapshot-2022-04-13T00:01:05 Users/magnus/Desktop/trx-farfar/t3-3/guA/default.out



[1] https://github.com/borgbackup/borg/issues/4092
[2] https://gitlab.com/essembeh/borg-find

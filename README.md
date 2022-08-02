# borg-search

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

	(base) ➜  borg-search git:(main) ✗ ./borg-index.py -h
	usage: borg-index.py [-h] [-v] [--only ONLY]

	Search for phrase in all of your repos or in --only::

		/Users/magnus/workspace/borg-search/borg-index.py --only m1.
		> args: Namespace(only='m1.', verbose=False)
		> repo: 'm1.local-2022-01-26-143942'

	files will be created so you can grep them::

		(base) ➜  mq git:(master) ✗ grep 'Miro' m1*
		m1.local-2022-01-26-143942.txt:drwxr-xr-x magnus staff         0 Mon, 2021-07-26 17:02:21 Volumes/HD/docs/Movies/Miro Video Converter

	and then to extract::

		borg extract ::m1.local-2022-01-26-143942 'Volumes/HD/docs/Movies

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --verbose  be verbose
	  --only ONLY    only this repo, like 'snapshot' or 'snapshot-2022-04' (dont use here *, just write part of repo names; of '*' then take all (by default)


grep resulting from borg-index.py files:

	(base) ➜  mnt grep t3-3 *.txt | grep def
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4950526 Wed, 2022-03-16 16:20:53 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff    114210 Tue, 2022-04-12 18:19:44 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out.2.pdb
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff    114534 Tue, 2022-04-12 18:19:44 Users/magnus/Desktop/trx-farfar/t3-3/UAA/default.out.1.pdb
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4955668 Thu, 2022-03-17 15:05:50 Users/magnus/Desktop/trx-farfar/t3-3/cAc/default.out
	snapshot-2022-04-13T00:01:05.txt:-rw-r--r-- magnus staff   4936946 Wed, 2022-03-16 15:27:04 Users/magnus/Desktop/trx-farfar/t3-3/aAg/default.out
	
extract:

	(base) ➜  mnt borg extract ::snapshot-2022-04-13T00:01:05 Users/magnus/Desktop/trx-farfar/t3-3/guA/default.out

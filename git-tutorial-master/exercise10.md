# Exercise 10 - Understanding Commits

1. Look at your commit log

        git log --oneline

2. Choose a commit hash

3. See what type of object that hash names

        git cat-file -t <hash>

        commit

4. Examine the contents of that commit closely

        git cat-file -p <hash>

        tree 6805767853c43b3dba9558ffcfa0414a7a95d9b0
        parent a8eaed1c4bdbf6ac107e68489de1f22f8cae7fd2
        author Judy Kuo <ambergld99@gmail.com> 1666194710 -0700
        committer Judy Kuo <ambergld99@gmail.com> 1666194710 -0700

        Added items to files

5. Find the parent's hash in the commit log
        parent a8eaed1c4bdbf6ac107e68489de1f22f8cae7fd2

6. Look at the contents of the tree

        git cat-file -p <hash>

        tree a4702b9d260ab704a9cb748d74f7f874ad01043f
        parent b49815ef998ba7cdf3a4f49a73b5f4cb2a031e8d
        author Judy Kuo <ambergld99@gmail.com> 1666194388 -0700
        committer Judy Kuo <ambergld99@gmail.com> 1666194388 -0700

        Added items to files


7. Examine the contents of one of the blobs
        160000 commit 2249720ecfe4040c4da2faeaef94d28e3bc77920  equipment
        100644 blob 6b8a3cb4ea4fcae7b9b579dd54db6e03999497f6    fruits.txt
        100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    vegetables.txt


8. What type of object does the parent hash represent?

        git cat-file -t <hash>

        commit

9. Examine the contents of the parent and its tree
        tree 7129756e2d1c1c799b129c427d6958c5121d8b4c
        parent d76b13e531fd5f01ab31d96debb05425ccec1cc4
        author Judy Kuo <ambergld99@gmail.com> 1666193123 -0700
        committer Judy Kuo <ambergld99@gmail.com> 1666193123 -0700

        First commit


10. Do the trees you looked at have any matching hashes listed?
        No matches. they all have unque hashes.
'Git Commit Analytics'

import sys

import git


def committed_datetime(commits):
    'commit.committed_datetime'
    for commit in commits:
        yield commit.committed_datetime


def main(repo, branch):
    "__name__ == '__main__'"
    for c_dt in committed_datetime(git.Repo(repo).iter_commits(branch)):
        print(c_dt)


if __name__ == '__main__':
    main(sys.argv[1], 'master')

'Git Commit Analytics'

import sys

import git


def main(repo, branch):
    "__name__ == '__main__'"
    for commit in git.Repo(repo).iter_commits(branch):
        print(commit.committed_datetime)


if __name__ == '__main__':
    main(sys.argv[1], 'master')

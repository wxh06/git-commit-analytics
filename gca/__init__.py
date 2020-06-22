'Git Commit Analytics'

from math import ceil
import shutil
import sys

import git


def committed_datetime(commits):
    'commit.committed_datetime'
    for commit in commits:
        yield commit.committed_datetime


def hour(commits):
    'Commits per day hour'
    hours = [
        {'insertions': 0, 'deletions': 0, 'files': 0, 'lines': 0}
        for i in range(24)
    ]
    for commit in commits:
        for stat in hours[commit.committed_datetime.hour].keys():
            hours[commit.committed_datetime.hour][stat] \
                += commit.stats.total[stat]
    return hours


def main(repo, branch, author):
    "__name__ == '__main__'"
    commits = git.Repo(repo).iter_commits(branch, author=author)
    hours = hour(commits)
    max_lines = max(i['lines'] for i in hours)
    terminal_size = shutil.get_terminal_size((80, 20))
    ratio = (terminal_size.columns - 6) / max_lines
    for i, cnt in zip(range(24), hours):
        print(f"{i:2}: \x1b[32m{'+' * ceil(cnt['insertions'] * ratio)}"
              f"\x1b[31m{'-' * ceil(cnt['deletions'] * ratio)}\x1b[0m")


if __name__ == '__main__':
    main(*sys.argv[1:])

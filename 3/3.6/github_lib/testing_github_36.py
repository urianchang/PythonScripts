# Python 3.6
from github import Github
import json
import pprint

with open('config.json') as json_config_file:
    config = json.load(json_config_file)

API_KEY = config['api_key']

"""
def get_branch_commit_sha(repo, branch_name):
    d = dict(
        (branch.name, branch.commit.sha)
        for branch in repo.get_branches()
    )
    return d.get(branch_name)

def get_status(repo, commit):
    return repo.get_commits(query)[0].get_statuses()[0].state

g = Github(API_KEY)
sm = g.get_organization('sightmachine')

req_repo = input('Repo: ').strip()
repo = sm.get_repo(req_repo)
query = input('Branch/Commit_SHA/Artifact: ')
branch_sha = get_branch_commit_sha(repo, query)

if branch_sha:
    branch_status = get_status(repo, branch_sha)
    print("{} has a status of: {}".format(query, branch_status))
else:
    commit_status = get_status(repo, query)
    print("{} has a status of: {}".format(query, commit_status))
"""

g = Github(API_KEY)
sm = g.get_organization('sightmachine')
print(sm.get_repo('int-test').trees_url)

from github import Github
import json
import pprint

class Octocat(object):
    """
    Octocat leverages the PyGitHub library and GitHub API to process
    information about repositories, branches, tags, and commits.

    URL ref: http://pygithub.readthedocs.io/en/latest/introduction.html
    """
    def __init__(self, org_name):
        self.github = self._init_app(org_name)
        self.get_repos()
        self.repo_branches = {}

    def _init_app(self, org_name):
        # (str) -> Type github.Organization.Organization
        """
        Initializes a GitHub object with API key and returns GitHub organization object
        based on the name supplied.

        URL ref: http://pygithub.readthedocs.io/en/latest/github_objects/Organization.html#github.Organization.Organization

        :param org_name: String name of organization
        :return GitHub organization object:
        """
        with open('./config.json') as json_config_file:
            config = json.load(json_config_file)

        API_KEY = config['api_key']
        return Github(API_KEY).get_organization(org_name)

    def _check_repo(self, repo_name):
        # (str) -> bool
        """
        Gets all the repositories in the organization and checks if a
        specified repository exists in tuple.
        """
        self.get_repos()
        return repo_name in self.repos

    def _check_branch(self, repo_name, branch_name):
        # (str, str) -> bool
        """
        Gets all the branches in a repository and checks if a branch
        exists in the list.
        """
        if self._check_repo(repo_name):
            self.get_repo_branches(repo_name)
            return branch_name in self.repo_branches[repo_name].keys()

    def _get_branch_commit_sha(self, repo_name, branch_name):
        # (str, str) -> str
        """
        Checks if the branch exists. If true, gets the latest commit SHA for the branch.
        """
        if self._check_branch(repo_name, branch_name):
            return self.repo_branches[repo_name].get(branch_name)

    def get_repos(self):
        """
        Retrieves all the repositories in an organization and saves them to self.
        Returns 'self' for method chaining.
        """
        self.repos = tuple(
            repo.full_name.split('/')[1]
            for repo in self.github.get_repos()
        )
        return self

    def get_repo_branches(self, repo_name):
        """
        Retrieves all branches in a specified repository and saves them to self.
        Returns 'self' for method chaining.
        """
        if self._check_repo(repo_name):
            branches = dict(
                (branch.name, branch.commit.sha)
                for branch in self.github.get_repo(repo_name).get_branches()
            )
            self.repo_branches[repo_name] = branches
        return self

    def show_repos(self):
        """
        Pretty prints all the repositories in the organization. Can be modified
        to return these repositories for processing. Return 'self' for method chaining.
        """
        self.get_repos()
        pprint.pprint(self.repos, indent=4)
        return self

    def show_branches(self, repo_name):
        """
        Pretty prints all the branches in a specified repository. Can be modified
        to return these branches for processing. Return 'self' for method chaining.
        """
        if self._check_repo(repo_name):
            self.get_repo_branches(repo_name)
            pprint.pprint(self.repo_branches[repo_name], indent=4)
        return self

    def get_commit_status(self, repo_name, commit):
        # (str, str) -> str
        """
        Gets the state of a specific commit: 'error', 'failure', 'pending', or 'success'.

        URL ref: https://developer.github.com/v3/repos/statuses/
        """
        if self._check_repo(repo_name):
            return self.github.get_repo(repo_name).get_commits(commit)[0].get_statuses()[0].state

    def resolve(self, repo_name, query):
        # (str, str) -> bool
        """
        Checks the commit status of a given query in a specified repo. The query can be
        a branch name, commit SHA, or artifact (e.g. 'v4.11.0-216-ga7a8f6e3c'). Returns
        a Boolean if the commit status is 'success'. Maybe consider returning the
        state string for processing elsewhere.
        """
        if self._check_repo(repo_name):
            # Check if query is a branch name
            if self._check_branch(repo_name, query):
                commit_sha = self._get_branch_commit_sha(repo_name, query)
            else:
                commit_sha = query

            status = self.get_commit_status(repo_name, commit_sha)

            return True if status == "success" else False

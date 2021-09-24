import json
import os
import requests 
from pprint import pprint
from typing import Any, Callable, NamedTuple
from urllib.parse import urljoin


username = "urianchang"
token = os.getenv("GITHUB_ACCESS_TOKEN")

bot_headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {token}",
    "Content-type": "application/json; charset=utf-8",
}


def github_url(ends: list) -> str:
    base_url = "https://api.github.com/orgs/cerebrotech/"
    endpoint = '/'.join(s.strip("/") for s in ends)
    return urljoin(base_url, endpoint)    


def is_engineer(user: str) -> bool:
    url = github_url(["teams", "Engineers", "memberships", user])
    res = requests.get(url, auth=(username, token))
    data = res.json()
    return data['state'] == 'active' and data['role'] == 'member'


def iter_pages(make_request: Callable, params: dict) -> Any:
    response = make_request(params)
    data = response.json()
    if len(data) == 0:
        return
    yield data
    while "next" in response.links:
        response = requests.get(response.links["next"]["url"], auth=(username, token))
        yield response.json()   


def all_engineers(params: dict) -> requests.Response:
    url = github_url(["teams", "Engineers", "members"])
    return requests.get(url, params, auth=(username, token))


def all_child_teams(params: dict) -> requests.Response:
    url = github_url(["teams", "Engineers", "teams"])
    return requests.get(url, params, auth=(username, token))

def engineers(team: str, params: dict) -> requests.Response:
    url = github_url(["teams", team, "members"])
    return requests.get(url, headers=bot_headers, params=params)
    # return requests.get(url, params, auth=(username, token))


class Something(NamedTuple):
    current: str

    def __str__(self):
        return str(self.current)


if __name__ == "__main__":
    # if is_engineer(username):
    #     users = set()
    #     for result in iter_pages(all_engineers, {"page": 1, "per_page": 100}):
    #         users.update([user['login'] for user in result])
    #     print(f"There are {len(users)} users in the Engineers team")

    #     teams = set()
    #     for result in iter_pages(all_child_teams, {"page": 1, "per_page": 100}):
    #         teams.update([team['name'] for team in result])
    #     print(f"There are {len(teams)} child teams in the Engineers team")
    # else:
    #     print(f"{username} is not a member of Engineers")
    #     exit(1)

    resp = engineers("dev-productivity", {"page": 1, "per_page": 100})
    print(resp.headers)
    # for member in resp.json():
    #     print(member['login'])

    # print(f"a new thing: {Something(current='hi')}")

    # Get metadata about the DevProd GitHub team
    # url = github_url(["teams", "dev-productivity"])
    # pprint(requests.get(url, {}, auth=(username, token)).json())

    # url = "https://api.github.com/repos/cerebrotech/merge-queue-sandbox1/pulls/1125/requested_reviewers"
    # resp = requests.post(
    #     url, 
    #     auth=(username, token),
    #     data=json.dumps({
    #         "team_reviewers": ["dev-productivity"]
    #     })
    # )
    # print(resp.status_code)
    # pprint(resp.json()['requested_teams'])

    exit(0)

import requests

from BearerAuth import BearerAuth

GITHUB_API_URL = "https://api.github.com"
GITHUB_PROJECT = "SeleniumHQ"
GITHUB_TOKEN = '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'


def get_list_repos():
    url = GITHUB_API_URL + "/users/" + GITHUB_PROJECT + "/repos"
    response = requests.get(url, auth=BearerAuth(GITHUB_TOKEN))
    repos = []
    for item in response.json():
        repos.append(item["full_name"])
    return repos


def get_list_repos_sort_by_date_updated_in_descending_order():
    url = GITHUB_API_URL + "/users/" + GITHUB_PROJECT + "/repos?sort=updated&direction=desc"
    response = requests.get(url, auth=BearerAuth(GITHUB_TOKEN))
    repos = []
    for item in response.json():
        repos.append(item["full_name"])
    return repos


def get_total_number_of_open_issues_in_all_repos():
    repos = get_list_repos()
    counts = 0
    for project in repos:
        url = GITHUB_API_URL + "/repos/" + project + "/issues?state=open"
        response = requests.get(url, auth=BearerAuth(GITHUB_TOKEN))
        # print(project + ":" + str(len(response.json())))
        counts += len(response.json())
    return counts


def get_the_most_watchers_repos():
    repos = get_list_repos()

    max_count = 0
    for project in repos:
        url = GITHUB_API_URL + "/repos/" + project + "/subscribers"
        response = requests.get(url, auth=BearerAuth(GITHUB_TOKEN))
        if max_count < len(response.json()):
            max_count = len(response.json())

    the_most_watchers_repos = {}
    for project in repos:
        url = GITHUB_API_URL + "/repos/" + project + "/subscribers"
        response = requests.get(url, auth=BearerAuth(GITHUB_TOKEN))
        if max_count == len(response.json()):
            the_most_watchers_repos[project] = max_count
    return the_most_watchers_repos


if __name__ == '__main__':
    # a
    print(get_total_number_of_open_issues_in_all_repos())
    # b
    print(get_list_repos_sort_by_date_updated_in_descending_order())
    # c
    print(get_the_most_watchers_repos())

import os
import time
from dotenv import load_dotenv
from github import Github, RateLimitExceededException
from frictionless import Resource, transform, steps


load_dotenv()
PAUSE = 1
RETRY = 10
QUERY = "ckanext in:name stars:>0"
github = Github(os.environ["GITHUB_TOKEN"], per_page=100)


# Source


def fetch_source():
    source = []
    result = github.search_repositories(QUERY, sort="stars", order="desc")
    time.sleep(PAUSE)
    page = 0
    while True:
        try:
            repos = result.get_page(page)
        except RateLimitExceededException:
            time.sleep(RETRY)
            continue
        time.sleep(PAUSE)
        page += 1
        if not repos:
            break
        for repo in repos:
            data = {}
            data["code"] = "-".join([repo.owner.login, repo.name])
            data["user"] = repo.owner.login
            data["repo"] = repo.name
            data["branch"] = repo.default_branch
            data["stars"] = repo.stargazers_count
            data["description"] = repo.description
            source.append(data)
        print(f"Found items: {len(source)}")
    return source


# General


transform(
    Resource(fetch_source()),
    steps=[
        steps.row_sort(field_names=["stars"], reverse=True),
        steps.table_write(path="data/extensions.csv"),
    ],
)

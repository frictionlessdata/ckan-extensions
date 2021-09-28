import os
import time
from dotenv import load_dotenv
from frictionless import Resource
from github import Github, RateLimitExceededException


load_dotenv()
PAUSE = 1
RETRY = 10
QUERY = "ckanext in:name stars:>0"
github = Github(os.environ["GITHUB_TOKEN"], per_page=100)


# Source


def search_items():
    items = []
    results = github.search_repositories(QUERY, sort="stars", order="desc")
    time.sleep(PAUSE)
    page_number = 0
    while True:
        try:
            page = results.get_page(page_number)
        except RateLimitExceededException:
            time.sleep(RETRY)
            continue
        time.sleep(PAUSE)
        page_number += 1
        if not page:
            break
        for result in page:
            item = {}
            item["code"] = "-".join([result.owner.login, result.name])
            item["user"] = result.owner.login
            item["repo"] = result.name
            item["branch"] = result.default_branch
            item["stars"] = result.stargazers_count
            item["description"] = result.description
            items.append(item)
        print(f"Found items: {len(items)}")
    return items


# General


resource = Resource(search_items())
resource.write("data/extensions.raw.csv")

import requests
import json

# generate your own github api token
TOKEN = open("TOKEN", 'r').read()
header = {"Accept": "application/vnd.github.mercy-preview+json", "Authorization": "token " + TOKEN}

# github api to search github repos
url = "https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc"

res = json.loads(requests.get(url, headers=header).content)

structured_res = json.dumps(res, indent=2)

# print(structured_res)

repo_items = res['items']
sample_item = repo_items[0]

print(json.dumps(sample_item, indent=2))

repo_name = sample_item["name"]
repo_owner = sample_item["owner"]["login"]
readme_url = "https://api.github.com/repos/{repo_owner}/{repo_name}/readme".\
    format(repo_owner=repo_owner, repo_name=repo_name)

readme_res = json.loads(requests.get(readme_url, headers=header).content)
print(readme_res)

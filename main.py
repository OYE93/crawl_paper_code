import requests
import json

# generate your own github api token
TOKEN = open("TOKEN", 'r').read()

# set url request header
header = {"Accept": "application/vnd.github.mercy-preview+json", "Authorization": "token " + TOKEN}


# github api to search github repos
def search_repo(key_word, start_time, end_time):
    per_page = 10
    time_range = "{start}..{end}".format(start=start_time, end=end_time)

    url = "https://api.github.com/search/repositories?" \
          "q={key_word} created:{time_range}&per_page={per_page}&sort=stars&order=desc"\
          .format(key_word=key_word, time_range=time_range, per_page=per_page)
    request_result = requests.get(url, headers=header)
    print(request_result.headers)
    remaining_limits = request_result.headers.get('X-RateLimit-Remaining')
    print(remaining_limits)
    print(request_result.text)
    res = json.loads(request_result.text)
    structured_res = json.dumps(res, indent=2)
    print(structured_res)

    repo_items = res['items']
    print(len(repo_items))
    return repo_items


def main():
    key_word = "paper"
    start_time = "2012-01-01"
    end_time = "2019-01-01"
    repo_items = search_repo(key_word, start_time, end_time)
    sample_item = repo_items[0]

    print(json.dumps(sample_item, indent=2))

    repo_name = sample_item["name"]
    repo_owner = sample_item["owner"]["login"]
    readme_url = "https://api.github.com/repos/{repo_owner}/{repo_name}/readme".\
        format(repo_owner=repo_owner, repo_name=repo_name)

    readme_res = json.loads(requests.get(readme_url, headers=header).text)
    print(readme_res)


if __name__ == '__main__':
    main()
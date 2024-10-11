import requests

# 设置你的GitHub个人访问令牌和组织名称
personal_access_token = ''
org_name = '2024-HIT-AIoT'

# 邮箱列表，每个元素是一个邮箱地址
emails_to_invite = ['']

# 设置请求头部
headers = {
    'Authorization': f'token {personal_access_token}',
    'Accept': 'application/vnd.github.v3+json',
}

# 邀请用户加入组织
for email in emails_to_invite:
    # 构造邀请URL
    url = f'https://api.github.com/orgs/{org_name}/invitations'

    # 构造请求体
    payload = {
        'email': email  # 使用email'字段来邀请
    }

    # 发送邀请请求
    response = requests.post(url, headers=headers, json=payload)

    # 检查响应
    if response.status_code == 201:
        print(f'Successfully invited {email}')
    else:
        print(f'Failed to invite {email}. Status code: {response.status_code}, Response: {response.json()}')

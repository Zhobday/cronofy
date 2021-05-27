import requests
import json


token_params = {
  "client_id": "QGSW-bJJlQaLz_QjTsRmzndkTHjBtuiV",
  "client_secret": "N8WdNQsK9miw5DaV9QEF5NRYRRdKFInkgERnYzYyJIV4P3ZqR686qdSQLPa8L6wra-s-9J36-0-dADztjFPJkA",
  "grant_type": "refresh_token",
  "refresh_token": "1cnWIxhANZ5cWOVpwhNXf82KVJhqpDhc"
}

token_url = "https://api-uk.cronofy.com/oauth/token"

ava_url = 'https://api.cronofy.com/v1/availability'
auth_headers = {"Authorization": "Bearer N8WdNQsK9miw5DaV9QEF5NRYRRdKFInkgERnYzYyJIV4P3ZqR686qdSQLPa8L6wra-s-9J36-0-dADztjFPJkA"}

payload = {
  "participants": [
    {
      "members": [
        {
          "sub": "acc_60af501ec270a7003304cbd1",
          "calender_ids": ["pro_YK9RWRMxGQAyA7dP"]
        }
      ],
      "required": "all"
    }
  ],
  "required_duration": {"minutes": 60},
  "query_periods": [
    {
      "start": "2021-05-28T09:00:00Z",
      "end": "2021-06-28T18:00:00Z"
    }
  ]
}

token_request = requests.post(token_url,data=token_params)

print(token_request.status_code)

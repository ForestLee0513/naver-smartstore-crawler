import os
import requests

def get_kakao_token(redirect_uri, auth_code):
    KAKAO_REST_API_KEY=os.environ.get('KAKAO_REST_API_KEY')
    get_token_request_param_dict = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_REST_API_KEY,
        "redirect_uri": redirect_uri,
        "code": auth_code
    }

    return requests.post('https://kauth.kakao.com/oauth/token', params=get_token_request_param_dict).json()

def get_kakao_user_info(token):
    get_user_info_request_header_dict = {
        "Authorization": f'Bearer {token}',
        "Content-type": "Content-type: application/x-www-form-urlencoded;charset=utf-8"
    }

    return requests.post('https://kapi.kakao.com/v2/user/me', headers=get_user_info_request_header_dict).json()
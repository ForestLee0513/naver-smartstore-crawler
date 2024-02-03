from flask import Blueprint, request
import os
import requests

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/kakao', methods=["POST"])
def sign_up():
    KAKAO_REST_API_KEY=os.environ.get('KAKAO_REST_API_KEY')
    data = request.json
    KAKAO_REDIRECT_URI = data['redirect_uri']
    KAKAO_AUTH_CODE = data['code']

    paramDict = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_REST_API_KEY,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": KAKAO_AUTH_CODE
    }

    response = requests.post('https://kauth.kakao.com/oauth/token', params=paramDict)

    print(response.json())

    return "kakao signin/singup view."
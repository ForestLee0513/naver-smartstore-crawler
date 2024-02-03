from flask import Blueprint, request

from ..service.auth.kakao_auth import get_kakao_token, get_kakao_user_info

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/kakao', methods=["POST"])
def kakao_login():
    data = request.json
    KAKAO_REDIRECT_URI = data['redirect_uri']
    KAKAO_AUTH_CODE = data['code']

    kakao_token_response = get_kakao_token(KAKAO_REDIRECT_URI, KAKAO_AUTH_CODE)
    kakao_user_info_response = get_kakao_user_info(kakao_token_response['access_token'])

    return kakao_user_info_response

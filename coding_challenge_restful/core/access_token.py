from coding_challenge_restful.auth import generate_jwt_auth_token


def get_access_token():
    """
    Get access token

    :return: jwt access token
    """

    access_token = generate_jwt_auth_token(str(1))
    return access_token

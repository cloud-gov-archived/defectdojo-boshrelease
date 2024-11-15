# local_settings.py
# this file will be included by settings.py *after* loading settings.dist.py

import environ

env = environ.Env(
    DD_SOCIAL_AUTH_OIDC_AUTH_ENABLED=(bool, False),
    DD_SOCIAL_AUTH_OIDC_OIDC_ENDPOINT=(str, ''),
    DD_SOCIAL_AUTH_OIDC_ID_KEY=(str, ''),
    DD_SOCIAL_AUTH_OIDC_KEY=(str, ''),
    DD_SOCIAL_AUTH_OIDC_SECRET=(str, ''),
    DD_SOCIAL_AUTH_OIDC_USERNAME_KEY=(str, ''),
    DD_SOCIAL_AUTH_OIDC_WHITELISTED_DOMAINS=(list, ['']),
    DD_SOCIAL_AUTH_OIDC_JWT_ALGORITHMS=(list, ["RS256","HS256"]),
    DD_SOCIAL_AUTH_OIDC_ID_TOKEN_ISSUER=(str, ''),
    DD_SOCIAL_AUTH_OIDC_ACCESS_TOKEN_URL=(str, ''),
    DD_SOCIAL_AUTH_OIDC_AUTHORIZATION_URL=(str, ''),
    DD_SOCIAL_AUTH_OIDC_USERINFO_URL=(str, ''),
    DD_SOCIAL_AUTH_OIDC_JWKS_URI=(str, ''),
) + env

AUTHENTICATION_BACKENDS += (
    'social_core.backends.open_id_connect.OpenIdConnectAuth',
)

OIDC_AUTH_ENABLED = env('DD_SOCIAL_AUTH_OIDC_AUTH_ENABLED')
SOCIAL_AUTH_OIDC_OIDC_ENDPOINT = env('DD_SOCIAL_AUTH_OIDC_OIDC_ENDPOINT')
SOCIAL_AUTH_OIDC_ID_KEY = env('DD_SOCIAL_AUTH_OIDC_ID_KEY')
SOCIAL_AUTH_OIDC_KEY = env('DD_SOCIAL_AUTH_OIDC_KEY')
SOCIAL_AUTH_OIDC_SECRET = env('DD_SOCIAL_AUTH_OIDC_SECRET')
SOCIAL_AUTH_OIDC_USERNAME_KEY = env('DD_SOCIAL_AUTH_OIDC_USERNAME_KEY')
SOCIAL_AUTH_OIDC_WHITELISTED_DOMAINS = env('DD_SOCIAL_AUTH_OIDC_WHITELISTED_DOMAINS')
SOCIAL_AUTH_OIDC_JWT_ALGORITHMS = env('DD_SOCIAL_AUTH_OIDC_JWT_ALGORITHMS')
SOCIAL_AUTH_OIDC_ID_TOKEN_ISSUER = env('DD_SOCIAL_AUTH_OIDC_ID_TOKEN_ISSUER')
SOCIAL_AUTH_OIDC_ACCESS_TOKEN_URL = env('DD_SOCIAL_AUTH_OIDC_ACCESS_TOKEN_URL')
SOCIAL_AUTH_OIDC_AUTHORIZATION_URL = env('DD_SOCIAL_AUTH_OIDC_AUTHORIZATION_URL')
SOCIAL_AUTH_OIDC_USERINFO_URL = env('DD_SOCIAL_AUTH_OIDC_USERINFO_URL')
SOCIAL_AUTH_OIDC_JWKS_URI = env('DD_SOCIAL_AUTH_OIDC_JWKS_URI')


LOGIN_EXEMPT_URLS += (
    r'oauth2/idpresponse',
)

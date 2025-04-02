import os
from amocrm.v2 import tokens


async def create_amocrm_token(
    client_id: str,
    client_secret: str,
    subdomain: str,
    redirect_url: str,
    twety_min_code: str
):
    tokens.default_token_manager(
        client_id=client_id,
        client_secret=client_secret,
        subdomain=subdomain,
        redirect_url=redirect_url,
        storage=tokens.FileTokensStorage(),
    )
    tokens.default_token_manager.init(
        code=twety_min_code,
        skip_error=True)
    return tokens


async def token_initialization():
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    subdomain = os.environ.get('subdomain')
    redirect_url = os.environ.get('redirect_url')
    twety_min_code = os.environ.get('twety_min_code')

    return await create_amocrm_token(
        client_id=client_id,
        client_secret=client_secret,
        subdomain=subdomain,
        redirect_url=redirect_url,
        twety_min_code=twety_min_code
    )

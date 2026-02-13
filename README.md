# Ever Gauzy Python SDK

Official Python SDK for the [Ever Gauzy](https://gauzy.co) API, auto-generated using [Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/).

## Installation

```bash
pip install ever-gauzy-sdk
```

## Quick Start

```python
import asyncio
from azure.identity import ClientSecretCredential
from microsoft_kiota_authentication_azure import AzureIdentityAuthenticationProvider
from microsoft_kiota_http.httpx_request_adapter import HttpxRequestAdapter
from ever_gauzy_sdk.ever_gauzy_api_client import EverGauzyApiClient

# Create the API client
request_adapter = HttpxRequestAdapter(auth_provider)
client = EverGauzyApiClient(request_adapter)

# Example: List employees
async def main():
    employees = await client.api.employee.get()
    print(employees)

asyncio.run(main())
```

## Authentication

The Gauzy API supports multiple authentication methods:

- **Bearer Token (JWT)**: For user-authenticated requests
- **API Key**: Via `X-API-Key` header
- **OAuth2**: Authorization code flow

## API Documentation

- **Swagger UI**: https://api.gauzy.co/swg
- **Scalar Docs**: https://api.gauzy.co/docs
- **OpenAPI Spec**: https://api.gauzy.co/swg-json

## Development

```bash
# Clone the repository
git clone https://github.com/ever-co/ever-gauzy-sdk-python.git
cd ever-gauzy-sdk-python

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v
```

## SDK Generation

This SDK is auto-generated from the Ever Gauzy OpenAPI specification using Microsoft Kiota.
To regenerate, trigger the "Generate SDK" GitHub Action workflow.

## License

This SDK is licensed under the [MIT](LICENSE) license.

## Links

- [Ever Gauzy](https://gauzy.co)
- [API Documentation](https://docs.gauzy.co)
- [GitHub](https://github.com/ever-co/ever-gauzy)

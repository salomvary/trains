# Trains

Various tools and unofficial API clients and tools for MÁV - Hungarian Railways.

- `vonatinfo_spec`: OpenApi spec for [Vonatinfó](https://vonatinfo.mav-start.hu/) ("Train Info") API
- `vonatinfo_client`: generated Python client for Vonatinfó API
- `vontinfo_api`: developer friendly wrapper around `vonatinfo_client`
- `vonatinfo_web`: web interface for `vonatinfo_client`
- `vontinfo_cli`: command line interface for `vonatinfo_client`
- `elvira_spec`: OpenApi spec for [Új ELVIRA](https://jegy.mav.hu/) (new ticket sales and planning system) API
- `elvira_client`: generated Python client for ELVIRA API
- `elvira_api`: developer friendly wrapper around `elvira_client`
- `elvira_cli`: command line interface for `elvira_client`

The generated clients are based on reverse engineering the APIs and manually creating OpenAPI
specifications. See the `openapi.json` files in the respective directories.

- [Open Vonatinfó API in Swagger Editor](https://editor-next.swagger.io/?url=https://raw.githubusercontent.com/salomvary/trains/refs/heads/main/vonatinfo_spec/openapi.json)
- [Open ELVIRA API in Swagger Editor](https://editor-next.swagger.io/?url=https://raw.githubusercontent.com/salomvary/trains/refs/heads/main/elvira_spec/openapi.json)

## Usage

    python -m venv .venv
	source .venv/bin/activate
    pip install -r requirements.txt

Start `vonatinfo_web`:

    ./manage.py runserver

Use the CLIs: see Readme files in `vonatinfo_cli` and `elvira_cli` directories.

## Generating Python clients

    brew install openapi-generator
    make vonatinfo-client
    make elvira-client

## Deploying to Dokku

    dokku apps:create trains
    dokku postgres:create trains
    dokku postgres:link trains trains
    dokku config:set DEBUG=False ALLOWED_HOSTS=trains.example.com
    dokku config:set DISABLE_COLLECTSTATIC=1

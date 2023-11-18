vonatinfo-client:
	openapi-generator generate \
		--input-spec vonatinfo_spec/openapi.json \
		--generator-name python \
		--library asyncio \
		--package-name vonatinfo_client \
		--global-property models,apis,apiTests=false,apiDocs=false,modelTests=false,modelDocs=false,supportingFiles=api_client.py:api_response.py:configuration.py:exceptions.py:__init__.py:rest.py \
		--output .

elvira-client:
	openapi-generator generate \
		--input-spec elvira_spec/openapi.json \
		--generator-name python \
		--library asyncio \
		--package-name elvira_client \
		--global-property models,apis,apiTests=false,apiDocs=false,modelTests=false,modelDocs=false,supportingFiles=api_client.py:api_response.py:configuration.py:exceptions.py:__init__.py:rest.py \
		--output .

#!/usr/bin/env bash

rm -rf ../../sdk_generated/

java -DapiTests=false -DmodelTests=false -cp openapi-generator-cli.jar:opsgenie-python-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate -g geniepy -i ../../opsgenie-oas.yml -c config.json -o ../../sdk_generated -t ../../templates

python refactor_project.py

rsync -avh ../../sdk_generated/ ../../

rm -rf ../../sdk_generated/

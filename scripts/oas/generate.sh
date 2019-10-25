#!/usr/bin/env bash

while getopts o: option
do
case "${option}"
    in
    o) OPSGENIE_OAS=${OPTARG};;
    esac
done

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${OPSGENIE_OAS}"
node "${OPSGENIE_OAS}/multi-file-swagger/index.js" "${OPSGENIE_OAS}/swagger.yaml" alert incident heartbeat account > "${DIR}/../../opsgenie-oas.json"
cd "${DIR}"

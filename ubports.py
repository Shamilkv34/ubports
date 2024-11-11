#!/usr/bin/env bash

set -e

TMPDIR=""

trap ctrl_c INT

function ctrl_c {
    printf "\n\nCTRL-C received\n"
    for JOB in $(jobs -p); do
        kill -9 "$JOB"
    done
    exit 1
}


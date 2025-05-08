#!/usr/bin/env bash

script_dir=$( dirname "$0" )
cd "$script_dir"


executor_image_tag=think-with-feedback-lua-executor
docker build -t "$executor_image_tag" .

#!/bin/bash

MESSAGE=${1:-"Auto update"}
git add .
git commit -m "$MESSAGE"
git push

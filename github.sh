#!/bin/bash

str="$(git status 2>&1)"
substr="fatal"
if [[ $str == *"$substr"* ]];
then
    echo "fatal: not a git repository (or any of the parent directories): .git"
else
    str="$(git status 2>&1)"
    substr="nothing to commit"
    if [[ $str == *"$substr"* ]];
    then
        echo "It is up to date! Nothing to commit. :-)"
    else
        git add --all
        git status
        echo "What is your commit message?"
        read msg
        git commit -m "$msg"
        echo "Which branch do you want to push your commit to?"
        read branch
        git push origin $msg
    fi
fi
echo ""
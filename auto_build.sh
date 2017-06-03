#!/bin/bash

# watch files change and auto make html docs .

fswatch -d source |(while read;do make html;done)

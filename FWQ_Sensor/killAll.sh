#!/bin/bash

ps aux | grep 'main.py sensor' | awk '{print $2}' | xargs -I {} kill -s SIGINT {} 2>/dev/null

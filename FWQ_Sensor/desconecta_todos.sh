#!/bin/bash

ps aux | grep -E 'main.py [0-9]* sensor' | awk '{print $2}' | xargs -I{} kill {}

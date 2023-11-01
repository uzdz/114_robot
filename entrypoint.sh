#!/bin/sh

python /app/robot.py \
    --cookie="$BOT_COOKIE" \
    --exclude="$BOT_EXCLUDE_DATE" \
    --urls="$BOT_OS_URLS" \
    --time="$BOT_CYCLE_TIME" \
    --ding="$BOT_DING_WEBHOOK" \
    --lark="$BOT_LARK_WEBHOOK"
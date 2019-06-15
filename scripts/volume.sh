#!/bin/sh


volume="$(amixer sget Master | awk -F "[][]" '/dB/ {print $2}')"

status="$(amixer sget Master | grep Mono: | awk '{print $6}')"

if [ "$status" = "[off]" ]
then
    echo "🔇 0%"
else
    echo "🔉 $volume"
fi

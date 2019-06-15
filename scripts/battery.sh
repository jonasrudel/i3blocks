#!/bin/sh

state="$(acpi | awk '{print $3}')"

percentage="$(acpi | awk '{$0=substr($4,1,length($4)-1); print $0}')"
charging="Charging,"
if [ "$state" = "$charging" ]; then
    echo "🔌 $percentage"
else
    echo "$percentage"
fi

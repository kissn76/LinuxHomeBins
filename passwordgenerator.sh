#!/bin/sh

LENGTH=$1

< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-${LENGTH}}
#!/bin/bash

echo "User: $USER"
echo "Date: $(date)"
echo "Local IP: $(hostname -I)"
ping -c 2 google.com

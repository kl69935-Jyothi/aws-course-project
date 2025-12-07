#!/bin/bash
set -e

echo "Cleaning old files in /var/www/html..."
rm -rf /var/www/html/*
mkdir -p /var/www/html
echo "Cleanup complete."

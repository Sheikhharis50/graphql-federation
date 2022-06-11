#!/bin/sh

PROJECT_DIR=`pwd`

echo "Environment loaded"
. $PROJECT_DIR/venv/bin/activate

cd gateway

echo "Running all services..."
npm run dev
#!/bin/bash
cd client && yarn install && yarn build && cp -r build/* ../static/client/
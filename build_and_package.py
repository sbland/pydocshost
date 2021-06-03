#!/usr/bin/env python
import os
os.system('cd client && yarn install && yarn build && cp -r build/* ../static/client/')

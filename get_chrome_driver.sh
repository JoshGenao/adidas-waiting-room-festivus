#!/bin/bash
# platform options: linux32, linux64, mac64, win32
PLATFORM=mac64
VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)

echo "Getting chromedriver version $VERSION"

curl http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip | bsdtar -xvf - -C .
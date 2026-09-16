#!/bin/bash
set -e

uv run pyinstaller --noconfirm --onedir --windowed --name=PasswordGen __main__.py

wget -v https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage

mkdir -p AppDir/usr/bin
cp -r dist/PasswordGen/* AppDir/usr/bin/

touch passwordgen.svg

./linuxdeploy-x86_64.AppImage --appdir=AppDir -d passwordgen.desktop -i passwordgen.svg --output appimage

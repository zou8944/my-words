#!/usr/bin/env bash

readme=README.md

echo "# 叫我果冻" > $readme
echo >> $readme
echo "[果冻的碎碎念 - zou8944.com](https://zou8944.com)" >> $readme
echo >> $readme

bash ./script/toc-echo.sh >> $readme
#!/bin/python
#-*-coding:utf-8-*-

import os
import subprocess as sub
import shutil

#windowsの場合はpwdをchdirに変える
#copy前のディレクトリを指定
os.chdir(".")
#現在の場所を取得
moto=sub.check_output("pwd")
#コピー先のディレクトリに移動
os.chdir("/tmp")
#コピー先のパス
gennzai=sub.check_output("pwd")
ago=moto.strip()
future=gennzai.strip()
#コピー前でコピーしたいファイルをつける
agos=ago+"/"+"ss.py"
#コピーする
shutil.copy(agos,future)


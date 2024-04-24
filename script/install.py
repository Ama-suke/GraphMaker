# pyinstaller を使ってexe化するためのスクリプト
import os
import subprocess

subprocess.call("pyinstaller --onefile --noconsole ./script/graphmaker.py")
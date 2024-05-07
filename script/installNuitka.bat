
@REM このファイルがあるワークスペースに移動する
cd %~dp0/../

@REM pythonの仮想環境を作成する
py -3.11 -m venv venv

@REM 仮想環境を有効化する
call venv\Scripts\activate

@REM 必要なライブラリをインストールする
pip install pySide6==6.6.3
pip install nuitka zstandard
pip install matplotlib

@REM pyinstallerで実行ファイルを作成する
nuitka ./script/graphmaker.py --onefile --disable-console --enable-plugin=pyside6

@REM 仮想環境を無効化する
deactivate

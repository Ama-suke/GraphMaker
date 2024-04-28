@REM 仮想環境でビルドするとレイアウトが崩れるので、仮想環境は使わない

@REM このファイルがあるワークスペースに移動する
cd %~dp0/../

@REM pythonの仮想環境を作成する
@REM py -m venv venv

@REM 仮想環境を有効化する
@REM call venv\Scripts\activate

@REM 必要なライブラリをインストールする
pip install pySide6
pip install pyinstaller
pip install matplotlib

@REM pyinstallerで実行ファイルを作成する
pyinstaller ./script/graphmaker.py --clean --onefile --noconfirm --noconsole

@REM 仮想環境を無効化する
@REM deactivate

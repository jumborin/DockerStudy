### コンテナに接続
docker exec -it chrome bash

### APTリポジトリを最新化
sudo apt -y update

### Seleniumをインストール
sudo pip install selenium --break-system-package

### Sleniumテスト実行方法
cd /home/seluser/code
python3 test.py

以上
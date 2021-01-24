# bitnami/redmineの標準コンテナの利用

#事前準備
dockerとdocker-composeが利用可能であること。(Windows機の場合、DockerDesktopインストール済みであればよい）

#元ファイル
https://raw.githubusercontent.com/bitnami/bitnami-docker-redmine/master/docker-compose.yml

#使用時コマンド
docker-compose up -d

#注意点
docker-compose.ymlを格納するフォルダおよび実行時のカレントディレクトリのフルパスには日本語が含まれていないこと。

以上
# bitnami/redmineの標準コンテナの利用

## 事前準備
dockerとdocker-composeが利用可能であること。
(Windows機の場合、DockerDesktopがインストール済みであればよい）
docker-compose.ymlが適当なフォルダに格納されていること。
コマンドプロンプトまたはターミナルにて、docker-compose.ymlが格納されているフォルダがカレントディレクトリになっていること。

## 注意点
docker-compose.ymlを格納するフォルダおよび実行時のカレントディレクトリのフルパスには日本語が含まれていないこと。
docker-compose.ymlファイルが格納されているフォルダ名がボリューム名の先頭に付与されることで判断すること。

## 元ファイル
https://raw.githubusercontent.com/bitnami/bitnami-docker-redmine/master/docker-compose.yml

# docker操作
## コンテナ起動コマンド
docker-compose up -d

## コンテナの一覧を表示するコマンド
docker ps

## コンテナ終了コマンド
docker-compose down

## データを格納するボリュームの一覧を取得
docker volume ls

## データ削除コマンド（ボリューム削除）
### MySQLのコンテナのデータ削除（登録データの削除等）
docker volume rm フォルダ名_mariadb_data

### Redmineのコンテナのデータ削除（プラグイン削除等）
docker volume rm フォルダ名_redmine_data

# Redmineの初期設定
## デフォルト設定
Redmine管理者ユーザ名：user
Redmine管理者パスワード：bitnami1
Redmine管理者メールアドレス：user@example.com
Redmine言語：英語
DBの管理者ユーザ名；bn_redmine
DBの管理者パスワード：
DB名：bitnami_redmine
MYSQLサーバのホスト名：mariadb
PostgreSQLサーバのホスト名：なし
DBサーバのポート番号：3306

以上
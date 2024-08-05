
# ビットコイントップアドレス取得スクリプト

このプロジェクトは、毎朝9時にmempoolからビットコインのトップ保有アドレスを取得するPythonスクリプトです。このスクリプトは、Webスクレイピングを使用してアドレスとその残高を取得し、コンソールに表示します。

## 機能
- 毎日9時にmempoolからビットコインのトップ保有アドレスを自動的に取得
- アドレスと保有BTCの数をコンソールに表示

## 使用方法

### 必要なライブラリ
このスクリプトは以下のPythonライブラリに依存しています：
- `requests`
- `beautifulsoup4`
- `schedule`

これらのライブラリは、以下のコマンドでインストールできます：

```sh
pip install requests beautifulsoup4 schedule
```

### スクリプトの実行
スクリプトを実行するには、ターミナルまたはコマンドプロンプトで以下のコマンドを入力してください：

```sh
python main.py
```

スクリプトは毎日9時にトップアドレスを取得し、コンソールに出力します。

## 注意事項
- このスクリプトはWebスクレイピングを利用していますが、APIが利用可能な場合はそちらを利用することを推奨します。
- 公開されているAPIキーや個人情報を含まないように注意してください。
- 本プロジェクトの使用により生じた損害について、作者は一切の責任を負いません。

## ライセンス
このプロジェクトはMITライセンスの下で提供されています。詳細は`LICENSE`ファイルを参照してください。


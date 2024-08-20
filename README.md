# ハムスター認識🐹
[URL](https://hamster-percentage-recognition.streamlit.app/)</br>
YOLOにハムスター認識がなかったため、作成しました。
どのくらいハムスターか表示してくれます。

#### 作成にあたり、参考・使用したサイトです。
- データセット：[Roboflow](https://universe.roboflow.com/)
- 画像認識: [yolov8n](https://github.com/ultralytics/ultralytics)
- [YOLOトレーニング資料](https://docs.ultralytics.com/ja/tasks/detect/)
- [【YOLOv8で学習→物体検出】楽に学習データを用意して好きなものを検出してみよう](https://qiita.com/ysv/items/2bc7fe4f927fa2c10156)

#### 感想
ハムスターの認識がなぜ公式に存在しないのか、デモを起こしそうになりました。
データセットとして始めは**fiftyone**や**open-images-v7**を用いようとしましたが、yolov8nの形式に合わせることが大変だったため、**Roboflow**を使用させていただきました。ハムスター認識に力を入れすぎて、程度しか表示するようにしかしていないです。はむううううううううううううううううううううううううう

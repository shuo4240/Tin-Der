# AI 音樂生成與風格辨認
本專案主要目的為透過HuggingFace 的 MusicGen 模型生成音樂(驗證集)， 並使用CNN 搭配 Transformer 建立的分類模型來判別音樂種類，模型使用的訓練集為[GTZAN](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)


---

### 功能特色
- **語言**：Python 3
- **用途**：利用分類模型判別音樂種類
- **特色**：
     - 透過prompt從 MusicGen 中產生特定風格的音樂
     - 建立可自動判別音樂風格的模型


### 安裝要求
請使用 **Python 3.8+** 的環境（建議使用 [Google Colab](https://colab.research.google.com/)），並安裝以下必要套件：
```bash
pip install transformers==4.37.2 accelerate torchaudio --quiet
pip install scipy librosa soundfile tensorflow tf-keras natsort
pip install natsort kaggle

### 模型架構說明：CNN + Transformer 混合網路

- **CNN**：提取音訊影像的局部特徵
- **Transformer**：補足 CNN 無法建模的長期依賴（時間序列記憶）

輸入格式：`(batch_size, 173, 89, 1)`

| 層級 | 類型與說明 |
|------|------------|
| Layer 1 | `Input(shape=(173, 89, 1))` - 音訊時頻圖輸入 |
| Layer 2 | `Conv2D(8) + MaxPooling2D + BatchNormalization` - 初步影像特徵抽取 |
| Layer 3 | `Reshape((86, 352))` - 攤平通道與頻率以符合 Transformer 輸入格式 |
| Layer 4 | `MultiHeadAttention(num_heads=1, key_dim=16)` - 捕捉時間依賴關係 |
| Layer 5 | `Add + LayerNormalization` - 殘差連接與正規化（Transformer 標準結構） |
| Layer 6 | `Dense(352) + Add + LayerNorm` - Feed Forward Network |
| Layer 7 | `GlobalAveragePooling1D()` - 聚合時間維度資訊 |
| Layer 8 | `Dense(32) + Dropout(0.5)` - 特徵壓縮與正則化 |
| Layer 9 | `Dense(10, activation='softmax')` - 多分類輸出（10 種音樂風格） |

📌 最終模型包含 CNN 的局部感知力與 Transformer 的全局依賴能力，特別適合處理結構複雜的音訊資料。

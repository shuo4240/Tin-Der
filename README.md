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

![image](https://github.com/AndyXu66/MLfinal/blob/main/image/initial_screen_md.png)

<h3 align="center">
    <p>A chance to fall in love with music you never knew you needed.</p>
</h3>

## Usage Instructions
🔘 Start
- Click Start to launch the application.
- Enter the main interface to begin the music recommendation process.

🔘 Information
- View the model’s training results and music classification performance.
- Displays the model's classification accuracy to help assess overall performance.
- Shows a confusion matrix to visualize prediction versus actual labels, identifying common misclassifications.

🔘 Q&A Interaction
- Answer a short set of questions to help determine your preferred music style.
- Based on your responses, the system will recommend 10 songs matching the selected genre.

🔘 Preference Tagging
- For each recommended song, mark it as "Liked" or "Disliked".
- A personalized playlist will be generated based on your preferences.

🔘 Playlist Management
- Your final personalized playlist will be displayed.
- You can remove songs you dislike.
- You can also download the songs you like to your device.

📁 Source File
- To launch the UI, run the file: **tinder_music_final.py**

## GTZAN Genre Classification

This code is designed to run on [Google Colab](https://colab.research.google.com/drive/1P2eNgk16cU3vyIxCBVW-3XeklvCDTMQf?usp=sharing), and is implemented in the notebook file **GTZAN_Genre_Collection.ipynb**. 

🔘 Dataset
- Dataset used: GTZAN Genre Collection
- Genres include: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, and rock.

🔘 Feature Extraction
- Extracts Mel spectrograms from audio files.
- Preprocessing includes audio segmentation and normalization.

🔘 Model Training
- Combines CNN for feature extraction and Transformer for temporal modeling.
- The trained model is stored in the **music_models/cnn_transformer_model.h5** directory.

🔘 Music Generation
- Music is generated using a model accessed via [Hugging Face Transformers](https://github.com/huggingface/transformers)
- Generated audio samples are saved in the **music/** directory.

🔘 Classification of Generated Music
- After generation, the new audio files are passed through the trained model, **cnn_transformer_model.h5**, to determine their predicted genres.











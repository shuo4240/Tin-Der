from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import os

class Ui_TinderMusicApp(object):
    def play_selected_track(self, item):
        text = item.text()
        # 移除前面的 ▶️ 和後面的 ⬇️ ❌ ⏸️ 等符號，只保留 track_name
        track_name = text.replace("▶️", "").split()[0].strip()
        filepath = f"music/{track_name}.wav"
        print(f"[DEBUG] 播放清單中選擇的：{filepath}")
        self.play_music(filepath)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 800)

        #字顯示
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 500, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)           
        self.label.setFont(font)

        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(0, 120, 600, 60))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)           
        self.label.setFont(font)

        #image
        self.initial_label = QtWidgets.QLabel(Form)
        self.initial_label.setGeometry(QtCore.QRect(0, 0, 600, 800))  # 根據你視窗大小調整
        self.initial_label.setPixmap(QtGui.QPixmap("image/initial_screen.png"))
        self.initial_label.setScaledContents(True)  # 自動縮放圖片以符合 label
        self.initial_label.setObjectName("initial_image")

        self.question1_image = QtWidgets.QLabel(Form)
        self.question1_image.setGeometry(QtCore.QRect(-12, 60, 624, 360))
        self.question1_image.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = QtGui.QPixmap("image/question1.png")
        scaled_pixmap = pixmap.scaled(624, 360, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.question1_image.setPixmap(scaled_pixmap)
        self.question1_image.setObjectName("question1_image")
        self.question1_image.hide()

        self.training_image = QtWidgets.QLabel(Form)
        self.training_image.setAlignment(QtCore.Qt.AlignCenter)
        pix_train = QtGui.QPixmap("image/training_result.jpg")
        scaled_train = pix_train.scaled(500, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.training_image.setPixmap(scaled_train)
        w_train, h_train = scaled_train.width(), scaled_train.height()
        self.training_image.setGeometry(50, 60, w_train, h_train)
        self.training_image.hide()

        self.accuracy_image = QtWidgets.QLabel(Form)
        self.accuracy_image.setAlignment(QtCore.Qt.AlignCenter)
        pix_acc = QtGui.QPixmap("image/Classification_accuracy.jpg")
        scaled_acc = pix_acc.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.accuracy_image.setPixmap(scaled_acc)
        w_acc, h_acc = scaled_acc.width(), scaled_acc.height()
        self.accuracy_image.setGeometry(100, 60, w_acc, h_acc)
        self.accuracy_image.hide()

        self.confusion_image = QtWidgets.QLabel(Form)
        self.confusion_image.setAlignment(QtCore.Qt.AlignCenter)
        pix_conf = QtGui.QPixmap("image/Classification_confusion.jpg")
        scaled_conf = pix_conf.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.confusion_image.setPixmap(scaled_conf)
        w_conf, h_conf = scaled_conf.width(), scaled_conf.height()
        self.confusion_image.setGeometry(100,  440, w_conf, h_conf)
        self.confusion_image.hide()

        #button
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(200, 450, 200, 40))
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Start 🎶")

        self.information_button = QtWidgets.QPushButton(Form)
        self.information_button.setGeometry(QtCore.QRect(200, 510, 200, 40))
        self.information_button.setObjectName("information_button")
        self.information_button.setText("Information ℹ️")

        self.btn_training = QtWidgets.QPushButton(Form)
        self.btn_training.setGeometry(QtCore.QRect(200, 50, 200, 40))
        self.btn_training.setText("📊 Training Results")
        self.btn_training.hide()
        self.btn_training.clicked.connect(self.show_training)

        self.btn_prediction = QtWidgets.QPushButton(Form)
        self.btn_prediction.setGeometry(QtCore.QRect(200, 110, 200, 40))
        self.btn_prediction.setText("📊 Classification Results")
        self.btn_prediction.hide()
        self.btn_prediction.clicked.connect(self.show_prediction)

        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setGeometry(100, 20, 200, 40)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.hide()

        self.back_button = QtWidgets.QPushButton("🔙 Back to cover", Form)
        self.back_button.setGeometry(10, 5, 200, 30)
        self.back_button.hide()
        self.back_button.clicked.connect(self.back_to_cover)

        self.button_chill = QtWidgets.QPushButton(Form)
        self.button_chill.setGeometry(QtCore.QRect(220, 500, 80, 40))
        self.button_chill.hide()

        self.button_sad = QtWidgets.QPushButton(Form)
        self.button_sad.setGeometry(QtCore.QRect(340, 500, 80, 40))
        self.button_sad.hide()

        self.button_lyrical = QtWidgets.QPushButton(Form)
        self.button_lyrical.setGeometry(QtCore.QRect(220, 500, 80, 40))
        self.button_lyrical.hide()

        self.button_upbeat = QtWidgets.QPushButton(Form)
        self.button_upbeat.setGeometry(QtCore.QRect(340, 500, 80, 40))
        self.button_upbeat.hide()

        self.button_heartfelt = QtWidgets.QPushButton(Form)
        self.button_heartfelt.setGeometry(QtCore.QRect(220, 500, 80, 40))
        self.button_heartfelt.hide()

        self.button_thunderous = QtWidgets.QPushButton(Form)
        self.button_thunderous.setGeometry(QtCore.QRect(340, 500, 80, 40))
        self.button_thunderous.hide()

        self.button_restart = QtWidgets.QPushButton(Form)
        self.button_restart.setGeometry(QtCore.QRect(270, 700, 100, 40))# 580, 600
        self.button_restart.setText("🔄 重選")
        self.button_restart.hide()

        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(220, 500, 160, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.hide()

        self.summary_box = QtWidgets.QGroupBox(Form)
        self.summary_box.setGeometry(QtCore.QRect(150, 100, 300, 150))
        self.summary_box.setTitle("你的選擇")
        self.summary_box.hide()
        self.summary_layout = QtWidgets.QVBoxLayout(self.summary_box)

        self.label_emotion = QtWidgets.QLabel(self.summary_box)
        self.label_genre = QtWidgets.QLabel(self.summary_box)
        self.label_type = QtWidgets.QLabel(self.summary_box)
        for lbl in [self.label_emotion, self.label_type, self.label_genre]:
            lbl.setFixedWidth(260)
            lbl.setFixedHeight(30)
            lbl.setAlignment(QtCore.Qt.AlignLeft)
            lbl.setWordWrap(True)
            self.summary_layout.addWidget(lbl)

        self.button_confirm = QtWidgets.QPushButton(Form)
        self.button_confirm.setGeometry(QtCore.QRect(220, 500, 80, 40))
        self.button_confirm.setText("✅ 是")
        self.button_confirm.hide()

        self.button_decline = QtWidgets.QPushButton(Form)
        self.button_decline.setGeometry(QtCore.QRect(340, 500, 80, 40))
        self.button_decline.setText("❌ 否")
        self.button_decline.hide()

        self.music_label = QtWidgets.QLabel(Form)
        self.music_label.setGeometry(QtCore.QRect(150, 300, 300, 30))
        self.music_label.setAlignment(QtCore.Qt.AlignCenter)
        self.music_label.hide()

        self.list_widget = QtWidgets.QListWidget(Form)
        self.list_widget.setGeometry(QtCore.QRect(100, 340, 400, 300))
        self.list_widget.hide()

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.stage = 0 
        self.emotion = None
        self.genre = None
        self.type = None

        self.chill_genres = ['jazz', 'pop', 'classical', 'reggae', 'disco']
        self.sad_genres = ['blues', 'metal', 'country', 'rock', 'hiphop']
        self.lyrical_type = ['jazz', 'classical']
        self.upbeat_type = ['pop', 'reggae', 'disco']
        self.heartfelt_type = ['blues', 'country', 'hiphop']
        self.thunderous_type = ['metal', 'rock']

        self.preview_tracks = [f"blues_{i+1}" for i in range(10)]
        self.liked_tracks = []
        self.current_index = 0
        self.track_index = 0

        self.player = QMediaPlayer()

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Yes).setText("👍")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.No).setText("👎")

        self.information_button.clicked.connect(self.show_information)
        self.buttonBox.accepted.connect(self.handle_yes)
        self.buttonBox.rejected.connect(self.handle_no)
        self.start_button.clicked.connect(self.start_app)
        self.button_chill.clicked.connect(self.choose_chill)
        self.button_sad.clicked.connect(self.choose_sad)
        self.button_lyrical.clicked.connect(lambda: self.choose_type('lyrical'))
        self.button_upbeat.clicked.connect(lambda: self.choose_type('upbeat'))
        self.button_heartfelt.clicked.connect(lambda: self.choose_type('heartfelt'))
        self.button_thunderous.clicked.connect(lambda: self.choose_type('thunderous'))
        self.button_restart.clicked.connect(self.restart_app)
        self.button_confirm.clicked.connect(self.type_music)
        self.button_decline.clicked.connect(self.restart_app)
        self.list_widget.itemClicked.connect(self.play_selected_track)
    
        self.retranslateUi(Form)
        self.update_stage()

    def show_information(self):
        self.initial_label.hide()
        self.start_button.hide()
        self.information_button.hide()

        self.info_label.show()
        self.back_button.show()
        self.btn_training.show()
        self.btn_prediction.show()

    def back_to_cover(self):
        for w in [self.info_label, self.back_button,self.button_chill,
                  self.btn_training, self.btn_prediction,self.button_sad,
                  self.training_image, self.accuracy_image,self.confusion_image,
                  self.list_widget, self.music_label,self.question1_image,
                  self.buttonBox, self.image_label,self.information_button,
                  self.summary_box, self.button_confirm,self.initial_label,
                  self.button_decline, self.button_restart]:
            w.hide()
        # 重設到最初狀態
        self.player.stop()
        self.initial_label.show()
        self.start_button.show()
        self.information_button.show()

    def show_training(self):
        self.btn_training.hide()
        self.btn_prediction.hide()
        self.info_label.hide()
        self.training_image.show()
        self.back_button.show()

    def show_prediction(self):
        self.btn_training.hide()
        self.btn_prediction.hide()
        self.info_label.hide()
        self.accuracy_image.show()
        self.confusion_image.show()
        self.back_button.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Music Tinder"))
        self.button_chill.setText(_translate("Form", "Chill"))
        self.button_sad.setText(_translate("Form", "Sad"))
        self.button_lyrical.setText(_translate("Form", "Lyrical"))
        self.button_upbeat.setText(_translate("Form", "Upbeat"))
        self.button_heartfelt.setText(_translate("Form", "Heartfelt"))
        self.button_thunderous.setText(_translate("Form", "Thunderous"))


    def play_music(self, filepath):
        self.player.stop()  # 防止重複播放卡住
        if os.path.exists(filepath):
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filepath)))
            self.player.play()


    def start_app(self):
        self.initial_label.hide()
        self.start_button.hide()
        self.question1_image.hide()
        self.information_button.hide()
        self.stage = 1
        self.update_stage()

    def update_stage(self):
    # Reset UI
        for btn in [self.button_chill, self.button_sad,
                    self.button_lyrical, self.button_upbeat,
                    self.button_heartfelt, self.button_thunderous]:
            btn.hide()
        self.label.hide()
        self.image_label.hide()
        self.question1_image.hide()
        self.music_label.hide()
        self.buttonBox.hide()
        self.summary_box.hide()
        self.button_confirm.hide()
        self.button_decline.hide()
        self.list_widget.hide()

        if self.stage == 1:
            self.question1_image.show()
            self.button_chill.show()
            self.button_sad.show()

        elif self.stage == 2:
            self.label.setText("選擇你想要的音樂類型：")
            self.label.show()
            if self.emotion == 'chill':
                self.button_lyrical.show()
                self.button_upbeat.show()
            elif self.emotion == 'sad':
                self.button_heartfelt.show()
                self.button_thunderous.show()

        elif self.stage == 3:
            genre = self.options[self.current_index]
            self.label.setText(f"喜歡這種風格嗎？ {genre}")
            self.label.show()
            self.image_label.setText(genre)
            self.image_label.show()
            self.buttonBox.show()
            self.play_music(f"samples/{genre}_sample.wav")

        elif self.stage == 4:
            self.show_track()

    def choose_chill(self):
        self.emotion = 'chill'
        self.stage = 2
        self.update_stage()

    def choose_sad(self):
        self.emotion = 'sad'
        self.stage = 2
        self.update_stage()

    def choose_type(self, selected_type):
        self.genre_type = selected_type
        if selected_type == 'lyrical':
            self.options = self.lyrical_type
        elif selected_type == 'upbeat':
            self.options = self.upbeat_type
        elif selected_type == 'heartfelt':
            self.options = self.heartfelt_type
        elif selected_type == 'thunderous':
            self.options = self.thunderous_type
        self.type = selected_type
        self.current_index = 0
        self.stage = 3
        self.update_stage()

    def handle_yes(self):
        if self.stage == 3:
            self.genre = self.options[self.current_index]
            self.preview_tracks = [f"{self.genre}_{i+1}" for i in range(10)]
            self.show_summary()

    def handle_no(self):
        if self.stage == 3:
            self.current_index += 1
            if self.current_index >= len(self.options):
                self.label.setText("沒找到喜歡的風格，請重新開始")
                self.image_label.setText("")
                self.buttonBox.setDisabled(True)
                self.button_restart.show()
            else:
                self.update_stage()

    def show_summary(self):
        self.stage = 99
        self.buttonBox.hide()
        self.image_label.hide()
        self.label_emotion.clear()
        self.label_type.clear()
        self.label_genre.clear()
        self.summary_box.show()
        self.label.setText("請確認你的選擇：")
        self.label_emotion.setText(f"情緒：{self.emotion}")
        self.label_type.setText(f"類型：{self.type}")
        self.label_genre.setText(f"風格：{self.genre}")
        self.button_confirm.show()
        self.button_decline.show()

    def restart_app(self):
        self.stage = 1
        self.current_index = 0
        self.track_index = 0
        self.emotion = None
        self.genre = None
        self.type = None
        self.liked_tracks.clear()
        self.buttonBox.setDisabled(False)
        self.player.stop()
        self.update_stage()


    def type_music(self):
        self.stage = 4
        self.track_index = 0
        self.summary_box.hide()
        self.button_confirm.hide()
        self.button_decline.hide()
        self.label.setText("試聽音樂 🎧，喜歡就按👍")
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        self.buttonBox.accepted.connect(self.like_track)
        self.buttonBox.rejected.connect(self.next_track)
        self.show_track()
        
    def refresh_track_list(self):
        self.list_widget.clear()
        for track in self.liked_tracks:
            item = QtWidgets.QListWidgetItem()
            widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(5, 0, 5, 0)

            # 標題/播放區
            label = QtWidgets.QLabel(track)
            label.setMinimumWidth(150)
            label.mousePressEvent = lambda e, name=track: self.play_music(f"music/{name}.wav")

            # 下載按鈕
            btn_download = QtWidgets.QPushButton("⬇️")
            btn_download.setFixedSize(30, 30)
            btn_download.clicked.connect(lambda _, name=track: self.download_track(name))

            # 刪除按鈕
            btn_delete = QtWidgets.QPushButton("❌")
            btn_delete.setFixedSize(30, 30)
            btn_delete.clicked.connect(lambda _, name=track: self.delete_track(name))

            layout.addWidget(label)
            layout.addStretch()
            layout.addWidget(btn_download)
            layout.addWidget(btn_delete)

            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)


    def play_selected_track(self, item):
        text = item.text()
        if '⬇️' in text or '❌' in text:
            track_name = text.split('⬇️')[0].strip()
            if '⬇️' in text:
                self.download_track(track_name)
            elif '❌' in text:
                self.delete_track(track_name)
        else:
            track_name = text.strip()
            self.play_music(f"music/{track_name}.wav")

    def download_track(self, track_name):
        source_path = f"music/{track_name}.wav"
        if os.path.exists(source_path):
            save_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                None, "儲存音樂", f"{track_name}.wav", "音樂檔案 (*.wav)")
            if save_path:
                try:
                    import shutil
                    shutil.copyfile(source_path, save_path)
                    QtWidgets.QMessageBox.information(None, "下載成功", f"已下載：{save_path}")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(None, "錯誤", f"下載失敗：{e}")
        else:
            QtWidgets.QMessageBox.warning(None, "找不到檔案", f"{source_path} 不存在")

    def delete_track(self, track_name):
        if track_name in self.liked_tracks:
            self.liked_tracks.remove(track_name)
            self.refresh_track_list()

    def show_track(self):
        if self.track_index >= len(self.preview_tracks):
            self.player.stop()
            self.label.setText("你的音樂清單 🎵")
            self.image_label.hide()
            self.music_label.hide()
            self.buttonBox.hide()
            self.refresh_track_list()  # 用 refresh 取代手動建構 list_widget
            self.list_widget.show()
            self.back_button.show()
        else:
            track_name = self.preview_tracks[self.track_index]
            self.music_label.setText(f"🎵 {track_name}")
            self.music_label.show()
            self.image_label.setText("♪ ♫ ♪")
            self.image_label.show()
            self.buttonBox.show()
            self.play_music(f"music/{track_name}.wav")

    def next_track(self):
        self.track_index += 1
        self.show_track()

    def like_track(self):
        track_name = self.preview_tracks[self.track_index]
        self.liked_tracks.append(track_name)
        self.next_track()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TinderMusicApp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

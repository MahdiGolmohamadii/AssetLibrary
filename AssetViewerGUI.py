import datetime
import sys
import json

from PySide6 import QtWidgets, QtCore, QtGui


class assetViewDialog(QtWidgets.QDialog):
    FILE_PASS = './Assets'
    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = IMAGE_WIDTH / 1.77778

    FILE_FILTERS = '*.png;; *.jpg;; *.jpeg;; All Files (*.*)'
    selected_filter = '*.jpg'

    def __init__(self):
        super(assetViewDialog, self).__init__(parent=None)
        self.setWindowTitle('Asset Viewer')
        self.setMinimumSize(300, 500)

        self.json_file_pass = self.FILE_PASS + '/assets.json'

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.load_asset_from_json()

    def create_widgets(self):
        # Asset list DropDown widgets
        self.asset_list_label = QtWidgets.QLabel('asset list')
        self.asset_list_cb = QtWidgets.QComboBox()
        # image Widgets
        self.preview_image_label = QtWidgets.QLabel()
        self.preview_image_label.setFixedHeight(self.IMAGE_HEIGHT)
        # info widgets
        self.name_le = QtWidgets.QLineEdit()
        self.description_pt = QtWidgets.QPlainTextEdit()
        self.description_pt.setFixedHeight(150)
        self.creator_le = QtWidgets.QLineEdit()
        self.created_date_le = QtWidgets.QLineEdit()
        self.modified_date_le = QtWidgets.QLineEdit()
        #set infor widgets to read only
        self.name_le.setReadOnly(True)
        self.description_pt.setReadOnly(True)
        self.description_pt.setReadOnly(True)
        self.creator_le.setReadOnly(True)
        self.created_date_le.setReadOnly(True)
        self.modified_date_le.setReadOnly(True)
        # buttons
        self.edit_bt = QtWidgets.QPushButton('edit')
        self.save_changes_btn = QtWidgets.QPushButton('save')
        self.save_changes_btn.setVisible(False)
        self.cancel_btn = QtWidgets.QPushButton('cancel')
        self.cancel_btn.setVisible(False)

    def create_layout(self):
        # Asset list DropDown
        asset_list_layout = QtWidgets.QHBoxLayout()
        asset_list_layout.addStretch()
        asset_list_layout.addWidget(self.asset_list_label)
        asset_list_layout.addWidget(self.asset_list_cb)
        # image
        preview_image_layout = QtWidgets.QHBoxLayout()
        preview_image_layout.addWidget(self.preview_image_label)
        # form
        info_form_layout = QtWidgets.QFormLayout()
        info_form_layout.addRow('Name:', self.name_le)
        info_form_layout.addRow('Description', self.description_pt)
        info_form_layout.addRow('Creator', self.creator_le)
        info_form_layout.addRow('Created: ', self.created_date_le)
        info_form_layout.addRow('Modified', self.modified_date_le)

        # buttons
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.save_changes_btn)
        button_layout.addWidget(self.edit_bt)
        button_layout.addWidget(self.cancel_btn)




        # main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(asset_list_layout)
        main_layout.addLayout(preview_image_layout)
        main_layout.addLayout(info_form_layout)
        main_layout.addLayout(button_layout)


    def create_connections(self):
        self.asset_list_cb.currentTextChanged.connect(self.refresh_asset_details)

        self.edit_bt.clicked.connect(self.edit_asset_details)
        self.save_changes_btn.clicked.connect(self.save_changes)
        self.cancel_btn.clicked.connect(self.edit_cancelled)


    def edit_cancelled(self):
        self.refresh_asset_details()
        self.set_edit_mode(False)
    def load_asset_from_json(self):
        with open(self.json_file_pass, 'r') as file_for_read:
            self.assets = json.load(file_for_read)
        for asset_code in self.assets:
            self.asset_list_cb.addItem(asset_code)

    def save_assets_to_json(self):
        with open(self.json_file_pass, 'w') as file_for_write:
            json.dump(self.assets, file_for_write, indent=4)

    def set_preview_image(self, file_name):
        img_path = self.FILE_PASS + '/{0}'.format(file_name)
        file_info = QtCore.QFileInfo(img_path)
        if file_info.exists():
            image = QtGui.QImage(img_path)
            image = image.scaled(self.preview_image_label.width(), self.preview_image_label.height(),
                                 QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            pixmap = QtGui.QPixmap()
            pixmap.convertFromImage(image)

        else:
            print('file not found')
            pixmap = QtGui.QPixmap(self.preview_image_label.size())
            pixmap.fill(QtCore.Qt.transparent)

        self.preview_image_label.setPixmap(pixmap)

    def refresh_asset_details(self):
        asset_code = self.asset_list_cb.currentText()
        current_asset = self.assets[asset_code]

        self.name_le.setText(current_asset['name'])
        self.description_pt.setPlainText(current_asset['description'])
        self.creator_le.setText(current_asset['creator'])
        self.created_date_le.setText(current_asset['created'])
        self.modified_date_le.setText(current_asset['modified'])

        self.set_preview_image(current_asset['image_path'])
    def edit_asset_details(self):
        self.set_edit_mode(True)

    def set_edit_mode(self, state):

        #change read only fields
        self.name_le.setReadOnly(not state)
        self.description_pt.setReadOnly(not state)
        self.description_pt.setReadOnly(not state)
        self.creator_le.setReadOnly(not state)
        self.created_date_le.setReadOnly(not state)
        self.modified_date_le.setReadOnly(not state)

        self.save_changes_btn.setVisible(state)
        self.edit_bt.setVisible(not state)
        self.cancel_btn.setVisible(state)


    def save_changes(self):
        print('TODO:: sae changes made to asset')
        self.set_edit_mode(False)

        modified = datetime.datetime.now()
        self.modified_date_le.setText(modified.strftime("%Y/%m/%d %H:%M:%S"))

        asset_code = self.asset_list_cb.currentText()
        curr_asset = self.assets[asset_code]
        curr_asset['name'] = self.name_le.text()
        curr_asset['description'] = self.description_pt.toPlainText()
        curr_asset['modified'] = self.modified_date_le.text()

        self.save_assets_to_json()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('windows'))

    window = assetViewDialog()
    window.show()
    app.exec()

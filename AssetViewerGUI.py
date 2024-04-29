import sys

from PySide6 import QtWidgets


class assetViewDialog(QtWidgets.QDialog):

    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = IMAGE_WIDTH / 1.77778


    def __init__(self):
        super(assetViewDialog, self).__init__(parent=None)
        self.setWindowTitle('Asset Viewer')
        self.setMinimumSize(300,500)

        self.creat_widgets()
        self.creat_layout()
        self.creat_connections()


    def creat_widgets(self):
        # Asset list DropDown widgets
        self.asset_list_label = QtWidgets.QLabel('asset list')
        self.asset_list_cb = QtWidgets.QComboBox()
        #image Widgets
        self.preview_image_label = QtWidgets.QLabel()
        self.preview_image_label.setFixedHeight(self.IMAGE_HEIGHT)
        #info widgets
        self.name_le = QtWidgets.QLineEdit()
        self.description_pt = QtWidgets.QPlainTextEdit()
        self.description_pt.setFixedHeight(150)
        self.creator_le = QtWidgets.QLineEdit()
        self.created_date_le = QtWidgets.QLineEdit()
        self.modified_date_le = QtWidgets.QLineEdit()
        #buttons
        self.ok_bt = QtWidgets.QPushButton('ok')
        self.cancel_btn = QtWidgets.QPushButton('cancel')

    def creat_layout(self):
        #Asset list DropDown
        asset_list_layout = QtWidgets.QHBoxLayout()
        asset_list_layout.addStretch()
        asset_list_layout.addWidget(self.asset_list_label)
        asset_list_layout.addWidget(self.asset_list_cb)
        #image
        preview_image_layout = QtWidgets.QHBoxLayout()
        preview_image_layout.addWidget(self.preview_image_label)
        #form
        info_form_layout = QtWidgets.QFormLayout()
        info_form_layout.addRow('Name:', self.name_le)
        info_form_layout.addRow('Description', self.description_pt)
        info_form_layout.addRow('Creator', self.creator_le)
        info_form_layout.addRow('Created: ', self.created_date_le)
        info_form_layout.addRow('Modified', self.modified_date_le)

        #buttons
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_bt)
        button_layout.addWidget(self.cancel_btn)

        #main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(asset_list_layout)
        main_layout.addLayout(preview_image_layout)
        main_layout.addLayout(info_form_layout)
        main_layout.addLayout(button_layout)

    def creat_connections(self):
        pass





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('windows'))

    window = assetViewDialog()
    window.show()
    app.exec()


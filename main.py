from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget
import sys



from database import Database

# Hàm để căn cửa sổ ra giữa màn hình
def center_widget(widget):
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    widget_geometry = widget.frameGeometry()
    widget_geometry.moveCenter(screen_geometry.center())
    widget.move(widget_geometry.topLeft())

# Cửa sổ đăng nhập
class DangNhap(QMainWindow):
    def __init__(self):
        super(DangNhap, self).__init__()
        uic.loadUi("DangNhap.ui", self)
        center_widget(self)
        self.btnLogin.clicked.connect(self.DangNhap)

    def DangNhap(self):
        username = self.txtName.text()
        password = self.txtPass.text()
        if username == "1" and password == "1":
            widget.setFixedWidth(981)
            widget.setFixedHeight(728)
            center_widget(widget)
            widget.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "Thông báo", "Sai tên đăng nhập hoặc mật khẩu")

# Cửa sổ Trang Chủ
class TrangChu(QMainWindow):
    def __init__(self):
        super(TrangChu, self).__init__()
        uic.loadUi("TrangChu.ui", self)
        widget.setFixedWidth(1081)
        widget.setFixedHeight(900)
        center_widget(self)

        self.btnQuanLyNguoiDung.clicked.connect(self.QuanLyNguoiDung)
        self.btnQuanLySanPham.clicked.connect(self.QuanLySanPham)
        self.btnQuanlyDichVu.clicked.connect(self.QuanlyDichVu)

    def QuanLyNguoiDung(self):
        widget.setFixedWidth(1215)
        widget.setFixedHeight(721)
        center_widget(widget)
        widget.setCurrentIndex(2)

    def QuanLySanPham(self):
        widget.setFixedWidth(1215)
        widget.setFixedHeight(721)
        center_widget(widget)
        widget.setCurrentIndex(3)

    def QuanlyDichVu(self):
        widget.setFixedWidth(1079)
        widget.setFixedHeight(561)
        center_widget(widget)
        widget.setCurrentIndex(4)


# Cửa sổ Quản Lý Người Dùng
class QuanLyNguoiDung(QMainWindow):
    def __init__(self):
        super(QuanLyNguoiDung, self).__init__()
        uic.loadUi("QuanLyNguoiDung.ui", self)
        center_widget(self)
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')

        # Kết nối sự kiện khi chọn một dòng trong tableWidget
        self.tableWidget.itemSelectionChanged.connect(self.select_user)

        self.btnThem.clicked.connect(self.Them_user)
        self.btnSua.clicked.connect(self.Sua_user)
        self.btnXoa.clicked.connect(self.Xoa)
        self.btnThoat.clicked.connect(self.QuayLai)
        self.load_user()


    def load_user(self):
        try:
            data = self.db.read_user()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu phim: {str(e)}")

    def select_user(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return

        try:
            id = self.tableWidget.item(selected_row, 0).text()
            username = self.tableWidget.item(selected_row, 1).text()
            sdt = self.tableWidget.item(selected_row, 2).text()
            email = self.tableWidget.item(selected_row, 3).text()
            diachi = self.tableWidget.item(selected_row, 4).text()
            luong = self.tableWidget.item(selected_row, 5).text()
            vitri = self.tableWidget.item(selected_row, 6).text()
            quyen = self.tableWidget.item(selected_row, 7).text()
            ngaysinh = self.tableWidget.item(selected_row, 8).text()

            self.txtHoTen.setText(username)
            self.txtDienThoai.setText(sdt)
            self.txtEmail.setText(email)
            self.txtDiaChi.setText(diachi)
            self.txtLuong.setText(luong)
            self.txtViTri.setText(vitri)
            self.txtQuyen.setText(quyen)
            self.dateNamSinh.setDate(QtCore.QDate.fromString(ngaysinh, "yyyy-MM-dd"))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn người dùng: {str(e)}")

    def Them_user(self):
        username = self.txtHoTen.text()
        sdt = self.txtDienThoai.text()
        email = self.txtEmail.text()
        diachi = self.txtDiaChi.text()
        luong = self.txtLuong.text()
        vitri = self.txtViTri.text()
        quyen = self.txtQuyen.text()
        ngaysinh = self.dateNamSinh.date().toString("yyyy-MM-dd")

        # Kiểm tra các trường có rỗng không
        if username == "" or sdt == "" or email == "" or diachi == "" or luong == "" or vitri == "" or quyen == "":
            QMessageBox.information(self, "Thông báo", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            self.db.insert_user(username, sdt, email, diachi, luong, vitri, quyen, ngaysinh)
            QMessageBox.information(self, "Thông báo", "Đã thêm người dùng thành công.")

            self.load_user()
        except Exception as e:
            QMessageBox.information(self, "Thông báo", "Đã xảy ra lỗi khi thêm người dùng.")

    def Sua_user(self):
        selected_row = self.tableWidget.currentRow()
        id = self.tableWidget.item(selected_row, 0).text()
        username = self.txtHoTen.text()
        sdt = self.txtDienThoai.text()
        email = self.txtEmail.text()
        diachi = self.txtDiaChi.text()
        luong = self.txtLuong.text()
        vitri = self.txtViTri.text()
        quyen = self.txtQuyen.text()
        ngaysinh = self.dateNamSinh.date().toString("yyyy-MM-dd")
        self.db.update_user(id, username, sdt, email, diachi, luong, vitri, quyen, ngaysinh)
        QMessageBox.information(self, "Thông báo", "Đã cập nhật thông tin thành công.")
        self.load_user()

    def Xoa(self):
        try:
            selected_row = self.tableWidget.currentRow()
            id = self.tableWidget.item(selected_row, 0).text()
            self.db.delete_user(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa người dùng thành công.")
            self.load_user()
        except Exception as e:
            QMessageBox.information(self, "Thông báo", "Đã xảy ra lỗi khi xóa người dùng.")

    def QuayLai(self):
        widget.setCurrentIndex(1)

class QuanLySanPham(QMainWindow):
    def __init__(self):
        super(QuanLySanPham, self).__init__()
        uic.loadUi("QuanLySanPham.ui", self)
        center_widget(self)
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')  # Tìm tableWidget trong UI

        # Kết nối sự kiện khi chọn một dòng trong tableWidget
        self.tableWidget.itemSelectionChanged.connect(self.select_row)

        self.btnThem.clicked.connect(self.Them)
        self.btnSua.clicked.connect(self.Sua)
        self.btnXoa.clicked.connect(self.Xoa)
        self.btnThoat.clicked.connect(self.QuayLai)
        self.load_product()

    def load_product(self):
        try:
            data = self.db.read_product()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu sản phẩm: {str(e)}")

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return

        try:
            id = self.tableWidget.item(selected_row, 0).text()
            ten_san_pham = self.tableWidget.item(selected_row, 1).text()
            loai_san_pham = self.tableWidget.item(selected_row, 2).text()
            gia = self.tableWidget.item(selected_row, 3).text()
            mo_ta = self.tableWidget.item(selected_row, 4).text()
            so_luong = self.tableWidget.item(selected_row, 5).text()
            chat_lieu = self.tableWidget.item(selected_row, 6).text()
            da_ban = self.tableWidget.item(selected_row, 7).text()

            self.txtTenSanPham.setText(ten_san_pham)
            self.txtLoaiSanPham.setText(loai_san_pham)
            self.txtGia.setText(gia)
            self.txtMoTa.setText(mo_ta)
            self.txtSoLuongSanPham.setText(so_luong)
            self.txtChatLieu.setText(chat_lieu)
            self.txtDaBan.setText(da_ban)

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn sản phẩm: {str(e)}")
    def Them(self):
        ten_san_pham = self.txtTenSanPham.text()
        loai_san_pham = self.txtLoaiSanPham.text()
        gia = self.txtGia.text()
        mo_ta = self.txtMoTa.text()
        so_luong = self.txtSoLuongSanPham.text()
        chat_lieu = self.txtChatLieu.text()
        da_ban = self.txtDaBan.text()

        # Kiểm tra các trường có rỗng không
        if ten_san_pham == "" or loai_san_pham == "" or gia == "" or mo_ta == "" or so_luong == "" or chat_lieu == "" or da_ban == "":
            QMessageBox.information(self, "Thông báo", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            self.db.insert_product(ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban)
            QMessageBox.information(self, "Thông báo", "Đã thêm sản phẩm thành công.")
            self.load_product()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm sản phẩm: {str(e)}")

    def Sua(self):
        selected_row = self.tableWidget.currentRow()
        id = self.tableWidget.item(selected_row, 0).text()
        ten_san_pham = self.txtTenSanPham.text()
        loai_san_pham = self.txtLoaiSanPham.text()
        gia = self.txtGia.text()
        mo_ta = self.txtMoTa.text()
        so_luong = self.txtSoLuongSanPham.text()
        chat_lieu = self.txtChatLieu.text()
        da_ban = self.txtDaBan.text()
        self.db.update_product(id, ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban)
        QMessageBox.information(self, "Thông báo", "Đã cập nhật thông tin thành công.")
        self.load_product()

    def Xoa(self):
        try:
            selected_row = self.tableWidget.currentRow()
            id = self.tableWidget.item(selected_row, 0).text()
            self.db.delete_product(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa sản phẩm thành công.")
            self.load_product()
        except Exception as e:
            QMessageBox.information(self, "Thông báo", "Đã xảy ra lỗi khi xóa sản phẩm.")

    def QuayLai(self):
        widget.setCurrentIndex(1)

class QuanLyDichVu(QMainWindow):
    def __init__(self):
        super(QuanLyDichVu, self).__init__()
        uic.loadUi("QuanLyDichVu.ui", self)
        center_widget(self)
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')  # Tìm tableWidget trong UI

        # Kết nối sự kiện khi chọn một dòng trong tableWidget
        self.tableWidget.itemSelectionChanged.connect(self.select_row)

        self.btnThem.clicked.connect(self.Them)
        self.btnSua.clicked.connect(self.Sua)
        self.btnXoa.clicked.connect(self.Xoa)
        self.btnThoat.clicked.connect(self.QuayLai)
        self.load_service()

    def load_service(self):
        try:
            data = self.db.read_service()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu dịch vụ: {str(e)}")

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return

        try:
            id = self.tableWidget.item(selected_row, 0).text()
            ten_dich_vu = self.tableWidget.item(selected_row, 1).text()
            gia = self.tableWidget.item(selected_row, 3).text()
            mo_ta = self.tableWidget.item(selected_row, 4).text()

            self.txtTenDichVu.setText(ten_dich_vu)
            self.txtGia.setText(gia)
            self.txtMoTa.setText(mo_ta)

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn dịch vụ: {str(e)}")

    def Them(self):
        ten_dich_vu = self.txtTenDichVu.text()
        gia = self.txtGia.text()
        mo_ta = self.txtMoTa.text()

        # Kiểm tra các trường có rỗng không
        if ten_dich_vu == "" or gia == "" or mo_ta == "":
            QMessageBox.information(self, "Thông báo", "Vui lòng nhập đầy đủ thông tin.")
            return
        try:
            self.db.insert_service(ten_dich_vu, gia, mo_ta)
            QMessageBox.information(self, "Thông báo", "Đã thêm dịch vụ thành công.")
            self.load_service()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm dịch vụ: {str(e)}")



    def Sua(self):
        selected_row = self.tableWidget.currentRow()
        id = self.tableWidget.item(selected_row, 0).text()
        ten_dich_vu = self.txtTenDichVu.text()
        gia = self.txtGia.text()
        mo_ta = self.txtMoTa.text()
        self.db.update_service(id, ten_dich_vu, gia, mo_ta)
        QMessageBox.information(self, "Thông báo", "Đã cập nhật thông tin thành công.")
        self.load_service()

    def Xoa(self):
        try:
            selected_row = self.tableWidget.currentRow()
            id = self.tableWidget.item(selected_row, 0).text()
            self.db.delete_service(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa dịch vụ thành công.")
            self.load_service()
        except Exception as e:
            QMessageBox.information(self, "Thông báo", "Đã xảy ra lỗi khi xóa dịch vụ.")

    def QuayLai(self):
        widget.setCurrentIndex(1)





# Khởi tạo ứng dụng
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

# Khởi tạo các cửa sổ
dangnhap_f = DangNhap()
trangchu_f = TrangChu()
quanlynguoidung_f = QuanLyNguoiDung()
quanlysanpham_f = QuanLySanPham()
quanlydichvu_f = QuanLyDichVu()

# Thêm các cửa sổ vào stacked widget
widget.addWidget(dangnhap_f)
widget.addWidget(trangchu_f)
widget.addWidget(quanlynguoidung_f)
widget.addWidget(quanlysanpham_f)
widget.addWidget(quanlydichvu_f)

# Thiết lập cửa sổ ban đầu
widget.setCurrentIndex(0)
widget.setFixedWidth(719)
widget.setFixedHeight(625)
center_widget(widget)
widget.show()

sys.exit(app.exec())



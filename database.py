import MySQLdb as mdb

class Database:
    def __init__(self):
        self.con = mdb.connect('localhost', 'root', '', 'cua_hang_thoi_trang')
        self.cur = self.con.cursor()
        print("Kết nối thành công")

    def read_user(self):
        self.cur.execute("SELECT * FROM user")
        return self.cur.fetchall()

    def insert_user(self, username, sdt, email, diachi, luong, vitri, quyen, ngaysinh):
        query = "INSERT INTO user(ten, so_dien_thoai, email, dia_chi, luong, vi_tri, quyen, ngay_sinh) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (username, sdt, email, diachi, luong, vitri, quyen, ngaysinh))
        self.con.commit()

    def update_user(self, id, username, sdt, email, diachi, luong, vitri, quyen, ngaysinh):
        query = "UPDATE user SET ten=%s, so_dien_thoai=%s, email=%s, dia_chi=%s, luong=%s, vi_tri=%s, quyen=%s, ngay_sinh=%s WHERE id=%s"
        values = (username, sdt, email, diachi, luong, vitri, quyen, ngaysinh, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_user(self, id):
        query = "DELETE FROM user WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()

    def read_product(self):
        self.cur.execute("SELECT * FROM product")
        return self.cur.fetchall()

    def insert_product(self, ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban):
        query = "INSERT INTO product(ten, loai, gia, mo_ta, so_luong_san_pham, chat_lieu, da_ban) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban))
        self.con.commit()

    def update_product(self, id, ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban):
        query = "UPDATE product SET ten=%s, loai=%s, gia=%s, mo_ta=%s, so_luong_san_pham=%s, chat_lieu=%s, da_ban=%s WHERE id=%s"
        values = (ten_san_pham, loai_san_pham, gia, mo_ta, so_luong, chat_lieu, da_ban, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_product(self, id):
        query = "DELETE FROM product WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()

    def read_service(self):
        self.cur.execute("SELECT * FROM dich_vu")
        return self.cur.fetchall()

    def insert_service(self, ten_dich_vu, gia, mo_ta):
        query = "INSERT INTO dich_vu(ten_dich_vu, gia, mo_ta) VALUES(%s, %s, %s)"
        self.cur.execute(query, (ten_dich_vu, gia, mo_ta))
        self.con.commit()

    def update_service(self, id, ten_dich_vu, gia, mo_ta):
        query = "UPDATE dich_vu SET ten_dich_vu=%s, gia=%s, mo_ta=%s WHERE id=%s"
        values = (ten_dich_vu, gia, mo_ta, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_service(self, id):
        query = "DELETE FROM dich_vu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()




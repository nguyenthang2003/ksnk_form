from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Đường dẫn lưu file Excel
FILE_PATH = "data.xlsx"

# Định nghĩa route cho trang chính
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Lấy dữ liệu từ form
        ho_ten = request.form.get("ho_ten")
        so_dien_thoai = request.form.get("so_dien_thoai")

        # Tạo dataframe với dữ liệu mới
        new_data = pd.DataFrame({
            "Họ tên": [ho_ten],
            "Số điện thoại": [so_dien_thoai]
        })

        # Kiểm tra file Excel đã tồn tại chưa
        if os.path.exists(FILE_PATH):
            # Nếu file tồn tại, append dữ liệu vào file
            existing_data = pd.read_excel(FILE_PATH)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
            updated_data.to_excel(FILE_PATH, index=False)
        else:
            # Nếu chưa có file, tạo mới và ghi dữ liệu
            new_data.to_excel(FILE_PATH, index=False)

        # Chuyển hướng về trang form sau khi lưu dữ liệu
        return redirect(url_for("index"))

    # Hiển thị trang HTML
    return render_template("index.html")

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)

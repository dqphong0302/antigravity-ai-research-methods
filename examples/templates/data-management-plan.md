# Kế Hoạch Quản Lý Dữ Liệu (Data Management Plan)

> **Mục đích:** Mô tả cách dữ liệu nghiên cứu được thu thập, xử lý, lưu trữ,
> chia sẻ và bảo quản. Nhiều quỹ tài trợ và journal yêu cầu DMP khi nộp.

---

## 1. Thông Tin Chung

| Mục | Nội dung |
|---|---|
| Tên dự án | |
| Người chịu trách nhiệm dữ liệu | |
| Ngày tạo DMP | |
| Cập nhật lần cuối | |

---

## 2. Mô Tả Dữ Liệu

### 2.1 Loại dữ liệu sẽ thu thập

| Loại | Mô tả | Định dạng | Kích thước ước tính |
|---|---|---|---|
| Khảo sát | Bảng hỏi Likert 5 mức | .csv, .xlsx | ~500 dòng |
| Phỏng vấn | Transcript bán cấu trúc | .docx, .txt | ~20 file |
| Dữ liệu thí nghiệm | Số liệu đo lường | .csv | ~1000 dòng |
| Hình ảnh/video | Quan sát thực địa | .jpg, .mp4 | ~5 GB |

### 2.2 Dữ liệu có sẵn (secondary data)
<!-- Nếu có sử dụng dữ liệu thứ cấp, mô tả nguồn và điều kiện truy cập -->

---

## 3. Thu Thập Dữ Liệu

### 3.1 Phương pháp thu thập
<!-- Mô tả quy trình cụ thể -->

### 3.2 Công cụ / phần mềm
<!-- Google Forms, Qualtrics, thiết bị đo, phần mềm ghi âm... -->

### 3.3 Kiểm soát chất lượng
- [ ] Pilot test trước khi thu chính thức
- [ ] Double entry / validation rules
- [ ] Mã hóa nhất quán (codebook có sẵn)

---

## 4. Xử Lý & Phân Tích

### 4.1 Phần mềm phân tích
<!-- Python, R, SPSS, NVivo, Atlas.ti... -->

### 4.2 Quy trình xử lý
1. Nhập dữ liệu thô vào `data/raw/`
2. Làm sạch → lưu vào `data/processed/`
3. Phân tích → lưu kết quả vào `results/`

### 4.3 Version control
- [ ] Code được quản lý bằng Git
- [ ] Data files có naming convention rõ ràng
- [ ] Mỗi lần xử lý ghi log (ngày, thay đổi, lý do)

### 4.4 Sử dụng AI trong xử lý
<!-- Mô tả AI tools nào (nếu có), cho bước nào, mức kiểm soát -->

---

## 5. Lưu Trữ & Sao Lưu

### 5.1 Trong quá trình nghiên cứu

| Vị trí | Loại dữ liệu | Tần suất sao lưu | Bảo mật |
|---|---|---|---|
| Máy tính cá nhân | Tất cả | Hàng ngày | Mật khẩu + mã hóa |
| Cloud (Google Drive) | Dữ liệu đã ẩn danh | Hàng tuần | 2FA |
| USB/External drive | Bản sao lưu đầy đủ | Hàng tháng | Mã hóa |

### 5.2 Sau khi nghiên cứu kết thúc
- Dữ liệu sẽ được lưu giữ trong: [___] năm
- Vị trí lưu trữ dài hạn: [Institutional repository / OSF / Zenodo / ...]
- Sau thời hạn: [Xóa / Lưu vĩnh viễn ở dạng ẩn danh]

---

## 6. Chia Sẻ & Công Khai (Open Science)

### 6.1 Dữ liệu có thể chia sẻ không?
- [ ] Có — công khai qua repository
- [ ] Có — theo yêu cầu (request-based)
- [ ] Không — dữ liệu nhạy cảm, không thể ẩn danh đầy đủ

### 6.2 Nếu chia sẻ

| Mục | Chi tiết |
|---|---|
| Repository | OSF / Zenodo / Figshare / GitHub |
| License | CC-BY 4.0 / CC0 / Restricted |
| DOI | Sẽ được cấp khi publish |
| Kèm theo | Data dictionary / Codebook / README |

### 6.3 FAIR Principles
- **Findable:** Dữ liệu có metadata và DOI
- **Accessible:** Truy cập qua repository công khai hoặc theo yêu cầu
- **Interoperable:** Định dạng mở (.csv, .json, .txt)
- **Reusable:** Kèm license, codebook, và documentation

---

## 7. Đạo Đức & Bảo Mật

### 7.1 Dữ liệu cá nhân
- [ ] Dữ liệu có chứa PII (Personally Identifiable Information)?
- [ ] Quy trình ẩn danh: [mô tả]
- [ ] Consent form bao phủ việc lưu trữ và chia sẻ dữ liệu?

### 7.2 Tuân thủ
- [ ] Quy định của Hội đồng Đạo đức / IRB
- [ ] Quy định của đơn vị đào tạo
- [ ] Luật bảo vệ dữ liệu cá nhân (nếu applicable)

---

## 8. Phân Công Trách Nhiệm

| Vai trò | Người phụ trách | Nhiệm vụ |
|---|---|---|
| Data steward | | Quản lý lưu trữ, backup |
| Data collector | | Thu thập, nhập liệu |
| Data analyst | | Xử lý, phân tích |
| PI / GVHD | | Phê duyệt cuối cùng |

---

> 💡 **Mẹo Antigravity:** Dùng AI để tự động sinh file `README.md` và
> `codebook.md` cho dataset trước khi public. AI rất giỏi chuyện này và
> nó thuộc vùng Xanh trong khung đèn giao thông đạo đức (Chương 16).

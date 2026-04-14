---
name: Literature Review Assistant
description: >
  Tổng hợp bài báo khoa học theo Literature Matrix. Trích xuất metadata,
  phân loại theo theme, và phát hiện research gap từ tập hợp tài liệu.
---

# Phạm vi
Skill này hỗ trợ giai đoạn **Tổng quan tài liệu** (Chương 4). Agent sẽ đọc
tài liệu đã được cung cấp (PDF text, abstract, hoặc summary) và trích xuất
thông tin có cấu trúc.

# Quy trình
1. Nhận danh sách bài báo từ User (dạng file text, abstract, hoặc link).
2. Với mỗi bài, trích xuất theo prompt chuẩn trong `prompts/extract.md`.
3. Tổng hợp thành bảng Literature Matrix.
4. Phân nhóm theo theme/methodology/variable.
5. Xác định gap dựa trên pattern thiếu trong matrix.

# Output mong đợi
- File `literature_matrix.md` chứa bảng tổng hợp.
- Danh sách 3-5 research gaps tiềm năng (có trích dẫn nguồn).

# Quy tắc cấm
- KHÔNG bịa citation. Nếu không tìm thấy thông tin → ghi "Not available".
- KHÔNG tự gán phương pháp. Nếu abstract không nêu rõ → ghi "Not stated".
- KHÔNG tóm tắt thay việc đọc. Output là trích xuất, không phải diễn giải.

# Khi gặp lỗi
- File không đọc được → Báo User, bỏ qua file đó, tiếp tục các file khác.
- Abstract quá ngắn (< 50 từ) → Đánh dấu "Insufficient data" trong matrix.

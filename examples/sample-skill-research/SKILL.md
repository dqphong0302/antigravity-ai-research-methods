---
name: Academic Literature Analyzer
description: Skill dùng để tự động trích xuất thông tin, tóm tắt và tổng hợp các bài báo khoa học trong một thư mục, hỗ trợ xây dựng Literature Matrix cho nghiên cứu.
---

# Lĩnh vực áp dụng
Skill này dành cho AI Agent (như Antigravity hoặc OpenClaw) để xử lý lượng lớn tài liệu PDF (papers) và trích xuất dữ liệu có cấu trúc. Phù hợp cho giai đoạn "Tổng quan tài liệu" (Literature Review - Chương 4).

# Nguyên tắc hoạt động
Khi User yêu cầu "tổng hợp thư mục tài liệu", bạn CHỈ ĐƯỢC PHÉP thực hiện các bước sau:
1. Quét thư mục chứa các file PDF do User cung cấp.
2. Sử dụng công cụ `run_command` để gọi script `extract_pdf_metadata.py` nhằm lấy tiêu đề, tác giả, và abstract.
3. Sử dụng prompt chuẩn trong `prompts/literature_synthesis.md` để đánh giá từng bài báo.
4. Luân phiên xử lý từng bài để tránh quá tải bộ nhớ context.
5. Sau khi quét xong toàn bộ, tổng hợp kết quả thành một bảng Literature Matrix dạng Markdown và tạo file `literature_matrix_result.md`.

# Các quy tắc cấm (Anti-hallucination)
- KHÔNG ĐƯỢC tự bịa ra nội dung (hallucinate) nếu script thông báo không đọc được file PDF.
- KHÔNG ĐƯỢC thay đổi tên tác giả hoặc năm xuất bản. Mọi metadata phải trích xuất chính xác 100% từ file gốc.
- Nếu bài báo không đề cập đến Phương pháp (Method) một cách rõ ràng, phải ghi là "Not clearly stated", tuyệt đối không tự suy diễn phương pháp dựa trên abstract.

# Kịch bản thất bại
- Nếu script extractor trả về lỗi `FileNotFoundError` hoặc rỗng, hãy báo ngay cho User biết "Không tìm thấy file hợp lệ trong đường dẫn". Dừng tiến trình.

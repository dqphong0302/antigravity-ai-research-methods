# Sample Skill Folder: Công cụ tùy chỉnh cho AI Agent trong nghiên cứu

Trong hệ sinh thái làm việc với AI Agents (như Antigravity hoặc OpenClaw), một "Skill" (kỹ năng) là một gói hướng dẫn và công cụ đặc thù giúp AI thực hiện một nhiệm vụ hẹp, chuyên sâu với độ chính xác cao. Việc sử dụng Skills giúp tách biệt tư duy của AI khi xử lý từng khâu.

Thư mục `sample-skill-research` này là một **template mẫu** minh họa cho một Skill được thiết kế để phân tích và tổng hợp số lượng lớn bài báo khoa học.

### Cấu trúc của một Skill Folder

Một skill folder chuẩn chuyên cho học thuật sẽ bao gồm các thành phần sau:

1. **`SKILL.md` (Bắt buộc)**:
   File cấu hình chính của Skill. Nó chứa Metadata (tên, mô tả ngắn gọn bằng YAML) và Markdown chỉ định rõ **phạm vi, quy tắc hoạt động, các hành vi bị cấm, và cách đón luồng lỗi**. Điều này giúp đóng khung Agent để nó không bao giờ suy diễn (hallucinate) ngoài vùng cho phép.

2. **`prompts/`**:
   Thư mục chứa các template ngữ cảnh (Prompt templates) chuẩn hóa. Viết prompt ra các file riêng biệt giúp AI giữ tính nhất quán theo đúng các chuẩn mực học thuật (vd: trích xuất theo khung IMRaD, đánh giá methodology).

3. **`scripts/`**:
   Chứa các đoạn mã nguồn công cụ (Python, Bash...) hỗ trợ AI. Thay vì AI phải tự làm những tác vụ tốn kém token và dễ sai sót (như đọc trực tiếp byte của file PDF), Agent sẽ thao tác qua Script để trích xuất thành văn bản thô cực nhanh.

### Cách ứng dụng trong Ebook "Antigravity Nghiên Cứu"
- Dành cho **Chương 4: Tổng quan tài liệu**. Khi gặp hàng chục file PDF cần làm Literature Matrix, độc giả có thể tạo một thư mục skill (sao chép từ template này), cài đặt Agent trỏ tới folder này.
- Mô hình làm việc này đưa AI từ vị trí "Chatbot chỉ biết trả lời thụ động" trở thành "Trợ lý Nghiên cứu" (Research Assistant) có thể chạy hàng loạt công việc và tuân thủ chặt đạo đức học thuật (như cấm ảo giác số liệu).

---
*Template này được thiết kế tương thích với Antigravity System và các nền tảng Agent Platform sử dụng Model Context Protocol (MCP).*

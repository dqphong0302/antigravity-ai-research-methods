# Phụ Lục E: Hướng Dẫn Kết Nối MCP (Model Context Protocol)

MCP (Model Context Protocol) là một chuẩn giao tiếp mở được thiết kế để kết nối các mô hình trí tuệ nhân tạo (AI Models) với các nguồn dữ liệu, biểu đồ, cơ sở dữ liệu nội bộ và các công cụ bên ngoài. Trong quy trình nghiên cứu Agentic của *Antigravity*, MCP là "chìa khóa" giúp AI thoát khỏi hộp đen hội thoại để chủ động gọi công cụ (ví dụ: quét PDF, tìm kiếm web, truy vấn CSDL học thuật).

Phụ lục này hướng dẫn cách kết nối và sử dụng các MCP cần thiết cho quy trình nghiên cứu.

---

## E.1 Tại Sao Phải Kết Nối MCP Trong Nghiên Cứu?

Một AI thông thường (như ChatGPT bản chuẩn) không thể tự động mở một file PDF được mã hóa trong máy tính của bạn, không thể vào thư mục dự án để làm sạch file CSV, và không có quyền lấy dữ liệu real-time từ các trang web cấm thu thập nếu không có plugin phù hợp.

**Khi tích hợp MCP, AI trở thành một Agent thực thụ:**
- **Thao tác Local:** Đọc, ghi, và sửa lỗi trực tiếp trên thư mục dự án (workspace) của bạn.
- **Sử dụng Tool Chuyên Sâu:** Tự động gọi máy chủ `Smart OCR` để quét tài liệu scan nhòe, hoặc mượn sức mạnh của `NotebookLM` để phân tích hàng loạt.
- **Tự Động Hóa:** Giảm thiểu thao tác "copy-paste" thủ công giữa các bên.

---

## E.2 Các MCP Server Thiết Yếu Cho Antigravity

Dưới đây là danh sách các MCP Server thường được sử dụng trong hệ thống Antigravity:

| Tên MCP Server | Chức Năng Cốt Lõi | Ứng dụng trong nghiên cứu |
| :--- | :--- | :--- |
| **`consensus`** | Truy vấn CSDL học thuật chuyên sâu | Tìm kiếm Literature, đối chiếu chéo (Cross-reference), trích xuất citation thực. |
| **`mcp_smart-pdf-ocr`** | Quét và nhận diện ký tự quang học | Số hóa báo cáo scan cũ, xử lý biểu đồ/bảng số liệu phức tạp trong PDF bản in. |
| **`mcp_notebooklm-mcp`** | Tương tác với Google NotebookLM | RAG tự động, tạo audio overview, tạo summary matrix cho hàng chục papers cùng lúc. |
| **`mcp_perplexity`** | Web-grounded reasoning | Kiểm chứng Web theo thời gian thực (Real-time fact-checking). |
| **`mcp_playwright`** | Tự động hóa trình duyệt web | Scrape dữ liệu Mở (GSO, World Bank), chụp ảnh lưu vết bằng chứng. |

---

## E.3 Xử Lý Sự Cố Thường Gặp (Troubleshooting)

- **Lỗi "Command not found" hoặc "Server disconnected":**
  Kiểm tra xem bạn đã cài đặt môi trường chạy (Node.js cho file `.js`, Python cho module `.py`) chưa. Đảm bảo đường dẫn (path) trong block `args` là đường dẫn tuyệt đối chính xác nếu khai báo thủ công.
- **Lỗi xác thực (Authentication Errors):**
  Nhiều MCP (như NotebookLM) yêu cầu cookie hoặc token. Đảm bảo bạn đã cung cấp đúng quyền truy cập. Với NotebookLM, có thể bạn cần chạy công cụ dòng lệnh (CLI - ví dụ: `nlm login`) để ủy quyền trước.
- **AI không dùng MCP dù đã kết nối:**
  Hãy điều chỉnh Prompt của bạn. Dùng từ khóa rõ ràng, ví dụ: *"Sử dụng công cụ Consensus để tìm 3 bài báo về..."* thay vì chỉ hỏi chung chung. Bạn cần tường minh "cấp phép" cho AI kích hoạt công cụ.

---

> 💡 **Tip:** Nếu bạn không phải dân lập trình, hãy nhờ một công cụ AI trợ lý giúp bạn viết file `claude_desktop_config.json` sao cho đúng định dạng, tránh lỗi thiếu dấu phẩy `,` hoặc ngoặc kép `"`, vốn là lỗi phổ biến nhất khi chỉnh sửa file cấu hình định dạng JSON.

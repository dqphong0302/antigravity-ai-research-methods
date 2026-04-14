# Lời Nói Đầu

![Lời Nói Đầu — AI & Nghiên Cứu](../assets/images/preface_book_illustration_1776093934972.png)

---

> *"Nghiên cứu không phải là đặc quyền của thiên tài — nó là kỷ luật của sự tò mò có phương pháp."*

---

Cuốn sách bạn đang cầm trên tay — hoặc đang đọc trên màn hình — ra đời từ một trải nghiệm rất cá nhân.

Vào một buổi tối muộn năm 2025, tôi ngồi trước máy tính với hàng trăm tab trình duyệt mở cùng lúc. Trên màn hình bên trái là Google Scholar với hàng nghìn kết quả cho từ khóa tìm kiếm mà tôi đã tinh chỉnh suốt hai tiếng đồng hồ. Màn hình bên phải là một file Word trống trơn — phần tổng quan tài liệu cho dự án nghiên cứu mới vẫn chưa có một dòng nào. Trên bàn là ba ly cà phê đã nguội.

Đó là khoảnh khắc tôi tự hỏi: **Phải có cách tốt hơn.**

Và quả thật, có.

---

## Antigravity Là Gì?

Antigravity không nên được hiểu như một chatbot “hỏi gì đáp nấy”, cũng không chỉ là một danh sách tool ghép lại. Trong cuốn sách này, hãy hiểu nó như một **AI workspace cho nghiên cứu**: một agent có thể làm việc với file, dùng tool, gọi connector, chạy code, đọc tài liệu, và hỗ trợ bạn giữ cả workflow học thuật trong một nơi.

Nói thực dụng hơn, Antigravity phối hợp các MCP server chuyên dụng cho nghiên cứu:

- **Consensus MCP** — tìm kiếm trên 200 triệu bài báo peer-reviewed, trả về metadata, trích dẫn và link trực tiếp;
- **Perplexity MCP** (`perplexity_ask`, `perplexity_reason`, `perplexity_research`) — quét web, grey literature, stress-test lập luận bằng AI có nguồn;
- **NotebookLM MCP** — gom notes, tạo podcast, quiz, slide, briefing doc, mind map từ nguồn đã thu thập;
- **Smart PDF OCR MCP** — số hóa tài liệu scan, tự động phân loại trang (digital/scan đơn giản/scan phức tạp) và chọn engine phù hợp;
- **Playwright MCP** — truy cập web, scrape dữ liệu, chụp screenshot khi cần kiểm chứng trực quan;
- **Code/Terminal tích hợp** — chạy Python, R, tạo figure, làm sạch dữ liệu, xuất kết quả ngay trong workspace.

Điểm quan trọng không phải là bạn có bao nhiêu tool. Điểm quan trọng là agent có biết **dùng đúng tool cho đúng việc học thuật** hay không. Một workflow tốt không bắt đầu bằng “hãy viết cho tôi câu trả lời”, mà bắt đầu bằng:

- tìm đúng nguồn;
- đọc đúng file;
- chạy đúng thao tác;
- lưu đúng output;
- rồi mới tóm tắt, so sánh, phản biện và viết.

---

## Cuốn Sách Này Dành Cho Ai?

Cuốn sách được viết cho:

- **Nghiên cứu sinh (PhD candidates)** — những người đang vật lộn với tổng quan tài liệu, thiết kế nghiên cứu, và áp lực xuất bản
- **Học viên cao học** — những người cần hoàn thành luận văn hiệu quả trong thời gian hạn chế
- **Giảng viên-nhà nghiên cứu** — những người phải cân bằng giữa giảng dạy và nghiên cứu với quỹ thời gian eo hẹp
- **Nhà nghiên cứu độc lập** — những người không thuộc một viện nghiên cứu lớn nhưng vẫn muốn đóng góp cho khoa học

Dù bạn thuộc lĩnh vực nào — từ Vật lý lượng tử đến Xã hội học, từ Y sinh đến Giáo dục, từ Kỹ thuật đến Nhân học — cuốn sách này đều có nội dung phù hợp. Mỗi chương đều có **ví dụ song hành** cho cả khoa học tự nhiên và xã hội, cả nghiên cứu định tính và định lượng.

---

## Cuốn Sách Này KHÔNG Phải Là Gì?

Hãy để tôi nói rõ ngay từ đầu:

- **Đây không phải sách dạy phương pháp nghiên cứu.** Tôi giả định bạn đã có kiến thức cơ bản về phương pháp luận nghiên cứu. Cuốn sách này hướng dẫn bạn cách **áp dụng AI vào quy trình nghiên cứu** mà bạn đã biết.

- **Đây không phải hướng dẫn "để AI viết hộ".** Triết lý cốt lõi của chúng ta là **AI-as-Junior-Assistant** — AI là trợ lý cấp dưới, còn bạn là nhà nghiên cứu chính, người ra quyết định khoa học.

- **Đây không phải lời hứa phép màu.** AI giúp bạn nhanh hơn, toàn diện hơn, nhưng không thể thay thế tư duy phản biện, sự sáng tạo, và trách nhiệm đạo đức của bạn.

---

## Cách Đọc Cuốn Sách Này

Cuốn sách được tổ chức theo **quy trình nghiên cứu tự nhiên** — từ ý tưởng ban đầu đến xuất bản kết quả. Bạn có thể đọc:

### 📚 Đọc tuần tự (nếu bạn mới bắt đầu)
Đi từ Chương 0 đến Chương 16, theo đúng thứ tự. Mỗi chương xây dựng trên nền tảng của chương trước.

### 🎯 Đọc theo nhu cầu (nếu bạn đang giữa chừng dự án)
- Đang gặp khó khăn với tổng quan tài liệu? → **Chương 4**
- Cần thiết kế bảng hỏi? → **Chương 6**
- Muốn phân tích phỏng vấn? → **Chương 11**
- Đang viết bài báo? → **Chương 13**

### 🛠️ Đọc như sách tham khảo
Phụ lục chứa prompt frameworks, checklists, templates, và case studies để bạn thích nghi theo dự án thật. Chúng không nhằm biến bạn thành người “chép prompt”, mà giúp bạn đặt đúng việc cho agent và đúng công cụ cho workflow nghiên cứu.

---

## Quy Ước Trong Sách

Xuyên suốt cuốn sách, bạn sẽ gặp các ký hiệu sau:

> 💡 **Mẹo (Tip):** Những khuyến nghị giúp bạn sử dụng Antigravity hiệu quả hơn.

> ⚠️ **Cảnh báo (Warning):** Những điều cần cẩn thận — đặc biệt liên quan đến độ chính xác của AI.

> 🧪 **Ví dụ Tự Nhiên:** Minh họa từ khoa học tự nhiên (Vật lý, Hóa học, Sinh học, Kỹ thuật...).

> 📊 **Ví dụ Xã Hội:** Minh họa từ khoa học xã hội (Giáo dục, Xã hội học, Kinh tế, Luật...).

> 🔧 **Hands-on:** Bài tập thực hành bạn có thể làm ngay trên Antigravity.

> 📋 **Prompt Template:** Mẫu khởi động để bạn giao việc cho agent. Luôn cần chỉnh theo bối cảnh, dữ liệu, tool và mức kiểm chứng của dự án thật.

---

## Lời Cảm Ơn

Cuốn sách này được viết với sự hỗ trợ của chính Antigravity, nhưng không theo kiểu “AI viết hộ”. Trong quá trình biên soạn, AI được dùng đúng vai trò mà cuốn sách cổ vũ: tìm nguồn, đối chiếu cấu trúc, stress-test logic, hỗ trợ biên tập, và giúp giữ workflow có thể truy lại. Phần quyết định học thuật, kiểm chứng cuối cùng và trách nhiệm nội dung vẫn thuộc về con người.

Tôi viết cuốn sách này với hy vọng rằng nó sẽ giúp các nhà nghiên cứu Việt Nam — đặc biệt những người đang phải làm việc với nguồn lực hạn chế — có thêm một đồng minh mạnh mẽ trong hành trình khám phá tri thức.

*Phong Đặng*
*Tháng 4, 2026*

---

> 📖 **Tiếp theo:** [Chương 0: AI Trong Nghiên Cứu Khoa Học — Bối Cảnh & Xu Hướng →](chuong-00-ai-trong-nghien-cuu.md)

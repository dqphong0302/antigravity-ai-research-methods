# 📂 Examples — Tài Nguyên Thực Hành Cho Ebook

Thư mục này chứa toàn bộ **tài nguyên thực hành** đi kèm cuốn sách "Antigravity — Phương Pháp Nghiên Cứu Với Trí Tuệ Nhân Tạo".

Mục tiêu: cung cấp cho người đọc những **template có thể tải về và chạy ngay**, thay vì chỉ đọc lý thuyết.

---

## Bản Đồ Thư Mục

```
examples/
│
├── sample-project-photocatalysis/   ← Dự án mẫu hoàn chỉnh (định lượng)
│   ├── data/raw/                    ← Dataset thô
│   ├── data/processed/              ← Dataset đã làm sạch
│   ├── scripts/                     ← Pipeline Python (generate → clean → analyze)
│   ├── results/figures/             ← Biểu đồ phân tích
│   ├── results/tables/              ← Bảng thống kê
│   └── results/analysis_report.md   ← Báo cáo tự động
│
├── sample-skill-research/           ← Template Skill cho AI Agent
│   ├── SKILL.md                     ← File cấu hình chính (Literature Analyzer)
│   ├── prompts/                     ← Prompt chuẩn hóa
│   └── scripts/                     ← Script công cụ hỗ trợ
│
├── skills/                          ← Bộ sưu tập Skill templates theo giai đoạn
│   ├── 01-literature-review/        ← Skill: Tổng quan tài liệu
│   ├── 02-methodology-reviewer/     ← Skill: Rà soát phương pháp
│   ├── 03-stats-assistant/          ← Skill: Trợ lý thống kê
│   ├── 04-writing-editor/           ← Skill: Biên tập viên học thuật
│   └── 05-ethics-auditor/           ← Skill: Kiểm toán đạo đức AI
│
├── templates/                       ← Bộ templates tài liệu nghiên cứu
│   ├── research-proposal.md         ← Mẫu đề cương nghiên cứu
│   ├── ai-use-log.md                ← Nhật ký sử dụng AI
│   ├── consent-form.md              ← Phiếu đồng thuận tham gia
│   ├── data-management-plan.md      ← Kế hoạch quản lý dữ liệu
│   └── ai-disclosure.md             ← Mẫu khai báo sử dụng AI
│
└── workflow-map.md                  ← Bản đồ quy trình tổng thể
```

---

## Cách Sử Dụng

### 1. Muốn xem ví dụ phân tích hoàn chỉnh?
→ Mở `sample-project-photocatalysis/`. Chạy 3 script Python theo thứ tự `00 → 01 → 02`.

### 2. Muốn tạo AI Agent chuyên cho nghiên cứu?
→ Copy bất kỳ skill nào trong `skills/`, chỉnh sửa cho phù hợp đề tài của bạn.

### 3. Muốn template để bắt đầu viết ngay?
→ Copy file phù hợp từ `templates/` vào thư mục dự án của bạn.

### 4. Muốn hiểu toàn bộ quy trình?
→ Đọc `workflow-map.md` — bản đồ kết nối tất cả lại với nhau.

---

*Mọi template đều theo triết lý của ebook: AI hỗ trợ, con người chịu trách nhiệm.*

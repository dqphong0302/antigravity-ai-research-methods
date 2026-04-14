# Phụ Lục C: Templates Đồng Bộ Với Ebook

![Research Templates](../assets/images/appendix_c_templates_1776093985103.png)

---

> *Template tốt không làm thay bạn. Nó chỉ giảm ma sát ở những chỗ lẽ ra không nên tốn quá nhiều năng lượng.*

---

Phụ lục này dùng cùng một logic với `Chương 1` và `Chương 2`: một dự án nghiên cứu cần **workspace rõ, log rõ, dấu vết AI rõ, và cấu trúc file đủ ổn định để còn truy vết**. Hãy xem đây là các mẫu khởi động, không phải biểu mẫu pháp lý hay chuẩn cứng cho mọi ngành.

## C.1 `README.md` Mẫu Cho Dự Án Nghiên Cứu

```markdown
# [Tên Dự Án]

## Mô tả ngắn
[2-4 câu mô tả đề tài, bối cảnh và vì sao nó đáng nghiên cứu]

## Problem Statement
[1 đoạn ngắn]

## Research Questions
- RQ1:
- RQ2:
- RQ3: [nếu có]

## Thiết kế nghiên cứu
- Approach: [Quantitative / Qualitative / Mixed Methods]
- Context:
- Population / Participants:
- Main data sources:

## Trạng thái hiện tại
- Đã hoàn thành:
- Đang làm:
- Tiếp theo:

## Thư mục quan trọng
- `01-literature/`
- `02-design/`
- `03-data/`
- `04-results/`
- `05-writing/`
- `06-outputs/`

## Ghi chú về AI
- AI được dùng cho:
- AI không được dùng cho:
- Xem thêm: `ai-use-log.md` và `data-policy.md`
```

---

## C.2 `research-log.md` Mẫu

```markdown
# Research Log — [Project Name]

## Session: [YYYY-MM-DD] | [Start Time] - [End Time]

### Mục tiêu của phiên làm việc
- [Hôm nay tôi muốn làm rõ điều gì?]

### Việc đã làm
1. [Hoạt động 1]
2. [Hoạt động 2]
3. [Hoạt động 3]

### Tài liệu / dữ liệu đã chạm tới
- [Paper / transcript / dataset / folder]

### Findings / Điều học được
- [Insight 1]
- [Insight 2]

### Quyết định đã chốt
- [Decision + vì sao]

### Việc còn mở
- [Điểm chưa chắc]
- [Điểm cần kiểm chứng]

### Next Steps
- [ ] [Việc tiếp theo 1]
- [ ] [Việc tiếp theo 2]

### Memo nhanh
[Phản tư, băn khoăn, điều cần nhắc lại cho phiên sau]
```

---

## C.3 `ai-use-log.md` Mẫu

````markdown
# AI Use Log — [Project Name]

## Entry #[number] | [YYYY-MM-DD]

### Task
- [Tôi dùng AI để làm gì?]

### Tool / Environment
- Tool:
- Date/version (nếu cần):
- Environment note: [local / public / approved / unknown]

### Input đưa vào
- Dữ liệu hoặc ngữ cảnh đã dùng:
- Có dữ liệu nhạy cảm không: [Có/Không]
- Nếu có, đã ẩn danh chưa:

### Prompt / yêu cầu chính
```text
[paste prompt hoặc tóm tắt đủ rõ]
```

### Output nhận được
- [Tóm tắt ngắn]

### Verification
- Cách kiểm tra:
- Trạng thái: [done / partial / pending]
- Điểm cần kiểm chứng thêm:

### Phần đã giữ lại
- [Tôi dùng phần nào của output]

### Phần đã sửa hoặc loại bỏ
- [Tôi đã sửa gì, bỏ gì, và vì sao]

### Ảnh hưởng tới dự án
- [Output này được dùng ở bước nào tiếp theo?]
````

---

## C.4 Literature Matrix Mẫu

```markdown
# Literature Matrix — [Topic]

| # | Citation | Purpose | Context/Population | Theory/Framework | Method | Key Finding | Limitation | Relevance to My Study | Need to Verify |
|---|----------|---------|--------------------|------------------|--------|-------------|------------|-----------------------|----------------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
```

Gợi ý dùng cột `Need to Verify` cho các claim bạn chưa truy về nguồn gốc hoặc chưa chắc đã đọc đủ sâu.

---

## C.5 `data-policy.md` Mẫu

```markdown
# Data Policy — [Project Name]

## 1. Các loại dữ liệu trong dự án
- [Ví dụ: survey CSV, audio phỏng vấn, transcript, PDF chính sách]

## 2. Dữ liệu nào là nhạy cảm?
- [Loại dữ liệu]
- Vì sao nhạy cảm:
- Mức độ rủi ro:

## 3. Dữ liệu nào được phép đưa vào AI?
- Được phép:
- Chỉ được phép sau khi ẩn danh:
- Không được phép:

## 4. Quyền truy cập
- Ai được xem raw data:
- Ai được xem anonymized data:
- Ai được xem outputs:

## 5. Lưu trữ và backup
- Primary location:
- Backup location:
- Quy tắc đặt tên:

## 6. Consent và disclosure
- Đã có/đang chuẩn bị consent:
- Có cần nói rõ về AI trong consent không:
- Có yêu cầu ethics approval không:

## 7. Quy tắc đỏ của dự án này
- [Ví dụ: không upload transcript chưa ẩn danh]
- [Ví dụ: không chia sẻ raw data qua môi trường công khai]
- [Ví dụ: mọi output AI có liên quan đến phân tích đều phải được log]
```

---

## C.6 Mẫu Consent/Participant Information Starter

Mẫu này chỉ là khung khởi động. Hãy luôn điều chỉnh theo yêu cầu pháp lý, quy định của đơn vị, và advice của GVHD/ethics board.

```markdown
# Phiếu thông tin và chấp thuận tham gia nghiên cứu

## Tên nghiên cứu
[Tên nghiên cứu]

## Người thực hiện
- Họ tên:
- Đơn vị:
- Email:

## Mục đích nghiên cứu
[Mô tả ngắn, dễ hiểu]

## Bạn sẽ được yêu cầu làm gì?
- [Hoạt động 1]
- [Hoạt động 2]
- Thời lượng dự kiến:

## Rủi ro và bất tiện có thể có
- [Mô tả trung thực]

## Bảo mật và sử dụng dữ liệu
- Dữ liệu của bạn sẽ được lưu như thế nào
- Dữ liệu nào sẽ được ẩn danh
- Có dùng công cụ AI ở bước nào không
- Nếu có, dữ liệu sẽ được xử lý với điều kiện gì

## Quyền của người tham gia
- Bạn có quyền từ chối hoặc dừng tham gia bất kỳ lúc nào
- Bạn có thể hỏi thêm trước khi quyết định

## Xác nhận
Tôi đã đọc, hiểu, và đồng ý tham gia một cách tự nguyện.
```

---

## C.7 Codebook Mẫu Cho Định Tính

```markdown
# Codebook — [Project Name]
Version: [v0.1 / v1.0]
Last updated: [YYYY-MM-DD]

## Category: [Tên category]

### Code: [Tên code]
- Definition:
- Khi dùng:
- Khi không dùng:
- Related codes:
- Example quote:
- Analytic note:

## Category: [Tên category]

### Code: [Tên code]
- Definition:
- Khi dùng:
- Khi không dùng:
- Related codes:
- Example quote:
- Analytic note:
```

---

## C.8 Disclosure Statement Mẫu

```markdown
## Statement on AI Use

Generative AI tools were used in limited ways during this project to support tasks such as [literature organization / language editing / outline refinement / coding draft support / figure drafting]. AI was not used to replace the author's responsibility for research design, data interpretation, or final academic judgment.

All AI-assisted outputs that materially informed the project were reviewed and verified by the researcher through [source checking / manual reading / rerunning analysis / advisor review / comparison with raw data].

The author takes full responsibility for the accuracy, interpretation, and integrity of the final work.
```

Bạn có thể thêm một phiên bản chi tiết hơn trong phụ lục nội bộ hoặc `ai-use-log.md` nếu venue yêu cầu.

---

## C.9 Cấu Trúc Workspace Mẫu

Mẫu này được đồng bộ với `Chương 1`.

```text
my-research-project/
│
├── 01-literature/
│   ├── papers/
│   ├── notes/
│   ├── literature-matrix.md
│   └── synthesis.md
│
├── 02-design/
│   ├── problem-statement.md
│   ├── framework.md
│   ├── instruments/
│   └── ethics/
│
├── 03-data/
│   ├── raw/
│   ├── anonymized/
│   ├── processed/
│   ├── analysis/
│   └── codebook.md
│
├── 04-results/
│   ├── figures/
│   ├── tables/
│   └── memos/
│
├── 05-writing/
│   ├── drafts/
│   ├── manuscript.md
│   └── references.bib
│
├── 06-outputs/
│   ├── slides/
│   ├── briefs/
│   └── media/
│
├── research-log.md
├── ai-use-log.md
├── data-policy.md
└── README.md
```

---

## C.10 Cách Dùng Template Đúng Cách

Template này đang giúp bạn nếu:

- nó làm bạn bắt đầu nhanh hơn;
- nó giúp dấu vết dự án rõ hơn;
- nó khiến việc trao đổi với GVHD hoặc cộng tác viên dễ hơn.

Template này đang làm hại bạn nếu:

- bạn giữ nguyên từng mục dù không còn phù hợp với đề tài;
- bạn điền cho đủ mà không thật sự dùng lại;
- hoặc bạn tạo thêm quá nhiều biểu mẫu khiến dự án nặng hơn chính nghiên cứu.

Luôn nhớ: template là công cụ phục vụ workflow, không phải workflow tự nó.

---

> 📖 **Tiếp theo:** [Phụ Lục D: Case Studies →](phu-luc-d-case-studies.md)

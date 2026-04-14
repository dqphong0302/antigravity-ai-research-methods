# 🗺️ Bản Đồ Quy Trình Nghiên Cứu Với AI

Bản đồ này kết nối **từng giai đoạn nghiên cứu** với các **chương trong ebook**, **skills AI**, và **templates** tương ứng trong thư mục `examples/`.

---

## Tổng Quan Quy Trình

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VÒNG ĐỜI NGHIÊN CỨU HỌC THUẬT                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ① Ý tưởng & Bối cảnh       ──→  Chương 0, 2                      │
│       ↓                                                             │
│  ② Xác định vấn đề          ──→  Chương 3                          │
│       ↓                                                             │
│  ③ Tổng quan tài liệu       ──→  Chương 4   ⚡ Skill: lit-review   │
│       ↓                                                             │
│  ④ Khung lý thuyết          ──→  Chương 5                          │
│       ↓                                                             │
│  ⑤ Viết đề cương            ──→  📄 Template: research-proposal    │
│       ↓                                                             │
│  ⑥ Thiết kế phương pháp     ──→  Chương 6-8  ⚡ Skill: methodology │
│       ↓                                                             │
│  ⑦ Xin phép đạo đức (IRB)  ──→  📄 Template: consent-form         │
│       ↓                                                             │
│  ⑧ Thu thập dữ liệu        ──→  Chương 9    📄 Template: DMP      │
│       ↓                                                             │
│  ⑨ Phân tích dữ liệu       ──→  Chương 10-11 ⚡ Skill: stats      │
│       ↓                                                             │
│  ⑩ Trực quan hóa            ──→  Chương 12                         │
│       ↓                                                             │
│  ⑪ Viết bài báo / luận văn  ──→  Chương 13-14 ⚡ Skill: writing    │
│       ↓                                                             │
│  ⑫ Khai báo AI              ──→  Chương 16   📄 Template: disclose │
│       ↓                                                             │
│  ⑬ Truyền thông khoa học    ──→  Chương 15                         │
│       ↓                                                             │
│  ⑭ Kiểm toán đạo đức       ──→  Chương 16   ⚡ Skill: ethics      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Chi Tiết Từng Giai Đoạn

### ① Ý tưởng & Bối cảnh
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 0, 2 |
| AI làm gì | Brainstorm hướng nghiên cứu, phân tích xu hướng |
| AI không làm gì | Chọn đề tài thay bạn |
| Skill | — |
| Template | — |

### ② Xác định vấn đề nghiên cứu
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 3 |
| AI làm gì | Tìm research gap, so sánh các hướng tiếp cận |
| AI không làm gì | Quyết định câu hỏi NC cuối cùng |
| Tool MCP | Perplexity (tìm kiếm), Consensus (tìm bài báo) |
| Template | — |

### ③ Tổng quan tài liệu
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 4 |
| AI làm gì | Trích xuất metadata PDF, tóm tắt sơ bộ, xây Literature Matrix |
| AI không làm gì | Thay thế việc đọc bài gốc |
| **Skill** | `skills/01-literature-review/` |
| Tool MCP | Perplexity, Consensus, NotebookLM, Smart PDF OCR |

### ④ Khung lý thuyết & Giả thuyết
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 5 |
| AI làm gì | Map concepts, gợi ý mô hình lý thuyết, phản biện giả thuyết |
| AI không làm gì | Chọn lập trường lý thuyết |
| Skill | — |

### ⑤ Viết đề cương nghiên cứu
| Mục | Chi tiết |
|---|---|
| Chương ebook | (Bổ sung — giữa Phần II và III) |
| AI làm gì | Gợi ý cấu trúc, mô phỏng phản biện hội đồng, lập Gantt chart |
| AI không làm gì | Viết hoàn chỉnh đề cương thay bạn |
| **Template** | `templates/research-proposal.md` |

### ⑥ Thiết kế phương pháp
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 6, 7, 8 |
| AI làm gì | So sánh design, tính sample size, review protocol |
| AI không làm gì | Quyết định design cuối cùng |
| **Skill** | `skills/02-methodology-reviewer/` |

### ⑦ Xin phép đạo đức (IRB)
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 16 (mở rộng) |
| AI làm gì | Soạn nháp consent form, rà soát câu hỏi khảo sát |
| AI không làm gì | Quyết định mức rủi ro đạo đức |
| **Template** | `templates/consent-form.md` |

### ⑧ Thu thập dữ liệu
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 9 |
| AI làm gì | Tự động tạo Google Forms, scrape, chuẩn hóa format |
| AI không làm gì | Thay thế fieldwork hoặc đánh giá chất lượng dữ liệu |
| **Template** | `templates/data-management-plan.md` |
| Ví dụ thực tế | `sample-project-photocatalysis/` |

### ⑨ Phân tích dữ liệu
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 10, 11 |
| AI làm gì | Viết script phân tích, gợi ý test thống kê, hỗ trợ coding định tính |
| AI không làm gì | Diễn giải ý nghĩa kết quả |
| **Skill** | `skills/03-stats-assistant/` |
| Ví dụ thực tế | `sample-project-photocatalysis/scripts/` |

### ⑩ Trực quan hóa
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 12 |
| AI làm gì | Vẽ chart, chỉnh aesthetic, gợi ý loại biểu đồ phù hợp |
| AI không làm gì | Chọn narrative cho figure |
| Ví dụ thực tế | `sample-project-photocatalysis/results/figures/` |

### ⑪ Viết bài báo / luận văn
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 13, 14 |
| AI làm gì | Soạn nháp từ outline, rà coherence, mô phỏng reviewer |
| AI không làm gì | Thay thế tư duy lập luận |
| **Skill** | `skills/04-writing-editor/` |

### ⑫ Khai báo AI & Kiểm toán đạo đức
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 16 |
| AI làm gì | Rà soát workflow, gợi ý disclosure phù hợp với journal |
| AI không làm gì | Hợp thức hóa hành vi trái đạo đức |
| **Skill** | `skills/05-ethics-auditor/` |
| **Template** | `templates/ai-use-log.md`, `templates/ai-disclosure.md` |

### ⑬ Truyền thông khoa học
| Mục | Chi tiết |
|---|---|
| Chương ebook | Chương 15 |
| AI làm gì | Chuyển đổi paper → blog/infographic/podcast script |
| AI không làm gì | Thay thế sự hiểu biết về audience |

---

## Nguyên Tắc Xuyên Suốt

1. **AI là cộng sự, không phải tác giả.** Mọi quyết định học thuật phải do con người đưa ra.
2. **Mọi đầu ra AI phải được kiểm chứng.** Không bao giờ giữ nội dung mà bạn không tự giải thích được.
3. **Ghi log liên tục.** Dùng `ai-use-log.md` để truy vết khi cần.
4. **Skills giúp đóng khung AI.** Thay vì dùng AI như chatbot chung, hãy cấu hình nó cho từng nhiệm vụ cụ thể.

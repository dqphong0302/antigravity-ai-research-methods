Bạn là kiểm toán viên đạo đức AI trong nghiên cứu. Hãy rà soát workflow sau.

**Mô tả workflow của User:**
```
{{WORKFLOW_DESCRIPTION}}
```

**Checklist kiểm toán:**

### 1. Phân loại Xanh / Vàng / Đỏ

Với MỖI BƯỚC trong workflow, phân loại theo khung đèn giao thông:

🟢 **Xanh** — Rủi ro thấp, nên dùng (miễn là vẫn kiểm tra):
- Tìm kiếm từ khóa, format tài liệu, sửa ngữ pháp, viết code kỹ thuật

🟡 **Vàng** — Có thể dùng, cần điều kiện kiểm soát:
- Coding định tính sơ bộ, viết nháp từ outline, dịch transcript, so sánh literature

🔴 **Đỏ** — Không nên dùng hoặc cần phê duyệt đặc biệt:
- Upload PII, bịa citation, để AI quyết định kết luận, viết phần mình không hiểu

### 2. Kiểm tra dữ liệu
- [ ] Dữ liệu có chứa thông tin nhận diện cá nhân (PII) không?
- [ ] Consent form có bao phủ việc xử lý bằng AI không?
- [ ] Dữ liệu nhạy cảm có được giữ local hay đã upload lên cloud?

### 3. Kiểm tra kiểm chứng
- [ ] Mọi citation có được truy về nguồn gốc không?
- [ ] Code phân tích có được đọc hiểu bởi User không?
- [ ] Kết luận có dựa trên dữ liệu thật hay output AI?

### 4. Kiểm tra trách nhiệm
- [ ] User có thể giải thích mọi section trong bài không?
- [ ] GVHD/đồng tác giả có biết về việc dùng AI không?
- [ ] Disclosure phù hợp với yêu cầu journal/trường?

**Trả về:**
```markdown
## Traffic Light Map
| Bước | Mô tả | Phân loại | Rủi ro | Khuyến nghị |
|---|---|---|---|---|

## Critical Risks
- ...

## AI Disclosure Draft (Short)
...

## AI Disclosure Draft (Detailed)
...
```

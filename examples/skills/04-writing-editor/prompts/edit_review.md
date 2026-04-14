Bạn là biên tập viên học thuật. Rà soát draft sau và trả về diagnostic report.

**Draft:**
```
{{DRAFT_TEXT}}
```

**Câu hỏi nghiên cứu (nếu có):**
{{RQ}}

**Phân tích theo các tiêu chí:**

### 1. Argument Clarity
- Luận điểm trung tâm của bài/section này là gì? (Tóm 1-2 câu)
- Luận điểm đó có được phát biểu rõ ràng không?
- Có chỗ nào đang nói nhiều thứ cùng lúc mà không chốt được?

### 2. Structure & Flow
- Thứ tự các phần có logic không?
- Transitions giữa các đoạn có mượt không?
- Có đoạn nào lạc khỏi thread chính?

### 3. Evidence Quality
- Mỗi claim có được hỗ trợ bởi dữ liệu hoặc citation không?
- Có chỗ nào overclaim (nói quá mức bằng chứng cho phép)?
- Results và Discussion có bị overlap không?

### 4. Tone & Hedging
- Giọng văn có phù hợp với thể loại (paper/thesis)?
- Có chỗ nào quá tự tin mà nên thêm hedging?
- Có chỗ nào quá hedge mà làm yếu đóng góp?

### 5. Red Flags
- Citation nào nghi ngờ không tồn tại?
- Đoạn nào "nghe quá mượt" mà thiếu substance?
- Có dấu hiệu AI-generated text chưa được kiểm tra?

**Trả về:**
```markdown
## Central Argument
...

## Strengths
- ...

## Issues Found
- [Location] [Issue Type] Description → Suggestion

## Priority Fixes (Top 3)
1. ...
2. ...
3. ...
```

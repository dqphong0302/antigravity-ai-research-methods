# Phụ Lục A: Prompt Cookbook Theo Mục Đích Nghiên Cứu

![Prompt Engineering Cookbook](../assets/images/appendix_a_prompts_1776093952195.png)

---

> *Prompt tốt không phải prompt nghe phức tạp. Prompt tốt là prompt đặt đúng việc, đúng bối cảnh, và để lại đủ dấu vết để còn kiểm chứng.*

---

Phụ lục này nên được đọc cùng với `Chương 2`, không tách khỏi nó. Mục tiêu ở đây không phải đưa cho bạn một danh sách lệnh để copy-paste nguyên xi theo từng tool. Mục tiêu là cho bạn một bộ **khung prompt theo mục đích nghiên cứu**, để bạn có thể tự thích nghi theo:

- đề tài của mình;
- loại dữ liệu mình có;
- giai đoạn dự án;
- mức độ nhạy cảm của đầu vào;
- và yêu cầu của journal, hội đồng, hay đơn vị đào tạo.

## A.1 Cách Dùng Cookbook Này

### Luôn bắt đầu từ ý định nghiên cứu

Trước khi viết prompt, hãy tự trả lời ba câu:

1. Tôi đang cần làm rõ điều gì?
2. Output này sẽ được dùng ở bước nào tiếp theo?
3. Tôi sẽ kiểm chứng output này bằng cách nào?

Nếu chưa trả lời được ba câu đó, đừng viết prompt quá sớm.

### Khung xương sống: `RCTFC`

Phần lớn prompt trong sách này đều có thể đi từ khung:

```text
[ROLE] AI cần đóng vai gì?
[CONTEXT] Bối cảnh nghiên cứu của tôi là gì?
[TASK] Tôi cần làm việc cụ thể nào?
[FORMAT] Tôi muốn output được trình bày ra sao?
[CONSTRAINT] Giới hạn, tiêu chí, hoặc điều không được làm là gì?
```

### Dòng kiểm chứng nên thêm vào rất thường xuyên

Bạn có thể thêm một hoặc vài câu kiểu này vào cuối prompt:

```text
Chỉ nêu điều anh/chị có thể chống lưng bằng nguồn hoặc logic rõ.
Nếu có điểm chưa chắc, hãy tách riêng thành mục "Cần kiểm tra thêm".
Không bịa citation, không suy diễn vượt quá bằng chứng đã nêu.
```

### Cách nâng cấp một prompt còn yếu

Nếu output đang quá chung chung, hãy thử thêm một trong bốn kiểu ràng buộc sau:

- ràng buộc theo `audience`: viết cho ai;
- ràng buộc theo `task`: cần ra quyết định gì;
- ràng buộc theo `format`: bảng, bullet, matrix, memo, outline;
- ràng buộc theo `verification`: điều gì phải được đánh dấu là chưa chắc.

---

## A.2 Khám Phá Vấn Đề Nghiên Cứu

### A-01: Quét landscape ban đầu

```text
[ROLE] Đóng vai trợ lý nghiên cứu đang giúp tôi quét một lĩnh vực mới.
[CONTEXT] Tôi đang ở giai đoạn đầu của dự án về [topic]. Tôi chưa cần literature review hoàn chỉnh; tôi cần một bản đồ ban đầu để biết field này đang bàn gì.
[TASK] Hãy cho tôi một landscape scan ngắn về [topic].
[FORMAT] Trình bày theo 5 mục:
1. Các hướng nghiên cứu chính
2. Các tranh luận hoặc tension nổi bật
3. Các bối cảnh/population thường được nghiên cứu
4. Những khoảng trống tiềm năng
5. 5-8 nguồn neo nên đọc trước
[CONSTRAINT] Phân biệt rõ giữa điều đã được hỗ trợ tốt và điều mới chỉ là gợi ý. Không viết như thể đây đã là literature review hoàn chỉnh.
```

### A-02: Phân loại gap thay vì chỉ ghi "thiếu nghiên cứu"

```text
[ROLE] Đóng vai methodological reviewer.
[CONTEXT] Tôi đã có vài nguồn neo về [topic] và đang cố xác định gap.
[TASK] Hãy giúp tôi phân loại các gap tiềm năng thành empirical, contextual, theoretical, methodological, hoặc contradictory findings.
[FORMAT] Tạo bảng gồm: Gap signal | Loại gap | Vì sao đáng chú ý | Điều cần đọc thêm để xác nhận.
[CONSTRAINT] Không gọi một chỗ là gap chỉ vì "ít nghiên cứu". Chỉ ghi gap khi có logic giải thích vì sao nó quan trọng.
```

### A-03: Từ gap sang problem statement

```text
[ROLE] Đóng vai người phản biện đề cương nghiên cứu.
[CONTEXT] Tôi đang làm đề tài về [topic]. Đây là gap tôi đang thấy: [gap draft].
[TASK] Hãy giúp tôi chuyển gap này thành một problem statement.
[FORMAT] 
- Trước hết, chỉ ra 4 thành phần nên có: bối cảnh, điều chưa rõ, hệ quả của sự thiếu đó, đóng góp dự kiến.
- Sau đó đề xuất 2 phiên bản problem statement dài 1 đoạn.
- Cuối cùng nêu 3 điểm còn yếu cần tự sửa.
[CONSTRAINT] Không dùng ngôn ngữ thổi phồng. Nếu gap còn quá mơ hồ, hãy nói thẳng.
```

### A-04: Stress-test research question

```text
[ROLE] Đóng vai reviewer khó tính.
[CONTEXT] Tôi đang cân nhắc research question sau: [RQ].
Problem statement của tôi là: [problem statement].
[TASK] Hãy phản biện câu hỏi nghiên cứu này.
[FORMAT] Chia làm 4 mục:
1. Điểm mạnh
2. Điểm mơ hồ
3. Rủi ro về feasibility hoặc logic
4. Phiên bản chỉnh gợi ý
[CONSTRAINT] Chỉ phê bình dựa trên logic phương pháp, không sửa câu hỏi theo hướng đổi hẳn đề tài nếu chưa cần.
```

---

## A.3 Tổng Quan Tài Liệu

### A-05: Xây search strategy

```text
[ROLE] Đóng vai research librarian hỗ trợ chiến lược tìm kiếm.
[CONTEXT] Tôi đang làm literature review cho đề tài [topic].
Problem statement/RQ hiện tại: [paste].
[TASK] Hãy giúp tôi tạo search strategy ban đầu.
[FORMAT]
- 1 review question
- 3-5 search strings
- keywords cốt lõi
- keywords đồng nghĩa
- keywords bối cảnh
[CONSTRAINT] Tránh làm chuỗi quá rộng. Tách rõ phần nào là academic core, phần nào là contextual/local sources.
```

### A-06: Sàng lọc theo inclusion/exclusion

```text
[ROLE] Đóng vai trợ lý hỗ trợ screening.
[CONTEXT] Tôi đã có danh sách nguồn sau: [list hoặc bảng ngắn].
[TASK] Hãy đề xuất tiêu chí inclusion/exclusion phù hợp với review question của tôi.
[FORMAT] Tạo 2 danh sách:
- Inclusion criteria
- Exclusion criteria
Sau đó minh họa bằng cách áp dụng thử cho 5 nguồn đầu tiên.
[CONSTRAINT] Không quyết định thay tôi. Nếu dữ liệu chưa đủ để loại/giữ, hãy đánh dấu "cần đọc thêm".
```

### A-07: Trích xuất có mục đích từ nguồn neo

```text
[ROLE] Đóng vai reading assistant.
[CONTEXT] Tôi đang đọc nguồn sau: [citation hoặc đoạn tóm tắt].
[TASK] Hãy giúp tôi trích xuất những gì thực sự cần cho literature review.
[FORMAT] Trả về bảng:
Purpose | Theory/framework | Method | Sample/context | Key finding | Limitation | Relevance to my study
[CONSTRAINT] Không viết quá phần nguồn cho phép. Nếu không thấy thông tin, ghi "chưa xác định từ dữ liệu hiện có".
```

### A-08: Phân biệt summary và synthesis

```text
[ROLE] Đóng vai biên tập viên học thuật.
[CONTEXT] Đây là đoạn literature review tôi vừa viết: [paste].
[TASK] Hãy kiểm tra xem đoạn này đang là summary hay synthesis.
[FORMAT]
- Nhận định chung
- 3 dấu hiệu đang còn summary
- 3 gợi ý để chuyển sang synthesis
- 1 phiên bản rewrite ngắn minh họa
[CONSTRAINT] Không rewrite toàn bộ theo giọng bóng bẩy. Mục tiêu là chỉ ra logic lập luận còn thiếu.
```

### A-09: Viết positioning paragraph

```text
[ROLE] Đóng vai reviewer của phần Introduction.
[CONTEXT] Tôi đã xác định được các theme và tension sau trong literature: [paste].
[TASK] Hãy giúp tôi viết một đoạn positioning cho nghiên cứu của mình.
[FORMAT] 
- 1 câu chốt bối cảnh học thuật
- 1 câu nêu tension hoặc thiếu hụt
- 1 câu nêu nghiên cứu của tôi sẽ làm gì
- 1 đoạn hoàn chỉnh 120-180 từ
[CONSTRAINT] Không nói quá đóng góp. Chỉ nêu thứ tôi thực sự có thể làm.
```

---

## A.4 Khung Lý Thuyết Và Thiết Kế

### A-10: Theory fit matrix

```text
[ROLE] Đóng vai methodological advisor.
[CONTEXT] Tôi đang cân nhắc 3 khung lý thuyết cho đề tài [topic]:
[list frameworks].
[TASK] Hãy giúp tôi lập theory fit matrix.
[FORMAT] Bảng gồm:
Framework | Explanatory fit | Context fit | Level of analysis fit | Method fit | Limitations | Why it may or may not suit my study
[CONSTRAINT] Không mặc định framework nổi tiếng là tốt hơn. Nếu một khung nghe hay nhưng khó dùng trong bối cảnh của tôi, hãy nói rõ.
```

### A-11: Từ framework sang design logic định lượng

```text
[ROLE] Đóng vai quantitative design reviewer.
[CONTEXT] Framework của tôi là [framework]. RQ/H là [paste].
[TASK] Hãy chuyển framework này thành design logic định lượng.
[FORMAT]
- constructs chính
- biến có thể đo
- loại thiết kế định lượng phù hợp
- phân tích chính có thể dùng
- những chỗ cần chú ý về validity
[CONSTRAINT] Phân biệt rõ construct với variable. Không giả định tôi có thể suy luận nhân quả nếu thiết kế không hỗ trợ.
```

### A-12: Chọn approach định tính

```text
[ROLE] Đóng vai qualitative methods advisor.
[CONTEXT] Tôi muốn nghiên cứu hiện tượng [phenomenon] trong bối cảnh [context].
RQ hiện tại: [paste].
[TASK] Hãy so sánh 3 approach định tính phù hợp nhất.
[FORMAT] Bảng gồm:
Approach | Câu hỏi nào nó trả lời tốt | Dữ liệu chính | Cỡ mẫu điển hình | Điểm mạnh | Điểm yếu | Fit với đề tài của tôi
[CONSTRAINT] Không chọn giúp ngay. Hãy chỉ ra trade-off thật giữa các approach.
```

### A-13: Integration map cho mixed methods

```text
[ROLE] Đóng vai reviewer của mixed methods design.
[CONTEXT] Tôi đang cân nhắc thiết kế hỗn hợp cho đề tài [topic].
Overall RQ: [paste].
QUAN strand: [paste].
QUAL strand: [paste].
[TASK] Hãy giúp tôi lập integration map.
[FORMAT] Tạo bảng:
Overall RQ | QUAN task | QUAL task | Integration point | Final product
[CONSTRAINT] Nếu mixed methods hiện tại chỉ là "làm cả hai cho chắc", hãy nói rõ và gợi ý cách thu gọn.
```

---

## A.5 Thu Thập Và Quản Trị Dữ Liệu

### A-14: Data collection readiness check

```text
[ROLE] Đóng vai project reviewer trước khi thu dữ liệu.
[CONTEXT] Tôi sắp thu dữ liệu cho nghiên cứu [topic].
Thiết kế hiện tại: [paste].
[TASK] Hãy kiểm tra mức độ sẵn sàng trước khi thu dữ liệu.
[FORMAT] Chia thành 5 mục:
1. Dữ liệu này trả lời RQ nào?
2. Đơn vị phân tích là gì?
3. Tiêu chí "đủ dữ liệu" là gì?
4. Rủi ro đạo đức/bảo mật là gì?
5. Dữ liệu sẽ được lưu và log ra sao?
[CONSTRAINT] Nếu có chỗ nào chưa chốt được, đánh dấu "chưa sẵn sàng" thay vì cố lấp.
```

### A-15: Kiểm tra rủi ro trước khi scrape hoặc OCR

```text
[ROLE] Đóng vai ethics and data governance checker.
[CONTEXT] Tôi muốn thu thập dữ liệu bằng [web collection / OCR] cho [mục đích].
Đầu vào của tôi gồm: [mô tả dữ liệu].
[TASK] Hãy giúp tôi rà rủi ro trước khi làm.
[FORMAT]
- Loại dữ liệu
- Rủi ro chính
- Điều kiện tối thiểu để tiếp tục
- Khi nào nên dừng hoặc đổi cách làm
[CONSTRAINT] Ưu tiên cảnh báo rủi ro hơn là tối ưu tốc độ.
```

### A-16: Dựng data dictionary hoặc metadata starter pack

```text
[ROLE] Đóng vai data manager.
[CONTEXT] Tôi đang thu dữ liệu cho nghiên cứu [topic]. Dữ liệu của tôi gồm [mô tả].
[TASK] Hãy giúp tôi tạo metadata starter pack.
[FORMAT]
- file naming convention
- bảng data dictionary tối thiểu
- cột nên có trong metadata log
- các thư mục raw / anonymized / processed nên chứa gì
[CONSTRAINT] Làm theo logic tái lập, không theo logic "miễn dễ nhớ với tôi".
```

---

## A.6 Phân Tích Định Lượng

### A-17: Analysis plan từ RQ và biến

```text
[ROLE] Đóng vai statistical reviewer.
[CONTEXT] RQ/H của tôi là [paste].
Các biến hiện có trong dataset là [list].
[TASK] Hãy đề xuất analysis plan ngắn gọn.
[FORMAT] Bảng gồm:
RQ/H | Variables | Main analysis | Assumptions to check | Output I should report
[CONSTRAINT] Không đề xuất test chỉ vì phổ biến. Mỗi lựa chọn phải nối với loại câu hỏi.
```

### A-18: Assumption audit

```text
[ROLE] Đóng vai statistical checker.
[CONTEXT] Tôi đã chạy mô hình/phép kiểm sau: [paste].
[TASK] Hãy liệt kê các assumptions chính và cách kiểm tra chúng.
[FORMAT]
- Assumption
- Why it matters
- How to check
- Nếu vi phạm thì có thể xử lý thế nào
[CONSTRAINT] Không coi assumption checking là phần phụ. Nếu một assumption quan trọng chưa kiểm, nói rõ kết luận nào đang bị yếu đi.
```

### A-19: Tách Results và Discussion

```text
[ROLE] Đóng vai biên tập viên bài báo.
[CONTEXT] Đây là đoạn viết kết quả của tôi: [paste].
[TASK] Hãy chỉ ra phần nào thuộc Results, phần nào thuộc Discussion.
[FORMAT]
- Câu/đoạn nên giữ ở Results
- Câu/đoạn nên chuyển sang Discussion
- Lý do
[CONSTRAINT] Không rewrite toàn bộ nếu chưa cần. Mục tiêu là tách chức năng cho rõ.
```

### A-20: Effect size và practical significance

```text
[ROLE] Đóng vai statistical interpreter.
[CONTEXT] Đây là output chính của tôi: [paste].
[TASK] Hãy giúp tôi diễn giải kết quả ở 4 lớp:
1. Hướng và độ lớn hiệu ứng
2. Mức chắc chắn
3. Ý nghĩa thực tiễn
4. Điều chưa thể kết luận
[FORMAT] Bullet ngắn, trung thực, tránh khoa trương.
[CONSTRAINT] Không biến p-value nhỏ thành kết luận quá tay.
```

---

## A.7 Phân Tích Định Tính

### A-21: Familiarization note helper

```text
[ROLE] Đóng vai trợ lý đọc dữ liệu.
[CONTEXT] Tôi vừa đọc transcript/tài liệu sau: [paste đoạn ngắn hoặc tóm tắt].
[TASK] Hãy giúp tôi tạo 5-7 câu familiarization notes ban đầu.
[FORMAT]
- Điều gây chú ý
- Cụm từ hoặc hình ảnh lặp lại
- Điều mâu thuẫn hoặc bất ngờ
- Câu hỏi cần đọc tiếp
[CONSTRAINT] Đây chỉ là ghi chú đọc đầu tiên, không được giả vờ như thematic findings cuối cùng.
```

### A-22: Draft open coding có kiểm soát

```text
[ROLE] Đóng vai coding assistant.
[CONTEXT] Tôi đang ở giai đoạn open coding cho dữ liệu [mô tả].
[TASK] Hãy gợi ý draft open codes cho đoạn dữ liệu sau: [paste].
[FORMAT] Bảng:
Quote | Draft code | Why this code | Note for researcher review
[CONSTRAINT] Đánh dấu rõ đây là draft. Ưu tiên mã bám sát dữ liệu, không nhảy vội lên lý thuyết.
```

### A-23: Theme stress test

```text
[ROLE] Đóng vai reviewer của thematic analysis.
[CONTEXT] Tôi hiện có các themes sau: [list].
[TASK] Hãy stress-test hệ theme này.
[FORMAT]
- Theme nào đang mạnh
- Theme nào đang trùng nhau
- Theme nào quá rộng hoặc quá mơ hồ
- Negative cases hoặc quotes nào tôi nên tìm thêm
[CONSTRAINT] Không tạo theme mới chỉ để cho đẹp cấu trúc. Ưu tiên kiểm tra logic và độ sâu.
```

### A-24: Trustworthiness audit

```text
[ROLE] Đóng vai qualitative methods reviewer.
[CONTEXT] Tôi đang phân tích định tính theo [approach].
[TASK] Hãy rà mức độ trustworthiness hiện tại.
[FORMAT] Bảng:
Credibility | Transferability | Dependability | Confirmability
Mỗi cột gồm: tôi đã làm gì, còn thiếu gì, bằng chứng nào nên lưu lại
[CONSTRAINT] Nếu tôi mới có ý định mà chưa thực hiện, hãy ghi là "planned", không ghi như đã hoàn thành.
```

---

## A.8 Viết, Sửa Và Phản Biện Bản Thảo

### A-25: Contribution statement 5 câu

```text
[ROLE] Đóng vai biên tập viên học thuật.
[CONTEXT] Dựa trên nghiên cứu của tôi về [topic], với phương pháp [method], findings chính là [paste].
[TASK] Hãy giúp tôi nén đóng góp thành 5 câu.
[FORMAT]
1. Bài này nghiên cứu gì
2. Gap là gì
3. Tôi dùng cách nào
4. Finding chính là gì
5. Đóng góp chính là gì
[CONSTRAINT] Nếu câu nào còn sáo rỗng, hãy chỉ ra thay vì làm cho nghe kêu hơn.
```

### A-26: Methods justification check

```text
[ROLE] Đóng vai reviewer.
[CONTEXT] Đây là draft Methods của tôi: [paste].
[TASK] Hãy kiểm tra xem phần này đang mô tả hay đã biện minh đủ cho lựa chọn phương pháp.
[FORMAT]
- Điểm nào đã rõ
- Điểm nào mới chỉ kể lại quy trình
- Chỗ nào cần giải thích thêm "vì sao chọn cách này"
[CONSTRAINT] Không yêu cầu thêm chi tiết thừa nếu nó không phục vụ tính tin cậy hoặc khả năng đánh giá của người đọc.
```

### A-27: Discussion restraint check

```text
[ROLE] Đóng vai reviewer khó tính.
[CONTEXT] Đây là draft Discussion của tôi: [paste].
[TASK] Hãy rà 4 rủi ro:
1. lặp lại Results
2. diễn giải quá mức
3. tuyên bố nhân quả quá tay
4. né tránh limitation
[FORMAT] Chỉ ra câu/đoạn cụ thể và gợi ý sửa ngắn.
[CONSTRAINT] Giữ giọng thận trọng, không làm yếu đóng góp một cách vô cớ.
```

### A-28: Citation audit

```text
[ROLE] Đóng vai citation auditor.
[CONTEXT] Tôi cần rà danh sách trích dẫn hoặc một đoạn có nhiều citation sau: [paste].
[TASK] Hãy tạo checklist audit theo 3 mức:
1. Tồn tại
2. Khớp hình thức
3. Khớp nội dung tôi đang gán cho nguồn
[FORMAT] Bảng:
Citation | Existence check | Format check | Content check | Action needed
[CONSTRAINT] Nếu chưa truy ra nguồn gốc thật, không đánh dấu "đã xác minh".
```

---

## A.9 Truyền Thông Và Đạo Đức

### A-29: Core message ladder

```text
[ROLE] Đóng vai science communication editor.
[CONTEXT] Nghiên cứu của tôi là [topic]. Finding chính: [paste].
[TASK] Hãy giúp tôi tạo message ladder.
[FORMAT]
- 1 câu core message
- 3 supporting points
- 1 câu về giới hạn hoặc mức chắc chắn
- 3 phiên bản ngắn cho 3 audience khác nhau
[CONSTRAINT] Không biến correlation thành causation. Không bỏ mất giới hạn quan trọng.
```

### A-30: Audience translation

```text
[ROLE] Đóng vai communication strategist.
[CONTEXT] Tôi cần truyền thông nghiên cứu này cho [audience].
Nguồn gốc học thuật hiện có: [paper/chapter/slides].
[TASK] Hãy dịch thông điệp sang ngôn ngữ phù hợp với audience đó.
[FORMAT]
- họ quan tâm gì nhất
- điều nên nói trước
- thuật ngữ nào nên giữ / nên bỏ
- draft outline cho format phù hợp
[CONSTRAINT] Không làm nội dung giật gân hơn bản gốc.
```

### A-31: Communication risk audit

```text
[ROLE] Đóng vai ethical communication reviewer.
[CONTEXT] Đây là bản truyền thông của tôi: [paste].
[TASK] Hãy kiểm tra 5 rủi ro:
1. phóng đại kết quả
2. bỏ mất giới hạn
3. đơn giản hóa quá mức
4. nhầm tương quan với nhân quả
5. audience có thể hiểu sai ở đâu
[FORMAT] Bảng ngắn: Risk | Why it matters | How to fix
[CONSTRAINT] Ưu tiên trung thực khoa học hơn là tính hấp dẫn.
```

### A-32: AI disclosure draft

```text
[ROLE] Đóng vai compliance-aware editor.
[CONTEXT] Tôi đã dùng AI cho các việc sau trong dự án/bản thảo: [list].
[TASK] Hãy giúp tôi viết một disclosure statement.
[FORMAT]
- 1 phiên bản ngắn cho manuscript/thesis
- 1 phiên bản chi tiết cho phụ lục hoặc hồ sơ nội bộ
[CONSTRAINT] Chỉ mô tả đúng phần AI đã tham gia, cách tôi kiểm chứng, và trách nhiệm cuối cùng thuộc về ai. Không viết phòng thủ hoặc khoa trương.
```

### A-33: Ethics traffic-light check

```text
[ROLE] Đóng vai ethics checker.
[CONTEXT] Tôi muốn dùng AI cho việc sau: [mô tả task, input, tool, output dự kiến].
[TASK] Hãy đánh giá theo khung đèn giao thông.
[FORMAT]
- Xanh / Vàng / Đỏ
- Vì sao
- Điều kiện tối thiểu nếu vẫn muốn tiếp tục
- Khi nào nên dừng và hỏi GVHD / ethics board / data steward
[CONSTRAINT] Nếu task liên quan dữ liệu nhạy cảm hoặc quyền riêng tư, ưu tiên cảnh báo rủi ro hơn là tối ưu workflow.
```

---

## A.10 Ba Câu Hỏi Nên Gắn Vào Gần Mọi Prompt

Khi nghi ngờ prompt của mình còn thiếu chiều sâu, hãy thêm một trong ba câu sau:

```text
Điểm nào trong output này tôi cần tự kiểm chứng bằng nguồn gốc hoặc bằng dữ liệu thật?
Những giả định ngầm nào đang nằm trong câu trả lời của anh/chị?
Nếu phải phản biện chính output này, ba điểm yếu lớn nhất sẽ là gì?
```

Ba câu đó thường giá trị hơn việc thêm hàng loạt tham số kỹ thuật.

---

## A.11 Cách Dùng Phụ Lục Này Cho Đúng

Phụ lục này làm tốt nhiệm vụ của nó khi bạn dùng prompt như:

- một **khung để nghĩ**;
- một **cách cấu trúc trao đổi** với AI;
- và một **bộ nhắc kiểm chứng** cho từng giai đoạn nghiên cứu.

Phụ lục này làm sai nhiệm vụ của nó khi bạn dùng prompt như:

- câu thần chú phải copy-paste nguyên xi;
- cách tránh việc tự đọc và tự nghĩ;
- hoặc bằng chứng rằng AI đã "làm hộ xong" phần việc học thuật khó nhất.

Nếu bạn luôn giữ được khoảng cách đó, prompt sẽ trở thành đòn bẩy rất mạnh. Nếu không, prompt rất dễ biến thành lớp sơn phủ lên một workflow còn yếu.

---

> 📖 **Tiếp theo:** [Phụ Lục B: Checklists →](phu-luc-b-checklists.md)

# Chương 13: Viết Bài Báo Khoa Học

![Writing Scientific Paper](../assets/images/ch13_writing_scientific_paper_1776092441013.png)

---

> *"Writing is thinking on paper."* — William Zinsser

---

Chương này hướng dẫn bạn viết bài báo khoa học theo đúng chức năng từng section: Title/Abstract → Introduction → Methods → Results → Discussion → Conclusion. AI giúp bạn draft nhanh, rà coherence, so sánh findings với literature, chuẩn bị phản hồi reviewer — nhưng không thay bạn quyết định đóng góp chính là gì. Đầu vào tốt nhất là từ `Chương 10-12`: kết quả sạch, figure rõ, caption chín.

---

## 13.1 Bài Báo Khoa Học Thực Chất Là Gì?

Một bài báo khoa học tốt không phải là “bản tóm tắt của luận văn”. Nó là một lập luận học thuật có cấu trúc rõ, nhằm chứng minh một đóng góp cụ thể cho một cộng đồng đọc cụ thể.

### Một bài báo thường phải trả lời 5 câu hỏi

- Vấn đề nào đang được quan tâm?
- Khoảng trống nào trong tri thức hiện tại cần được lấp?
- Nghiên cứu này đã làm gì để trả lời khoảng trống đó?
- Kết quả chính là gì?
- Vậy điều đó có nghĩa gì cho lý thuyết, phương pháp, hay thực tiễn?

Nếu một bài báo không trả lời được rõ 5 câu hỏi này, người đọc sẽ cảm thấy nó hoặc quá tản, hoặc quá kỹ thuật nhưng thiếu điểm tựa.

### Bài báo khác luận văn ở đâu?

| Tiêu chí | Luận văn/luận án | Bài báo khoa học |
|---|---|---|
| Mục tiêu | Chứng minh năng lực nghiên cứu toàn diện | Công bố một đóng góp cụ thể |
| Độ dài | Dài, có thể giữ nhiều bước trung gian | Nén, chọn lọc, rất tiết kiệm |
| Độc giả | GVHD, hội đồng, khoa/phòng đào tạo | Reviewer, biên tập viên, cộng đồng chuyên môn |
| Mức giải thích | Có thể giải thích dài | Chỉ giữ cái phục vụ lập luận chính |
| Giọng văn | Có thể rộng và biện giải hơn | Cô đọng, có chủ đích, rất trọng tâm |

### Điều này dẫn đến một nguyên tắc quan trọng

> Bài báo không cần kể hết. Bài báo cần kể đúng.

Nhiều bài viết yếu không phải vì dữ liệu kém, mà vì người viết muốn giữ lại quá nhiều thứ:

- quá nhiều literature không phục vụ gap;
- quá nhiều chi tiết phương pháp không liên quan đến quyết định cốt lõi;
- quá nhiều kết quả phụ;
- hoặc quá nhiều diễn giải “an toàn” khiến đóng góp bị chìm.

---

## 13.2 Chọn Journal Trước Khi Viết Nghiêm Túc

Rất nhiều người viết xong bài rồi mới nghĩ xem gửi đâu. Điều đó khiến bài dễ rơi vào trạng thái “không phải của tạp chí nào cả”.

### Vì sao phải chọn journal target sớm?

Vì journal target quyết định:

- độ dài bài;
- mức độ lý thuyết cần nhấn mạnh;
- kỳ vọng về phương pháp;
- mức chi tiết của literature review;
- cách trình bày bảng, hình, reference;
- và cả giọng của Discussion.

### 3 câu hỏi nên trả lời sớm

1. Tạp chí này đọc loại đóng góp nào?
2. Độc giả chính của nó là ai?
3. Bài của tôi nên được kể theo hướng lý thuyết, thực nghiệm, phương pháp, hay ứng dụng?

### Bảng đối chiếu journal target

| Tiêu chí | Journal A | Journal B | Journal C |
|---|---|---|---|
| Lĩnh vực | | | |
| Loại bài phổ biến | | | |
| Độ dài thường gặp | | | |
| Nhấn mạnh | Theory / methods / application | | |
| Yêu cầu AI disclosure | | | |
| Phù hợp với bài của tôi ở điểm nào? | | | |
| Điểm nào phải chỉnh để khớp? | | | |

### Prompt chọn journal

> 📋 **Prompt Template — Journal Fit Matrix**
> ```
> Tôi muốn chọn journal phù hợp cho nghiên cứu của mình:
> - Topic: [topic]
> - Method: [method]
> - Main finding/contribution: [1-2 câu]
> - Target audience: [field/community]
> 
> Hãy giúp tôi:
> 1. Đề xuất 5 journal tiềm năng
> 2. So sánh scope, loại bài, độ dài, và phong cách
> 3. Chỉ ra bài của tôi phù hợp nhất với journal nào
> 4. Nói rõ tôi cần điều chỉnh gì để tăng journal fit
> 5. Tạo một bảng đối chiếu ngắn gọn
> ```

> 💡 **Điểm dừng để suy nghĩ:** Cùng một nghiên cứu, nếu gửi sai journal, rất dễ bị từ chối không phải vì chất lượng thấp mà vì câu chuyện đang được kể sai cộng đồng.

---

## 13.3 IMRaD Không Chỉ Là Cấu Trúc, Mà Là Logic

![Cấu Trúc Bài Báo Khoa Học IMRaD](../assets/images/ch13_paper_structure_1776094342661.png)

IMRaD là khung kinh điển:

| Section | Nhiệm vụ chính |
|---|---|
| Introduction | Xác lập vấn đề, gap, mục tiêu, đóng góp |
| Methods | Chứng minh cách tiếp cận là hợp lý và có thể tin cậy |
| Results | Cho thấy bạn đã tìm được gì |
| Discussion | Giải thích điều đó có nghĩa gì |
| Abstract | Nén toàn bộ lập luận thành một đoạn |

Sai lầm phổ biến là xem IMRaD như checklist cơ học. Thực ra, nó là một chuỗi logic:

1. Có một vấn đề đáng quan tâm.
2. Tri thức hiện tại còn thiếu một chỗ.
3. Nghiên cứu này chọn một cách làm cụ thể để xử lý chỗ thiếu đó.
4. Dữ liệu cho ra một số phát hiện.
5. Những phát hiện này có ý nghĩa gì và giới hạn ở đâu.

### Điều khiến bài báo yếu đi

- Introduction rộng nhưng không chốt gap.
- Methods dài nhưng không biện minh.
- Results đầy số nhưng không có trọng tâm.
- Discussion lặp lại Results thay vì diễn giải.

Khi viết, hãy luôn nhớ: mỗi section không tồn tại độc lập; nó phải kéo người đọc đi tiếp sang section sau.

---

## 13.4 Thứ Tự Viết Khôn Ngoan: Không Viết Theo Thứ Tự Đọc

Nhiều người mắc kẹt vì cố viết từ Introduction. Đây thường là cách khó nhất.

### Thứ tự viết thường hiệu quả hơn

```text
1. Methods
2. Results
3. Tables/Figures + captions
4. Discussion
5. Introduction
6. Abstract
7. Title
8. Cover letter / submission metadata
```

### Vì sao nên viết như vậy?

**Methods trước**

Vì đây là phần bạn nắm chắc nhất. Viết Methods trước giúp chốt ngôn ngữ mô tả nghiên cứu và làm rõ chính bạn đã thực sự làm gì.

**Results sau**

Khi Results được viết tốt, bạn sẽ biết article đang có “xương sống” ở đâu. Nhiều khi chỉ lúc viết Results, bạn mới nhìn rõ finding nào thực sự là finding chính.

**Discussion sau Results**

Discussion phải phản chiếu findings thực sự, chứ không phản chiếu kỳ vọng ban đầu của bạn.

**Introduction viết sau**

Chỉ khi biết bài báo đang nói đóng góp gì, bạn mới viết được phần dẫn nhập sắc.

### Prompt lập writing workflow

> 📋 **Prompt Template — Paper Writing Workflow**
> ```
> Tôi chuẩn bị viết bài báo từ nghiên cứu đã hoàn thành:
> - Topic: [topic]
> - Method: [method]
> - Main findings: [list]
> - Target journal: [name hoặc loại]
> 
> Hãy giúp tôi:
> 1. Chọn thứ tự viết phù hợp
> 2. Xác định deliverable cho từng bước
> 3. Nói phần nào nên viết từ dữ liệu gốc, phần nào nên viết từ outline
> 4. Chỉ ra 3 điểm dễ bị kẹt nhất
> 5. Đề xuất kế hoạch 7 ngày / 14 ngày để có full draft
> ```

---

## 13.5 Introduction: Viết Gap Chứ Không Kể Danh Sách Bài Báo

Introduction không phải là nơi chứng minh bạn đã đọc nhiều. Nó là nơi chứng minh bạn đọc đúng thứ cần để xây vấn đề.

### Một Introduction thường phải làm 4 việc

1. Đặt bối cảnh nghiên cứu.
2. Tóm tắt landscape vừa đủ để người đọc thấy câu chuyện chung.
3. Chỉ ra gap hoặc tension thật sự.
4. Nói rõ nghiên cứu này làm gì để xử lý gap đó.

### Cấu trúc hữu ích: bối cảnh -> tranh luận -> gap -> mục tiêu

Ví dụ khung:

- Vấn đề này quan trọng vì...
- Các nghiên cứu trước đã chỉ ra...
- Tuy nhiên, vẫn còn thiếu...
- Vì vậy, nghiên cứu này nhằm...

### Sai lầm rất phổ biến

**1. Literature review kiểu “kể tên bài báo”**

Ví dụ:

> Tác giả A nghiên cứu X. Tác giả B nghiên cứu Y. Tác giả C nghiên cứu Z.

Chuỗi này không tạo ra gap. Nó chỉ tạo ra danh sách.

**2. Gap giả**

Ví dụ:

> “Chưa có nghiên cứu nào ở Việt Nam.”

Đây có thể là một phần của gap, nhưng hiếm khi đủ. Gap mạnh hơn thường là:

- chưa ai kiểm tra mối quan hệ này trong bối cảnh X;
- nghiên cứu trước cho kết quả mâu thuẫn;
- thang đo hiện có chưa phù hợp;
- phương pháp trước chưa giải thích được cơ chế.

**3. Purpose statement quá mơ hồ**

Nếu mục tiêu chỉ là “tìm hiểu thực trạng”, bài báo rất dễ bị phẳng và thiếu đóng góp.

### Prompt viết Introduction

> 📋 **Prompt Template — Introduction Builder**
> ```
> Tôi đang viết Introduction cho bài báo về [topic].
> 
> Đây là những gì tôi đã có:
> - Bối cảnh: [context]
> - Literature chính: [summary]
> - Điều còn thiếu/gap: [gap]
> - Nghiên cứu của tôi làm gì: [purpose]
> - Main contribution: [1-2 câu]
> 
> Hãy giúp tôi:
> 1. Sắp lại logic Introduction
> 2. Chỉ ra chỗ nào vẫn đang là "kể tên nghiên cứu"
> 3. Viết một purpose statement rõ hơn
> 4. Gợi ý 1 đoạn kết Introduction dẫn sang Methods
> ```

### Một câu tự kiểm rất quan trọng

> Sau khi đọc xong Introduction, người đọc có biết vì sao bài này phải tồn tại không?

Nếu câu trả lời chưa rõ, Introduction chưa xong.

---

## 13.6 Methods: Không Chỉ Mô Tả, Mà Phải Biện Minh

Methods là nơi bạn chứng minh rằng kết quả của mình đáng tin và có thể được hiểu đúng.

### Một phần Methods tốt thường cần trả lời

- Bạn chọn thiết kế nào và vì sao?
- Đối tượng/mẫu là ai?
- Công cụ hoặc dữ liệu là gì?
- Thu thập dữ liệu thế nào?
- Phân tích ra sao?
- Các cân nhắc đạo đức là gì?
- AI đã được dùng ở đâu, nếu có?

### Điều reviewer rất quan tâm

Không chỉ là bạn đã làm gì, mà là:

- cách làm đó có phù hợp với câu hỏi nghiên cứu không;
- có đủ chi tiết để hiểu và lặp lại ở mức hợp lý không;
- có điểm yếu nào cần nói thẳng không.

### Hai lỗi thường gặp

**1. Methods quá khô, như nhật ký thao tác**

Ví dụ:

> Chúng tôi phát bảng hỏi, nhập dữ liệu, xử lý bằng SPSS.

Đoạn này mô tả thao tác nhưng không cho thấy logic phương pháp.

**2. Methods giấu điểm yếu**

Reviewer thường thích tác giả trung thực hơn là cố tạo cảm giác hoàn hảo. Nếu có giới hạn về chọn mẫu, công cụ, hoặc dữ liệu, hãy nói rõ ở mức phù hợp.

### Prompt viết Methods

> 📋 **Prompt Template — Methods Draft**
> ```
> Viết phần Methods dựa trên protocol sau:
> - Design: [type]
> - Participants/sample: [details]
> - Instruments/data sources: [details]
> - Procedure: [details]
> - Analysis: [details]
> - Ethics: [details]
> - AI tools used: [nếu có]
> 
> Yêu cầu:
> 1. Viết theo giọng học thuật, cô đọng
> 2. Không chỉ mô tả thao tác, phải thể hiện logic lựa chọn
> 3. Chỉ ra chỗ nào cần thêm thông tin để đủ tính tái lập
> 4. Gợi ý một câu disclosure nếu có dùng AI hỗ trợ
> ```

---

## 13.7 Results: Báo Cáo Chứ Không Bình Luận

Results là nơi bài báo rất dễ trượt sang hai thái cực:

- hoặc chỉ liệt kê số mà không có cấu trúc;
- hoặc giải thích quá nhiều, lấn sang Discussion.

### Results phải làm gì?

- tổ chức findings theo logic câu hỏi nghiên cứu hoặc giả thuyết;
- trình bày số liệu và mẫu hình quan trọng;
- gọi đúng bảng và figure;
- giữ giọng báo cáo khách quan.

### Results không nên làm gì?

- bàn luận tại sao lại như vậy;
- tuyên bố đóng góp lý thuyết;
- tranh luận với literature quá sớm;
- phóng đại ý nghĩa của thống kê.

### Một cấu trúc hữu ích cho Results

1. Mô tả mẫu hoặc dữ liệu chính.
2. Báo cáo finding cho RQ/H1.
3. Báo cáo finding cho RQ/H2.
4. Findings bổ sung, robustness checks, hoặc kết quả phụ nếu thật sự cần.

### Hãy để figure và table làm việc của chúng

Nguyên tắc:

- Bảng giữ con số chính xác.
- Figure giúp người đọc thấy mẫu hình.
- Đoạn văn dẫn người đọc qua điều quan trọng.

Nếu đoạn văn lặp lại toàn bộ số đã có trong bảng, phần Results sẽ nặng và chậm.

### Prompt viết Results

> 📋 **Prompt Template — Results Writer**
> ```
> Viết phần Results từ các đầu vào sau:
> - Research questions / hypotheses: [list]
> - Key statistics: [paste]
> - Tables: [list]
> - Figures: [list]
> 
> Yêu cầu:
> 1. Tổ chức theo logic RQ/H
> 2. Report số liệu chính xác, không diễn giải quá mức
> 3. Gọi đúng bảng/hình
> 4. Chỉ ra chỗ nào đang lặp lại thông tin đã có trong table/figure
> 5. Đề xuất một opening sentence cho Results
> ```

### Một câu hỏi tự kiểm

> Nếu bỏ hết phần Discussion đi, Results có vẫn cho người đọc biết “chuyện gì đã được tìm thấy” không?

Nếu chưa, Results còn mờ.

---

## 13.8 Discussion: Từ Finding Đến Ý Nghĩa

Discussion là phần khó nhất của nhiều bài báo. Đây là nơi bạn phải cho thấy mình không chỉ có dữ liệu, mà còn có phán đoán học thuật.

### Discussion cần làm gì?

- tóm tắt findings chính ở mức ngắn;
- giải thích ý nghĩa của findings;
- đối thoại với literature;
- nêu đóng góp lý thuyết, phương pháp, hoặc thực tiễn;
- thành thật về giới hạn;
- mở ra hướng nghiên cứu tiếp theo.

### Sự khác nhau giữa Results và Discussion

| Results | Discussion |
|---|---|
| Chuyện gì được tìm thấy | Điều đó có nghĩa gì |
| Tập trung vào bằng chứng | Tập trung vào diễn giải |
| Giữ giọng mô tả | Giữ giọng lập luận |
| Không đi xa khỏi dữ liệu | Có thể nối với lý thuyết và literature, nhưng phải có căn cứ |

### Một cấu trúc Discussion thường hiệu quả

1. Mở đầu bằng 2-3 câu chốt findings chính.
2. Lần lượt đi qua từng finding quan trọng.
3. Với mỗi finding:
   - nó nhất quán hay mâu thuẫn với literature nào;
   - điều đó gợi ý gì;
   - có cơ chế hoặc bối cảnh nào giải thích được không.
4. Nêu implications.
5. Nêu limitations.
6. Kết bằng một conclusion ngắn, có trọng lượng.

### Lỗi Discussion rất hay gặp

**1. Chỉ lặp lại Results bằng từ ngữ khác**

**2. So sánh literature quá rời rạc**

**3. Nói đóng góp quá lớn so với bằng chứng**

**4. Viết limitations như thủ tục cho có**

Limitations tốt không phải là tự dìm bài, mà là cho thấy bạn hiểu ranh giới của kết luận.

### Prompt viết Discussion

> 📋 **Prompt Template — Discussion Builder**
> ```
> Tôi cần viết Discussion cho bài báo:
> - Main findings: [list]
> - Literature để đối chiếu: [list]
> - Theoretical lens: [nếu có]
> - Practical context: [nếu có]
> 
> Hãy giúp tôi:
> 1. Tổ chức Discussion theo 3-5 cụm lập luận chính
> 2. Với mỗi cụm, chỉ ra literature nên đối thoại
> 3. Chỉ ra chỗ nào có nguy cơ lặp Results
> 4. Gợi ý phần limitations trung thực nhưng không tự phá bài
> 5. Viết một đoạn kết Discussion 4-5 câu
> ```

---

## 13.9 Abstract, Title, Keywords và Cover Letter

Nhiều bài tốt bị đánh giá thấp ngay từ đầu vì abstract và title không làm lộ được đóng góp.

### Abstract không phải mini-Introduction

Abstract phải là bản nén của toàn bộ bài:

- bối cảnh rất ngắn;
- mục tiêu rõ;
- phương pháp vừa đủ;
- findings chính;
- đóng góp hoặc hàm ý chính.

### Một abstract tốt cần trả lời

- Bài này nghiên cứu gì?
- Bằng cách nào?
- Tìm thấy gì?
- Điều đó quan trọng ở đâu?

### Title nên làm gì?

Title không cần “kêu”. Title cần:

- đúng trọng tâm;
- gợi rõ biến/chủ đề/bối cảnh;
- đủ cụ thể để người đúng cộng đồng nhận ra bài có liên quan.

### Keywords nên nghĩ chiến lược

Keywords không phải phần phụ. Chúng giúp bài được tìm thấy.

Hãy phối hợp:

- khái niệm rộng;
- khái niệm chuyên biệt;
- bối cảnh;
- phương pháp nếu thực sự quan trọng cho truy xuất.

### Cover letter có đáng chú ý không?

Có. Cover letter không nên dài, nhưng cần nói rõ:

- bài này phù hợp với journal vì sao;
- đóng góp chính là gì;
- bài chưa được gửi nơi khác;
- và nếu có dùng AI theo chính sách của journal, bạn đã khai báo ra sao.

### Prompt cho abstract và title

> 📋 **Prompt Template — Abstract & Title Pack**
> ```
> Dựa trên bài báo của tôi, hãy tạo:
> 1. 3 phương án title
> 2. 1 abstract 150-250 từ
> 3. 5-7 keywords
> 4. 1 cover letter ngắn cho journal target [name]
> 
> Lưu ý:
> - abstract phải có bối cảnh, mục tiêu, phương pháp, findings, implication
> - title không được quá chung chung
> - cover letter phải nêu rõ journal fit
> ```

---

## 13.10 AI Trong Quy Trình Viết: Biên Tập Viên, Không Phải Ghostwriter

Đây là phần cần nói thẳng. AI rất hữu ích trong writing pipeline, nhưng giá trị lớn nhất của nó không phải là tạo ra bản nháp nghe mượt. Giá trị lớn nhất là giúp bạn phát hiện chỗ yếu trong lập luận nhanh hơn.

### AI nên hỗ trợ ở đâu?

| Công việc | AI có thể giúp | Bạn phải giữ |
|---|---|---|
| Tạo outline | Đề xuất cấu trúc và khoảng trống | Chốt logic |
| Chuyển outline thành draft thô | Tăng tốc viết lần đầu | Kiểm soát luận điểm và bằng chứng |
| Polishing | Coherence, transitions, grammar, style | Giữ giọng học thuật và ý nghĩa |
| So sánh với literature | Gợi ý papers đối thoại | Kiểm chứng nguồn gốc |
| Citation audit | Phát hiện thiếu/sai | Xác nhận cuối bằng nguồn thật |
| Reviewer response | Soạn khung phản hồi | Quyết định thừa nhận/sửa/giữ |

### AI không nên làm gì?

- bịa citations;
- viết discussion thay cho tư duy của bạn;
- làm như bài có đóng góp lớn hơn thực tế;
- dùng ngôn ngữ bóng bẩy để che chỗ chưa chắc;
- tạo một “giọng học thuật giả” mà bạn không thể giải thích lại bằng miệng.

### Một nguyên tắc vàng

**Nếu bạn không thể nói lại luận điểm chính của mỗi section bằng lời của mình, section đó chưa thật sự thuộc về bạn.**

### Prompt dùng AI như biên tập viên

> 📋 **Prompt Template — Logic and Coherence Review**
> ```
> Đây là draft hiện tại của bài báo tôi:
> [paste]
> 
> Hãy review như một biên tập viên học thuật:
> 1. Luận điểm chính của bài là gì?
> 2. Chỗ nào Introduction chưa dẫn đủ vào gap?
> 3. Chỗ nào Results và Discussion đang lẫn nhau?
> 4. Chỗ nào đang phóng đại đóng góp?
> 5. Chỗ nào cần bằng chứng/literature thêm?
> 
> Không viết lại toàn bài; chỉ chẩn đoán và gợi ý sửa.
> ```

---

## 13.11 Citation Verification và Kiểm Soát Tính Chính Xác

Trước khi submit, reference list và trích dẫn trong bài phải được rà như một khâu bắt buộc, không phải phụ việc.

### Những lỗi rất hay gặp

- cite trong bài nhưng không có trong reference list;
- có trong reference list nhưng không cite;
- sai tên tác giả, năm, journal;
- trích dẫn một paper mà thực ra chưa đọc nguồn gốc;
- dùng secondary citation như primary citation.

### Citation audit nên làm ở 3 mức

**Mức 1: Hình thức**

- Đúng style journal chưa?
- In-text citation và reference list có khớp chưa?

**Mức 2: Tồn tại**

- Paper có thật không?
- Metadata có đúng không?

**Mức 3: Nội dung**

- Paper đó có thật sự nói điều bạn đang gán cho nó không?

### Prompt citation audit

> 📋 **Prompt Template — Citation Audit**
> ```
> Kiểm tra danh sách references và in-text citations sau:
> [paste]
> 
> Với mỗi reference:
> 1. Xác nhận tồn tại
> 2. Kiểm tra tác giả, năm, tiêu đề, journal
> 3. Đánh dấu thiếu/không khớp
> 4. Chỉ ra citation nào có nguy cơ đang bị diễn giải quá mức
> ```

> ⚠️ **Cảnh báo:** Không bao giờ trích dẫn chỉ từ trí nhớ của AI hoặc từ một bản tóm tắt AI-generated. Reviewer phát hiện những lỗi kiểu này rất nhanh.

---

## 13.12 Reviewer Comments, Revision và Đời Sống Sau Submission

Viết xong và gửi đi chưa phải là kết thúc. Đời sống thật của bài báo thường bắt đầu ở vòng phản hồi.

### Các kịch bản phổ biến

- Desk reject
- Reject after review
- Major revision
- Minor revision
- Accept with small edits

### Cách nhìn hữu ích về review

Reviewer comments không chỉ là danh sách lỗi. Chúng thường cho bạn biết:

- chỗ nào câu chuyện chưa rõ;
- chỗ nào phương pháp chưa thuyết phục;
- chỗ nào đóng góp chưa lộ;
- chỗ nào bạn và độc giả đang không gặp nhau.

### Response letter tốt cần gì?

- tôn trọng, rõ ràng, không phòng thủ;
- trả lời từng comment;
- nêu cụ thể đã sửa ở đâu;
- nếu không làm theo, phải giải thích có lý do.

### Bảng xử lý review gợi ý

| Reviewer comment | Type | Action | Location revised |
|---|---|---|---|
| “Gap is unclear” | Argument | Rewrite final paragraph of Introduction | p.2-3 |
| “Sample justification is weak” | Method | Add rationale and citation | Methods |
| “Discussion overstates causality” | Interpretation | Tone down claim, add limitation | Discussion |

### Prompt chuẩn bị reviewer response

> 📋 **Prompt Template — Reviewer Response Draft**
> ```
> Tôi nhận được reviewer comments như sau:
> [paste]
> 
> Hãy giúp tôi:
> 1. Phân loại comment: argument / method / evidence / style
> 2. Gợi ý hướng xử lý cho từng comment
> 3. Soạn draft response letter lịch sự, rõ ràng
> 4. Chỉ ra comment nào cần sửa bài thật sự, comment nào chỉ cần giải thích
> 5. Chỉ ra chỗ nào reviewer có thể hiểu sai vì bài viết chưa rõ
> ```

---

## 13.13 LaTeX: Từ Draft Đến Manuscript Sẵn Nộp

Hầu hết journal khoa học (IEEE, Springer, Elsevier, ACM, MDPI...) yêu cầu hoặc khuyến khích nộp bài bằng LaTeX. Nếu bạn chưa quen, đây là những gì cần biết để bắt đầu nhanh.

### Hai cách dùng LaTeX

| Lựa chọn | Khi nào dùng | Ưu điểm |
|----------|-------------|---------|
| **Overleaf** ([overleaf.com](https://www.overleaf.com)) | Mới bắt đầu, cần cộng tác real-time | Không cần cài đặt, có sẵn template journal, share link cho GVHD |
| **TeX Live local** | Cần compile offline, project lớn, tích hợp CI/CD | Nhanh hơn, không phụ thuộc internet, AI có thể đọc/ghi file `.tex` trực tiếp |

**Cài TeX Live (nếu chọn local):**

```bash
# macOS
brew install --cask mactex-no-gui

# Ubuntu/Debian
sudo apt install texlive-full

# Windows
# Tải từ https://tug.org/texlive/
```

### Cấu trúc project LaTeX chuẩn

```
paper/
├── main.tex            # File chính, \input từng section
├── sections/
│   ├── 01_introduction.tex
│   ├── 02_related_work.tex
│   ├── 03_methodology.tex
│   ├── 04_results.tex
│   └── 05_discussion.tex
├── figures/
│   ├── fig1_architecture.pdf
│   └── fig2_results.pdf
├── tables/
│   └── tab1_comparison.tex
├── references.bib      # BibTeX database
├── IEEEtran.cls        # Class file của journal (hoặc template khác)
└── Makefile             # Tùy chọn: tự động compile
```

### File `main.tex` mẫu (IEEE format)

```latex
\documentclass[conference]{IEEEtran}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cite}

\title{Your Paper Title Here}
\author{
  \IEEEauthorblockN{Nguyen Van A}
  \IEEEauthorblockA{University Name\\Email: a@uni.edu}
}

\begin{document}
\maketitle

\begin{abstract}
Your abstract here (150-250 words).
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\end{IEEEkeywords}

\input{sections/01_introduction}
\input{sections/02_related_work}
\input{sections/03_methodology}
\input{sections/04_results}
\input{sections/05_discussion}

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

### BibTeX: Quản lý references

File `references.bib` chứa tất cả nguồn trích dẫn:

```bibtex
@article{smith2024deep,
  title     = {Deep Learning for Channel Estimation in 6G},
  author    = {Smith, John and Nguyen, Thi B.},
  journal   = {IEEE Transactions on Communications},
  volume    = {72},
  number    = {3},
  pages     = {1234--1248},
  year      = {2024},
  doi       = {10.1109/TCOMM.2024.xxxxx}
}

@inproceedings{tran2025transformer,
  title     = {Transformer-Based Beamforming for ISAC Systems},
  author    = {Tran, Van C. and Le, Minh D.},
  booktitle = {IEEE ICC 2025},
  pages     = {100--105},
  year      = {2025}
}
```

**Trích dẫn trong text:** `\cite{smith2024deep}` → [1], `\cite{smith2024deep, tran2025transformer}` → [1], [2]

> 💡 **Tip:** Export BibTeX từ Google Scholar: bấm dấu `"` dưới mỗi bài → chọn BibTeX → copy vào file `.bib`.

### Compile LaTeX

```bash
# Compile cơ bản (3 bước để resolve references)
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Hoặc dùng latexmk (tự động)
latexmk -pdf main.tex
```

### AI hỗ trợ viết LaTeX: prompt thực tế

**1. Sinh LaTeX từ outline:**

> 📋 **Prompt Template — LaTeX Draft**
> ```text
> Tôi đang viết paper cho [tên journal/conference].
> Dưới đây là outline của section [Introduction/Methods/...]:
> [paste outline]
>
> Sinh LaTeX cho section này theo format [IEEEtran/Springer LNCS/Elsevier].
> Dùng \cite{} cho references, \ref{} cho figures/tables.
> Giữ giọng văn học thuật, tránh phóng đại.
> ```

**2. Tạo bảng LaTeX từ dữ liệu:**

> 📋 **Prompt Template — LaTeX Table**
> ```text
> Chuyển bảng sau sang LaTeX dùng booktabs (\toprule, \midrule, \bottomrule).
> Thêm caption và label. Format số với 2-3 chữ số thập phân.
>
> | Model | Accuracy | F1 | Params |
> |-------|----------|-----|--------|
> | CNN   | 0.923    | 0.91| 2.1M   |
> | ViT   | 0.948    | 0.94| 86M    |
> ```

**3. Debug lỗi compile:**

> 📋 **Prompt Template — LaTeX Debug**
> ```text
> LaTeX compile lỗi như sau:
> [paste error log]
>
> File liên quan:
> [paste đoạn code gây lỗi]
>
> Giải thích lỗi và sửa.
> ```

### Các lỗi LaTeX thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-------------|----------|
| `Undefined control sequence` | Thiếu `\usepackage` | Thêm package tương ứng |
| `Missing $ inserted` | Ký tự đặc biệt (`_`, `%`, `&`) ngoài math mode | Escape: `\_`, `\%`, `\&` |
| `Citation undefined` | Chưa chạy `bibtex` | Chạy đủ: pdflatex → bibtex → pdflatex × 2 |
| `Float too large` | Figure quá lớn | Thêm `[h!]` hoặc `[H]` (cần `\usepackage{float}`) |
| `Overfull hbox` | Text tràn lề | Dùng `\sloppy` hoặc chỉnh wording |

### Template journal phổ biến

| Publisher | Template | Link |
|-----------|----------|------|
| **IEEE** | IEEEtran | [ieee.org/conferences/publishing/templates](https://www.ieee.org/conferences/publishing/templates.html) |
| **Springer** | LNCS / svjour3 | [springer.com/gp/authors-editors/latex](https://www.springer.com/gp/computer-science/lncs/editor-guidelines/latex-templates) |
| **Elsevier** | elsarticle | [ctan.org/pkg/elsarticle](https://ctan.org/pkg/elsarticle) |
| **ACM** | acmart | [acm.org/publications/proceedings-template](https://www.acm.org/publications/proceedings-template) |
| **MDPI** | mdpi | [mdpi.com/authors/latex](https://www.mdpi.com/authors/latex) |

> 💡 **Overleaf có sẵn tất cả template trên** — search tên journal trong gallery sẽ ra ngay.

---

## 13.14 Bài Tập Thực Hành

### 🔧 Hands-on 13.1: Contribution Statement

Viết 5 câu:

- bài này nghiên cứu gì;
- gap là gì;
- tôi dùng phương pháp gì;
- finding chính là gì;
- đóng góp chính là gì.

Nếu 5 câu này chưa sắc, bài chưa nên đi vào polishing.

### 🔧 Hands-on 13.2: Section Separation Drill

Lấy một đoạn trong Results và một đoạn trong Discussion. Tự hỏi:

- đoạn Results có đang diễn giải không;
- đoạn Discussion có đang lặp lại số liệu không.

Sửa để hai phần tách chức năng thật rõ.

### 🔧 Hands-on 13.3: Journal Fit Matrix

Lập bảng so sánh 3 journal mục tiêu và quyết định:

- journal ưu tiên;
- journal dự phòng;
- điều chỉnh cần làm cho từng nơi.

### 🔧 Hands-on 13.4: Citation Audit

Kiểm tra ít nhất 15 references của chính bạn theo 3 mức:

- hình thức;
- tồn tại;
- nội dung.

### 🔧 Hands-on 13.5: Reviewer Simulation

Đưa abstract và outline Discussion vào AI, yêu cầu đóng vai reviewer khó tính. Ghi lại 5 phản biện mạnh nhất và thử sửa ngay trong draft.

---

## 13.15 Tóm Tắt Chương

Viết bài báo khoa học là quá trình nén một công trình nghiên cứu thành một lập luận học thuật đủ sắc để thuyết phục cộng đồng chuyên môn. Điều làm bài mạnh không phải là số lượng từ ngữ học thuật, mà là sự rõ ràng của gap, sự phù hợp của phương pháp, sự kỷ luật trong Results, và chiều sâu diễn giải trong Discussion. AI có thể giúp bạn đi nhanh hơn trong quá trình này, nhưng chỉ khi nó được dùng như một biên tập viên và bộ tăng lực cho tư duy, chứ không phải như người viết thay.

**Deliverable cuối chương:** đến đây, bạn nên có một `paper submission kit` gồm:

- contribution statement 5 câu;
- journal fit matrix;
- full draft theo IMRaD;
- abstract, title, keywords, cover letter;
- citation audit log;
- reviewer-response template cho vòng sửa bài.

Nếu công trình của bạn được công bố theo hướng paper-first, bộ này gần như là đầu ra trung tâm của cả dự án. Nếu bạn còn phải hoàn thiện luận văn hoặc luận án, đây sẽ là một lát cắt cô đọng giúp bạn bước sang `Chương 14` với một luận điểm đã được nén sắc và một bộ lập luận có thể tái dùng.

---

> 📖 **Tiếp theo:** [Chương 14: Viết Luận Văn/Luận Án →](chuong-14-viet-luan-van.md)

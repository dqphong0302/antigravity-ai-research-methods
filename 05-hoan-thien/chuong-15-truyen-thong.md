# Chương 15: Truyền Thông Khoa Học

![Science Communication](../assets/images/ch15_science_communication_1776092476293.png)

---

> *"Science that stays only inside a PDF has not finished its social life."*

---

Chương này hướng dẫn bạn biến 1 notebook nghiên cứu thành nhiều định dạng truyền thông cho nhiều đối tượng: podcast, slide, briefing doc, blog post, quiz, video — tất cả bằng **NotebookLM MCP** (`studio_create`). Đọc xong, bạn sẽ biết: **(1)** map audience → format phù hợp, **(2)** tạo từng loại artifact step-by-step, **(3)** kiểm soát để không diễn giải quá mức kết quả gốc.

Theo nghĩa đó, chương này nhận đầu vào trực tiếp từ `Chương 13` và `Chương 14`: paper, chapter, slide, notebook, figures, discussion đã chốt. Bạn sẽ truyền thông tốt hơn rất nhiều nếu xuất phát từ một bản diễn giải học thuật đã đủ chín, thay vì nhảy thẳng từ dữ liệu thô hoặc ghi chú rời sang nội dung cho công chúng.

---

## 15.1 Vì Sao Nhà Nghiên Cứu Phải Truyền Thông?

Nhiều người mặc định rằng công bố bài báo là đủ. Nhưng bài báo chỉ là một định dạng, không phải đích đến duy nhất của tri thức.

### Ba lý do cốt lõi

**1. Để tri thức được sử dụng**

Một phát hiện có thể rất mạnh trên phương diện học thuật nhưng vẫn không đi vào thực tiễn nếu người cần dùng nó không tiếp cận được. Ví dụ:

- nghiên cứu giáo dục không đến được giáo viên hoặc nhà trường;
- nghiên cứu chính sách không đến được đơn vị ra quyết định;
- nghiên cứu y tế công không đến được nhân viên tuyến đầu hoặc cộng đồng liên quan.

**2. Để nghiên cứu được hiểu đúng**

Khoảng trống giữa nghiên cứu gốc và cách công chúng hiểu về nghiên cứu là nơi rất nhiều sai lệch xuất hiện. Nếu chính tác giả không tham gia giải thích, người khác có thể kể thay bạn bằng một phiên bản đơn giản quá mức, giật gân quá mức, hoặc lệch khỏi giới hạn thật của công trình.

**3. Để mở rộng tác động của công trình**

Một công trình mạnh có thể sống dưới nhiều hình thức:

- bài báo cho cộng đồng chuyên môn;
- briefing note cho người ra quyết định;
- bài giảng cho sinh viên;
- slide deck cho seminar;
- podcast hoặc bài viết phổ thông cho công chúng.

> 💡 **Điểm dừng để suy nghĩ:** Truyền thông khoa học không phải “làm màu sau nghiên cứu”. Nó là phần tiếp nối của trách nhiệm nghiên cứu.

### Truyền thông không có nghĩa là đơn giản hóa vô điều kiện

Mục tiêu của truyền thông khoa học không phải là làm mọi thứ trở nên “ngắn và dễ nghe” bằng mọi giá. Mục tiêu là:

- giữ thông điệp cốt lõi;
- bỏ bớt tầng kỹ thuật không cần thiết với người nghe cụ thể;
- nhưng không bóp méo mức chắc chắn, phạm vi áp dụng, hay giới hạn của kết quả.

Đó là ranh giới giữa truyền thông tốt và truyền thông nguy hiểm.

---

## 15.2 Bắt Đầu Từ Audience, Không Bắt Đầu Từ Công Cụ

![Audience Mapping — Từ nghiên cứu đến các nhóm đối tượng](../assets/images/ch15_audience_mapping_1776094103464.png)

Sai lầm phổ biến nhất là hỏi: “tôi nên làm podcast hay infographic?”. Câu hỏi đúng phải là: “tôi cần nói với ai, để họ làm gì, và họ cần nhớ điều gì?”

### 4 nhóm audience thường gặp

| Audience | Họ cần gì? | Họ quan tâm nhất điều gì? | Dạng truyền thông phù hợp |
|---|---|---|---|
| Đồng nghiệp học thuật | Logic nghiên cứu, phương pháp, đóng góp | Độ tin cậy và tính mới | Paper, conference slides, seminar deck |
| Người ra quyết định/quản lý | Kết quả chính và hàm ý hành động | Ảnh hưởng thực tiễn, chi phí, ưu tiên | Briefing doc, policy memo, executive summary |
| Sinh viên/người học | Hiểu khái niệm và logic nghiên cứu | Tính rõ ràng, tính sư phạm | Slide, podcast, quiz, flashcards |
| Công chúng | Vì sao nghiên cứu này quan trọng với đời sống | Tính gần gũi, dễ hiểu, không jargon | Blog post, explainer video, podcast ngắn |

### Ba câu hỏi phải trả lời trước khi tạo bất kỳ format nào

1. Audience này đã biết gì?
2. Audience này cần biết gì thêm?
3. Sau khi tiếp cận nội dung, họ cần làm gì, nghĩ gì, hoặc nhớ gì?

### Một nghiên cứu, nhiều mục đích

Ví dụ cùng là một nghiên cứu về burnout của giáo viên:

- Với đồng nghiệp: bạn nhấn vào design, sampling, coding, và so sánh với literature.
- Với hiệu trưởng hoặc Sở GD: bạn nhấn vào mô hình hỗ trợ, tín hiệu cảnh báo, và khuyến nghị khả thi.
- Với công chúng: bạn nhấn vào trải nghiệm của giáo viên, hậu quả với chất lượng dạy học, và điều cần tránh khi diễn giải nguyên nhân.

Thông tin gốc không đổi. Cách kể thay đổi.

### Prompt xác định audience-fit

> 📋 **Prompt Template — Audience Mapping**
> ```
> Tôi muốn truyền thông nghiên cứu về [topic].
> 
> Hãy giúp tôi phân tích 4 audience:
> 1. Đồng nghiệp học thuật
> 2. Nhà quản lý / người ra quyết định
> 3. Sinh viên / người học
> 4. Công chúng
> 
> Với mỗi audience, chỉ ra:
> - Điều họ quan tâm nhất
> - Điều tôi nên nhấn mạnh
> - Điều tôi nên lược bỏ
> - Mức độ thuật ngữ có thể dùng
> - Format phù hợp nhất
> ```

---

## 15.3 Một Nghiên Cứu, Nhiều Phiên Bản: Khung "Core Message"

Để truyền thông tốt, trước hết bạn phải rút được **thông điệp lõi** của nghiên cứu.

### Core message là gì?

Đó là câu trả lời ngắn gọn cho ba điểm:

- nghiên cứu này hỏi điều gì;
- phát hiện chính là gì;
- và tại sao nó đáng quan tâm.

Nếu bạn không nói được core message trong 3-4 câu, mọi phiên bản truyền thông sau đó rất dễ bị loãng.

### Công thức đơn giản

```text
Nghiên cứu này xem xét [vấn đề]
trong bối cảnh [đối tượng/bối cảnh].
Kết quả cho thấy [finding chính],
điều này gợi ý [ý nghĩa hoặc hàm ý].
```

### Ví dụ song hành

#### 🧪 Ví dụ Tự Nhiên: STEM education

“Nghiên cứu này xem xét tác động của mô hình dạy học STEM dự án đối với năng lực giải quyết vấn đề của học sinh THPT. Kết quả cho thấy tác động tích cực xuất hiện rõ ở các trường có mức hỗ trợ triển khai cao. Điều này gợi ý rằng hiệu quả của STEM không chỉ nằm ở mô hình dạy học, mà còn phụ thuộc mạnh vào điều kiện tổ chức.”

#### 📊 Ví dụ Xã Hội: Burnout giáo viên

“Nghiên cứu này xem xét trải nghiệm burnout của giáo viên tiểu học sau đại dịch. Kết quả cho thấy kiệt sức không chỉ đến từ khối lượng công việc, mà còn từ cảm giác thiếu kiểm soát và thiếu hỗ trợ chuyên môn. Điều này gợi ý rằng các giải pháp chỉ giảm giờ làm có thể chưa đủ.”

### Từ core message sang message ladder

Khi đã có thông điệp lõi, bạn có thể tạo các lớp thông điệp:

- **Phiên bản 1 câu**: cho mở đầu slide hoặc phần giới thiệu;
- **Phiên bản 1 đoạn**: cho abstract phổ thông, briefing note;
- **Phiên bản 3 phút**: cho podcast ngắn hoặc video overview;
- **Phiên bản 10-15 phút**: cho seminar hoặc conference talk.

> ⚠️ **Cảnh báo:** Đừng để AI tạo 5 định dạng khác nhau trước khi bạn tự chốt core message. Nếu không, bạn sẽ có 5 sản phẩm nhất quán về câu chữ nhưng lệch về nội dung.

---

## 15.4 Truyền Thông Khoa Học Có Trách Nhiệm

Đây là phần quyết định phẩm chất của chương này. Truyền thông mạnh không chỉ là dễ hiểu; nó còn phải trung thực.

### Bốn rủi ro rất hay gặp

**1. Thổi phồng mức chắc chắn**

Ví dụ từ “có liên quan” thành “gây ra”, từ “một nghiên cứu nhỏ” thành “đã chứng minh”, từ “cho thấy xu hướng” thành “khẳng định”.

**2. Giật tít để gây chú ý**

Đây là lỗi rất dễ xảy ra khi chuyển nghiên cứu sang social media hoặc blog post. Một tiêu đề hấp dẫn là cần thiết, nhưng tiêu đề không được vượt quá điều dữ liệu cho phép.

**3. Bỏ mất giới hạn nghiên cứu**

Công chúng và cả nhà quản lý thường không đọc methods section. Vì vậy, nếu bạn không chủ động nêu giới hạn trong ngôn ngữ dễ hiểu, người tiếp nhận sẽ tưởng kết quả có thể áp dụng rộng hơn thực tế.

**4. Đơn giản hóa đến mức sai bản chất**

Ví dụ:

- biến một hiện tượng đa nguyên nhân thành một nguyên nhân duy nhất;
- kể một nghiên cứu định tính như thể là “đại diện cho tất cả mọi người”;
- hoặc nén một nghiên cứu hỗn hợp thành đúng một slogan.

### Một checklist rất hữu ích trước khi xuất bản nội dung truyền thông

- Tôi có đang dùng từ mạnh hơn mức dữ liệu cho phép không?
- Tôi có đang biến tương quan thành quan hệ nhân quả không?
- Tôi đã nêu giới hạn chính bằng ngôn ngữ dễ hiểu chưa?
- Audience có thể hiểu nhầm điều gì từ nội dung này?
- Nếu chính reviewer của bài báo đọc bản truyền thông này, tôi có thấy xấu hổ không?

### Prompt kiểm tra rủi ro truyền thông

> 📋 **Prompt Template — Communication Risk Audit**
> ```
> Đây là bản truyền thông nghiên cứu của tôi:
> [paste nội dung]
> 
> Hãy kiểm tra theo 5 tiêu chí:
> 1. Có chỗ nào thổi phồng mức chắc chắn không?
> 2. Có chỗ nào biến tương quan thành nhân quả không?
> 3. Có giới hạn quan trọng nào đang bị bỏ mất không?
> 4. Audience phổ thông có thể hiểu sai chỗ nào?
> 5. Hãy đề xuất phiên bản trung thực hơn nhưng vẫn dễ tiếp cận.
> ```

---

## 15.5 Từ Bài Báo/Notebook Thành Các Định Dạng Cụ Thể

![Multi-Format Output — Một nghiên cứu, nhiều định dạng](../assets/images/ch15_multi_format_1776094117072.png)

Sau khi chốt audience và core message, lúc đó công cụ mới thật sự phát huy tác dụng.

### Workflow tổng quát với Antigravity

1. Gom nguồn gốc đáng tin vào một notebook hoặc một thư mục làm việc rõ ràng.
2. Chốt core message cho từng audience.
3. Chọn format phù hợp.
4. Tạo bản nháp bằng AI.
5. Tự rà lại theo checklist trách nhiệm truyền thông.
6. Chỉnh tay để thêm giọng người viết, bối cảnh, và lưu ý giới hạn.

### Các nguồn nên đưa vào notebook

- bài báo cuối cùng;
- slides hoặc outline seminar;
- bảng kết quả và figure đã được kiểm chứng;
- đoạn discussion hoặc kết luận mạnh nhất;
- nếu cần, cả policy documents hoặc nền bối cảnh để AI không kể câu chuyện quá “trôi nổi”.

### Một nguyên tắc rất quan trọng

**Đừng để AI truyền thông từ dữ liệu thô nếu bạn đã có bản diễn giải học thuật tốt hơn.** Hãy cho nó bám vào phiên bản bạn đã kiểm chứng, chẳng hạn:

- phần kết quả đã được bạn rà;
- discussion đã chốt;
- executive summary do bạn soạn.

Như vậy sản phẩm truyền thông sẽ grounded hơn rất nhiều.

---

## 15.6 Podcast, Audio Overview và Nội Dung Dạng Nghe

Podcast rất hữu ích vì nó giúp nghiên cứu đi ra khỏi định dạng văn bản dày đặc. Nhưng podcast không phù hợp với mọi mục đích.

### Khi nào podcast phù hợp?

- Seminar nhóm nghiên cứu
- Tóm tắt cho người ngoài ngành
- Nội dung bồi dưỡng hoặc học tập
- Tạo “cửa vào” trước khi người nghe đọc sâu hơn

### Ba kiểu podcast hữu ích

**1. Deep dive**

Phù hợp khi audience đã có nền và cần nghe mạch vấn đề, kết quả, tranh luận, hàm ý.

**2. Brief overview**

Phù hợp với công chúng hoặc người cần nắm nhanh nội dung.

**3. Debate / contrasting perspectives**

Phù hợp khi nghiên cứu chạm vào một tranh luận hoặc có kết quả dễ gây hiểu lầm.

### Prompt tạo podcast nghiên cứu

> 📋 **Prompt Template — Research Podcast**
> ```
> Tạo audio overview cho nghiên cứu của tôi:
> - Topic: [topic]
> - Audience: [đồng nghiệp / sinh viên / công chúng]
> - Format: [deep dive / brief / debate]
> - Length: [5 / 10 / 15] phút
> 
> Yêu cầu:
> 1. Giải thích vấn đề bằng ngôn ngữ phù hợp với audience
> 2. Nêu findings chính
> 3. Có 1 đoạn nói rõ giới hạn nghiên cứu
> 4. Kết thúc bằng "vì sao điều này đáng quan tâm"
> ```

### Điều phải rà lại sau khi AI tạo audio script

- có câu nào nghe quá tự tin không;
- có chỗ nào biến nuance thành slogan không;
- người nghe có thể phân biệt rõ đâu là finding, đâu là diễn giải không.

---

## 15.7 Slide Deck, Seminar và Conference Presentation

Slide không phải là bản thu nhỏ của luận văn. Một bộ slide tốt làm được một việc: giữ người nghe nhìn đúng vào thông điệp chính ở mỗi thời điểm.

### Quy tắc "mỗi slide một ý"

Nếu một slide chứa ba ý lớn, khán giả thường không nhớ được ý nào. Với nội dung nghiên cứu, mỗi slide nên trả lời một câu hỏi:

- vấn đề là gì;
- khoảng trống ở đâu;
- tôi đã làm gì;
- tôi tìm thấy gì;
- điều đó có nghĩa gì.

### Cấu trúc presentation thường dùng

| Bối cảnh sử dụng | Số slide gợi ý | Điều nên nhấn mạnh |
|---|---:|---|
| Lab meeting / seminar nội bộ | 8-12 | Logic thiết kế, điểm chưa chắc, xin phản hồi |
| Conference presentation | 10-15 | Research gap, methods, findings, contribution |
| Defense / bảo vệ | 12-15 | Tính nhất quán toàn công trình và năng lực bảo vệ quyết định |
| Teaching session | 8-10 | Khái niệm, ví dụ, bài học |

### Prompt tạo slide deck

> 📋 **Prompt Template — Conference Presentation**
> ```
> Tạo slide deck cho nghiên cứu của tôi:
> - Audience: [conference / seminar / lớp học]
> - Duration: [x] phút
> - Topic: [topic]
> 
> Tôi cần:
> 1. Outline 10-15 slide
> 2. Mỗi slide có 1 thông điệp chính
> 3. Chỉ ra slide nào nên dùng bảng, hình, hay trích dẫn
> 4. Gợi ý câu nói mở đầu và câu kết
> 5. Chỉ ra 3 slide có nguy cơ quá tải nội dung
> ```

### Sai lầm phổ biến của slide nghiên cứu

- đưa nguyên cả đoạn literature review lên slide;
- trình bày phương pháp quá kỹ nhưng không nói rõ vì sao nó quan trọng;
- cho kết quả nhiều nhưng không chốt insight;
- thiếu slide giới hạn nghiên cứu hoặc hàm ý.

---

## 15.8 Briefing Document, Policy Memo và Executive Summary

Đây là định dạng cực kỳ quan trọng nhưng thường bị đánh giá thấp. Một policy brief tốt có thể tác động thực tiễn mạnh hơn một bài báo rất hay nhưng chỉ nằm trong journal.

### Audience của briefing doc khác gì với audience học thuật?

Người ra quyết định thường không hỏi:

- “mô hình lý thuyết của bạn đóng góp gì cho tranh luận X?”

Họ hỏi:

- “vấn đề là gì?”
- “kết quả đáng tin đến đâu?”
- “nên làm gì tiếp theo?”
- “nếu chỉ ưu tiên một việc, đó là việc gì?”

### Cấu trúc briefing doc ngắn gọn

| Phần | Nội dung |
|---|---|
| Vấn đề | Vì sao nên quan tâm ngay bây giờ |
| Kết quả chính | 2-4 phát hiện quan trọng nhất |
| Điều cần hiểu đúng | Giới hạn hoặc điều không nên suy diễn |
| Hàm ý hành động | 3-5 gợi ý khả thi |
| Nếu cần | Nguồn dữ liệu, phương pháp ngắn gọn |

### Prompt tạo briefing document

> 📋 **Prompt Template — Research Briefing Doc**
> ```
> Tạo briefing document từ nghiên cứu của tôi:
> - Topic: [topic]
> - Audience: nhà quản lý / người ra quyết định
> - Length: 1-2 trang
> 
> Yêu cầu:
> 1. Mở bằng vấn đề thực tiễn
> 2. Tóm tắt 3 findings chính
> 3. Nói rõ điều nghiên cứu này KHÔNG khẳng định
> 4. Đề xuất 3 khuyến nghị hành động khả thi
> 5. Tránh jargon học thuật
> ```

### Một cảnh báo quan trọng

Khuyến nghị chính sách không được đi xa hơn bằng chứng. Nhiều nghiên cứu chỉ đủ để gợi ý định hướng, chưa đủ để kết luận nên ban hành một giải pháp ở quy mô lớn.

---

## 15.9 Blog Post, Video Giải Thích và Nội Dung Cho Công Chúng

Truyền thông cho công chúng là nơi AI rất dễ tạo ra nội dung “nghe hay nhưng mỏng”. Vì vậy bạn càng phải kiểm soát kỹ.

### Điều công chúng cần không giống điều reviewer cần

Công chúng thường cần:

- bối cảnh gần gũi;
- ví dụ dễ hình dung;
- ít thuật ngữ;
- câu trả lời cho câu “chuyện này liên quan gì đến tôi?”

Nhưng điều đó không có nghĩa là được hy sinh độ trung thực.

### Blog post tốt thường có 4 phần

1. Một câu hỏi hoặc tình huống mở đầu gần gũi.
2. Vấn đề nghiên cứu được giải thích bằng ngôn ngữ thường.
3. Findings chính được kể bằng 2-3 điểm rõ ràng.
4. Một đoạn nêu giới hạn hoặc điều không nên hiểu quá mức.

### Video overview phù hợp khi nào?

- Khi chủ đề cần hình ảnh minh họa;
- Khi muốn tiếp cận sinh viên hoặc người xem mạng xã hội;
- Khi cần tăng khả năng chia sẻ ngoài môi trường học thuật.

### Prompt tạo blog post / explainer

> 📋 **Prompt Template — Public-Facing Summary**
> ```
> Chuyển nghiên cứu của tôi thành bản truyền thông cho công chúng:
> - Format: [blog post / video script]
> - Audience: người không chuyên
> - Length: [600-800 từ / 3-5 phút]
> 
> Yêu cầu:
> 1. Mở đầu bằng một tình huống gần gũi
> 2. Giải thích nghiên cứu bằng ngôn ngữ đơn giản
> 3. Nêu 2-3 findings chính
> 4. Có một đoạn "điều nghiên cứu này chưa thể kết luận"
> 5. Tránh headline giật gân
> ```

### Dấu hiệu cho thấy bản truyền thông đang quá tay

- tiêu đề nghe như quảng cáo;
- mọi phát hiện đều được kể như “đột phá”;
- không còn dấu vết nào của giới hạn nghiên cứu;
- khuyến nghị nghe như “công thức áp dụng cho tất cả”.

---

## 15.10 Dùng Nghiên Cứu Cho Giảng Dạy: Quiz, Flashcards, Mind Map

Nếu bạn cũng giảng dạy, đây là một cơ hội rất lớn. Một nghiên cứu của bạn có thể trở thành tài liệu học tập sống động cho sinh viên.

### Tại sao phần này có ý nghĩa?

Vì nó biến nghiên cứu từ một sản phẩm “để nộp” thành một nguồn lực học tập:

- giúp sinh viên thấy nghiên cứu thật vận hành thế nào;
- kéo gần khoảng cách giữa lý thuyết và dữ liệu;
- và giúp chính bạn hiểu nghiên cứu của mình sâu hơn, vì dạy lại luôn là một cách kiểm chứng hiểu biết.

### Ba định dạng hữu ích

**1. Quiz**

Phù hợp để kiểm tra khái niệm, logic phương pháp, hoặc hiểu kết quả.

**2. Flashcards**

Phù hợp để giới thiệu nhanh thuật ngữ, framework, hoặc những điểm cần nhớ.

**3. Mind map**

Phù hợp để cho thấy cấu trúc ý tưởng của công trình, đặc biệt hữu ích với sinh viên mới học phương pháp nghiên cứu.

### Prompt tạo teaching materials

> 📋 **Prompt Template — Teaching Materials**
> ```
> Tạo teaching materials từ nghiên cứu của tôi:
> - Topic: [topic]
> - Audience: sinh viên [năm / bậc học]
> 
> Tôi cần:
> 1. Quiz 10 câu
> 2. 10 flashcards cho các khái niệm chính
> 3. Một mind map tóm tắt logic nghiên cứu
> 4. Chỉ ra 3 chỗ sinh viên dễ hiểu sai nhất
> ```

### Lưu ý

Teaching materials không nên chỉ hỏi “finding là gì”. Hãy ưu tiên câu hỏi giúp sinh viên hiểu:

- vì sao chọn phương pháp đó;
- logic của research gap;
- mối quan hệ giữa dữ liệu và diễn giải.

---

## 15.11 Chiến Lược Phổ Biến Đa Định Dạng

Điểm mạnh lớn nhất của AI không phải là tạo ra một sản phẩm duy nhất, mà là cho phép bạn triển khai một **hệ phổ biến nhiều lớp** từ cùng một lõi nghiên cứu.

### Một chiến lược đơn giản nhưng hiệu quả

| Tầng | Format | Audience | Mục tiêu |
|---|---|---|---|
| Tầng 1 | Paper / thesis chapter | Học thuật | Đóng góp chuyên môn |
| Tầng 2 | Slide deck / seminar talk | Đồng nghiệp / hội thảo | Thảo luận, phản biện, lan tỏa trong giới chuyên môn |
| Tầng 3 | Briefing doc | Nhà quản lý | Dịch findings thành hàm ý hành động |
| Tầng 4 | Blog / podcast / video | Công chúng | Tăng khả năng tiếp cận và hiểu đúng |
| Tầng 5 | Quiz / flashcards / mind map | Sinh viên | Tái sử dụng cho giảng dạy |

### Một nghiên cứu có thể đi theo lộ trình này

1. Hoàn thiện paper hoặc chapter chính.
2. Tạo seminar slides để trình bày trong nhóm nghiên cứu.
3. Từ đó rút ra một briefing note 1-2 trang.
4. Chuyển briefing thành blog post hoặc video script dễ hiểu hơn.
5. Cuối cùng tái sử dụng thành material cho lớp học.

Đây là cách để một công trình sống lâu hơn, đi xa hơn, và không bị khóa trong một định dạng duy nhất.

### Prompt tạo dissemination plan

> 📋 **Prompt Template — Multi-Format Dissemination Strategy**
> ```
> Hãy tạo kế hoạch phổ biến đa định dạng cho nghiên cứu của tôi:
> - Topic: [topic]
> - 3 audience ưu tiên: [list]
> - Nguồn hiện có: [paper / thesis chapter / notebook / slides]
> 
> Tôi cần:
> 1. 3-5 format phù hợp
> 2. Mục tiêu của từng format
> 3. Format nào nên làm trước
> 4. Những rủi ro truyền thông của từng format
> 5. Một lịch triển khai trong 4 tuần
> ```

---

## 15.12 Bài Tập Thực Hành

### 🔧 Hands-on 15.1: Core Message Drill

Viết 3 phiên bản của cùng một nghiên cứu:

- 1 câu;
- 1 đoạn 100 từ;
- 1 bản nói 3 phút.

Nếu ba phiên bản này nói những điều quá khác nhau, bạn chưa chốt được thông điệp lõi.

### 🔧 Hands-on 15.2: Audience Translation

Chọn một nghiên cứu của bạn và viết:

- 1 abstract học thuật ngắn;
- 1 briefing note cho nhà quản lý;
- 1 đoạn giải thích cho công chúng.

So sánh xem điều gì thay đổi và điều gì phải giữ nguyên.

### 🔧 Hands-on 15.3: Communication Risk Audit

Lấy một bài post, video script, hoặc bài nói đã tạo bằng AI. Chạy lại qua checklist ở Mục 15.4 và ghi ra:

- 3 chỗ có nguy cơ thổi phồng;
- 2 chỗ bỏ mất giới hạn;
- 1 chỗ cần thay bằng ngôn ngữ trung thực hơn.

### 🔧 Hands-on 15.4: Dissemination Plan

Tạo kế hoạch 4 tuần cho chính nghiên cứu của bạn:

- tuần 1: format học thuật;
- tuần 2: format seminar;
- tuần 3: format policy/public;
- tuần 4: format teaching.

Mỗi tuần phải nêu rõ:

- sản phẩm;
- audience;
- thông điệp lõi;
- tiêu chí kiểm tra chất lượng.

---

## 15.13 Tóm Tắt Chương

Truyền thông khoa học không phải là bước “trang trí” sau nghiên cứu. Nó là phần tiếp nối của trách nhiệm học thuật: giúp tri thức được dùng, được hiểu đúng, và đi đến đúng người. AI làm cho việc tạo nhiều định dạng trở nên nhanh hơn, nhưng tốc độ chỉ có ý nghĩa khi bạn bắt đầu từ audience, chốt được core message, và luôn giữ kỷ luật trung thực với dữ liệu, giới hạn, và mức chắc chắn của kết quả.

**Deliverable cuối chương:** đến đây, bạn nên có một `research communication kit` gồm:

- core message của nghiên cứu;
- audience map;
- ít nhất 3 phiên bản truyền thông cho 3 audience khác nhau;
- 1 checklist kiểm tra rủi ro diễn giải sai;
- 1 dissemination plan 4 tuần.

Nhưng bộ này chỉ thực sự hoàn chỉnh khi nó đi cùng một lớp tự kiểm đạo đức đủ mạnh. Vì càng truyền thông rộng, nguy cơ diễn giải quá tay, giản lược quá mức, hay làm mờ giới hạn nghiên cứu càng tăng. Đó là lý do `Chương 16` không phải phần phụ lục đạo đức, mà là điểm chốt để giữ toàn bộ vòng đời công trình đứng vững.

---

> 📖 **Tiếp theo:** [Chương 16: Đạo Đức Nghiên Cứu Với AI →](chuong-16-dao-duc.md)

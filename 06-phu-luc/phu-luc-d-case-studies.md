# Phụ Lục D: Case Studies Minh Họa Theo Workflow

![Case Studies](../assets/images/appendix_d_case_studies_1776094002182.png)

---

> *Case study tốt không hứa rằng workflow sẽ luôn trơn tru. Nó cho thấy người nghiên cứu đã phải quyết định, kiểm tra, và sửa sai ở đâu.*

---

Ba case dưới đây là **case tổng hợp** từ những kiểu dự án rất thường gặp. Chúng không nhằm hứa hẹn kết quả đẹp, thời gian thần tốc, hay "cứ làm theo là thành công". Mục tiêu của phụ lục này là cho thấy Antigravity có thể đi vào workflow nghiên cứu ở đâu, nhưng cũng cho thấy:

- chỗ nào con người vẫn phải tự quyết;
- chỗ nào verification tốn công hơn tưởng tượng;
- chỗ nào phải cắt scope để cứu dự án;
- và chỗ nào AI chỉ thật sự hữu ích sau khi logic học thuật đã đủ rõ.

## D.1 Case 1: Định Lượng Trong Giáo Dục STEM

### Bối cảnh

- Người nghiên cứu: học viên cao học ngành giáo dục
- Mối quan tâm ban đầu: dạy học STEM ở bậc THPT
- Dạng nghiên cứu sau cùng: quasi-experimental study quy mô vừa

### Điểm xuất phát

Ở giai đoạn đầu, người nghiên cứu có một ý tưởng khá rộng: "so sánh hiệu quả của dạy STEM với dạy truyền thống". Vấn đề là ý tưởng này quá lớn và quá mơ hồ:

- chưa chốt outcome chính là gì;
- chưa rõ can thiệp sẽ kéo dài bao lâu;
- chưa biết trường nào thật sự cho phép triển khai;
- và chưa biết nên đo hiệu quả học tập, thái độ, hay cả hai.

### AI đã giúp gì ở giai đoạn đầu?

Antigravity hữu ích nhất ở ba việc:

1. quét nhanh landscape của field để biết những outcome nào hay được dùng;
2. gom các thang đo và thiết kế quasi-experimental thường gặp;
3. dựng trước một `RQ-to-design map` để thấy chỗ nào đang hứa quá sức.

Ví dụ prompt kiểu này tỏ ra hữu ích:

```text
Tôi đang cân nhắc nghiên cứu về hiệu quả của dạy học STEM ở THPT.
Hãy giúp tôi:
1. liệt kê 3 outcome phổ biến và điểm mạnh/yếu của từng outcome;
2. gợi ý thiết kế phù hợp nếu tôi chỉ tiếp cận được 2 trường;
3. chỉ ra rủi ro nếu tôi cố đo quá nhiều thứ cùng lúc.
```

### Chỗ AI không thể làm thay

Sau khi có gợi ý, người nghiên cứu vẫn phải tự chốt:

- outcome nào là trung tâm;
- trường nào thật sự có thể phối hợp;
- nhóm đối chứng có khả thi không;
- mức can thiệp nào đủ để còn diễn giải được kết quả.

Điểm khó nhất không phải chọn test thống kê. Điểm khó nhất là **cắt bớt tham vọng** để thiết kế còn sống được trong điều kiện thật.

### Chỗ dự án suýt đi lệch

Ban đầu người nghiên cứu định:

- đo thành tích học tập;
- đo thái độ với STEM;
- đo self-efficacy;
- và thêm một survey cho giáo viên.

Antigravity giúp nhìn ra thiết kế nghe có vẻ giàu dữ liệu, nhưng khi đưa vào timeline thật thì:

- instrument quá dài;
- nguy cơ missing data cao;
- và power cho nhiều outcome cùng lúc trở nên khó kiểm soát.

Kết quả là đề tài được thu lại còn:

- một outcome học tập chính;
- một outcome thái độ phụ;
- và protocol thu dữ liệu rõ hơn.

### Verification overhead

Một điểm dễ bị đánh giá thấp là phần kiểm chứng:

- các thang đo gợi ý bởi AI phải truy về nguồn gốc;
- các thông số sample size phải được tự chạy lại;
- mọi câu mô tả kết quả sau phân tích đều phải so lại với output thật;
- figure do AI/code gợi ý vẫn phải tự rà trục, nhãn, caption.

Nói cách khác, AI làm bước chuẩn bị nhanh hơn, nhưng **không làm biến mất công việc kiểm soát chất lượng**.

### Trạng thái cuối cùng của dự án

Case này kết thúc không phải bằng một câu chuyện "thần kỳ", mà bằng một bộ deliverable đủ mạnh để đi tiếp:

- một quasi-experimental design đủ gọn;
- bộ instrument đã pilot ở mức cơ bản;
- dataset được tổ chức tốt;
- analysis plan rõ;
- và một draft Results/Discussion có thể phát triển thành paper hoặc chapter.

### Bài học chính

- Thiết kế định lượng mạnh lên chủ yếu nhờ cắt đúng, không nhờ thêm thật nhiều biến.
- Prompt tốt nhất ở case này là prompt giúp thu hẹp thiết kế, không phải prompt giúp làm nó nghe lớn hơn.
- AI hữu ích nhất khi đứng ở vai trò stress-test logic và chuẩn hóa workflow.

---

## D.2 Case 2: Định Tính Về Burnout Của Giáo Viên

### Bối cảnh

- Người nghiên cứu: học viên thạc sĩ ngành tâm lý học giáo dục
- Mối quan tâm ban đầu: burnout của giáo viên sau đại dịch
- Dạng nghiên cứu sau cùng: nghiên cứu định tính với phỏng vấn bán cấu trúc

### Điểm xuất phát

Ý tưởng ban đầu nghe hợp lý: phỏng vấn giáo viên về burnout. Nhưng ngay sau vài buổi đầu, người nghiên cứu gặp ba vấn đề:

- burnout là khái niệm quen thuộc nhưng trải nghiệm thực tế rất đa dạng;
- ngôn ngữ mà giáo viên dùng để mô tả vấn đề không hoàn toàn trùng với ngôn ngữ lý thuyết;
- và bộ interview guide đầu tiên hơi giống bảng hỏi mở rộng hơn là công cụ lắng nghe trải nghiệm.

### AI đã giúp gì?

Antigravity hữu ích nhất ở các bước:

- so sánh các approach định tính có thể dùng;
- tạo draft interview guide đầu tiên;
- gợi ý cách nhóm open codes ban đầu;
- tạo khung trustworthiness checklist để người nghiên cứu tự rà.

Ví dụ prompt hữu ích:

```text
Tôi muốn nghiên cứu trải nghiệm burnout của giáo viên tiểu học.
Hãy giúp tôi:
1. so sánh phenomenology với case study cho đề tài này;
2. chỉ ra dữ liệu loại nào sẽ phù hợp hơn với từng approach;
3. gợi ý một interview guide bản nháp nhưng giữ câu hỏi đủ mở.
```

### Chỗ AI dễ bị dùng sai

Ở giai đoạn coding, mô hình có thể tạo ra draft codes rất nhanh. Nhưng nếu nhận hết các code đó mà không tự đọc kỹ transcript, người nghiên cứu sẽ gặp hai rủi ro:

- codes nghe rất hợp lý nhưng bị "bình thường hóa" theo các nhãn quen thuộc;
- những điểm lệch, đau, hoặc mâu thuẫn trong trải nghiệm bị làm mờ đi.

Trong case này, cách dùng đúng là:

- để AI gợi ý draft open codes cho từng đoạn nhỏ;
- người nghiên cứu tự sửa, gộp, bỏ, đổi tên;
- và giữ analytic memo giải thích vì sao mình chọn cách đọc đó.

### Chỗ phải sửa giữa đường

Interview guide bản đầu hơi nặng lý thuyết. Sau 1-2 cuộc pilot, người nghiên cứu nhận ra:

- câu hỏi đi quá nhanh vào khung burnout quen thuộc;
- người tham gia trả lời "đúng sách" nhiều hơn là kể trải nghiệm thật;
- phần follow-up chưa đủ mở.

Antigravity có thể giúp viết lại guide, nhưng điều làm guide tốt hơn thật ra là:

- nghe lại pilot;
- nhận ra chỗ mình hỏi dẫn;
- và viết lại câu hỏi theo ngôn ngữ gần hơn với người tham gia.

### Verification overhead

Case định tính này tốn công ở các chỗ sau:

- transcript phải rà lại sau khi chuyển giọng nói thành văn bản;
- thông tin nhận diện phải được ẩn danh kỹ hơn tưởng tượng ban đầu;
- codes draft của AI phải được xem như gợi ý, không phải kết luận;
- thematic map chỉ có giá trị khi researcher có thể giải thích vì sao từng theme đứng vững.

### Trạng thái cuối cùng của dự án

Đầu ra mạnh nhất của case này không phải là số lượng code. Nó là:

- một corpus transcript đủ sạch;
- familiarization notes và memos có chiều sâu;
- một codebook đã qua vài vòng chỉnh;
- và 1-2 đoạn findings đủ tốt để làm lõi cho chương kết quả hoặc bài trình bày với GVHD.

### Bài học chính

- Nghiên cứu định tính yếu đi rất nhanh nếu AI được dùng để "đọc hộ".
- AI tốt hơn trong vai trò hỗ trợ tổ chức và phản biện, hơn là vai trò người diễn giải.
- Chất lượng của case này đến từ pilot, memoing, và sửa guide, không đến từ việc có nhiều output hơn.

---

## D.3 Case 3: Mixed Methods Về Thanh Niên Và Sự Tham Gia Chính Trị

### Bối cảnh

- Người nghiên cứu: nghiên cứu sinh hoặc nhóm nghiên cứu nhỏ ngành xã hội học/chính sách công
- Mối quan tâm ban đầu: tác động của mạng xã hội đến sự tham gia chính trị của thanh niên
- Dạng nghiên cứu sau cùng: explanatory sequential mixed methods

### Điểm xuất phát

Đây là kiểu đề tài rất dễ bị làm quá tay. Ngay từ đầu, nhóm nghiên cứu đã bị hấp dẫn bởi ý tưởng:

- survey quy mô lớn;
- thêm focus group;
- thêm phân tích nội dung bài đăng công khai;
- và nếu được, làm luôn dashboard truyền thông.

Antigravity giúp nhóm nhìn ra khá sớm rằng nếu giữ toàn bộ tham vọng đó, mixed methods sẽ trở thành ba dự án chồng lên nhau chứ không còn là một thiết kế tích hợp.

### AI đã giúp gì?

Giá trị lớn nhất nằm ở việc làm rõ integration:

- overall RQ là gì;
- nhánh QUAN cần trả lời gì trước;
- kết quả nào sẽ kích hoạt nhánh QUAL;
- và cuối cùng hai nhánh gặp nhau ở joint display nào.

Ví dụ prompt hữu ích:

```text
Tôi đang cân nhắc explanatory sequential mixed methods cho đề tài [topic].
Hãy giúp tôi:
1. viết overall RQ;
2. tách rõ QUAN và QUAL strands;
3. chỉ ra chính xác integration point;
4. cảnh báo chỗ nào thiết kế này đang quá sức.
```

### Chỗ khó thật của mixed methods

Mixed methods không khó vì phải dùng nhiều kỹ thuật. Nó khó vì phải giữ cho hai nhánh:

- không đứt logic với nhau;
- không chạy thành hai nghiên cứu độc lập;
- và không làm nhóm nghiên cứu kiệt sức vì scope.

Trong case này, nhóm phải bỏ bớt một thành phần phân tích nội dung công khai vì:

- nó làm design nặng lên rất nhiều;
- nhưng không thực sự trả lời thêm câu hỏi cốt lõi;
- và không có đủ nguồn lực để kiểm soát tốt chất lượng dữ liệu đó.

### Verification overhead

Mixed methods tạo thêm một lớp kiểm chứng nữa:

- mỗi nhánh phải tự đứng vững;
- phần tích hợp cũng phải được kiểm chứng logic;
- mọi joint display đều phải trung thực với cả hai nhánh, không ép chúng khớp nhau cho đẹp.

AI có thể giúp draft joint display, nhưng nhóm nghiên cứu vẫn phải tự hỏi:

- finding nào thực sự bổ sung cho nhau;
- finding nào chỉ đứng cạnh nhau;
- finding nào đang mâu thuẫn và cần được giữ nguyên sự mâu thuẫn đó.

### Trạng thái cuối cùng của dự án

Case này kết thúc ở trạng thái "đủ để đi tiếp", chứ không được kể như một chuyện thắng lớn:

- nhánh QUAN có analysis plan và kết quả chính đủ rõ;
- nhánh QUAL được thiết kế để giải thích đúng chỗ cần giải thích;
- integration map và joint display draft đã có;
- một briefing note sơ bộ có thể được phát triển sau khi phần học thuật chốt xong.

### Bài học chính

- Mixed methods mạnh lên nhờ integration rõ, không nhờ số lượng thành phần.
- Việc bỏ bớt một nhánh phụ đôi khi làm dự án tốt hơn.
- AI rất hữu ích trong việc ép nhóm nghiên cứu viết ra logic tích hợp, nhưng không thể quyết định thay đâu là chỗ đáng tích hợp thật.

---

## D.4 Những Mẫu Số Chung Rút Ra Từ Cả Ba Case

### 1. AI giúp nhìn nhanh hơn, không quyết định thay

Trong cả ba case, AI hữu ích nhất khi:

- giúp quét một field nhanh;
- gợi ý lựa chọn;
- ép người nghiên cứu phải hiện hình logic của mình;
- và chuẩn hóa vài tác vụ lặp lại.

Nó yếu đi ngay khi bị đẩy lên vai trò:

- chọn hộ đề tài;
- kết luận hộ từ dữ liệu;
- hoặc viết thay phần lập luận mà người nghiên cứu chưa thật sự hiểu.

### 2. Verification luôn tốn công hơn cảm giác ban đầu

Điểm chung lớn nhất là ở đâu AI làm nhanh hơn, ở đó con người cũng phải dành công để:

- truy nguồn gốc;
- đọc kỹ hơn;
- rà lại dữ liệu;
- hoặc viết memo giải thích quyết định của mình.

Không case nào thành công chỉ vì "prompt tốt". Chúng đứng vững nhờ prompt đi cùng kiểm chứng.

### 3. Scope cut là một năng lực học thuật

Mỗi case đều có một khoảnh khắc phải tự hỏi:

- bỏ bớt cái gì;
- giữ lại cái gì;
- và thế nào là "đủ tốt để đi tiếp".

Đó là kỹ năng rất thật của nghiên cứu. AI có thể giúp nhìn rõ hơn, nhưng không làm phần đau đầu này biến mất.

### 4. Output tốt nhất không phải lúc nào cũng là outcome đẹp nhất

Một workflow nghiên cứu tốt nên được đánh giá trước hết bằng:

- độ rõ của logic;
- độ sạch của dữ liệu;
- khả năng truy vết;
- và mức độ người nghiên cứu hiểu công trình của mình.

Journal cụ thể, điểm số cụ thể, hay thời gian rút ngắn bao nhiêu chỉ là kết quả phụ thuộc bối cảnh. Nếu lấy chúng làm thước đo chính, rất dễ trượt khỏi tinh thần của cả cuốn sách.

## D.5 Capstone Project: Cấu Trúc Báo Cáo Đánh Giá Khung Nghiên Cứu

Tất cả các case studies phía trên đều có thể được chuẩn hóa lại thành một bài **Individual Research Report** (8-10 trang) như một dự án Capstone cuối kỳ. Dưới đây là cấu trúc minh họa cho dạng bài tập rèn luyện tư duy thiết kế, không nặng về ra quyết định thực tế mà xoáy thẳng vào *tính logic của phương pháp*.

### 1. Introduction (Dẫn nhập - 1 trang)
*   **Context:** Giới thiệu bối cảnh và chủ đề nghiên cứu.
*   **RQ/Hypothesis:** Tuyên bố rõ ràng Câu hỏi hoặc Giả thuyết cốt lõi.
*   **Methodological Focus:** Giải thích ý nghĩa học thuật của việc nghiên cứu bài toán này và phác mộc cấu trúc báo cáo.

### 2. Literature Review and Theoretical Framework (Khung lý thuyết - 1.5 đến 2 trang)
*   **Synthesis:** Tóm tắt các lý thuyết và khái niệm liên quan.
*   **Design Rationale:** Thảo luận cách literature định hình việc chọn biến số, constructs, và phép phân tích.
*   **Methodological Gap:** Chỉ ra khoảng trống phương pháp (không phải khoảng trống nội dung) mà thiết kế này lấp đầy.

### 3. Research Design and Methodology (Thiết kế Nghiên cứu - 1.5 đến 2 trang)
Đây là "trái tim" của báo cáo Capstone, cần làm rõ 5 yếu tố:
1.  **Research Philosophy:** Nhận thức luận (Positivism, Interpretivism, Pragmatism) và cách nó chi phối.
2.  **Research Approach:** Suy diễn (Deductive) hay Quy nạp (Inductive).
3.  **Data Collection:** Nguồn dữ liệu, công cụ thu thập và lý do chọn lựa.
4.  **Sampling:** Xác định quần thể, kích thước mẫu, phương pháp lấy mẫu và biện luận.
5.  **Analysis Techniques:** Các kỹ thuật (VD: Regression, Thematic, ANOVA) và giải thích tại sao lại dùng chúng. Đề cập thêm vấn đề Đạo đức (Ethical considerations).

### 4. Data Analysis and Findings (Trình bày Dữ liệu - 2 đến 2.5 trang)
*   Báo cáo kết quả bằng bảng biểu, sơ đồ (chạy qua dữ liệu giả lập hoặc thực tế).
*   Chỉ bám vào RQ/H, tuyệt đối không "suy diễn" vượt ra ngoài những gì dữ liệu nói.
*   Bàn luận ý nghĩa thống kê hoặc ý nghĩa định tính một cách minh bạch.

### 5. Evaluation of Research Design (Đánh giá Khung Thiết Kế - 1 đến 1.5 trang)
*   Đánh giá phản biện (Critically assess) điểm mạnh và hạn chế của phương pháp đã chọn.
*   So sánh với các phương pháp thay thế (Alternative methods) và bàn luận sự đánh đổi (Trade-offs).
*   Đề xuất cải thiện (Ví dụ: Thêm mẫu lớn hơn, đổi mô hình, hoặc chuyển sang Mixed-methods).

### 6. Conclusion (Kết luận - 1 trang)
*   Tóm tắt dự án, quyết định phương pháp và kết quả chính.
*   Suy ngẫm (Reflect) về tính nghiêm ngặt để tạo ra tri thức đáng tin cậy.

> *Capstone Project này nhằm kiểm chứng khả năng áp dụng Antigravity Workflow ở mức cao nhất: Không chỉ biết cách làm một nghiên cứu, mà còn biết cách tự phê bình (critique) chính thiết kế của mình.*

---

> 📖 **Quay lại:** [Mục Lục →](../README.md)

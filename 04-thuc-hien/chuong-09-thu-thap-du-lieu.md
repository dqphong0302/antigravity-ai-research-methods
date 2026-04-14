# Chương 9: Thu Thập Dữ Liệu

![Data Collection](../assets/images/ch09_data_collection_1776092346891.png)

---

> *"Data is not information, information is not knowledge, knowledge is not wisdom."* — Clifford Stoll

---

Nhiều người bắt đầu giai đoạn thu thập dữ liệu với một tâm thế rất quen thuộc: càng lấy được nhiều dữ liệu càng tốt. Đây là một phản xạ dễ hiểu, nhưng trong nghiên cứu, nó thường dẫn đến ba rủi ro lớn:

- thu quá nhiều thứ nhưng không gắn chặt với câu hỏi nghiên cứu;
- tạo ra dữ liệu khó quản lý, khó làm sạch, khó phân tích;
- và nghiêm trọng hơn, vô tình đi qua ranh giới đạo đức hoặc pháp lý mà người nghiên cứu chưa nhìn đủ rõ.

Thu thập dữ liệu vì vậy không chỉ là bước “đi lấy nguyên liệu”. Nó là bước bạn quyết định nghiên cứu sẽ dựa trên loại bằng chứng nào, mức độ tin cậy ra sao, chi phí xử lý lớn đến đâu, và trách nhiệm của bạn với người tham gia hoặc với nguồn dữ liệu sẽ nặng đến mức nào.

Antigravity hỗ trợ giai đoạn này rất mạnh. Bạn có thể:

- thu thập dữ liệu web công khai bằng Playwright;
- số hóa tài liệu bằng OCR;
- tìm và tổ chức dữ liệu thứ cấp;
- tự động hóa cảnh báo tài liệu mới hoặc luồng xử lý dữ liệu bằng n8n;
- kết nối việc thu dữ liệu với quản lý tri thức và phân tích trong cùng một workspace.

Nhưng giống như các chương trước, công cụ chỉ là một nửa câu chuyện. Nửa còn lại là tư duy phương pháp: **nên thu dữ liệu gì, từ đâu, theo quy trình nào, và khi nào phải dừng lại**.

Nếu `Chương 6-8` là nơi bạn thiết kế logic của bằng chứng, thì chương này là nơi logic đó chạm vào dữ liệu thật. Một chương 9 làm tốt không chỉ tạo ra nhiều file hơn. Nó tạo ra một `dataset` hoặc `corpus` đủ sạch, đủ có nguồn gốc, và đủ được quản trị tốt để khi sang `Chương 10`, `Chương 11`, hoặc cả hai nhánh trong mixed methods, bạn không phải phân tích trong tình trạng mù về provenance.

---

## 9.1 Thu Thập Dữ Liệu Thực Chất Là Gì?

Thu thập dữ liệu không chỉ là hành vi lấy dữ liệu từ đâu đó về máy. Trong nghiên cứu, đó là quá trình thiết kế bằng chứng.

### Mỗi quyết định thu dữ liệu đều hàm chứa 4 lựa chọn

1. **Bạn tin loại bằng chứng nào?**
   Survey, phỏng vấn, tài liệu chính sách, dữ liệu hành vi, thống kê thứ cấp, log hệ thống, ảnh chụp, video, bài đăng mạng xã hội.

2. **Bạn tiếp cận bằng chứng đó theo cách nào?**
   Phát bảng hỏi, scrape web, phỏng vấn trực tiếp, tải dữ liệu mở, OCR tài liệu in, lấy log từ hệ thống nội bộ.

3. **Bạn giữ lại dữ liệu ở cấp độ nào?**
   Dữ liệu thô, dữ liệu đã ẩn danh, dữ liệu đã chuẩn hóa, metadata, field notes, screenshots bằng chứng.

4. **Bạn sẽ chịu trách nhiệm ra sao với dữ liệu đó?**
   Bảo mật, consent, lưu trữ, ẩn danh, quyền truy cập, tái lập quy trình, và minh bạch phương pháp.

### Một nguyên tắc cần nhớ

> Dữ liệu không phải thứ “có sẵn ở ngoài kia” chờ bạn nhặt về. Dữ liệu là kết quả của cách bạn định nghĩa, lọc, và ghi nhận thế giới.

Điều này đặc biệt đúng trong khoa học xã hội, giáo dục, và các nghiên cứu liên quan đến con người. Hai người cùng “thu dữ liệu về burnout giáo viên” có thể tạo ra hai bộ dữ liệu hoàn toàn khác nhau, chỉ vì:

- cách họ đặt câu hỏi khác nhau;
- thời điểm thu khác nhau;
- cách ghi âm, chép lại, hay làm sạch khác nhau;
- và cách họ loại bỏ/giữ lại thông tin khác nhau.

Vì vậy, chất lượng của dữ liệu luôn bắt đầu trước cả lúc bạn chạm tay vào công cụ.

---

## 9.2 Chốt Trước 5 Điều Trước Khi Thu Dữ Liệu

Rất nhiều lỗi lớn ở giai đoạn thu thập dữ liệu thực ra là lỗi thiết kế. Trước khi dùng Playwright, OCR, form khảo sát hay workflow tự động, bạn nên chốt 5 câu hỏi sau.

### 1. Dữ liệu này trả lời câu hỏi nghiên cứu nào?

Đừng thu vì “có thể sẽ hữu ích”. Hãy gắn từng nhóm dữ liệu với câu hỏi nghiên cứu cụ thể.

Ví dụ:

- RQ1: học sinh thay đổi kết quả học tập thế nào -> cần điểm pre/post, biến nhóm, covariates.
- RQ2: giáo viên trải nghiệm triển khai ra sao -> cần phỏng vấn, field notes, tài liệu trường học.

### 2. Đơn vị phân tích là gì?

Bạn đang phân tích:

- cá nhân;
- lớp học;
- trường học;
- bài báo;
- tài liệu chính sách;
- bài đăng mạng xã hội;
- hay phiên phỏng vấn?

Nếu đơn vị phân tích chưa rõ, dữ liệu thu về rất dễ lẫn cấp độ.

### 3. Bạn sẽ biết dữ liệu “đủ” khi nào?

Không phải nghiên cứu nào cũng cần thật nhiều.

- Với định lượng, “đủ” thường gắn với cỡ mẫu, power, tính đại diện, hoặc thiết kế phân tích.
- Với định tính, “đủ” thường gắn với saturation, độ dày của dữ liệu, và tính đa dạng của trường hợp.
- Với dữ liệu thứ cấp, “đủ” gắn với độ phủ biến số, độ tin cậy, và tính liên tục theo thời gian.

### 4. Dữ liệu có nhạy cảm không?

Ngay từ đầu phải phân loại:

- dữ liệu công khai;
- dữ liệu có thể nhận diện cá nhân;
- dữ liệu nhạy cảm (sức khỏe, giáo dục, chính trị, tài chính, trẻ em, khu vực công);
- dữ liệu nội bộ hoặc có ràng buộc chia sẻ.

### 5. Quy trình lưu trữ sau khi thu là gì?

Nếu chưa biết dữ liệu sẽ được lưu ở đâu, đặt tên thế nào, ai được truy cập, bản nào là raw, bản nào là cleaned, thì chưa nên thu ồ ạt.

### Prompt kiểm tra readiness trước khi thu

> 📋 **Prompt Template — Data Collection Readiness Check**
> ```
> Tôi sắp bước vào giai đoạn thu thập dữ liệu cho nghiên cứu:
> - Topic: [topic]
> - Research questions: [list]
> - Data types dự kiến: [list]
> - Participants/sources: [list]
> 
> Hãy giúp tôi kiểm tra:
> 1. Mỗi loại dữ liệu phục vụ RQ nào
> 2. Đơn vị phân tích là gì
> 3. Rủi ro về thiếu dữ liệu hoặc thu thừa dữ liệu
> 4. Dữ liệu nào là nhạy cảm
> 5. Tôi cần chốt gì trước khi bắt đầu thu
> ```

---

## 9.3 Phân Biệt Các Loại Dữ Liệu: Sơ Cấp, Thứ Cấp, Số Hóa, và Dữ Liệu Nhạy Cảm

Một chương về thu thập dữ liệu mà không phân biệt rõ loại dữ liệu sẽ rất dễ trượt vào kiểu “có công cụ gì thì dùng công cụ đó”.

### Dữ liệu sơ cấp

Là dữ liệu bạn trực tiếp tạo ra hoặc thu lần đầu cho mục tiêu nghiên cứu cụ thể.

Ví dụ:

- bảng hỏi khảo sát;
- phỏng vấn sâu;
- focus group;
- quan sát lớp học;
- nhật ký người tham gia;
- dữ liệu thí nghiệm.

**Điểm mạnh:** bám đúng RQ, kiểm soát quy trình tốt hơn.

**Điểm yếu:** tốn công, tốn thời gian, có nghĩa vụ đạo đức cao.

### Dữ liệu thứ cấp

Là dữ liệu đã tồn tại trước đó, được tạo ra bởi đơn vị khác hoặc cho mục đích khác.

Ví dụ:

- World Bank, GSO, UNESCO, WHO;
- open datasets;
- dữ liệu từ báo cáo chính sách;
- bộ dữ liệu từ nghiên cứu trước.

**Điểm mạnh:** nhanh, tiết kiệm, có thể có độ phủ lớn.

**Điểm yếu:** không phải lúc nào cũng vừa khít với RQ; định nghĩa biến có thể không do bạn kiểm soát.

### Dữ liệu số hóa

Đây là tài liệu giấy, scan, hoặc nguồn hình ảnh cần chuyển thành văn bản hoặc dạng có thể xử lý.

Ví dụ:

- luận văn in cũ;
- báo cáo nội bộ scan PDF;
- hồ sơ ảnh chụp;
- tài liệu tiếng Việt chỉ có bản in.

### Dữ liệu nhạy cảm

Không phải cứ “không công khai” mới là nhạy cảm. Một số dữ liệu công khai vẫn có thể nhạy cảm nếu ghép nối hoặc diễn giải sai.

Dữ liệu thường cần mức cảnh giác cao:

- thông tin cá nhân có thể nhận diện;
- dữ liệu trẻ em/học sinh;
- dữ liệu sức khỏe;
- dữ liệu chính trị, tôn giáo, hoặc hành vi riêng tư;
- dữ liệu nội bộ tổ chức, trường học, doanh nghiệp;
- transcript chứa mô tả tình huống dễ truy ngược danh tính.

### Vì sao phân loại này quan trọng?

Vì mỗi loại kéo theo:

- một cách thu khác;
- một cách lưu khác;
- một mức độ ẩn danh khác;
- và một rủi ro đạo đức khác.

---

## 9.4 Consent, Ẩn Danh và Metadata: Những Thứ Không Được Làm Sau

Nhiều nhóm nghiên cứu chỉ nghĩ đến consent hoặc ẩn danh sau khi dữ liệu đã thu xong. Đó là quá muộn.

### Consent không chỉ là ký tên

Consent tốt phải cho người tham gia biết:

- họ đang tham gia vào nghiên cứu gì;
- dữ liệu sẽ được dùng thế nào;
- ai có quyền truy cập;
- mức độ ẩn danh ra sao;
- họ có thể rút lui không;
- và có rủi ro nào cần hiểu trước không.

### Ẩn danh không chỉ là xóa tên

Một transcript có thể không còn tên thật nhưng vẫn dễ nhận diện qua:

- vị trí công tác;
- trường học cụ thể;
- chức danh hiếm;
- mốc sự kiện đặc trưng;
- hoặc cách kể chuyện rất đặc thù.

Ẩn danh tốt thường cần:

- thay tên riêng bằng mã;
- tách file danh tính khỏi file dữ liệu phân tích;
- làm mờ hoặc thay thế thông tin nhận diện gián tiếp;
- quản lý bản raw và bản anonymized riêng biệt.

### Metadata và data dictionary

Đây là chỗ rất nhiều dự án bỏ qua rồi sau đó trả giá ở giai đoạn phân tích.

**Metadata** giúp bạn biết dữ liệu đến từ đâu, khi nào, theo cách nào.

**Data dictionary** giúp bạn biết từng biến nghĩa là gì, được mã hóa ra sao, giá trị nào là missing, giá trị nào là lỗi.

Ví dụ data dictionary tối thiểu:

| Biến | Mô tả | Kiểu dữ liệu | Mã hóa | Ghi chú |
|---|---|---|---|---|
| `school_type` | Loại trường | categorical | 1 = công lập, 2 = tư thục | lấy từ bảng hỏi |
| `burnout_score` | Điểm burnout tổng | numeric | 0-54 | tính từ 9 items |
| `interview_id` | Mã phỏng vấn | text | P01, P02... | không dùng tên thật |

### Prompt thiết kế data governance tối thiểu

> 📋 **Prompt Template — Data Governance Starter**
> ```
> Tôi sắp thu thập dữ liệu cho nghiên cứu:
> - Data types: [list]
> - Participants/sources: [list]
> - Sensitive level: [mô tả]
> 
> Hãy giúp tôi tạo:
> 1. Checklist consent
> 2. Kế hoạch ẩn danh
> 3. Mẫu metadata log
> 4. Mẫu data dictionary
> 5. Gợi ý cấu trúc thư mục tách raw / anonymized / processed
> ```

> ⚠️ **Cảnh báo:** Đừng upload transcript còn nguyên tên, trường, hoặc mô tả dễ truy ngược lên các dịch vụ AI công cộng nếu chưa ẩn danh và chưa có cơ sở đạo đức rõ ràng.

---

## 9.5 Thu Thập Dữ Liệu Web Với Playwright

![Pipeline Thu Thập Dữ Liệu Đa Nguồn](../assets/images/ch09_data_pipeline_1776094276503.png)

Playwright rất mạnh khi bạn cần tương tác với website thực thay vì chỉ tải một file tĩnh. Nhưng với nghiên cứu, câu hỏi đầu tiên không phải “có scrape được không?”, mà là “có nên scrape không?”

### Khi nào phù hợp?

| Use case | Ví dụ | Có nên không? |
|---|---|---|
| Dữ liệu công khai, có cấu trúc | bảng thống kê GSO, World Bank | Thường có |
| Bài báo, tin tức, văn bản công khai | bài báo chí, thông cáo | Có, nếu trích nguồn đúng |
| Mạng xã hội công khai | bài đăng mở | Cần xem ToS, ethics, sensitivity |
| Nội dung sau đăng nhập/paywall | tài khoản cá nhân, kho dữ liệu đóng | Thường không, trừ khi có quyền rõ ràng |

### Những điều cần chốt trước khi scrape

- URL cụ thể;
- trường dữ liệu cần lấy;
- phạm vi thời gian;
- tần suất truy cập;
- cách lưu raw HTML / CSV / screenshot;
- cách ghi nguồn và thời điểm truy cập.

### Screenshot evidence khi nào hữu ích?

Rất hữu ích cho:

- case study;
- dữ liệu web có thể thay đổi theo thời gian;
- tài liệu công khai nhưng dễ bị sửa/xóa;
- minh chứng quy trình thu thập.

### Prompt thu thập dữ liệu web công khai

> 📋 **Prompt Template — Public Web Data Collection**
> ```
> Truy cập website [URL] và thu thập dữ liệu:
> - Nội dung cần lấy: [bảng/chỉ số/trường dữ liệu]
> - Khoảng thời gian: [range]
> - Định dạng lưu: CSV + screenshot bằng chứng
> 
> Yêu cầu:
> 1. Chỉ lấy dữ liệu công khai
> 2. Ghi rõ URL, ngày truy cập, timestamp
> 3. Lưu raw output vào data/raw/web/
> 4. Tạo một file metadata ghi nguồn và mô tả biến
> ```

### Khi nào không nên tự động hóa bằng Playwright?

- Website cấm scrape rõ ràng trong điều khoản.
- Dữ liệu thuộc vùng nhạy cảm liên quan đến con người.
- Bạn chỉ cần một vài bảng có thể tải hợp pháp bằng tay.
- Tự động hóa sẽ làm quy trình khó kiểm soát hơn lợi ích nó mang lại.

---

## 9.6 Số Hóa Tài Liệu Với OCR

OCR là một công cụ cực kỳ hữu ích cho nghiên cứu ở Việt Nam, vì rất nhiều nguồn quan trọng chỉ tồn tại dưới dạng scan, ảnh chụp, hoặc PDF không thể copy text.

### Khi nào cần OCR?

| Loại tài liệu | Cần OCR? | Lưu ý |
|---|---|---|
| PDF digital, copy được | Thường không | đọc trực tiếp hoặc trích text |
| PDF scan rõ | Có | OCR local có thể đủ |
| PDF scan mờ, bảng biểu phức tạp | Có | cần OCR chất lượng cao hơn |
| Tài liệu giấy chụp bằng điện thoại | Có | cần kiểm tra méo, bóng, mất nét |

### OCR không phải lúc nào cũng vô hại

Sai lầm OCR có thể kéo theo:

- trích sai số liệu;
- mất dấu bảng;
- nhầm tên riêng;
- rơi ký tự tiếng Việt;
- hoặc làm hỏng cấu trúc tài liệu.

Vì vậy, OCR tốt luôn đi kèm bước kiểm tra chất lượng.

### Workflow OCR hợp lý

1. Phân loại tài liệu: digital hay scan.
2. Chọn phương pháp OCR phù hợp.
3. Lưu bản text riêng.
4. Ghi mức độ tin cậy hoặc quality note.
5. Kiểm tra tay các phần quan trọng như bảng, số liệu, tên riêng.

### Prompt OCR batch

> 📋 **Prompt Template — Batch OCR Pipeline**
> ```
> Trong thư mục [path] có [N] file PDF cần OCR.
> 
> Với mỗi file:
> 1. Xác định là digital hay scan
> 2. Chọn phương pháp OCR phù hợp
> 3. Lưu text output vào data/processed/ocr/
> 4. Tạo quality note: tốt / trung bình / cần kiểm tra tay
> 5. Liệt kê trang nào có bảng biểu hoặc số liệu quan trọng
> 
> Cuối cùng tạo báo cáo:
> file | pages | method | quality | notes
> ```

### Một lưu ý rất thực tế

Nếu bạn dùng OCR để số hóa tài liệu làm nền cho literature review, có thể chấp nhận mức lỗi nhỏ. Nhưng nếu tài liệu đó chứa số liệu chính bạn sẽ đưa vào phân tích hoặc trích dẫn trực tiếp, mức kiểm tra phải cao hơn rất nhiều.

---

## 9.7 Thu Thập Dữ Liệu Thứ Cấp

Dữ liệu thứ cấp có thể rút ngắn rất nhiều thời gian nghiên cứu, nhưng chỉ khi bạn hiểu định nghĩa và giới hạn của dữ liệu đó.

### Nguồn phổ biến

| Nguồn | Loại dữ liệu | Điểm cần lưu ý |
|---|---|---|
| GSO | kinh tế, xã hội, dân số | cách định nghĩa chỉ số qua năm |
| World Bank | development indicators | độ trễ cập nhật, comparability |
| UNESCO | giáo dục | đơn vị tính và độ phủ quốc gia |
| WHO | y tế | metadata và nguồn quốc gia |
| OECD | giáo dục, kinh tế | mức phù hợp với bối cảnh Việt Nam |
| Kaggle / UCI | datasets đa dạng | nguồn gốc và chất lượng không đồng đều |

### 4 câu hỏi phải hỏi với dữ liệu thứ cấp

1. Ai tạo dữ liệu này?
2. Dữ liệu được tạo cho mục đích gì?
3. Định nghĩa biến có khớp với nghiên cứu của tôi không?
4. Có khoảng trống, missingness, hay thay đổi định nghĩa theo thời gian không?

### Prompt truy xuất dữ liệu thứ cấp

> 📋 **Prompt Template — Secondary Data Retrieval**
> ```
> Tôi cần dữ liệu thứ cấp về [indicator/topic]:
> - Quốc gia/khu vực: [scope]
> - Giai đoạn: [range]
> - Nguồn ưu tiên: [World Bank / GSO / UNESCO / WHO ...]
> 
> Hãy giúp tôi:
> 1. Tìm nguồn phù hợp nhất
> 2. Chỉ ra định nghĩa biến
> 3. Nêu rủi ro comparability hoặc missing data
> 4. Tải/lưu metadata nguồn
> 5. Gợi ý cách cite nguồn dữ liệu này trong Methods
> ```

### Dấu hiệu cho thấy dữ liệu thứ cấp không phù hợp

- biến nghe giống nhưng định nghĩa khác với khái niệm bạn cần;
- chuỗi thời gian đứt gãy hoặc đổi cách đo;
- chỉ có số tổng hợp nhưng RQ cần dữ liệu vi mô;
- nguồn không rõ phương pháp thu.

---

## 9.8 Tự Động Hóa Thiết Kế Và Lên Form Khảo Sát Tự Động

Khảo sát định lượng luôn đòi hỏi sự tỉ mỉ trong việc thiết kế câu hỏi, thang đo, và đẩy lên các nền tảng kỹ thuật số (như Google Forms, Microsoft Forms). Rất nhiều nghiên cứu sinh chọn cách làm thủ công: tự chép câu hỏi, tự tạo biến, và tự click chuột cấu hình từng câu trên form. 

Antigravity cung cấp cách thức chuyên nghiệp (programmatic approach) giúp bạn tạo form tự động hoàn toàn, giải quyết bài toán mệt mỏi này qua hai bước:

### Bước 1: Để AI Khai Sinh Câu Hỏi (Question Generation)

Thay vì ngồi "chế" câu hỏi, bạn có thể cấp Khung lý thuyết (Theoretical Framework) cho **Claude Opus** (chuyên lý luận, ngôn ngữ học thuật) hoặc **Gemini 3.1 Pro** để AI tiến hành:
- Bóc tách construct thành các items quan sát.
- Gắn thang đo Likert (5 hoặc 7 mức).
- Loại bỏ các lỗi double-barreled questions (câu hỏi đa nghĩa) hay thiên kiến dẫn dắt (leading bias).

> 📋 **Prompt Template — Survey Constructs to Items**
> ```
> Tôi đang làm nghiên cứu định lượng về chủ đề: [topic].
> Dựa trên khung lý thuyết [Tên Lý Thuyết] và biến [Tên Biến Cần Đo Lường], hãy:
> 1. Trích xuất/đề xuất 5-7 items quan sát kèm thang đo Likert [5/7] mức độ.
> 2. Đảm bảo ngôn ngữ ở cấp độ [Sinh viên/Chuyên gia/Khách hàng].
> 3. Tránh các lỗi dẫn dắt (bias) và câu hỏi ghép (double-barreled).
> ```

### Bước 2: Bắn Câu Hỏi Trực Tiếp Lên Hệ Thống Tự Động (Form Generation)

Việc AI thao tác chuột (browser automation) qua giao diện web để tạo Form thường dễ gặp rủi ro do Google/Microsoft chặn bảo mật (CAPTCHA, 2FA). 
Vì vậy, Antigravity tối ưu bằng cách đi thẳng qua mã lệnh hoặc tính năng thông minh của nền tảng:

**A. Đối với Google Forms (Sử dụng Google Apps Script - GAS)**
Antigravity sẽ viết đoạn mã Google Apps Script khai báo toàn bộ các biến, cấu trúc phần (sections), và thang đo.
*   **Cách làm:** Bạn mở `script.google.com`, dán mã từ Antigravity và nhấn Run.
*   **Kết quả:** Một Google Form mới toanh được tạo tự động trong 3 giây. Cách tiếp cận này đảm bảo mọi thiết lập là 100% chính xác, dễ tùy chỉnh đồng loạt, và loại bỏ hoàn toàn lỗi copy-paste.

**B. Đối với Microsoft Forms (Sử dụng tính năng Quick Import)**
Microsoft Forms ưu tiên tính năng nhập nhanh bằng AI (`Quick Import`) thay vì mã lệnh mạnh như GAS.
*   **Cách làm:** Antigravity sẽ format file Markdown/Word hoặc PDF thành danh sách đánh số cực chuẩn.
*   **Kết quả:** Bạn ném file Word đó vào trình Import của Microsoft Forms. Hệ thống tự nhận diện và nạp sẵn dạng câu hỏi lưới Likert/Trắc nghiệm. 

> 💡 **Tip:** Đừng cố hướng dẫn Agent mở trình duyệt vào Google Forms và tự click. Hãy yêu cầu Agent *viết Script cho Google Forms* hoặc *viết Markdown cho Microsoft Forms Quick Import*. Đó mới là cách người làm tự động hóa nghiên cứu thực hành!

---

## 9.9 Tự Động Hóa Với n8n: Mạnh, Nhưng Không Phải Cứ Tự Động Hóa Là Tốt

n8n rất hữu ích khi bạn có những luồng việc lặp đi lặp lại:

- cảnh báo bài báo mới;
- lưu trữ tài liệu mới;
- OCR hàng loạt;
- cập nhật data table hoặc database;
- đồng bộ metadata.

### Khi nào automation thật sự đáng làm?

- Công việc lặp lại nhiều lần
- Quy trình đầu vào/đầu ra tương đối ổn định
- Sai sót thủ công tốn kém
- Có lợi khi log hóa toàn bộ quá trình

### Ví dụ workflow hữu ích

**1. Research landscape monitoring**

- lịch chạy định kỳ;
- tìm paper mới theo từ khóa;
- nếu có kết quả mới thì gửi email/Slack;
- lưu metadata vào bảng theo dõi.

**2. Auto-archive sources**

- nhận URL;
- tải file;
- OCR nếu cần;
- lưu metadata;
- thêm vào không gian quản lý tri thức.

### Prompt tạo workflow cảnh báo tài liệu mới

> 📋 **Prompt Template — Research Alert Workflow**
> ```
> Tạo workflow n8n tự động:
> - Schedule: [thời gian]
> - Search query: [keywords]
> - Source: [Consensus / nguồn cụ thể]
> - Condition: chỉ báo khi có nội dung mới
> - Output: email/Slack + lưu metadata
> 
> Tôi cần:
> 1. Mô tả các node chính
> 2. Logic lọc trùng
> 3. Tên trường metadata cần lưu
> 4. Cảnh báo rủi ro nếu workflow hỏng
> ```

### Khi nào không nên tự động hóa?

- Khi quy trình còn thay đổi liên tục.
- Khi dữ liệu nhạy cảm cần kiểm duyệt thủ công.
- Khi lượng công việc nhỏ, làm tay rõ ràng hơn.
- Khi automation khiến bạn ít hiểu hơn về chính dữ liệu mình đang thu.

> ⚠️ **Cảnh báo:** Một workflow tự động hóa tệ có thể tạo ra hàng loạt dữ liệu bẩn nhanh hơn rất nhiều so với cách làm tay.

---

## 9.10 Cấu Trúc Lưu Trữ Có Thể Tái Lập

Dữ liệu nghiên cứu tốt không chỉ cần đúng. Nó còn phải tìm lại được.

### Cấu trúc thư mục gợi ý

```text
project/
├── data/
│   ├── raw/
│   │   ├── web/
│   │   ├── survey/
│   │   ├── interviews/
│   │   └── documents/
│   ├── anonymized/
│   ├── processed/
│   └── metadata/
├── evidence/
├── scripts/
└── research-log.md
```

### Naming convention

```text
[YYYY-MM-DD]_[source]_[description].[ext]

2026-04-13_gso_enrollment-by-region.csv
2026-04-13_interview_P03_audio.wav
2026-04-14_policy-report_moet_scan.pdf
```

### 3 lớp nên tách rõ

- `raw`: dữ liệu nguyên bản, không chỉnh sửa;
- `anonymized`: bản đã loại thông tin nhận diện;
- `processed`: bản đã làm sạch, chuẩn hóa, sẵn cho phân tích.

Nếu ba lớp này lẫn nhau, về sau rất khó biết bạn đã thay đổi gì trong dữ liệu.

### The 3-2-1 Backup Rule

```text
3 bản copy → 2 loại media → 1 bản offsite
```

Ví dụ:

- bản trên máy làm việc;
- bản trên ổ cứng ngoài;
- bản trên không gian lưu trữ từ xa được kiểm soát phù hợp.

### Prompt tạo data storage blueprint

> 📋 **Prompt Template — Data Storage Blueprint**
> ```
> Thiết kế cấu trúc lưu trữ dữ liệu cho dự án:
> - Data types: [list]
> - Sensitive level: [mô tả]
> - Team size: [số người]
> 
> Tôi cần:
> 1. Cấu trúc thư mục
> 2. Naming convention
> 3. Quy tắc tách raw / anonymized / processed
> 4. Metadata files cần có
> 5. Backup checklist tối thiểu
> ```

---

## 9.11 Khi Nào Không Nên Thu Thêm Dữ Liệu?

Đây là một mục nghe có vẻ lạ, nhưng rất quan trọng.

### Có những lúc dừng lại là quyết định tốt hơn

Bạn không nên tiếp tục mở rộng dữ liệu chỉ vì:

- sợ bài chưa “đủ dày”;
- thấy công cụ scrape được nhiều hơn;
- nghĩ thêm dữ liệu sẽ tự động làm nghiên cứu mạnh hơn;
- hoặc cảm thấy khó đối diện với giai đoạn phân tích/viết nên cứ trì hoãn bằng cách thu thêm.

### Dấu hiệu cho thấy nên dừng

- dữ liệu mới không còn thêm insight đáng kể;
- bạn đã đạt cỡ mẫu hoặc saturation hợp lý;
- chi phí làm sạch dữ liệu mới cao hơn giá trị nó mang lại;
- mỗi nguồn mới lại mở thêm một nhánh câu hỏi ngoài scope;
- đội nghiên cứu bắt đầu mất kiểm soát với metadata và versioning.

### Một câu hỏi rất đáng tự hỏi

> Dữ liệu tiếp theo tôi định thu sẽ giúp trả lời câu hỏi nghiên cứu tốt hơn, hay chỉ làm tôi cảm thấy yên tâm hơn?

Hai điều này không phải lúc nào cũng giống nhau.

---

## 9.12 Workflow Gợi Ý Với Antigravity

Một workflow thực dụng cho chương này có thể là:

1. Chốt data collection plan từ RQ.
2. Phân loại dữ liệu: sơ cấp / thứ cấp / số hóa / nhạy cảm.
3. Tạo cấu trúc lưu trữ và metadata templates trước khi thu.
4. Thu dữ liệu bằng công cụ phù hợp:
   - Playwright cho dữ liệu web công khai,
   - OCR cho tài liệu scan,
   - nguồn dữ liệu mở cho dữ liệu thứ cấp.
5. Ẩn danh và tách raw/anonymized/processed.
6. Tự động hóa những luồng lặp lại bằng n8n nếu thật sự đáng.
7. Cập nhật research log để giai đoạn phân tích và viết sau này không phải đoán lại quá trình thu.

### Prompt tổng hợp

> 📋 **Prompt Template — End-to-End Data Collection Plan**
> ```
> Tôi cần lập và triển khai kế hoạch thu thập dữ liệu cho nghiên cứu:
> - Topic: [topic]
> - Research questions: [list]
> - Data sources dự kiến: [list]
> - Sensitive level: [mô tả]
> 
> Hãy giúp tôi:
> 1. Tạo data collection plan
> 2. Phân loại nguồn dữ liệu
> 3. Đề xuất cấu trúc lưu trữ và metadata
> 4. Chỉ ra chỗ nào cần consent/ẩn danh
> 5. Gợi ý phần nào nên tự động hóa, phần nào nên làm tay
> 6. Tạo checklist sẵn sàng trước khi bước vào phân tích
> ```

---

## 9.13 Bài Tập Thực Hành

### 🔧 Hands-on 9.1: Data Source Map

Lập bảng 4 cột:

| Research Question | Data Needed | Source | Sensitive? |

Điền ít nhất cho toàn bộ các câu hỏi nghiên cứu hiện có của bạn.

### 🔧 Hands-on 9.2: Metadata Starter Pack

Tạo:

- 1 file metadata log;
- 1 data dictionary;
- 1 naming convention guide;
- 1 thư mục tách raw / anonymized / processed.

### 🔧 Hands-on 9.3: Web/OCR Trial

Thử:

- scrape một bảng công khai nhỏ bằng Playwright, hoặc
- OCR 2 tài liệu scan tiếng Việt.

Sau đó tự ghi lại:

- dữ liệu có sạch không;
- phần nào phải kiểm tra tay;
- metadata nào cần bổ sung.

### 🔧 Hands-on 9.4: Automation Decision

Chọn một tác vụ lặp đi lặp lại trong dự án của bạn và trả lời:

- có nên tự động hóa không;
- nếu có, automation sẽ tiết kiệm bước nào;
- nếu không, vì sao làm tay đáng tin hơn.

---

## 9.14 Tóm Tắt Chương

Thu thập dữ liệu là giai đoạn bạn thiết kế chất lượng bằng chứng cho toàn bộ nghiên cứu. Công cụ như Playwright, OCR, dữ liệu mở, hay n8n có thể giúp bạn đi nhanh hơn và quy củ hơn, nhưng chúng không thay thế được các quyết định nền tảng: dữ liệu nào thật sự cần, dữ liệu nào nhạy cảm, quy trình lưu trữ nào có thể tái lập, và khi nào nên dừng thay vì thu thêm. Nghiên cứu mạnh không nhất thiết có nhiều dữ liệu hơn. Nó có dữ liệu phù hợp hơn, sạch hơn, và được quản trị có trách nhiệm hơn.

**Deliverable cuối chương:** đến đây, bạn nên có một `data collection kit` gồm:

- data source map theo từng RQ;
- cấu trúc lưu trữ raw / anonymized / processed;
- metadata log và data dictionary;
- checklist consent và ẩn danh;
- quyết định rõ phần nào tự động hóa, phần nào không;
- research log đủ để bước sang phân tích.

Đây là bộ nền chung cho toàn bộ phần phân tích. Nếu nghiên cứu của bạn đi theo định lượng, nó sẽ chảy sang `Chương 10`. Nếu đi theo định tính, nó sẽ chảy sang `Chương 11`. Nếu là mixed methods, đây chính là nơi hai nhánh bắt đầu có dữ liệu đủ sạch để sau này còn tích hợp được ở `Chương 12` và các chương viết kết quả.

---

> 📖 **Tiếp theo:** [Chương 10: Phân Tích Dữ Liệu Định Lượng →](chuong-10-phan-tich-dinh-luong.md)

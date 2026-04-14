# Chương 6: Thiết Kế Nghiên Cứu Định Lượng

![Quantitative Analysis](../assets/images/ch06_quantitative_analysis_1776092272452.png)

---

> *"Not everything that counts can be counted, and not everything that can be counted counts."* — William Bruce Cameron

---

Thiết kế nghiên cứu định lượng thường bị hiểu như việc chọn một bộ công cụ: làm survey hay experiment, dùng Likert hay thang 7 điểm, cần bao nhiêu mẫu, chạy t-test hay regression. Nhưng ở cấp sâu hơn, thiết kế định lượng là quá trình chuyển một câu hỏi nghiên cứu thành một cấu trúc kiểm chứng được bằng dữ liệu.

Nói cách khác, trước khi nghĩ đến code, phần mềm, hay thống kê, bạn phải trả lời được:

- tôi muốn biết điều gì;
- điều đó sẽ được đo bằng biến nào;
- sự khác biệt hay mối quan hệ nào là trung tâm;
- và thiết kế nào đủ mạnh để tạo ra loại bằng chứng tôi cần.

Đây chính là nơi rất nhiều nghiên cứu bắt đầu lệch. Có đề tài hỏi về nhân quả nhưng chỉ dùng thiết kế mô tả. Có đề tài cần so sánh theo thời gian nhưng lại chỉ đo một lần. Có đề tài chọn thang đo đẹp trên lý thuyết nhưng không phù hợp với đối tượng thật. Có đề tài chạy power analysis rất nghiêm túc nhưng lại đo sai construct từ đầu.

Antigravity rất hữu ích ở giai đoạn thiết kế định lượng vì nó giúp bạn:

- chuyển câu hỏi nghiên cứu thành mô hình biến rõ hơn;
- so sánh nhiều phương án thiết kế;
- tính cỡ mẫu và thử các kịch bản;
- dựng draft questionnaire và kiểm tra content validity;
- mô phỏng các tình huống thiết kế;
- và chuẩn bị protocol để bước sang thu thập dữ liệu.

Nhưng như mọi chương khác trong sách này, AI không chọn thiết kế thay bạn. Nó chỉ giúp bạn nhìn rõ lựa chọn, hệ quả, và điểm yếu của từng lựa chọn nhanh hơn.

---

## 6.1 Thiết Kế Định Lượng Thực Chất Là Gì?

Thiết kế định lượng là bản đồ logic nối giữa:

- câu hỏi nghiên cứu;
- khái niệm lý thuyết;
- biến đo lường;
- mẫu và đơn vị phân tích;
- quy trình thu dữ liệu;
- và kế hoạch phân tích.

### Một thiết kế định lượng tốt cần làm được 4 việc

1. **Khớp với câu hỏi nghiên cứu**

Thiết kế phải trả lời đúng loại câu hỏi:

- mô tả hiện trạng;
- so sánh giữa nhóm;
- dự đoán;
- kiểm định mô hình;
- hay đánh giá tác động.

2. **Cho phép đo lường đáng tin**

Khái niệm phải được chuyển thành biến quan sát được, với công cụ đủ rõ và đủ phù hợp với đối tượng.

3. **Cho phép suy luận hợp lý**

Bạn không thể đòi kết luận nhân quả mạnh từ một thiết kế chỉ quan sát cắt ngang, trừ khi cực kỳ cẩn trọng trong phạm vi kết luận.

4. **Khả thi trong bối cảnh thật**

Một thiết kế đẹp trên giấy nhưng vượt quá thời gian, nguồn lực, khả năng tiếp cận mẫu, hoặc yêu cầu đạo đức thì không phải thiết kế tốt.

### Một nguyên tắc rất quan trọng

> Thiết kế tốt không phải thiết kế “phức tạp nhất”. Thiết kế tốt là thiết kế đơn giản nhất nhưng đủ mạnh để trả lời câu hỏi nghiên cứu của bạn.

---

## 6.2 Bắt Đầu Từ Câu Hỏi Nghiên Cứu và Logic Suy Luận

Trước khi chọn survey hay experiment, hãy chốt xem câu hỏi nghiên cứu của bạn thuộc loại nào.

### Những loại câu hỏi thường gặp

| Loại câu hỏi | Ví dụ | Logic thiết kế thường gặp |
|---|---|---|
| Mô tả | Tỷ lệ giáo viên dùng AI trong dạy học là bao nhiêu? | Descriptive survey |
| So sánh | Học sinh nhóm STEM có điểm cao hơn nhóm truyền thống không? | Experimental / quasi-experimental / comparative |
| Liên hệ | Stress có liên quan đến hiệu quả công việc không? | Correlational |
| Dự đoán | Những yếu tố nào dự đoán mức sẵn sàng dùng AI? | Regression-based design |
| Kiểm định mô hình | Hỗ trợ nhà trường ảnh hưởng kết quả học tập qua động lực học tập? | SEM / mediation / moderation |

### Từ câu hỏi đến loại bằng chứng

Ví dụ:

- Nếu câu hỏi là “có khác biệt không?”, bạn cần so sánh nhóm.
- Nếu câu hỏi là “cái gì dự đoán cái gì?”, bạn cần một thiết kế đủ dữ liệu cho hồi quy hoặc mô hình đa biến.
- Nếu câu hỏi là “can thiệp có hiệu quả không?”, bạn cần thiết kế đủ sức nói về tác động, không chỉ về tương quan.

### Prompt chuyển RQ thành design logic

> 📋 **Prompt Template — RQ to Design Logic**
> ```
> Đây là research questions / hypotheses của tôi:
> [list]
> 
> Hãy giúp tôi:
> 1. Xác định loại câu hỏi của từng RQ/H
> 2. Gợi ý loại thiết kế định lượng phù hợp
> 3. Chỉ ra đơn vị phân tích của từng câu hỏi
> 4. Chỉ ra mức suy luận hợp lý mà thiết kế đó cho phép
> 5. Nêu 3 rủi ro nếu tôi chọn thiết kế quá yếu hoặc quá phức tạp
> ```

### Một câu hỏi tự kiểm

> Thiết kế này cho phép tôi kết luận điều tôi thực sự muốn kết luận, hay chỉ cho phép một kết luận yếu hơn?

Nếu bạn chưa trả lời rõ, chưa nên khóa thiết kế.

---

## 6.3 Các Thiết Kế Định Lượng Chính và Khi Nào Nên Dùng

Không phải cứ nghiên cứu định lượng là giống nhau. Mỗi thiết kế phù hợp với một kiểu logic khác nhau.

### 1. Descriptive Survey

Phù hợp khi mục tiêu là mô tả hiện trạng, tần suất, phân bố, mức độ của một hiện tượng.

**Ví dụ:**

- mức độ sử dụng AI của giáo viên THPT;
- mức độ hài lòng của sinh viên;
- tỷ lệ doanh nghiệp áp dụng một chính sách nào đó.

**Điểm mạnh:** nhanh, dễ triển khai, cho bức tranh rộng.

**Điểm yếu:** không mạnh về nhân quả.

### 2. Correlational Design

Phù hợp khi bạn muốn xem các biến liên hệ với nhau ra sao mà không can thiệp.

**Ví dụ:**

- stress liên hệ thế nào với hiệu quả công việc;
- thời gian tự học liên hệ thế nào với kết quả học tập.

**Điểm mạnh:** phù hợp cho nghiên cứu dự đoán và khám phá quan hệ.

**Điểm yếu:** rất dễ bị diễn giải quá mức thành nhân quả.

### 3. True Experimental Design

Phù hợp khi bạn có thể kiểm soát can thiệp và phân nhóm ngẫu nhiên.

**Ví dụ:**

- RCT so sánh hai phương pháp dạy học;
- thử nghiệm can thiệp trong điều kiện kiểm soát.

**Điểm mạnh:** mạnh nhất về suy luận nhân quả.

**Điểm yếu:** khó triển khai trong nhiều bối cảnh giáo dục/xã hội.

### 4. Quasi-Experimental Design

Phù hợp khi bạn có can thiệp hoặc so sánh nhưng không thể random assignment thật sự.

**Ví dụ:**

- so sánh hai lớp học sẵn có;
- pre-post ở một trường với nhóm đối chứng tương đương.

**Điểm mạnh:** thực tế hơn trong bối cảnh trường học và tổ chức.

**Điểm yếu:** yếu hơn RCT về kiểm soát selection bias.

### 5. Simulation / Model-Based Design

Phù hợp trong STEM hoặc các bài toán hệ thống khi đối tượng nghiên cứu là cơ chế, quá trình, hoặc tham số.

**Ví dụ:**

- Monte Carlo;
- FEM;
- system dynamics;
- optimization simulation.

**Điểm mạnh:** cho phép thử nhiều kịch bản.

**Điểm yếu:** chất lượng phụ thuộc rất mạnh vào giả định mô hình.

### Bảng chọn nhanh

| Mục tiêu nghiên cứu | Thiết kế nên cân nhắc |
|---|---|
| Mô tả hiện trạng | Descriptive survey |
| Xem quan hệ giữa biến | Correlational / regression |
| Đánh giá tác động có thể random | True experimental |
| Đánh giá tác động khó random | Quasi-experimental |
| Nghiên cứu hệ thống/kịch bản | Simulation |

> ⚠️ **Cảnh báo:** Một thiết kế tương quan không tự động “nâng cấp” thành thiết kế nhân quả chỉ vì bạn chạy mô hình phức tạp hơn.

---

## 6.4 Biến, Construct và Operationalization

Đây là khâu mà rất nhiều nghiên cứu định lượng bị yếu ngay từ nền.

### Từ lý thuyết sang biến

Bạn thường bắt đầu bằng một construct ở cấp khái niệm:

- động lực học tập;
- burnout;
- self-efficacy;
- perceived organizational support.

Nhưng dataset không chứa “construct” ở dạng thuần túy. Nó chứa biến được operationalize từ construct đó.

### Một quy trình hữu ích

1. Xác định construct.
2. Định nghĩa hoạt động (operational definition).
3. Chọn hoặc xây công cụ đo.
4. Quyết định biến quan sát và cách mã hóa.
5. Kiểm tra độ phù hợp với đối tượng nghiên cứu.

### Các loại biến thường gặp

| Loại biến | Vai trò |
|---|---|
| Independent variable (IV) | yếu tố dự đoán/tác động |
| Dependent variable (DV) | kết quả đầu ra |
| Covariate | biến kiểm soát |
| Moderator | biến làm thay đổi độ mạnh/hướng quan hệ |
| Mediator | biến trung gian giải thích cơ chế |

### Sai lầm thường gặp

- gọi tên construct rất hay nhưng item đo không phản ánh đủ construct;
- dùng một biến rất thô để đại diện cho khái niệm phức tạp;
- không tách rõ outcome chính và biến kiểm soát;
- tạo quá nhiều biến mà không biết biến nào thật sự trả lời RQ.

### Prompt lập variable map

> 📋 **Prompt Template — Construct to Variable Map**
> ```
> Đây là các construct trong nghiên cứu của tôi:
> [list]
> 
> Với mỗi construct, hãy giúp tôi:
> 1. Viết operational definition
> 2. Gợi ý biến quan sát / item types phù hợp
> 3. Xác định vai trò: IV / DV / covariate / moderator / mediator
> 4. Chỉ ra rủi ro nếu operationalization quá thô
> 5. Gợi ý cách trình bày bảng variable map trong proposal
> ```

---

## 6.5 Validity, Reliability và Chất Lượng Thiết Kế

Một thiết kế định lượng mạnh không chỉ nằm ở cỡ mẫu. Nó còn nằm ở chất lượng của suy luận và đo lường.

### Internal validity

Câu hỏi: nếu bạn thấy một hiệu ứng, liệu nó có thực sự đến từ yếu tố bạn quan tâm không?

Rủi ro thường gặp:

- selection bias;
- maturation;
- history effects;
- testing effects;
- confounding variables.

### External validity

Câu hỏi: kết quả này có thể áp dụng sang bối cảnh khác đến đâu?

Rủi ro thường gặp:

- mẫu quá hẹp;
- bối cảnh quá đặc thù;
- công cụ đo chỉ phù hợp một nhóm nhỏ.

### Construct validity

Câu hỏi: bạn có thật sự đo đúng khái niệm mình muốn đo không?

### Reliability

Câu hỏi: công cụ đo có ổn định và nhất quán không?

### Một điều rất hay bị hiểu sai

Nhiều người nghĩ chỉ cần Cronbach's alpha là xong reliability. Thực tế:

- alpha chỉ là một mảnh của câu chuyện;
- reliability không cứu được một construct được operationalize kém;
- một thang đo rất nhất quán vẫn có thể đo sai thứ bạn muốn đo.

### Prompt stress-test thiết kế

> 📋 **Prompt Template — Quant Design Stress Test**
> ```
> Hãy đóng vai methodological reviewer cho thiết kế định lượng của tôi:
> - Topic: [topic]
> - Design: [type]
> - Variables: [list]
> - Instrument(s): [list]
> - Sample: [mô tả]
> 
> Hãy phản biện theo:
> 1. Internal validity
> 2. External validity
> 3. Construct validity
> 4. Reliability risks
> 5. Tính khả thi trong bối cảnh thật
> ```

---

## 6.6 Tính Cỡ Mẫu và Power Analysis

![Thiết Kế Thí Nghiệm & Tính Cỡ Mẫu](../assets/images/ch06_experiment_design_1776094243567.png)

Power analysis là nơi AI và code hỗ trợ rất tốt, nhưng trước hết bạn phải hiểu mình đang tính cho cái gì.

### Cỡ mẫu không phải chỉ để “đủ đẹp”

Cỡ mẫu cần gắn với:

- loại phân tích chính;
- effect size kỳ vọng;
- mức alpha;
- desired power;
- số nhóm hoặc số predictors;
- và tỷ lệ dropout/invalid responses.

### Một câu hỏi nên tự hỏi trước

> Tôi đang tính cỡ mẫu cho phân tích nào là phân tích chính?

Nếu không chốt được điều này, power analysis dễ trở thành hình thức.

### Prompt power analysis

> 📋 **Prompt Template — Power Analysis**
> ```
> Tính cỡ mẫu cho nghiên cứu của tôi:
> - Main analysis: [t-test / ANOVA / regression / chi-square / SEM]
> - Expected effect size: [ước tính]
> - Alpha: 0.05
> - Desired power: 0.80
> - Number of groups/predictors: [n]
> - Expected dropout/invalid rate: [%]
> 
> Tôi cần:
> 1. Code Python để tính
> 2. Kết quả cỡ mẫu tối thiểu
> 3. Điều chỉnh cho dropout
> 4. Giải thích effect size assumption có hợp lý không
> 5. Một đoạn mô tả có thể đưa vào proposal
> ```

### Ví dụ code đơn giản

```python
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()
n_per_group = analysis.solve_power(
    effect_size=0.5,
    alpha=0.05,
    power=0.80,
    alternative="two-sided"
)

dropout_rate = 0.15
adjusted_n = int(n_per_group / (1 - dropout_rate))

print(f"N toi thieu moi nhom: {int(n_per_group)}")
print(f"N sau dieu chinh dropout: {adjusted_n}")
print(f"Tong co mau: {adjusted_n * 2}")
```

### Với SEM thì sao?

Với SEM, cỡ mẫu không nên dựa vào một “quy tắc thần kỳ” duy nhất. Bạn cần nhìn đồng thời:

- độ phức tạp của mô hình;
- số observed variables;
- số parameters;
- chất lượng dữ liệu;
- và mục tiêu của mô hình (exploratory hay confirmatory).

> ⚠️ **Cảnh báo:** Đừng dùng một effect size “medium” mặc định chỉ vì sách hay ví dụ code dùng như vậy. Effect size giả định nên có căn cứ từ literature hoặc ít nhất phải được biện minh.

---

## 6.7 Thiết Kế Công Cụ Đo Lường

Đây là phần quyết định chất lượng của dữ liệu nhiều hơn cả công cụ phần mềm.

### Khi nào nên dùng thang đo có sẵn?

- construct đã ổn định trong literature;
- đã có validated scale;
- đối tượng nghiên cứu gần với bối cảnh scale gốc;
- bạn có thể xin phép hoặc trích dẫn đúng cách.

### Khi nào cần điều chỉnh hoặc xây mới?

- bối cảnh Việt Nam quá khác;
- đối tượng nghiên cứu khác biệt đáng kể;
- construct mới nổi;
- ngôn ngữ gốc không phù hợp;
- hoặc bạn cần instrument rất đặc thù cho một can thiệp cụ thể.

### Một questionnaire tốt nên có gì?

- item rõ, không ambiguous;
- tránh double-barreled;
- tránh leading wording;
- có ngôn ngữ phù hợp với population;
- có cấu trúc hợp lý về thứ tự;
- và có pilot test trước khi triển khai lớn.

### Prompt phát triển questionnaire

> 📋 **Prompt Template — Questionnaire Development**
> ```
> Giúp tôi thiết kế questionnaire cho nghiên cứu:
> - Construct(s): [list]
> - Operational definitions: [list]
> - Population: [mô tả]
> - Theoretical basis: [nếu có]
> 
> Yêu cầu:
> 1. Gợi ý 5-8 items cho mỗi construct
> 2. Chỉ ra item nào nên reverse-coded (nếu thực sự cần)
> 3. Kiểm tra ambiguity và double-barreled wording
> 4. Gợi ý cách pilot test
> 5. Tạo bảng item map: item / construct / source / notes
> ```

### Content validity cần nghĩ thế nào?

Content validity không phải chỉ là “nhờ 2 chuyên gia đọc qua”. Nó là câu hỏi:

- item có thực sự bao phủ construct không;
- có chiều cạnh nào bị thiếu không;
- item có phù hợp văn hóa và trình độ ngôn ngữ của người trả lời không.

### Prompt check content validity

> 📋 **Prompt Template — Content Validity Check**
> ```
> Đây là draft instrument của tôi:
> - Construct: [name]
> - Definition: [definition]
> - Items: [list]
> - Population: [mô tả]
> 
> Hãy đánh giá:
> 1. Item nào đo đúng construct
> 2. Item nào mơ hồ hoặc hỏi hai việc cùng lúc
> 3. Chiều cạnh nào của construct đang bị thiếu
> 4. Chỗ nào cần sửa ngôn ngữ cho phù hợp population
> ```

---

## 6.8 Thiết Kế Thí Nghiệm, Quasi-Experiment và Simulation

Không phải nghiên cứu định lượng nào cũng là survey.

### Với experimental/quasi-experimental design

Bạn cần chốt rõ:

- nhóm nào là can thiệp, nhóm nào là đối chứng;
- có pre-test không;
- thời gian can thiệp bao lâu;
- can thiệp được chuẩn hóa thế nào;
- fidelity of implementation được kiểm tra ra sao;
- và yếu tố nào có thể gây nhiễu.

### Những câu hỏi rất đáng hỏi

- Nếu không random được, tôi giảm selection bias bằng cách nào?
- Nếu hai nhóm khác nhau từ đầu, tôi xử lý thế nào trong phân tích?
- Nếu can thiệp triển khai không đồng đều, tôi ghi nhận điều đó ra sao?

### Với simulation/STEM design

Bạn phải nói rõ:

- hệ thống nào đang được mô phỏng;
- giả định nào được đưa vào mô hình;
- tham số nào thay đổi;
- baseline là gì;
- metric đánh giá là gì;
- và kết quả simulation được kiểm chứng ở mức nào.

### Prompt thiết kế simulation

> 📋 **Prompt Template — Simulation Design**
> ```
> Tôi cần thiết kế simulation study:
> - System/problem: [mô tả]
> - Parameters: [list]
> - Baseline: [method]
> - Metrics: [list]
> 
> Hãy giúp tôi:
> 1. Xây logic simulation design
> 2. Chỉ ra giả định nào là quan trọng nhất
> 3. Gợi ý sensitivity analysis
> 4. Viết skeleton code cho environment + evaluation
> 5. Chỉ ra chỗ nào kết quả simulation có thể bị hiểu quá mức
> ```

### Một cảnh báo

Một simulation rất đẹp không tự động là bằng chứng mạnh nếu giả định đầu vào quá lỏng hoặc không có đối chiếu hợp lý với hệ thống thực.

---

## 6.9 Sampling Strategy và Data Collection Protocol

Thiết kế định lượng không kết thúc ở khâu “chọn survey”. Nó phải đi tới một protocol đủ rõ để người khác hiểu bạn sẽ thu dữ liệu như thế nào.

### Sampling strategy cần trả lời

- population là ai;
- sampling frame là gì;
- cách chọn mẫu ra sao;
- cỡ mẫu tối thiểu là bao nhiêu;
- tỷ lệ phản hồi kỳ vọng là bao nhiêu;
- nếu response rate thấp thì phương án dự phòng là gì.

### Data collection protocol nên có

- timeline;
- từng bước triển khai;
- ai phụ trách bước nào;
- quality control;
- cách ghi nhận lỗi và ngoại lệ;
- cách quản lý dữ liệu sau khi thu.

### Prompt tạo protocol

> 📋 **Prompt Template — Data Collection Protocol**
> ```
> Tạo data collection protocol cho nghiên cứu:
> - Design: [type]
> - Population: [description]
> - Sample size target: [N]
> - Sampling strategy: [mô tả]
> - Data collection method: [survey / experiment / observation / simulation]
> - Duration: [timeframe]
> 
> Protocol cần có:
> 1. Timeline
> 2. Quy trình từng bước
> 3. Quality control measures
> 4. Ethical considerations
> 5. Data management notes
> 6. Contingency plan nếu response rate thấp hoặc dữ liệu lỗi
> ```

### Điểm nối sang Chương 9

Nếu Chương 6 làm tốt, bước sang Chương 9 bạn sẽ không còn “đi tìm dữ liệu”. Bạn chỉ còn việc triển khai một quy trình đã được thiết kế sẵn.

---

## 6.10 Những Sai Lầm Thiết Kế Định Lượng Rất Hay Gặp

### 1. Chọn design vì quen, không vì câu hỏi

### 2. Đặt mục tiêu nhân quả cho một thiết kế không đủ sức

### 3. Dùng construct lớn nhưng đo bằng biến quá thô

### 4. Tính cỡ mẫu mà không chốt main analysis

### 5. Xây questionnaire mà không pilot test

### 6. Đánh giá thấp bối cảnh triển khai thật

Ví dụ:

- giáo viên không đủ thời gian trả lời;
- học sinh không hiểu wording;
- nhóm đối chứng bị “nhiễm” can thiệp;
- response rate thấp hơn dự kiến nhiều.

### Checklist tự rà cuối chương

- RQ/H đã nối rõ với design chưa?
- Variable map đã rõ chưa?
- Power analysis có gắn với phân tích chính chưa?
- Instrument có pilot test và content validity plan chưa?
- Protocol thu dữ liệu có khả thi không?
- Tôi có đang đòi thiết kế này nói nhiều hơn thứ nó thật sự cho phép không?

---

## 6.11 Workflow Gợi Ý Với Antigravity

Một workflow thực dụng cho chương này:

1. Xác định RQ/H và loại logic suy luận.
2. Chọn thiết kế định lượng phù hợp.
3. Tạo construct-to-variable map.
4. Stress-test validity và feasibility.
5. Tính cỡ mẫu cho main analysis.
6. Thiết kế hoặc điều chỉnh instrument.
7. Viết sampling plan và data collection protocol.
8. Chỉ khi đó mới chuyển sang Chương 9 để triển khai thu dữ liệu.

### Prompt tổng hợp

> 📋 **Prompt Template — End-to-End Quant Design**
> ```
> Tôi cần thiết kế nghiên cứu định lượng cho đề tài:
> - Topic: [topic]
> - RQ/H: [list]
> - Population: [description]
> - Constraints: [time/resource/access]
> 
> Hãy giúp tôi:
> 1. Chọn design phù hợp
> 2. Tạo variable map
> 3. Xác định instrument needs
> 4. Tính cỡ mẫu cho main analysis
> 5. Tạo sampling + data collection protocol
> 6. Chỉ ra 3 điểm yếu lớn nhất của thiết kế hiện tại
> ```

---

## 6.12 Bài Tập Thực Hành

### 🔧 Hands-on 6.1: RQ-to-Design Map

Lập bảng:

| Research Question | Design | Variables | Level of Inference |

Điền cho toàn bộ các câu hỏi nghiên cứu hiện có của bạn.

### 🔧 Hands-on 6.2: Power and Sample Plan

Tính cỡ mẫu cho phân tích chính và ghi rõ:

- effect size assumption;
- dropout assumption;
- cỡ mẫu mục tiêu cuối cùng.

### 🔧 Hands-on 6.3: Instrument Draft

Chọn một construct chính, tạo draft items, rồi tự rà:

- item nào mơ hồ;
- item nào double-barreled;
- item nào có nguy cơ không phù hợp với population.

### 🔧 Hands-on 6.4: Protocol Brief

Viết một trang tóm tắt:

- design;
- sample;
- instruments;
- timeline;
- risks;
- contingency plan.

---

## 6.13 Tóm Tắt Chương

Thiết kế nghiên cứu định lượng là bước bạn biến câu hỏi nghiên cứu thành một kiến trúc bằng chứng có thể kiểm chứng được. Giá trị của bước này không nằm ở việc chọn được mô hình hay công cụ “xịn” nhất, mà ở chỗ bạn chọn được thiết kế phù hợp nhất với câu hỏi, đo đúng điều cần đo, tính được cỡ mẫu cho phân tích chính, và chuẩn bị một protocol đủ mạnh để giai đoạn thu dữ liệu và phân tích sau đó không bị chệch hướng. AI giúp bạn nhìn thiết kế rõ hơn, stress-test nhanh hơn, và chuẩn bị tài liệu tốt hơn, nhưng quyết định phương pháp vẫn phải là việc của nhà nghiên cứu.

**Deliverable cuối chương:** đến đây, bạn nên có một `quant design kit` gồm:

- RQ-to-design map;
- construct-to-variable map;
- power analysis note;
- instrument draft và content validity plan;
- sampling strategy;
- data collection protocol.

Nếu đây là hướng chính của đề tài, bộ này sẽ dẫn thẳng sang `Chương 9` để thu dữ liệu. Nếu sau này bạn chuyển sang mixed methods, đây vẫn là một nửa nền không thể thiếu: nhánh định lượng phải đủ rõ trước khi có thể tích hợp với nhánh định tính ở `Chương 8`.

---

> 📖 **Tiếp theo:** [Chương 7: Thiết Kế Nghiên Cứu Định Tính →](chuong-07-dinh-tinh.md)

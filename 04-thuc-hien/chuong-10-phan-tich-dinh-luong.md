# Chương 10: Phân Tích Dữ Liệu Định Lượng

![Stats Analysis](../assets/images/ch10_stats_analysis_1776092366432.png)

---

> *"Statistics is the grammar of science."* — Karl Pearson

---

Nhiều người bước vào giai đoạn phân tích định lượng với một cảm giác khá giống nhau: dữ liệu đã có rồi, bây giờ chỉ cần “chạy thống kê”. Chính cách nghĩ này là nguồn gốc của rất nhiều sai lầm. Phân tích định lượng không phải là chuỗi thao tác phần mềm, cũng không phải trò chọn phép kiểm nào “ra p-value đẹp hơn”. Nó là quá trình biến câu hỏi nghiên cứu thành bằng chứng có thể kiểm tra được, rồi diễn giải bằng chứng đó một cách trung thực.

Vì vậy, chương này không đi theo hướng “học thuộc tên các test”. Câu hỏi trung tâm ở đây là:

**với loại câu hỏi nghiên cứu này, kiểu dữ liệu này, và giới hạn thiết kế này, đâu là cách phân tích hợp lý nhất để đưa ra kết luận vừa đúng vừa có trách nhiệm?**

Antigravity có thể giúp bạn rất nhiều trong giai đoạn này. Bạn có thể:

- làm sạch dữ liệu;
- chạy thống kê mô tả và suy luận;
- kiểm tra giả định;
- tạo bảng và figure reproducible;
- soạn đoạn báo cáo theo chuẩn học thuật;
- rà logic diễn giải và so sánh với literature.

Nhưng AI và code chỉ làm cho bạn nhanh hơn. Chúng không thay thế được các quyết định cốt lõi:

- biến nào là trọng tâm;
- phép phân tích nào thật sự phù hợp;
- kết quả nào đáng nhấn mạnh;
- và quan trọng nhất, điều gì **chưa thể kết luận** từ dữ liệu hiện có.

Chương này được đọc tốt nhất khi bạn đã có từ `Chương 6` một thiết kế định lượng đủ rõ, và từ `Chương 9` một bộ dữ liệu đã được tổ chức, làm sạch ở mức cơ bản, và ghi log đủ để truy nguồn. Khi đó, phân tích không còn là bước “mò trong dataset”, mà là bước kiểm tra xem bằng chứng thực tế có đang trả lời đúng câu hỏi bạn đã thiết kế từ đầu hay không.

---

## 10.1 Phân Tích Định Lượng Thực Chất Là Gì?

Phân tích định lượng là quá trình dùng dữ liệu có cấu trúc để trả lời một câu hỏi nghiên cứu bằng logic suy luận rõ ràng.

### Nó không chỉ là tính toán

Một phân tích định lượng tốt luôn gắn với ít nhất 5 lớp quyết định:

1. **Câu hỏi nghiên cứu là gì?**
2. **Biến nào đại diện cho khái niệm đó?**
3. **Mô hình hoặc phép kiểm nào phù hợp với câu hỏi và cấu trúc dữ liệu?**
4. **Các giả định của mô hình có được đáp ứng không?**
5. **Kết quả có ý nghĩa thực chất không, ngoài việc có ý nghĩa thống kê không?**

Nếu bạn bỏ qua bất kỳ lớp nào trong số này, phân tích dễ trở thành “chạy test cho có”.

### Từ câu hỏi đến phân tích

Ví dụ:

- Nếu câu hỏi là “hai nhóm có khác nhau không?”, bạn đang ở logic so sánh.
- Nếu câu hỏi là “biến X liên hệ với Y ra sao?”, bạn đang ở logic tương quan hoặc hồi quy.
- Nếu câu hỏi là “nhiều biến cùng dự đoán Y như thế nào?”, bạn đang ở logic mô hình đa biến.
- Nếu câu hỏi là “cấu trúc khái niệm và quan hệ giữa các biến tiềm ẩn là gì?”, bạn có thể bước sang CFA/SEM.

### Một nguyên tắc rất quan trọng

> Không có phép kiểm nào “mạnh” một cách tuyệt đối. Chỉ có phép phân tích phù hợp hay không phù hợp với câu hỏi, dữ liệu và thiết kế.

Đây là chỗ AI rất dễ bị lạm dụng. Nếu bạn chỉ đưa cho AI tên biến và yêu cầu “chọn giúp tôi test tốt nhất”, nó có thể gợi ý một phép kiểm nghe đúng nhưng không hiểu đầy đủ bối cảnh thiết kế của bạn. Vì vậy, trước khi đòi AI trả lời, bạn phải tự làm rõ bối cảnh phương pháp.

---

## 10.2 Quy Trình Phân Tích Tổng Quát

Một pipeline gọn nhưng đáng tin thường đi như sau:

```text
Raw Data
  ↓
Data Audit
  ↓
Cleaning & Recoding
  ↓
Descriptive Statistics
  ↓
Assumption Checking
  ↓
Inferential Analysis / Modeling
  ↓
Effect Size & Robustness
  ↓
Visualization
  ↓
Interpretation & Reporting
```

### Ý nghĩa của từng bước

**Data audit**

Bạn kiểm tra:

- số dòng, số cột;
- missing data;
- giá trị bất thường;
- lỗi mã hóa;
- biến trùng hoặc biến sai kiểu.

**Cleaning & recoding**

Đây là bước chuẩn hóa để dữ liệu có thể phân tích đúng:

- recode biến phân loại;
- tạo composite scores;
- xác định và đánh dấu missing;
- tách bản raw với processed.

**Descriptive statistics**

Không chỉ để “mô tả cho có”, mà để hiểu dữ liệu trước khi chạy mô hình.

**Assumption checking**

Đây là chỗ rất nhiều người bỏ qua, rồi sau đó diễn giải kết quả quá tự tin.

**Inferential analysis**

Lúc này bạn mới chạy test hoặc mô hình chính, chứ không phải từ đầu.

**Effect size & robustness**

Một kết quả có p nhỏ chưa chắc quan trọng về mặt thực chất. Bạn phải xem effect size và độ ổn định của kết quả.

**Interpretation**

Đây là giai đoạn nối con số với câu hỏi nghiên cứu, chứ không biến con số thành những kết luận lớn hơn mức dữ liệu cho phép.

### Prompt dựng analysis pipeline

> 📋 **Prompt Template — Quant Analysis Pipeline**
> ```
> Tôi cần lập quy trình phân tích định lượng cho nghiên cứu:
> - Research questions / hypotheses: [list]
> - Dataset: [mô tả]
> - Variables: [list]
> - Sample size: [N]
> 
> Hãy giúp tôi:
> 1. Xây analysis pipeline theo từng bước
> 2. Chỉ ra bước nào là bắt buộc trước khi chạy mô hình
> 3. Gợi ý outputs cần lưu ở mỗi bước
> 4. Nêu 3 rủi ro nếu tôi đi quá nhanh vào inferential tests
> ```

---

## 10.3 Bắt Đầu Từ Câu Hỏi Nghiên Cứu, Không Bắt Đầu Từ p-value

Đây là chỗ phân biệt giữa một người “biết dùng thống kê” và một người “làm nghiên cứu bằng thống kê”.

### Hãy viết câu hỏi phân tích dưới dạng rõ ràng

Ví dụ:

- Nhóm can thiệp có điểm hậu kiểm cao hơn nhóm đối chứng không?
- Kinh nghiệm giảng dạy, quy mô lớp học, và mức hỗ trợ của nhà trường có dự đoán hiệu quả giảng dạy không?
- Mối quan hệ giữa mức độ stress và hiệu quả công việc có khác nhau theo giới tính không?

Mỗi câu như vậy kéo theo một cấu trúc phân tích khác.

### Từ khái niệm đến biến

Rất nhiều lỗi phân tích xảy ra vì người nghiên cứu trượt từ khái niệm sang biến quá nhanh.

Ví dụ:

- “burnout” có thể là tổng điểm, hoặc 3 chiều thành phần;
- “hiệu quả học tập” có thể là điểm cuối kỳ, gain score, hoặc composite competency index;
- “hỗ trợ triển khai” có thể là một thang đo hay chỉ là một biến phân loại thô.

Nếu bạn không làm rõ biến đại diện cho khái niệm nào, phần diễn giải sẽ rất dễ bị phóng đại.

### Prompt audit từ RQ sang biến

> 📋 **Prompt Template — RQ to Variable Map**
> ```
> Đây là research questions / hypotheses của tôi:
> [list]
> 
> Đây là các biến hiện có trong dataset:
> [list]
> 
> Hãy giúp tôi:
> 1. Ghép từng RQ/H với các biến tương ứng
> 2. Chỉ ra biến nào là DV, IV, covariate, moderator, mediator
> 3. Chỉ ra chỗ nào khái niệm và biến đang chưa khớp
> 4. Đề xuất một bảng analysis plan ngắn gọn
> ```

### Một câu hỏi tự kiểm

> Nếu tôi đưa dataset này cho một người khác, họ có hiểu ngay biến nào dùng để trả lời RQ nào không?

Nếu chưa, analysis plan cần làm lại rõ hơn.

---

## 10.4 Làm Sạch, Khám Phá và Thống Kê Mô Tả

Đây là giai đoạn dễ bị xem nhẹ, nhưng lại quyết định phần lớn độ tin cậy của toàn bộ phân tích.

### Data cleaning không chỉ là “xóa missing”

Bạn cần kiểm tra:

- dữ liệu nhập sai;
- giá trị ngoài khoảng hợp lệ;
- biến đảo chiều chưa recode;
- duplicated rows;
- dạng ngày tháng hoặc ký tự bị đọc sai;
- missing do lỗi quy trình hay do logic của thiết kế.

### Missing data: nhìn đúng trước khi xử lý

Không phải missing nào cũng giống nhau:

- missing hoàn toàn ngẫu nhiên;
- missing có liên quan đến nhóm người tham gia;
- missing do skip logic;
- missing do dữ liệu không được ghi nhận.

Xử lý missing mà không hiểu nguyên nhân có thể làm méo kết quả.

### Thống kê mô tả phải trả lời điều gì?

- Mẫu của tôi trông như thế nào?
- Các biến có phân phối ra sao?
- Có outlier hoặc pattern bất thường nào không?
- Các nhóm có mất cân bằng lớn không?

### Prompt cho descriptive statistics

> 📋 **Prompt Template — Descriptive Statistics**
> ```
> Đọc file dữ liệu tại [path].
> 
> Hãy thực hiện:
> 1. Demographic summary
> 2. Mean/SD/Min/Max cho biến liên tục
> 3. Frequency table cho biến phân loại
> 4. Missing data summary
> 5. Distribution plots cho các biến chính
> 6. Một bảng mô tả có thể dùng cho thesis/journal
> 
> Kèm theo:
> - code reproducible
> - cảnh báo nếu có biến bất thường
> - gợi ý chỗ cần kiểm tra tay
> ```

### Ví dụ code khởi đầu

```python
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/survey_data.csv")

continuous_vars = ["age", "experience_years", "score_pre", "score_post"]
categorical_vars = ["gender", "school_type", "region"]

desc = df[continuous_vars].describe().T
desc["skew"] = df[continuous_vars].skew()
desc["kurtosis"] = df[continuous_vars].kurtosis()
print(desc.round(3))

for var in categorical_vars:
    print(f"\n{var}")
    print(df[var].value_counts(dropna=False))

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for idx, var in enumerate(continuous_vars):
    ax = axes[idx // 2, idx % 2]
    sns.histplot(df[var].dropna(), kde=True, ax=ax)
    shapiro_stat, shapiro_p = stats.shapiro(df[var].dropna())
    ax.set_title(f"{var} | Shapiro p = {shapiro_p:.3f}")

plt.tight_layout()
plt.savefig("results/figures/distribution-checks.png", dpi=300)
```

### Vì sao phân tích dữ liệu nghiên cứu thường hay dùng Python?

Trong khoảng 10 năm gần đây, `Python` xuất hiện ngày càng nhiều trong workflow phân tích dữ liệu nghiên cứu. Điều này không có nghĩa là mọi nhà nghiên cứu đều phải dùng Python, và cũng không có nghĩa Python luôn tốt hơn `R`, `SPSS`, hay `Stata`. Nhưng nó phổ biến vì một số lý do rất thực dụng:

1. **Đọc và xử lý dữ liệu dạng bảng rất thuận**  
   Với `pandas`, bạn có thể đọc `CSV`, làm sạch dữ liệu, recode biến, gộp bảng, lọc mẫu, và tạo biến mới trong cùng một luồng làm việc.

2. **Một môi trường có thể làm được nhiều việc liên tiếp**  
   Cùng một script có thể:
   - nhập dữ liệu;
   - làm sạch;
   - chạy thống kê;
   - vẽ figure;
   - và xuất kết quả ra file.

3. **Phù hợp với workflow tái lập**  
   Thay vì click từng bước rồi quên mình đã làm gì, bạn giữ lại toàn bộ quy trình dưới dạng script. Điều này rất hữu ích khi cần chạy lại phân tích, sửa dữ liệu, hoặc giải thích phương pháp cho GVHD và reviewer.

4. **Kết nối tốt với dữ liệu từ nhiều nguồn**  
   Python hợp với dữ liệu từ khảo sát, log hệ thống, dữ liệu web, API, file `CSV`, Excel, cơ sở dữ liệu, thậm chí kết hợp với OCR hoặc scraping ở các bước trước đó.

5. **Hệ sinh thái thư viện rất rộng**  
   `pandas`, `numpy`, `scipy`, `statsmodels`, `scikit-learn`, `matplotlib`, `seaborn`... đủ mạnh để đáp ứng phần lớn nhu cầu phân tích định lượng ứng dụng.

6. **AI hỗ trợ viết và giải thích code Python khá tốt**  
   Đây là một lý do rất thực tế. Với mô tả phân tích đủ rõ, AI thường có thể draft nhanh code Python ở mức dùng được, giúp người nghiên cứu rút ngắn thời gian từ `analysis plan` sang `script đầu tiên`.

Điều quan trọng là: người nghiên cứu không cần trung thành tuyệt đối với Python. Nếu khoa của bạn quen `SPSS`, nhóm nghiên cứu của bạn dùng `R`, hoặc field của bạn quen `Stata`, bạn hoàn toàn có thể đi theo những công cụ đó. Thứ cần giữ ổn định không phải tên phần mềm, mà là **logic phân tích**.

### AI có thể giúp chuyển từ analysis plan sang script như thế nào?

Đây là một trong những chỗ AI hữu ích nhất với người học nghiên cứu:

- bạn mô tả `research question`, biến, loại mô hình, và các giả định cần kiểm tra;
- AI draft một script đầu tiên bằng Python;
- sau đó AI có thể giúp **dịch cùng logic đó** sang `R`, `SPSS syntax`, hoặc `Stata do-file`.

Cách dùng đúng ở đây là: xem AI như một **lớp chuyển ngữ giữa logic phương pháp và cú pháp công cụ**.

Điều AI có thể hỗ trợ tốt:

- viết skeleton script ban đầu;
- chuyển cùng một phân tích sang nhiều môi trường phần mềm;
- thêm comment để bạn hiểu từng bước đang làm gì;
- chỉ ra chỗ nào cần đổi nếu biến là categorical, ordinal, repeated measures, hay clustered data.

Điều AI không nên được phép quyết định thay bạn:

- tên biến nào thực sự đúng trong dataset;
- dữ liệu đã được recode đúng chưa;
- missing values đang mang ý nghĩa gì;
- mô hình nào là lựa chọn tốt nhất về mặt phương pháp;
- và kết luận nào là hợp lý từ output.

### Ví dụ minh họa: một bài toán, bốn môi trường

Giả sử bạn có file `survey_data.csv` và muốn kiểm tra:

- `post_score` là biến phụ thuộc;
- `pre_score` là covariate liên tục;
- `group_code` là nhóm can thiệp/đối chứng;
- `gender_code` là biến kiểm soát.

Mục tiêu là chạy một mô hình để xem `group_code` còn dự đoán `post_score` sau khi đã kiểm soát `pre_score` hay không.

#### Python

```python
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/processed/survey_data.csv")

model = smf.ols(
    "post_score ~ pre_score + C(group_code) + C(gender_code)",
    data=df
).fit()

print(model.summary())
```

#### R

```r
df <- read.csv("data/processed/survey_data.csv")

model <- lm(
  post_score ~ pre_score + factor(group_code) + factor(gender_code),
  data = df
)

summary(model)
```

#### SPSS Syntax

```spss
GET DATA
  /TYPE=TXT
  /FILE='data/processed/survey_data.csv'
  /DELCASE=LINE
  /DELIMITERS=","
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2.

UNIANOVA post_score BY group_code gender_code WITH pre_score
  /METHOD=SSTYPE(3)
  /INTERCEPT=INCLUDE
  /PRINT=DESCRIPTIVE PARAMETER ETASQ
  /DESIGN=pre_score group_code gender_code.
```

#### Stata

```stata
import delimited "data/processed/survey_data.csv", clear
reg post_score c.pre_score i.group_code i.gender_code
```

Điều đáng chú ý ở đây là: cú pháp khác nhau, nhưng **logic phân tích là cùng một logic**:

- nhập dữ liệu;
- xác định biến phụ thuộc, biến liên tục, biến phân loại;
- khai báo đúng vai trò của biến;
- chạy mô hình;
- rồi đọc kết quả theo cùng một câu hỏi nghiên cứu.

Nếu bạn mô tả logic đủ rõ, AI có thể giúp bạn đi từ:

`analysis plan -> Python script -> R script -> SPSS syntax -> Stata do-file`

mà không phải bắt đầu lại từ đầu ở từng phần mềm.

### Prompt để nhờ AI chuyển logic phân tích sang công cụ khác

> 📋 **Prompt Template — Translate Analysis Across Tools**
> ```
> Tôi có phân tích định lượng với thông tin sau:
> - Research question: [question]
> - Dependent variable: [DV]
> - Independent variables / covariates: [list]
> - Variable types: [continuous / categorical / ordinal]
> - Dataset path: [path]
> - Desired model/test: [model]
> 
> Hãy giúp tôi:
> 1. Viết script Python có comment ngắn
> 2. Viết phiên bản tương đương bằng R
> 3. Viết SPSS syntax tương đương
> 4. Viết Stata syntax tương đương
> 5. Chỉ ra chỗ nào cần điều chỉnh nếu biến phân loại đang được mã hóa khác
> 6. Nêu 3 điểm tôi bắt buộc phải kiểm tra tay trước khi chạy
> ```

Khi dùng prompt kiểu này, bạn sẽ thấy AI hữu ích nhất không phải ở chỗ “biết nhiều cú pháp”, mà ở chỗ nó giúp bạn nhận ra:

- đâu là phần cốt lõi của logic phân tích;
- đâu là phần chỉ khác nhau do ngôn ngữ phần mềm;
- và đâu là những giả định phương pháp vẫn phải do con người tự kiểm.

### Một lỗi hay gặp

Thấy Shapiro-Wilk p < .05 là lập tức kết luận “không được dùng parametric tests”. Điều này quá máy móc. Với mẫu lớn, kiểm định normality rất nhạy. Bạn cần xem thêm:

- histogram;
- Q-Q plot;
- skewness/kurtosis;
- và đặc biệt là loại mô hình bạn đang dùng.

---

## 10.5 Chọn Phép Kiểm Hay Mô Hình Phù Hợp

Đây là phần hay bị biến thành cây quyết định cơ học. Cây quyết định hữu ích, nhưng chỉ khi bạn hiểu logic bên dưới.

### Một bảng chọn nhanh

| Câu hỏi phân tích | Điều kiện thường gặp | Lựa chọn hay gặp |
|---|---|---|
| So sánh 2 nhóm độc lập | DV liên tục | Independent t-test / Mann-Whitney U |
| So sánh 2 thời điểm cùng nhóm | DV liên tục | Paired t-test / Wilcoxon |
| So sánh >2 nhóm | DV liên tục | ANOVA / Kruskal-Wallis |
| Liên hệ 2 biến liên tục | continuous-continuous | Pearson / Spearman |
| Dự đoán DV liên tục từ nhiều biến | nhiều IV | Multiple regression |
| DV nhị phân | 0/1 outcome | Logistic regression |
| Cấu trúc biến tiềm ẩn | latent constructs | CFA / SEM |

### Nhưng đừng dừng ở đây

Bạn còn phải hỏi:

- Thiết kế của tôi có lặp đo hay phân tầng không?
- Dữ liệu có cluster theo lớp/trường/tổ chức không?
- Có covariates cần kiểm soát không?
- Có tương tác/moderation cần kiểm tra không?

Nếu chỉ nhìn vào loại biến mà bỏ qua thiết kế, mô hình chọn ra có thể chưa phù hợp.

### Prompt chọn test/mô hình

> 📋 **Prompt Template — Test Selection**
> ```
> Tôi có:
> - Research question: [question]
> - DV: [biến + loại dữ liệu]
> - IV(s): [biến + loại dữ liệu]
> - Design: [independent / paired / longitudinal / clustered]
> - Sample size: [N]
> - Distribution notes: [mô tả]
> 
> Hãy:
> 1. Gợi ý phép kiểm hoặc mô hình phù hợp nhất
> 2. Nêu assumptions chính
> 3. Gợi ý alternative nếu assumptions vi phạm
> 4. Chỉ ra biến nào nên coi là covariate/moderator nếu có
> 5. Giải thích lý do chọn bằng ngôn ngữ dễ hiểu
> ```

### Một nguyên tắc quan trọng

> Đừng dùng mô hình phức tạp chỉ vì AI hoặc phần mềm làm được. Chỉ dùng khi câu hỏi nghiên cứu thực sự cần và dữ liệu đủ sức gánh.

---

## 10.6 Assumption Checking Là Một Phần Của Phân Tích, Không Phải Phần Phụ

Đây là nơi rất nhiều luận văn và bài báo bị yếu đi.

### Tại sao phải kiểm tra giả định?

Vì một mô hình có thể cho ra con số rất đẹp nhưng lại dựa trên những điều kiện mà dữ liệu của bạn không đáp ứng.

### Những giả định thường gặp

- phân phối phần dư;
- tuyến tính;
- đồng nhất phương sai;
- độc lập quan sát;
- đa cộng tuyến thấp;
- không có outlier ảnh hưởng quá mạnh.

### Điều cần nhớ

Giả định cần kiểm tra phụ thuộc vào mô hình, không phải có một checklist y hệt cho mọi phân tích.

Ví dụ:

- Regression cần residual diagnostics, VIF, homoscedasticity.
- ANOVA cần homogeneity of variance.
- Pearson correlation cần xem quan hệ tuyến tính và outliers.
- SEM cần xem fit indices và specification logic.

### Prompt assumption checking

> 📋 **Prompt Template — Assumption Check**
> ```
> Tôi sắp chạy [t-test / ANOVA / regression / logistic regression / SEM].
> 
> Dữ liệu: [mô tả]
> Variables: [list]
> 
> Hãy giúp tôi:
> 1. Liệt kê các assumptions cần kiểm tra
> 2. Viết code để kiểm tra từng assumption
> 3. Gợi ý cách xử lý nếu assumption bị vi phạm
> 4. Chỉ ra assumption nào là nghiêm trọng nhất cho mô hình này
> ```

### Cách nghĩ đúng khi assumption vi phạm

Không phải cứ vi phạm là “bỏ hết làm lại”. Bạn cần đánh giá:

- mức độ vi phạm;
- độ nhạy của mô hình với vi phạm đó;
- có alternative hợp lý không;
- và cách báo cáo trung thực trong Results/Methods.

---

## 10.7 Regression, Effect Size và Ý Nghĩa Thực Chất

![Mô Hình Hồi Quy & Phân Tích Thống Kê](../assets/images/ch10_regression_model_1776094294927.png)

Nhiều người dừng ở chỗ “p < .05”. Đây là một điểm dừng quá sớm.

### Một kết quả tốt cần được nhìn ở ít nhất 4 lớp

1. **Statistical significance**
   Có đủ bằng chứng để bác bỏ giả thuyết không?

2. **Effect size**
   Mức độ tác động mạnh hay yếu?

3. **Precision**
   Khoảng tin cậy rộng hay hẹp?

4. **Practical significance**
   Kết quả có đáng kể trong bối cảnh thực tế không?

### Ví dụ

Một biến có thể có p < .001 nhưng effect size rất nhỏ. Trong mẫu lớn, điều này rất thường xảy ra. Nếu chỉ báo “có ý nghĩa thống kê” mà không nói mức độ tác động, người đọc rất dễ hiểu quá mức.

### Prompt cho hồi quy

> 📋 **Prompt Template — Regression Analysis**
> ```
> Chạy multiple regression:
> - DV: [biến]
> - IVs: [list]
> - Covariates: [nếu có]
> - Data: [path]
> 
> Yêu cầu:
> 1. Kiểm tra assumptions
> 2. Chạy mô hình
> 3. Report R2, adjusted R2, F, coefficients, CI
> 4. Tính/nhấn effect size nếu phù hợp
> 5. Viết 1 đoạn diễn giải không phóng đại kết quả
> 6. Chỉ ra 2 giới hạn của mô hình
> ```

### Ví dụ code regression

```python
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv("data/processed/survey_data.csv")

model = smf.ols(
    "teaching_effectiveness ~ experience_years + class_size + support_score",
    data=df
).fit()

print(model.summary())

X = model.model.exog
vif = pd.DataFrame({
    "variable": model.model.exog_names,
    "VIF": [variance_inflation_factor(X, i) for i in range(X.shape[1])]
})
print(vif)
```

### Một câu hỏi quan trọng

> Kết quả này có thay đổi cách tôi hiểu hiện tượng không, hay chỉ là một khác biệt thống kê nhỏ trong mẫu?

Đây là cách tự buộc mình nghĩ vượt qua p-value.

---

## 10.8 Diễn Giải Kết Quả Với AI: Hỗ Trợ Viết, Không Thay Quyết Định

AI đặc biệt hữu ích ở khâu:

- chuyển output kỹ thuật thành ngôn ngữ học thuật rõ hơn;
- đối chiếu finding với literature;
- phát hiện chỗ diễn giải quá tay;
- gợi ý cách trình bày theo APA hoặc chuẩn journal.

### Nhưng AI không được làm gì?

- quyết định thay bạn một kết quả “có nghĩa” gì về mặt khoa học;
- tuyên bố nhân quả khi thiết kế không cho phép;
- nói quá mức so với effect size;
- lấp chỗ chưa hiểu bằng văn xuôi nghe mượt.

### Prompt diễn giải có kiểm soát

> 📋 **Prompt Template — Controlled Interpretation**
> ```
> Tôi có kết quả phân tích sau:
> [paste results]
> 
> Hãy giúp tôi:
> 1. Diễn giải bằng ngôn ngữ học thuật rõ ràng
> 2. Phân biệt đâu là statistical significance, đâu là practical significance
> 3. Chỉ ra chỗ nào tôi có nguy cơ diễn giải quá mức
> 4. Gợi ý 1 đoạn Results và 1 đoạn Discussion tách biệt chức năng
> 5. Gợi ý 2-3 papers để đối chiếu, nhưng không coi đó là nguồn cuối cùng
> ```

> ⚠️ **Cảnh báo quan trọng:** Nếu bạn không thể tự giải thích kết quả cho một đồng nghiệp bằng lời của mình, chưa nên để AI viết paragraph thay bạn.

---

## 10.9 Visualization, Reporting và APA-Style Logic

Kết quả phân tích định lượng không kết thúc ở output console. Bạn còn phải chuyển nó thành:

- bảng rõ;
- figure đúng mục đích;
- đoạn văn đúng chức năng;
- và format phù hợp với chuẩn bài báo hoặc luận văn.

### Nguyên tắc đơn giản

- Table giữ số chính xác.
- Figure cho thấy mẫu hình.
- Paragraph nói điều người đọc cần chú ý.

### APA-style logic

Với reporting theo APA hoặc gần APA, bạn nên chú ý:

- viết đúng thống kê: `t(df) = value, p = ..., d = ...`
- tránh lạm dụng số lẻ không cần thiết;
- giữ nhất quán về chữ nghiêng, ký hiệu, đơn vị;
- chỉ báo những chỉ số thực sự có ý nghĩa cho lập luận.

### Prompt báo cáo kết quả

> 📋 **Prompt Template — APA Reporting**
> ```
> Tôi cần báo cáo kết quả phân tích theo APA/journal style:
> - Test/model: [type]
> - Output: [paste]
> - Table/Figure liên quan: [list]
> 
> Hãy:
> 1. Viết đoạn Results ngắn gọn
> 2. Tạo bảng report nếu cần
> 3. Gợi ý caption cho figure
> 4. Chỉ ra chỗ nào còn thừa số liệu không cần đưa vào main text
> ```

---

## 10.10 Những Sai Lầm Định Lượng Rất Hay Gặp

### 1. Chạy nhiều test rồi chỉ giữ cái có ý nghĩa

Đây là một dạng rất quen của p-hacking, dù đôi khi người làm không cố ý.

### 2. Xem mọi p < .05 là “quan trọng”

Ý nghĩa thống kê không đồng nghĩa với ý nghĩa thực tiễn.

### 3. Dùng câu chữ nhân quả cho thiết kế không hỗ trợ nhân quả

Từ “predict” sang “cause” là một bước nhảy rất lớn.

### 4. Bỏ qua effect size và confidence interval

Khi đó người đọc biết có khác biệt, nhưng không biết khác biệt đó đáng kể đến đâu.

### 5. Chỉ tin output mà không nhìn dữ liệu

Nhiều vấn đề lộ ra rõ trên histogram, scatter plot, residual plot hơn là trên bảng output.

### 6. Để AI hoặc phần mềm quyết định thay mình

Một mô hình “chạy được” không đồng nghĩa với một mô hình “nên dùng”.

### Checklist tự rà cuối chương

- Mỗi phân tích có gắn với RQ/H rõ không?
- Tôi đã kiểm tra assumptions chưa?
- Tôi có đang báo cả effect size/chỉ số mức độ không?
- Tôi có chỗ nào đang lỡ diễn giải nhân quả không?
- Nếu reviewer hỏi “vì sao chọn mô hình này”, tôi có trả lời được ngay không?

---

## 10.11 Workflow Gợi Ý Với Antigravity

Một workflow thực dụng:

1. Tạo analysis plan từ RQ và biến.
2. Audit dữ liệu và làm sạch bản processed.
3. Chạy descriptive statistics và exploratory plots.
4. Kiểm tra assumptions cho mô hình chính.
5. Chạy inferential tests hoặc regression/SEM.
6. Tạo figure và bảng reproducible.
7. Dùng AI để rà logic diễn giải và viết đoạn Results/Discussion tách biệt.
8. Xuất output theo chuẩn luận văn hoặc journal.

### Prompt tổng hợp

> 📋 **Prompt Template — End-to-End Quant Analysis**
> ```
> Tôi cần phân tích định lượng cho nghiên cứu:
> - Research questions / hypotheses: [list]
> - Dataset: [path + mô tả]
> - Variables: [list]
> - Audience: [thesis / journal / defense]
> 
> Hãy:
> 1. Tạo analysis plan
> 2. Viết code descriptive + assumption checks + main model
> 3. Gợi ý figures/tables chính
> 4. Chỉ ra 3 rủi ro diễn giải sai
> 5. Gợi ý cách báo cáo kết quả theo chuẩn học thuật
> ```

---

## 10.12 Bài Tập Thực Hành

### 🔧 Hands-on 10.1: RQ-to-Model Map

Tạo bảng:

| Research Question | Variables | Planned Analysis | Assumptions |

Điền cho toàn bộ các RQ/H trong nghiên cứu của bạn.

### 🔧 Hands-on 10.2: Assumption Audit

Chọn mô hình chính và kiểm tra đầy đủ assumptions. Ghi ra:

- assumption nào đạt;
- assumption nào vi phạm;
- bạn xử lý ra sao.

### 🔧 Hands-on 10.3: Results vs Discussion Drill

Viết hai đoạn cho cùng một finding:

- một đoạn Results chỉ báo cáo;
- một đoạn Discussion chỉ diễn giải.

Mục tiêu là tách rõ hai chức năng này.

### 🔧 Hands-on 10.4: Effect Size Reflection

Chọn một kết quả có p nhỏ và tự trả lời:

- effect size là bao nhiêu;
- nó có đáng kể trong thực tế không;
- nếu giải thích cho người ngoài ngành, bạn sẽ nói thế nào để không phóng đại?

---

## 10.13 Tóm Tắt Chương

Phân tích dữ liệu định lượng là quá trình đưa câu hỏi nghiên cứu đi qua các bước làm sạch, mô hình hóa, kiểm tra giả định, và diễn giải có trách nhiệm. Giá trị của nó không nằm ở việc bạn chạy được bao nhiêu test, mà ở chỗ mỗi test hay mô hình đều phục vụ đúng một câu hỏi, được kiểm tra đúng điều kiện, và được báo cáo trung thực về mức độ cũng như giới hạn của kết quả. AI giúp bạn nhanh hơn ở khâu code, báo cáo, và rà logic, nhưng phán đoán thống kê và phán đoán khoa học vẫn phải là việc của người nghiên cứu.

**Deliverable cuối chương:** đến đây, bạn nên có một `quant analysis kit` gồm:

- analysis plan gắn với từng RQ/H;
- bản processed data đã audit;
- assumption check log;
- mô hình/phép kiểm chính có code reproducible;
- bảng/figure chính;
- một bộ đoạn Results và Discussion tách chức năng rõ ràng.

Nếu đề tài của bạn hoàn toàn đi theo định lượng, bộ này gần như đã chuẩn bị xong phần lõi cho `Chương 12` và các chương viết sau đó. Nếu bạn đang làm mixed methods, đây là nửa bằng chứng định lượng cần được giữ đủ sạch và đủ rõ để có thể đặt cạnh nhánh định tính ở `Chương 11`, rồi tích hợp bằng trực quan hóa hoặc joint display.

---

> 📖 **Tiếp theo:** [Chương 11: Phân Tích Dữ Liệu Định Tính →](chuong-11-phan-tich-dinh-tinh.md)

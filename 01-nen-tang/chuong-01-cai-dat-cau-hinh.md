# Chương 1: Cài Đặt và Cấu Hình Antigravity

![Ai Tools Setup](../assets/images/ch01_ai_tools_setup_1776092170769.png)

---

> *"Một thợ mộc giỏi dành thời gian mài dũa công cụ trước khi bắt đầu xây nhà."*

---

Nhiều người muốn bỏ qua chương cài đặt vì nghĩ rằng nó chỉ là một danh sách lệnh kỹ thuật. Nhưng trong nghiên cứu, phần "setup" không chỉ là làm sao để mở được công cụ. Nó là bước dựng hạ tầng để toàn bộ quá trình sau này có thể:

- làm việc ổn định
- lưu vết được
- kiểm chứng được
- bảo vệ được dữ liệu
- và không sụp đổ chỉ vì một connector hỏng hay một file bị đặt sai chỗ

Nếu chương 0 nói về vai trò của AI trong nghiên cứu, thì chương 1 là lúc biến ý tưởng đó thành một môi trường làm việc có thật. Mục tiêu ở đây không phải là thuộc lòng từng lệnh cài đặt, vì cách cài có thể thay đổi theo phiên bản, hệ điều hành, hay gói triển khai của trường/viện/lab. Mục tiêu là hiểu **logic của một workspace nghiên cứu tốt**:

- Antigravity là gì trong quy trình của cuốn sách này
- bạn cần chuẩn bị gì trước khi bắt đầu
- workspace nên được tổ chức ra sao
- các connector nên được cấu hình theo nguyên tắc nào
- keys và dữ liệu nhạy cảm cần được quản lý thế nào
- và làm sao biết hệ thống của bạn thật sự sẵn sàng cho nghiên cứu

Nói ngắn gọn: chương này không chỉ dạy bạn "cài xong", mà dạy bạn **dựng một môi trường nghiên cứu có thể sống được suốt cả dự án**.

## 1.1 Antigravity Trong Cuốn Sách Này Là Gì?

Trong ngữ cảnh của ebook này, hãy hiểu **Antigravity** như một AI workspace cho nghiên cứu, nơi bạn có thể làm việc với:

- cuộc hội thoại dài có ngữ cảnh
- file và thư mục của dự án
- các công cụ phân tích hoặc viết mã
- các connector tới nguồn học thuật, web, OCR, hay notebook tri thức
- quy trình lặp giữa hỏi, đọc, kiểm tra, sửa và lưu vết

Điều quan trọng là không xem Antigravity như một chatbot "đi hỏi câu nào trả lời câu đó". Trong workflow của cuốn sách này, nó đóng vai trò gần hơn với một **bàn làm việc nghiên cứu tích hợp**:

- bạn tìm tài liệu từ đây
- bạn tổ chức file từ đây
- bạn để nó giúp viết code hoặc rà soát logic từ đây
- bạn lưu lại dấu vết của các phiên làm việc từ đây

Chính vì vậy, chương này sẽ không bám chặt vào một nhà cung cấp, một kênh cài đặt hay một màn hình giao diện cố định. Những thứ đó có thể thay đổi. Thứ cần giữ ổn định là các nguyên tắc cấu hình:

- một launcher để vào workspace
- một nơi lưu file nghiên cứu
- một tập connector phục vụ đúng nhu cầu
- một cơ chế quản lý secrets
- và một quy trình kiểm tra đầu tiên trước khi bắt đầu dự án thật

## 1.2 Cài Đặt Không Phải Việc Của IT, Mà Là Việc Của Phương Pháp

Nhiều sự cố về sau tưởng như là "lỗi kỹ thuật", nhưng thật ra phá trực tiếp chất lượng nghiên cứu. Ví dụ:

- lưu transcript phỏng vấn lẫn với bản đã ẩn danh
- dùng connector học thuật nhưng không biết nó đang trả về nguồn nào
- để API key trong notebook hoặc bản thảo
- viết đè lên dữ liệu thô vì không tách `raw` và `processed`
- không lưu research log nên không truy lại được một kết luận xuất hiện từ đâu

Những chuyện này không chỉ gây phiền. Chúng ảnh hưởng tới:

- reproducibility
- transparency
- ethics
- khả năng làm việc với GVHD hoặc đồng tác giả
- khả năng bảo vệ luận văn hoặc phản hồi reviewer

Vì vậy, hãy xem phần setup như phần đầu của phương pháp luận. Một workspace tốt giúp bạn giảm lỗi cơ học để dành năng lượng cho tư duy học thuật. Một workspace tệ khiến bạn liên tục vá víu và đến cuối cùng không biết phiên bản nào mới là phiên bản đáng tin.

## 1.3 Ba Quyết Định Cần Chốt Trước Khi Cài

Trước khi đi vào lệnh hay file cấu hình, hãy chốt ba quyết định sau.

### 1. Bạn sẽ làm việc chủ yếu ở đâu?

Thông thường có ba mô hình:

- **Cá nhân local-first:** bạn làm việc trên máy cá nhân, dữ liệu và file chủ yếu nằm local.
- **Lab hoặc tổ chức quản lý:** bạn dùng môi trường đã được trường/viện/lab thiết lập sẵn, có thể kèm policy riêng.
- **Hybrid:** bạn làm local nhưng một số connector hoặc tài nguyên tính toán do bên ngoài cung cấp.

Mỗi mô hình kéo theo khác biệt về:

- quyền cài đặt phần mềm
- nơi lưu dữ liệu
- cách xác thực tài khoản
- giới hạn về bảo mật

### 2. Dữ liệu của bạn thuộc loại nào?

Ngay từ đầu, hãy tự hỏi dự án của bạn chủ yếu làm việc với:

- tài liệu công khai
- bài báo và dữ liệu thứ cấp
- dữ liệu nội bộ nhưng không nhạy cảm
- dữ liệu nhận diện cá nhân hoặc dữ liệu nhạy cảm

Nếu dữ liệu có yếu tố nhạy cảm, chương cài đặt không còn là câu chuyện "mở tool lên là xong". Bạn phải nghĩ đến:

- môi trường local hay private
- phân quyền file
- nơi nào tuyệt đối không upload dữ liệu
- ai được quyền truy cập workspace

### 3. Bộ connector cốt lõi của bạn là gì?

Không phải ai cũng cần cùng một cấu hình. Nhưng với phần còn lại của cuốn sách này, bộ tối thiểu thường gồm:

- một connector tìm kiếm học thuật
- một connector tìm web và reasoning
- một công cụ tổ chức tri thức
- một công cụ xử lý PDF/OCR khi cần
- một công cụ suy nghĩ theo chuỗi hoặc phản biện logic
- khả năng đọc/ghi file và chạy code ở mức cơ bản

Chốt ba quyết định này trước sẽ giúp bạn không cài theo kiểu "thấy gì hay thì thêm", rồi cuối cùng có một hệ thống nặng, rối và khó kiểm soát.

## 1.4 Chuẩn Bị Hệ Thống: Những Gì Cần Có Trước Khi Bấm Cài

Thay vì bắt đầu bằng lệnh cài, hãy kiểm tra môi trường trước. Một hệ thống nghiên cứu tối thiểu nên có:

| Thành phần | Mức tối thiểu | Khuyến nghị |
|-----------|---------------|-------------|
| **Hệ điều hành** | Máy cá nhân ổn định, cập nhật định kỳ | Một môi trường bạn quen thao tác file và terminal |
| **Dung lượng lưu trữ** | Đủ cho PDF, notes, dữ liệu và output | Có vùng riêng cho workspace nghiên cứu |
| **Terminal hoặc shell** | Có thể chạy lệnh cơ bản | Biết thao tác `cd`, `ls`, `mkdir`, kiểm tra file |
| **Trình soạn thảo** | Một editor bất kỳ | Editor hỗ trợ Markdown, code, search toàn thư mục |
| **Internet** | Ổn định cho xác thực và connector | Tách được lúc nào cần online, lúc nào làm local |
| **Ngôn ngữ phân tích** | Không bắt buộc ngay | Có Python hoặc R nếu dự án cần xử lý dữ liệu |
| **Trình duyệt** | Có thể đăng nhập và kiểm tra nguồn | Có bookmark cho các nguồn học thuật quan trọng |

Điều bạn cần nhất không phải cấu hình mạnh nhất, mà là một môi trường **ổn định và dự đoán được**. Một chiếc máy rất mạnh nhưng thư mục bừa bộn, secrets để lung tung và connector bật tắt thất thường vẫn là một môi trường nghiên cứu tệ.

## 1.5 Cài Đặt Theo Logic Đúng, Không Theo Thói Quen Chép Lệnh

Các bản phân phối của Antigravity có thể khác nhau theo:

- bản desktop hay bản terminal
- gói cá nhân hay môi trường do tổ chức quản lý
- cách phát hành của từng thời điểm

Vì vậy, thay vì đóng cứng một chuỗi lệnh có thể nhanh lỗi thời, hãy bám quy trình cài đặt sau:

### Bước 1: Cài launcher chính thức cho môi trường của bạn

Hãy dùng installer hoặc package channel chính thức của phiên bản bạn đang sử dụng. Mục tiêu của bước này là tạo ra một lối vào ổn định cho workspace.

Sau khi cài, tối thiểu bạn cần kiểm tra:

```bash
antigravity --version
antigravity
```

Nếu bản triển khai của bạn dùng tên launcher khác hoặc có alias ngắn hơn, hãy theo đúng tài liệu đi kèm của môi trường đó. Điều quan trọng không phải là thuộc một alias cụ thể, mà là xác nhận:

- launcher mở được
- workspace khởi động bình thường
- bạn có thể vào một session làm việc mới

### Bước 2: Xác thực tài khoản theo cách môi trường của bạn yêu cầu

Tùy cấu hình, việc xác thực có thể đi qua:

- đăng nhập qua trình duyệt
- token do tổ chức cấp
- hoặc cơ chế SSO nội bộ

Sau khi xác thực, hãy kiểm tra ba điều:

- bạn vào được workspace mà không bị trả về màn hình login
- các connector cần dùng không báo "unauthorized"
- phiên làm việc có thể đọc thư mục dự án của bạn

### Bước 3: Tách workspace nghiên cứu khỏi các thư mục linh tinh khác

Đừng bắt đầu trong `Downloads`, `Desktop`, hay một thư mục cá nhân lẫn đủ loại tài liệu không liên quan. Hãy tạo một thư mục gốc riêng cho dự án hoặc cho toàn bộ nghiên cứu.

Ví dụ:

```text
research-workspace/
```

Ngay từ đầu, việc này sẽ giúp bạn:

- tránh nhầm file
- dễ backup
- dễ chia sẻ với GVHD hoặc cộng tác viên
- dễ thiết lập quyền truy cập

## 1.6 Tổ Chức Workspace: Cấu Trúc Thư Mục Là Một Quyết Định Học Thuật

Một cấu trúc thư mục tốt không chỉ để "đẹp". Nó phản ánh cách bạn hiểu chuỗi công việc nghiên cứu. Dưới đây là một cấu trúc thực dụng, đủ linh hoạt cho hầu hết đề tài:

```text
my-research-project/
│
├── 01-literature/
│   ├── papers/
│   ├── notes/
│   ├── literature-matrix.md
│   └── synthesis.md
│
├── 02-design/
│   ├── problem-statement.md
│   ├── framework.md
│   ├── instruments/
│   └── ethics/
│
├── 03-data/
│   ├── raw/
│   ├── anonymized/
│   ├── processed/
│   ├── analysis/
│   └── codebook.md
│
├── 04-results/
│   ├── figures/
│   ├── tables/
│   └── memos/
│
├── 05-writing/
│   ├── drafts/
│   ├── manuscript.md
│   └── references.bib
│
├── 06-outputs/
│   ├── slides/
│   ├── briefs/
│   └── media/
│
├── research-log.md
├── ai-use-log.md
├── data-policy.md
└── README.md
```

### Tại sao cấu trúc này hữu ích?

- `literature/` tách việc đọc và tổng hợp khỏi phần viết chính.
- `design/` giữ problem statement, framework và instruments ở cùng một nơi.
- `data/raw/` không bao giờ bị chỉnh sửa trực tiếp.
- `data/anonymized/` giúp bạn tách dữ liệu dùng cho AI hoặc chia sẻ nội bộ khỏi dữ liệu nhận diện.
- `results/` là nơi lưu output đã đủ sạch để đi vào bản thảo.
- `research-log.md` và `ai-use-log.md` là xương sống của tính minh bạch.

### Điều tối thiểu phải tách riêng

Nếu bạn không muốn áp dụng toàn bộ cấu trúc trên, ít nhất hãy tách rõ:

- dữ liệu thô
- dữ liệu đã xử lý
- bản thảo viết
- notes đọc tài liệu
- output do AI hỗ trợ tạo ra

Không tách những phần này ngay từ đầu là công thức chắc chắn cho nhầm lẫn sau này.

## 1.7 File Nền Tảng Của Một Dự Án Nghiên Cứu

Ngoài thư mục, có bốn file rất đáng tạo ngay từ ngày đầu.

### 1. `README.md`

File này không cần cầu kỳ. Nó chỉ cần ghi:

- dự án nghiên cứu về gì
- ai đang tham gia
- cấu trúc thư mục chính
- dữ liệu nằm ở đâu
- bản thảo chính nằm ở đâu

README tốt giúp bạn quay lại dự án sau 2 tháng mà không mất 30 phút để nhớ xem mọi thứ nằm đâu.

### 2. `research-log.md`

Đây là nơi ghi lại tiến trình nghiên cứu theo phiên làm việc. Một entry đơn giản có thể như sau:

```markdown
# Research Log

## 2026-04-13

- Hoạt động: rà 12 bài báo về STEM implementation tại Đông Nam Á
- Công cụ đã dùng: academic search, reasoning, Notebook
- Kết quả chính: tách được 4 nhóm rào cản lặp lại
- Việc cần làm tiếp: kiểm tra literature tại Việt Nam
```

### 3. `ai-use-log.md`

File này nên ghi ở mức đủ để truy lại:

- công cụ nào đã dùng
- dùng cho việc gì
- loại đầu vào là gì
- mức kiểm chứng ra sao
- có cần disclosure hay không

Ví dụ:

```markdown
## 2026-04-13

- Tool: reasoning assistant
- Task: so sánh 3 framework cho RQ về STEM education
- Input: literature notes đã tổng hợp, không chứa dữ liệu nhạy cảm
- Human check: đối chiếu lại với 5 bài lý thuyết gốc
- Output used in: framework.md
```

### 4. `data-policy.md`

Đây là file rất nhiều người không tạo, nhưng nên có ngay khi dự án chạm vào dữ liệu thực. File này có thể ghi rất ngắn:

- dữ liệu nào là nhạy cảm
- thư mục nào không được upload ra ngoài
- thư mục nào đã ẩn danh
- connector nào được phép dùng với loại dữ liệu nào

## 1.8 Phân Vai Đội Ngũ AI: Lựa Chọn Giữa Gemini 3.1 Pro và Claude Opus

Trang bị công cụ tốt không bằng dùng đúng công cụ cho đúng việc. Trong hệ sinh thái Antigravity, bạn có thiết lập mặc định với hai mô hình tư duy (models) hàng đầu hiện nay, mỗi bên có một triết lý thiết kế và điểm mạnh riêng. Việc phân vai chúng đúng cách sẽ quyết định độ sâu và tốc độ nghiên cứu của bạn.

### Gemini 3.1 Pro: "Người Tổng Hợp" Nhanh Nhẹn Và Chịu Tải Cao
Được thiết kế với window context khổng lồ (thích dung nạp hàng triệu tokens) và tốc độ suy luận nhanh.
- **Điểm mạnh cốt lõi:** Khả năng đọc đồng thời hàng chục bài báo (PDF) mà không mất bối cảnh, cross-check dữ liệu thần tốc, và trích xuất thông tin diện rộng.
- **Khâu khuyên dùng:** 
  - Literature Review giai đoạn mở rộng (đọc lướt hàng nghìn trang).
  - Thực thi Code/Data pipeline, gọi công cụ qua MCP chuẩn xác.
  - Trích xuất dữ liệu, tổng hợp thông tin, chuyển đổi format.

### Claude Opus: "Nhà Lý Luận" Cẩn Trọng Và Sâu Sắc
Được thiết kế với văn phong tự nhiên, sự cẩn trọng cao độ và khả năng suy luận logic nhiều lớp (chain-of-thought) vững chắc.
- **Điểm mạnh cốt lõi:** Viết lách học thuật sắc bén, khả năng phát hiện điểm mù mâu thuẫn trong logic, và xử lý các concept lý thuyết phức tạp.
- **Khâu khuyên dùng:**
  - Chốt Research Gap và thiết kế Framework (Research Design).
  - Biên tập, làm mịn và nâng cấp bản thảo (Drafting & Refining).
  - Thảo luận sâu, phản biện giả thuyết (Bias Check).

**Tóm lại:** Hãy để **Gemini 3.1 Pro** "cày" khối lượng tài liệu khổng lồ để lấy ra quặng thô, rồi đưa quặng đó cho **Claude Opus** tinh chế và lập luận thành tác phẩm học thuật hoàn chỉnh.

## 1.9 Cấu Hình Connector - Sức Mạnh Thực Sự Của MCP (Model Context Protocol)

Phần mạnh nhất của Antigravity là khả năng kết nối nhiều hệ thống bên ngoài qua chuẩn MCP (Model Context Protocol). MCP giống như đóng vai "tay" và "mắt" giúp LLM thoát khỏi hộp chat đóng kín. Thay vì bạn phải tự mở trình duyệt, LLM có thể trực tiếp query web, đọc folder của hệ thống, gọi Perplexity hay Consensus. Nhưng cấu hình connector nên đi theo nguyên tắc **ít nhưng đúng**, không phải càng nhiều càng tốt.

### Bộ connector cốt lõi cho cuốn sách này

| Nhóm nhu cầu | Connector gợi ý | Dùng cho |
|-------------|------------------|----------|
| **Tìm học thuật** | Academic search | systematic review, xác minh paper, tìm review |
| **Web + reasoning** | Search/reasoning connector | bối cảnh, grey literature, stress-test logic |
| **Tri thức cá nhân** | Notebook / knowledge connector | tổng hợp nhiều nguồn, so theme, notes |
| **Tài liệu khó đọc** | PDF/OCR connector | số hóa PDF scan, tài liệu tiếng Việt, tài liệu in |
| **Suy nghĩ theo chuỗi** | Sequential thinking / analysis | problem decomposition, theory fit, phản biện |
| **Code và file** | Built-in execution + filesystem | xử lý dữ liệu, tạo file, lưu output |

### Nguyên tắc chọn connector

- Chỉ thêm connector phục vụ một nhu cầu rõ.
- Biết connector lấy dữ liệu từ đâu.
- Biết connector có gửi dữ liệu ra ngoài hay không.
- Biết loại đầu vào nào tuyệt đối không được dùng với connector đó.
- Nếu không hiểu rõ, đừng dùng nó với dữ liệu thật.

### Template cấu hình theo logic

Tùy môi trường của bạn, file cấu hình connector có thể khác nhau. Nhưng về logic, nó thường có dạng:

```json
{
  "mcpServers": {
    "consensus": {
      "command": "<launcher>",
      "args": ["<consensus-mcp-entrypoint>"],
      "env": {
        "CONSENSUS_API_KEY": "${CONSENSUS_API_KEY}"
      }
    },
    "perplexity": {
      "command": "<launcher>",
      "args": ["<perplexity-mcp-entrypoint>"],
      "env": {
        "PERPLEXITY_API_KEY": "${PERPLEXITY_API_KEY}"
      }
    },
    "notebook": {
      "command": "<launcher>",
      "args": ["<notebook-entrypoint>"]
    },
    "pdf_ocr": {
      "command": "<launcher>",
      "args": ["<ocr-entrypoint>"]
    },
    "sequential_thinking": {
      "command": "<launcher>",
      "args": ["<analysis-entrypoint>"]
    }
  }
}
```

Template này không nhằm để copy-paste nguyên xi. Nó nhằm giúp bạn hiểu ba thành phần phải có:

- **server name** để bạn biết đang gọi công cụ nào
- **entrypoint** để launcher biết khởi động connector nào
- **env vars** để giữ secret tách khỏi file nội dung nghiên cứu

### Điều cần nhớ về secrets

Không hard-code API key trực tiếp vào notes, prompt, manuscript, notebook hay bản chụp màn hình. Dùng:

- biến môi trường
- file secrets tách riêng khỏi workspace chia sẻ
- password manager hoặc secret store của tổ chức

## 1.10 Quản Lý Secrets Và Bảo Mật Ngay Từ Ngày Đầu

Đây là phần rất thực tế nhưng thường bị xem nhẹ.

### Không để keys trong:

- `README.md`
- screenshot
- prompt đang chuẩn bị gửi cho đồng nghiệp
- notebook sẽ nộp kèm luận văn
- file code sẽ chia sẻ công khai

### Tách dữ liệu theo mức nhạy cảm

Một nguyên tắc dễ nhớ là:

- **Công khai:** có thể dùng với hầu hết connector nếu cần
- **Nội bộ nhưng không nhạy cảm:** dùng thận trọng, biết rõ nơi gửi đi đâu
- **Nhạy cảm hoặc nhận diện cá nhân:** chỉ dùng trong môi trường đã được phép, hoặc không dùng AI nếu chưa chắc

### Quy tắc đỏ

Nếu bạn không thể trả lời rõ ba câu sau, đừng đưa dữ liệu vào connector:

- dữ liệu đang đi đâu
- ai có thể truy cập
- tôi có quyền làm vậy không

## 1.11 Phiên Khởi Động Đầu Tiên: Kiểm Tra Hệ Thống Theo Workflow Nghiên Cứu

Nhiều người kiểm tra hệ thống bằng cách xem tool có mở được không. Cách đó chưa đủ. Bạn nên kiểm tra theo đúng chuỗi công việc nghiên cứu mà mình sẽ dùng thật.

### Kiểm tra 1: Workspace có đọc/ghi file đúng chỗ không?

Tối thiểu hãy xác nhận:

- mở được thư mục dự án
- tạo được một file test
- đọc lại được file đó
- xóa hoặc đánh dấu rõ file test sau khi kiểm tra xong

### Kiểm tra 2: Research log có được tạo và cập nhật không?

Hãy thử tạo `research-log.md` và ghi một entry đầu tiên. Nếu ngay bước đầu bạn chưa giữ được log, rất dễ là cả dự án sẽ bỏ quên phần này.

### Kiểm tra 3: Connector học thuật có trả về nguồn đáng dùng không?

Thử một truy vấn đơn giản gắn với đề tài của bạn:

- tìm một systematic review
- tìm 3-5 bài báo gần đây
- kiểm tra xem kết quả có tên bài, tác giả, năm và nguồn rõ ràng không

### Kiểm tra 4: Connector reasoning có giúp được một câu hỏi thật không?

Ví dụ:

- "Hãy chỉ ra 3 research gaps có thể khai thác trong chủ đề X"
- "Hãy so sánh hai framework A và B"

Nếu output quá chung chung, đó là dấu hiệu bạn cần chỉnh prompt hoặc cân nhắc lại connector, chứ không nên vội tin.

### Kiểm tra 5: Code hoặc execution có chạy được tác vụ tối thiểu không?

Nếu dự án có phân tích dữ liệu, hãy thử một tác vụ nhỏ:

- chạy một script kiểm tra môi trường
- đọc một CSV mẫu
- tạo một bảng thống kê đơn giản

Bạn không cần chờ đến chương 10 mới biết execution đang lỗi.

### Kiểm tra 6: OCR hoặc xử lý PDF có hoạt động với tài liệu thật không?

Đừng chỉ test bằng PDF đẹp. Hãy thử một tài liệu gần với loại bạn sẽ dùng thật:

- bài scan tiếng Việt
- luận văn cũ
- báo cáo có bảng biểu

Mục tiêu là biết giới hạn của hệ thống sớm, không phải khi deadline đã tới.

## 1.12 Các Lỗi Setup Phổ Biến Và Cách Nghĩ Đúng Để Sửa

### Lỗi 1: Cài được rồi nhưng không biết dữ liệu đang nằm đâu

Đây thường không phải lỗi công cụ, mà là lỗi tổ chức. Hãy quay về:

- thư mục gốc rõ ràng
- raw và processed tách riêng
- README và data policy có mặt

### Lỗi 2: Connector hoạt động chập chờn

Nguyên nhân có thể là:

- auth hết hạn
- API key sai
- package connector đổi phiên bản
- đường dẫn hoặc launcher không còn đúng

Đừng sửa theo kiểu thử mò vô hạn. Hãy kiểm tra theo thứ tự:

- launcher có mở được không
- auth còn hiệu lực không
- env vars đã được nạp chưa
- connector cụ thể đang hỏng ở khâu nào

### Lỗi 3: AI truy cập được file nhưng không đúng file cần dùng

Thường do workspace bừa bộn hoặc đặt tên file không rõ. Một quy tắc đơn giản:

- tên file nên mô tả nội dung
- không để 7 file kiểu `draft-final-new-v2.md`
- dùng thư mục để quản lý version, không trông chờ trí nhớ

### Lỗi 4: Setup xong nhưng vẫn không dám dùng

Đây là lỗi tâm lý rất thường gặp. Người dùng mới thấy hệ thống quá nhiều thành phần nên sợ làm sai. Cách đúng không phải là học hết mọi connector rồi mới bắt đầu. Cách đúng là:

- chốt một đề tài nhỏ
- chạy một vòng workflow rất ngắn
- log lại điều gì hoạt động, điều gì chưa

Bạn không cần "thành thạo Antigravity" trước khi làm nghiên cứu. Bạn cần một môi trường đủ ổn để bắt đầu học bằng chính dự án của mình.

## 1.13 Thiết Lập Một Workspace Mẫu Trong 30-45 Phút

Nếu muốn làm thật thực dụng, bạn có thể đi theo trình tự sau:

### 10 phút đầu

- tạo thư mục gốc của dự án
- tạo các thư mục con chính
- tạo `README.md`, `research-log.md`, `ai-use-log.md`, `data-policy.md`

### 10 phút tiếp theo

- mở Antigravity trong thư mục dự án
- xác thực tài khoản nếu cần
- cấu hình hoặc bật các connector cốt lõi

### 10 phút tiếp theo

- test academic search với một query thật
- test reasoning với một câu hỏi thật
- test ghi log bằng một entry ngắn

### 10-15 phút cuối

- tạo một note đầu tiên về đề tài
- lưu một paper hoặc URL mẫu vào thư mục `literature/`
- viết ngắn 3 dòng: đề tài là gì, mục tiêu trước mắt là gì, bước tiếp theo là gì

Sau 30-45 phút, bạn chưa cần một hệ thống hoàn hảo. Bạn chỉ cần một workspace **có thể bắt đầu nghiên cứu được ngay ngày hôm nay**.

## 1.14 Đạo Đức Và Giới Hạn Ngay Từ Chương Cài Đặt

Việc dùng AI có trách nhiệm không bắt đầu ở chương đạo đức; nó bắt đầu ngay từ lúc bạn setup môi trường.

Ở chương này, hãy giữ bốn nguyên tắc:

- Không đưa dữ liệu nhạy cảm vào môi trường mình chưa hiểu rõ.
- Không để secrets lẫn vào file nghiên cứu.
- Không tin rằng "cài xong" nghĩa là "đã an toàn".
- Không cấu hình connector chỉ vì thấy hay; mỗi connector phải có mục đích rõ.

Nếu bạn làm đúng từ chương 1, các chương sau sẽ nhẹ đi rất nhiều. Nếu bạn làm ẩu ở chương 1, càng về sau bạn càng phải trả giá bằng sửa lỗi, mất log, lẫn phiên bản và rủi ro bảo mật.

## 1.15 Bài Tập Thực Hành

### Hands-on 1.1: Dựng workspace đầu tiên

Tạo một thư mục dự án cho đề tài bạn đang quan tâm và bên trong có tối thiểu:

- `01-literature/`
- `02-design/`
- `03-data/`
- `05-writing/`
- `README.md`
- `research-log.md`
- `ai-use-log.md`

Viết 3-5 dòng vào `README.md` mô tả mục tiêu nghiên cứu.

### Hands-on 1.2: Tạo phiên log đầu tiên

Mở `research-log.md` và ghi một entry đầu tiên:

- hôm nay bạn đã chuẩn bị gì
- đề tài của bạn là gì
- bạn muốn dùng AI giúp ở khâu nào
- điều gì bạn sẽ không giao cho AI

### Hands-on 1.3: Kiểm tra connector cốt lõi

Thử ba việc:

- tìm 3 bài báo về chủ đề của bạn
- hỏi một câu tổng quan hoặc so sánh framework
- lưu kết quả vào note hoặc log

Mục tiêu không phải là tìm ra phát hiện lớn, mà là xác nhận workflow cơ bản hoạt động.

### Hands-on 1.4: Viết data policy một trang

Viết ngắn:

- dữ liệu nào trong dự án của bạn là nhạy cảm
- dữ liệu nào có thể dùng với connector công khai
- thư mục nào tuyệt đối không được đưa ra ngoài
- ai có quyền truy cập workspace

## Deliverable Cuối Chương

Sau khi hoàn thành chương này, bạn nên có:

- một `research workspace` có cấu trúc rõ
- một bộ connector cốt lõi phù hợp với nhu cầu nghiên cứu
- một `research-log.md` và `ai-use-log.md` đã có entry đầu tiên
- một `data-policy.md` hoặc ít nhất là bộ quy tắc dữ liệu cá nhân
- một hệ thống đã được kiểm tra theo đúng workflow nghiên cứu cơ bản

Nếu đến cuối chương này bạn chỉ mới "mở được tool", thì vẫn chưa đủ. Nếu đến cuối chương bạn đã có một workspace mà ngày mai có thể bắt đầu literature review, ghi log và giữ dữ liệu có trật tự, thì lúc đó phần cài đặt mới thật sự hoàn thành nhiệm vụ. Nói cách khác, output của chương này là **nơi làm việc và bộ log nền**, để `Chương 2` dạy bạn cách sử dụng chúng với đúng kỷ luật nghiên cứu.

---

> 📖 **Tiếp theo:** [Chương 2: Tư Duy Nghiên Cứu Với AI — Nguyên Tắc Vàng →](chuong-02-tu-duy-nghien-cuu-voi-ai.md)

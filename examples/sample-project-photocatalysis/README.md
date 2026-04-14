# 🧪 Sample Project: Photocatalysis Degradation Efficiency

Đây là một **dự án nghiên cứu mẫu hoàn chỉnh** minh họa quy trình phân tích
dữ liệu định lượng từ đầu đến cuối, sử dụng AI hỗ trợ.

## Bối Cảnh Nghiên Cứu

Nghiên cứu ảnh hưởng của các tham số (loại chất xúc tác, nguồn sáng, liều lượng,
pH, thời gian) đến hiệu suất phân hủy quang xúc tác các chất ô nhiễm hữu cơ.

## Cấu Trúc Thư Mục

```
sample-project-photocatalysis/
├── data/
│   ├── raw/                         ← Dataset thô (150 thí nghiệm)
│   │   └── photocatalysis_experiments.csv
│   └── processed/                   ← Dataset đã làm sạch (146 quan sát)
│       └── photocatalysis_cleaned.csv
├── scripts/
│   ├── 00_generate_data.py          ← Bước 1: Sinh dữ liệu giả lập
│   ├── 01_clean_data.py             ← Bước 2: Làm sạch (missing, outlier)
│   └── 02_eda_and_stats.py          ← Bước 3: EDA + ANOVA + T-test + Regression
├── results/
│   ├── figures/                     ← 4 biểu đồ phân tích
│   │   ├── efficiency_distribution.png
│   │   ├── catalyst_vs_light.png
│   │   ├── dosage_impact.png
│   │   └── correlation_matrix.png
│   ├── tables/
│   │   └── stats_summary.txt        ← Bảng thống kê tổng hợp
│   └── analysis_report.md           ← Báo cáo kết quả tự động
└── requirements.txt                 ← Dependencies Python
```

## Cách Chạy

```bash
# 1. Cài đặt dependencies
pip install -r requirements.txt

# 2. Chạy pipeline theo thứ tự
python scripts/00_generate_data.py
python scripts/01_clean_data.py
python scripts/02_eda_and_stats.py
```

## Kết Quả Chính

- **ANOVA:** Có sự khác biệt có ý nghĩa thống kê giữa 3 loại chất xúc tác (p = 0.029)
- **Regression:** R² = 0.699 — mô hình giải thích 70% phương sai
- **TiO2/GO** là chất xúc tác hiệu quả nhất (+4.47% hiệu suất)
- **Thời gian tiếp xúc** là yếu tố dự báo mạnh nhất

## Liên Kết Với Ebook

| Script | Chương liên quan |
|---|---|
| `00_generate_data.py` | Chương 9: Thu thập dữ liệu |
| `01_clean_data.py` | Chương 9: Tiền xử lý |
| `02_eda_and_stats.py` | Chương 10: Phân tích định lượng + Chương 12: Visualization |
| `analysis_report.md` | Chương 13: Viết bài báo (phần Results) |

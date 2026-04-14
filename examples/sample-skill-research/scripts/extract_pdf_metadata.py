import sys
import os

def extract_metadata(pdf_path):
    """
    Script mẫu giả lập việc trích xuất metadata từ PDF.
    Trên thực tế, script này sẽ dùng PyMuPDF hoặc pdftotext
    để trích xuất Text, sau đó trả về cho AI Agent.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' không tồn tại.", file=sys.stderr)
        sys.exit(1)
        
    filename = os.path.basename(pdf_path)
    
    # OUTPUT trả về cho AI Agent đọc qua standard output
    print(f"--- METADATA TRÍCH XUẤT TỪ: {filename} ---")
    print("Title: [Mô phỏng tiêu đề bài báo từ PDF]")
    print("Authors: [Mô phỏng tác giả]")
    print("Abstract:")
    print("Bài báo này nghiên cứu ảnh hưởng của AI trong quá trình tổng quan tài liệu...")
    print("------------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python extract_pdf_metadata.py <đường_dẫn_file_pdf>")
        sys.exit(1)
        
    extract_metadata(sys.argv[1])

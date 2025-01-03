import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Application Config
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', 10))
SESSION_EXPIRY_MINUTES = int(os.getenv('SESSION_EXPIRY_MINUTES', 30))

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DOCUMENTS_DIR = os.path.join(DATA_DIR, 'documents')
VECTORSTORE_DIR = os.path.join(DATA_DIR, 'vectorstore')
METADATA_FILE = os.path.join(DATA_DIR, 'metadata.json')

# Khởi tạo cấu trúc thư mục và file
def init_storage():
    # Tạo các thư mục
    for directory in [DATA_DIR, DOCUMENTS_DIR, VECTORSTORE_DIR]:
        os.makedirs(directory, exist_ok=True)
    
    # Tạo file metadata.json nếu chưa tồn tại
    if not os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

# Gọi hàm khởi tạo
init_storage()

COHERE_MODEL = "command-xlarge-nightly"
SCHOOL_CONTACT_INFO = "Trường Cao đẳng Kinh tế Đối ngoại: ĐT (028)38446320, email: tuyensinh@cofer.edu.vn, Website: www.cofer.edu.vn"

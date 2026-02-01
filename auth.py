from passlib.context import CryptContext

# 암호화 설정 (bcrypt 알고리즘 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """비밀번호를 해싱하여 반환 (DB 저장용)"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """입력받은 비밀번호와 DB의 해시값을 비교"""
    return pwd_context.verify(plain_password, hashed_password)

# --- 테스트 예시 ---
raw_password = "my_secret_password_3182"
hashed = get_password_hash(raw_password)

print(f"원본: {raw_password}")
print(f"해싱된 결과: {hashed}") # $2b$12$... 처럼 복잡한 문자열로 변함
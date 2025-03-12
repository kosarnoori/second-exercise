import re

def validate_password(password):
    if len(password) < 8:
        return "رمز عبور ضعیف است: باید حداقل ۸ کاراکتر داشته باشد"
    
    if not any(char.isdigit() for char in password):
        return "رمز عبور ضعیف است: باید شامل حداقل یک عدد باشد"
    
    if not any(char.isupper() for char in password):
        return "رمز عبور ضعیف است: باید شامل حداقل یک حرف بزرگ باشد"
    
    if not any(char.islower() for char in password):
        return "رمز عبور ضعیف است: باید شامل حداقل یک حرف کوچک باشد"
    
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return "رمز عبور ضعیف است: باید شامل حداقل یک کاراکتر خاص باشد"
    
    return "رمز عبور قوی است"

password = input("رمز عبور را وارد کنید: ")
print(validate_password(password))

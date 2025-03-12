def validate_email(email):
    valid_domains = ["gmail.com", "yahoo.com", "outlook.com"]
    
    if " " in email:
        return "ایمیل نامعتبر است: نباید شامل فاصله باشد"
    
    if "@" not in email:
        return "ایمیل نامعتبر است: باید شامل @ باشد"
    
    username, domain = email.split("@", 1)
    
    if len(username) < 5:
        return "ایمیل نامعتبر است: باید حداقل ۵ کاراکتر قبل از @ داشته باشد"
    
    if domain not in valid_domains:
        return "ایمیل نامعتبر است: دامنه معتبر نیست"
    
    return "ایمیل معتبر است"

email = input("ایمیل را وارد کنید: ")
print(validate_email(email))

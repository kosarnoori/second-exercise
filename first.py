def validate_domain(domain):
    valid_extensions = ['.com', '.net', '.org', '.ir']
    
    if not domain.startswith("www."):
        return "نام دامنه معتبر نیست: باید با 'www.' شروع شود"
    
    if " " in domain:
        return "نام دامنه معتبر نیست: نباید شامل فاصله باشد"
    
    if "." not in domain:
        return "نام دامنه معتبر نیست: باید حداقل یک نقطه (.) داشته باشد."
    
    if not any(domain.endswith(ext) for ext in valid_extensions):
        return "نام دامنه معتبر نیست: پسوند دامنه معتبر نیست"
    
    return "نام دامنه معتبر است."

domain = input("نام دامنه را وارد کنید: ")
print(validate_domain(domain))

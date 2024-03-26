def tags(html_tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{html_tag}>{func(*args, **kwargs)}</{html_tag}>"
        return wrapper
    return decorator




@tags('h1')

def to_upper(text):
    return text.upper()

print(to_upper('hello'))
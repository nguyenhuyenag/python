data_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhwAAAKACAY"

if data_url.__contains__(','):
    # Split từ ',' đầu tiên
    _, base64_content = data_url.split(',', 1)
    result = {
        "base64": base64_content
    }
    print(result)

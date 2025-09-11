def main():
    filetype = otherchecker(input("File Name: "))
    print(filetype)

def checker(fn):  
    fn = fn.strip().casefold()

    if ("." not in fn):
        return "application/octet-stream"
    
    name, type = fn.rsplit(".", 1)
    if type in ["jpeg", "jpg", "png", "gif"]:
        return f"image/{type}"
    elif (type == "txt") | (type == "pdf"):
        return f"text/{type}"
    elif (type == "zip"):
        return f"file/{type}"

def otherchecker(fn):
    fn = fn.strip().casefold()

    if ("." not in fn):
        return "application/octet-stream"

    fn, ext = fn.rsplit(".", 1)
    ext_dict = {
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "txt": "text/txt",
        "pdf": "text/pdf",
        "zip": "file/zip"
    }

    return ext_dict.get(ext, "application/octet-stream")
main()
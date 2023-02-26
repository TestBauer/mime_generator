import json
from textwrap import wrap


def getListofNumArrayfromHeader(header_signs: str) -> list:
    num = None
    r2 = []
    for heads in header_signs:
        num = (wrap(heads.split(",")[1], 2))
        r = []
        paddingsize = int(heads.split(",")[0])
        if paddingsize > 0:
            # offset = padding_size * 1 byte
            for a in range(int(paddingsize)):
                r.append(int('0x00', 16))

        for i in num:
            a = ('0x' + str(i))
            a = int(a, 16)
            r.append(a)
        r2.append(r)
    return r2


def getHeaderbyExtension(extension: str, magiclist: json) -> object:
    r_list = {}
    try:
        r_list = magiclist[extension.lower()]

    except KeyError:
        print(f"Unknown Extension : {extension} !")

    finally:

        return r_list


if __name__ == "__main__":
    # // https://gist.github.com/qti3e/6341245314bf3513abb080677cd1c93b#file-extensions-json
    f = open("./config/magic.list.json")
    magicl = json.load(f)

    ext = "pcx"
    ext2 = "." + ext
    header = getHeaderbyExtension(extension=ext, magiclist=magicl)
    if header is not []:
        list_of_num = getListofNumArrayfromHeader(header["signs"])

        for count, num in enumerate(list_of_num):
            f = open(f"./output/file_{ext}_{count}{ext2}", "wb")
            arr = bytearray(num)
            f.write(arr)
            f.close()

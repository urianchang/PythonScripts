def sizeof_fmt(num: int, suffix: str = "B") -> str:
    floaty = float(num)
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(floaty) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        floaty /= 1024.0
    return "%.1f%s%s" % (floaty, "Yi", suffix)


if __name__ == "__main__":
    assert sizeof_fmt(168963795964) == "157.4GiB"

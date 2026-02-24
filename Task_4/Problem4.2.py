def read_file():
    try:
        f = open("students.txt", "r")
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            print("File is empty")
            return []

        return lines
    except:
        print("Cannot open file")
        return []


def analyze(lines):
    stu = {}
    sub = {}

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(parts) != 3:
            continue

        name = parts[0].strip()
        hrs = parts[1].strip()
        subject = parts[2].strip()

        if not hrs.isdigit():
            continue

        hrs = int(hrs)

        if name in stu:
            stu[name] = stu[name] + hrs
        else:
            stu[name] = hrs

        if subject in sub:
            sub[subject] = sub[subject] + hrs
        else:
            sub[subject] = hrs

    return stu, sub


def find_top(d):
    top_name = None
    top_val = 0

    for key in d:
        if top_name is None:
            top_name = key
            top_val = d[key]
        else:
            if d[key] > top_val:
                top_name = key
                top_val = d[key]

    return top_name, top_val


def write_file(stu, sub):
    f = open("summary.txt", "w")

    f.write("Total Hours Per Student:\n")
    for s in stu:
        f.write(s + ": " + str(stu[s]) + "\n")

    f.write("\nTotal Hours Per Subject:\n")
    for sb in sub:
        f.write(sb + ": " + str(sub[sb]) + "\n")

    top_s, val_s = find_top(stu)
    top_sub, val_sub = find_top(sub)

    f.write("\nTop Student: " + top_s +
            " (" + str(val_s) + " hours)\n")

    f.write("Most Studied Subject: " + top_sub)

    f.close()


lines = read_file()

if len(lines) > 0:
    stu, sub = analyze(lines)
    write_file(stu, sub)
    print("Done")
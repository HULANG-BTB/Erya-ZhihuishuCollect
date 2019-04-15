import csv

q_a_file = open("q.txt", "r", encoding="utf-8")

q_a = {}
q = ""
a = ""
a_a = ""
a_b = ""
a_c = ""
a_d =""
q_s = ""

for line in q_a_file:
    line = line.strip().replace(",","，") # .replace("(", "（").replace(")", "）")
    if "【单选题】" in line :
        q = line.replace("【单选题】","")
        a = ""
        if "A" in q:
            a = "A"
        elif "B" in q:
            a = "B"
        elif "C" in q:
            a = "C"
        elif "D" in q:
            a = "D"
        q = q.replace(a, "")
        q_s = ""
    elif "【判断题】" in line :
        q = line.replace("【判断题】","")
        if "错" in q or "×" in q:
            a = "×"
        elif "对" in q or "√" in q:
            a = "√"
        q = q.replace(a, "").replace("对","").replace("错","")
        q_a[q] = a
        q_s = ""
    elif "【多选题】" in line :
        q = line.replace("【多选题】","")
        a = ""
        if "A" in q:
            a = a + "A"
        if "B" in q:
            a = a + "B"
        if "C" in q:
            a = a + "C"
        if "D" in q:
            a = a + "D"
        q = q.replace(a, "")
        q_s = ""
    elif "A、" in line and "A" in a :
       q_s = line.replace("A、","")
       if q in q_a.keys() :
           q_a[q] += "|" + q_s
       else :
           q_a[q] = q_s
    elif "B、" in line and "B" in a :
       q_s = line.replace("B、","")
       if q in q_a.keys() :
           q_a[q] += "|" + q_s
       else :
           q_a[q] = q_s
    elif "C、" in line and "C" in a :
       q_s = line.replace("C、","")
       if q in q_a.keys() :
           q_a[q] += "|" + q_s
       else :
           q_a[q] = q_s
    elif "D、" in line and "D" in a :
       q_s = line.replace("D、","")
       if q in q_a.keys() :
           q_a[q] += "|" + q_s
       else :
           q_a[q] = q_s

    line
q_a_file.close()

csv_file = open("list.csv", "w+", encoding="utf-8", newline="")
csv_writer = csv.writer(csv_file)
for key in q_a.keys():
    print("【问题】：" + str(key))
    print("【答案】：" + str(q_a[key]))
    csv_writer.writerow([str(key), str(q_a[key])])
csv_file.close()


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

for line in q_a_file :
    line = line.strip().replace(",","，").replace(" ","") # .replace("(", "（").replace(")", "）")
    if "（）" in line :
        q = line
    elif "A、" in line :
        a_a = line.replace("A、","")
    elif "B、" in line :
        a_b = line.replace("B、","")
    elif "C、" in line :
        a_c = line.replace("C、","")
    elif "D、" in line :
        a_d = line.replace("D、","")
    elif "我的答案：" in line or "正确答案：" in line :
        ans = line
        if "A" in ans :
            if q in q_a.keys() :
                q_a[q] += "|" + a_a
            else :
                q_a[q] = a_a
        if "B" in ans :
            if q in q_a.keys() :
                q_a[q] += "|" + a_b
            else :
                q_a[q] = a_b
        if "C" in ans :
            if q in q_a.keys() :
                q_a[q] += "|" + a_c
            else :
                q_a[q] = a_c
        if "D" in ans :
            if q in q_a.keys() :
                q_a[q] += "|" + a_d
            else :
                q_a[q] = a_d
        if "对" in ans or "√" in ans :
            q_a[q] = "√"
        if "错" in ans or "×" in ans :
            q_a[q] = "×"
q_a_file.close()

csv_file = open("list.csv", "w+", encoding="utf-8", newline="")
csv_writer = csv.writer(csv_file)
for key in q_a.keys():
    print("【问题】：" + str(key))
    print("【答案】：" + str(q_a[key]))
    csv_writer.writerow([str(key), str(q_a[key])])
csv_file.close()

# To calculate test stats for university entrance test , data available publicly at http://www.neduet.edu.pk/admission/2017/19-08-2017/RESULT_2017_18/index.htm (assuming it's not taken down )
import bs4, requests, re

thingie = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "X", "Y", "S", "P",
           "V"]  # blocks of student roll numbers
test = []
test1 = []
for alphabet in thingie:
    link = "http://www.neduet.edu.pk/admission/2017/19-08-2017/RESULT_2017_18/sheets/BLOCK%20{}.htm".format(
        alphabet)  # making links for each block
    page = requests.get(link)  # getting page
    soup = bs4.BeautifulSoup(page.text, "lxml")  # making html parser object

    result = soup.body.find_all(string=re.compile("^X$"), recursive=True)  # searching for each failed student
    print("{}:{}".format(alphabet,
                         result))  # printing each block and its list of failed students because it looks cool in the terminal

    test.append(len(result))  # appending number of failed students in each block

    foo = soup.body.find(string=re.compile("^[0-9]+ to [0-9]+$"))  # finding total number of students in each block

    a = foo.split(" to ")

    bar = int(a[1]) - int(a[0])

    test1.append(bar)

num = sum(test)  # summing all failed students from each block
total = sum(test1)  # summing total number of students from each block
ratio = 100 - (num / total) * 100
print("""The following number of students attempted the paper: {}\n
The following failed: {}\n
Passing percentage: {}
""".format(total, num, ratio))

import re
#+7(812)382-2880 +7(980)382-27-11 +7(908)966-5971 +7(921)538-77-55 +7(996)675-1717 +7(495)382-02-39 +7(921)717-3511 +7(812)986-09-32 +7(345)660-9867 +7(343)120-44-29
string = input()
def auto_num(string):
    regex = r"\+7\(812\)\d{3}-\d{2}-?\d{2}|\+7\(921\)\d{3}-\d{2}-?\d{2}"
    return print(re.findall(regex, string))
auto_num(string)
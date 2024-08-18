from bs4 import BeautifulSoup


with open("following.html", "r", encoding="utf-8") as file1:
    cont1 = file1.read()

with open("followers_1.html", "r", encoding="utf-8") as file2:
    cont2 = file2.read()

s1 = BeautifulSoup(cont1, "html.parser")
following_names = [a.text for a in s1.find_all("a")]

s2 = BeautifulSoup(cont2, "html.parser")
followers_names = [a.text for a in s2.find_all("a")]

difference_names = set(following_names) - set(followers_names)
print(difference_names)


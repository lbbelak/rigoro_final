from requests import get
from bs4 import BeautifulSoup
page = get("https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089")
TEAM = "Brno"
content_all = page.content
soup = BeautifulSoup(content_all, 'html.parser')
matches = soup.find_all('a', class_="list-score-link")
final = ''
new_line = ''
for match in matches:
	content = match.text.split('\n')
	info = [line for line in content if line.strip() != '']
	if TEAM == info[3]:
		date = info[0].split('•')
		date = date[:1]
		score = info[4].split(':')
		if int(score[0]) > int(score[1]):
			new_line = date[0] + " jsme porazili " + info[8]
	elif TEAM == info[8]:
		date = info[0].split('•')
		date = date[:1]
		score = info[4].split(':')
		if score[0] < score[1]:
			new_line = date[0] + " jsme porazili " + info[3]
	else:
		new_line = ''
	if new_line:
		final += '\n' + new_line
print(final)

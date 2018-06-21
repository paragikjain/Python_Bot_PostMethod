import mechanize
br = mechanize.Browser(factory=mechanize.RobustFactory())
br.open("https://www.occultspeak.com/reincarnation/")
br.select_form(nr=0)
br.form['comment'] = 'Thank you For this Information'
br.form['author'] = 'Jos Peter'
br.form['email'] = 'jospeter@gmail.com'
br.form['url'] = 'http://www.mockinfo.com'
br.submit()
html=br.response().readlines()
for i in range(0,len(html)):
 print(html[i])
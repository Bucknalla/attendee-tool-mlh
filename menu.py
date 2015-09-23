import webbrowser
import mlh
import rumps

@rumps.clicked('Attendees','Dietary Restrictions')
def click_diet(self):
    window = rumps.Window(dimensions=(320,120))
    window.title = 'Dietary Restrictions'
    window.message = 'Information regarding dietary restrictions.'
    window.default_text = mlh.get_dietary_users()
    window.icon = 'mlh-gs.png'
    window.run()

@rumps.clicked('Attendees','Medical Needs')
def click_med(self):
    window = rumps.Window(dimensions=(320,120))
    window.title = 'Medical Needs'
    window.message = 'Information regarding medical needs.'
    window.default_text = mlh.get_special_users()
    window.icon = 'mlh-gs.png'
    window.run()

@rumps.clicked('MLH','Website')
def click_web(self):
    webbrowser.open_new_tab('http://www.mlh.io')

@rumps.clicked('MLH','Guides','Organiser')
def click_org(self):
    webbrowser.open_new_tab('http://guide.mlh.io')

@rumps.clicked('MLH','Guides','Sanctions')
def click_sanctions(self):
    webbrowser.open_new_tab('http://static.mlh.io/docs/event-sanctioning-guide.pdf')

@rumps.clicked('MLH','Guides','Code of Conduct')
def click_coc(self):
    webbrowser.open_new_tab('http://static.mlh.io/docs/mlh-code-of-conduct.pdf')

@rumps.clicked('MLH','Contacts','Info')
def click_info(self):
    webbrowser.open_new_tab('mailto:hi@mlh.io')

@rumps.clicked('MLH','Contacts','Incidents')
def click_incidents(self):
    webbrowser.open_new_tab('mailto:incidents@mlh.io')

@rumps.clicked('MLH','Contacts','Slack')
def click_slack(self):
    webbrowser.open_new_tab('https://mlh.slack.com/?redir=%2Fhome')

@rumps.clicked('About')
def click_about(self):
    window = rumps.Window(title="About",message="Created by Alex Bucknall 2015", dimensions=(0,0))
    window.icon = None
    window.run()

@rumps.clicked('Search')
def click_search(self):
    response = rumps.Window(cancel='Cancel',title='Enter a name',message='Enter a complete name or search by first/last name.',dimensions=(300,20)).run()
    if response.clicked:
        rumps.alert(title='Search: '+response.text,message=mlh.search_user(response.text))


if __name__ == "__main__":
    app = rumps.App("MLH Organiser Tool",  icon='mlh-gs.png')
    app.menu = [
        'Search',
        {'Attendees':
            {"Dietary Restrictions": [],
             "Medical Needs": []}},
        {'MLH':
            {"Guides": ["Organiser", "Sanctions","Code of Conduct"],
             "Contacts": ["Info","Slack","Incidents"],"Website": []}},
        None,
        'About',
        None
    ]

    app.run()
    AwesomeStatusBarApp().run()

import rumps
import webbrowser
import mlh

@rumps.clicked('Attendees','Dietary Restrictions')
def open_about(self):
    window = rumps.Window(dimensions=(320,120))
    window.title = 'Dietary Restrictions'
    window.message = 'Information regarding dietary restrictions.'
    window.default_text = mlh.get_dietary_users()
    window.icon = 'mlh.png'
    window.run()

@rumps.clicked('Attendees','Medical Needs')
def open_about(self):
    window = rumps.Window(dimensions=(320,120))
    window.title = 'Medical Needs'
    window.message = 'Information regarding medical needs.'
    window.default_text = mlh.get_special_users()
    window.icon = 'mlh.png'
    window.run()

@rumps.clicked('MLH','Website')
def something(self):
    webbrowser.open_new_tab('http://www.mlh.io')

@rumps.clicked('MLH','Guides','Organiser')
def something(self):
    webbrowser.open_new_tab('http://guide.mlh.io')

@rumps.clicked('MLH','Guides','Sanctions')
def something(self):
    webbrowser.open_new_tab('http://static.mlh.io/docs/event-sanctioning-guide.pdf')

@rumps.clicked('MLH','Guides','Code of Conduct')
def something(self):
    webbrowser.open_new_tab('http://static.mlh.io/docs/mlh-code-of-conduct.pdf')

@rumps.clicked('MLH','Contacts','Info')
def something(self):
    webbrowser.open_new_tab('mailto:hi@mlh.io')

@rumps.clicked('MLH','Contacts','Incidents')
def something(self):
    webbrowser.open_new_tab('mailto:incidents@mlh.io')

@rumps.clicked('MLH','Contacts','Slack')
def something(self):
    webbrowser.open_new_tab('https://mlh.slack.com/?redir=%2Fhome')

@rumps.clicked('About')
def open_about(self):
    window = rumps.Window(title="About",message="Created by Alex Bucknall 2015", dimensions=(0,0))
    window.icon = None
    window.run()

if __name__ == "__main__":
    app = rumps.App("MLH Organiser Tool",  icon='mlh.png')
    app.menu = [
        {'Attendees':
            {"Dietary Restrictions": [],
             "Medical Needs": []}},
        {'MLH':
            {"Guides": ["Organiser", "Sanctions","Code of Conduct"],
             "Contacts": ["Info","Slack","Incidents"],"Website": []}},
        'About',
        None
    ]

    app.run()
    AwesomeStatusBarApp().run()

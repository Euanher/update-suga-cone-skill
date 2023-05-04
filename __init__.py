from mycroft import MycroftSkill, intent_handler


class UpdateSugaCone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('cone.suga.update.intent')
    def handle_cone_suga_update(self, message):
        self.speak_dialog('cone.suga.update')


def create_skill():
    return UpdateSugaCone()


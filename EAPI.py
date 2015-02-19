import sys
from evernote.api.client import EvernoteClient
from evernote.edam.userstore import constants as UserStoreConstants


class NotAuthenticatedException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class SDKVersionException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class EAPI(object):
    def __init__(self):
        self.evernoteClient = None
        self.userStore = None
        self.noteStore = None

    def authenticate(self, token=None, login=None, password=None):
        # TODO: OAuth authentication
        self.evernoteClient = EvernoteClient(token=token, sandbox=True)
        self.userStore = self.evernoteClient.get_user_store()
        self.noteStore = self.evernoteClient.get_note_store()

        # check SDK version
        is_version_up_uo_date = self.userStore.checkVersion(
            "Snake Notes",
            UserStoreConstants.EDAM_VERSION_MAJOR,
            UserStoreConstants.EDAM_VERSION_MINOR
        )

        if not is_version_up_uo_date:
            raise SDKVersionException("Please update your Evernote SDK")

    def list_note_books(self):
        return self.noteStore.listNotebooks()

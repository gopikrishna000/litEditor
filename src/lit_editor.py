# main window of the app
# manages the EditorSession
from tkinter import Tk, Text, END

from src.logic import EditorSession


class LitEditor:
    editor_session: EditorSession = None

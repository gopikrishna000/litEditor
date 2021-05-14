# 🔥 litEditor

Simple Markdown Editor made with Python Tkinter

### 🚀 Aim

To Develop a Markdown Editor guided by the following Principles :

1. Minimal Traditional Functionality
1. Non-Native UX Patterns
1. KISS (Keep it simple and stupid)

### 🌌 Abstract

For long have existed vast markdown editors and tbc...

### 🍧 UI Spec

1. Tab Layout
   ```
   _________________________________________________________________
   | 📁  |                                                         |
   |-----|                                                          |
   | ✍  |                                                         |
   |-----|                    Selected Tab's Page                   |
   | 🔥  |                                                          |
   |-----|                                                          |
   | 👀  |                                                         | 
   |-----|                                                          |
   | ⚙   |                                                          |
   |_____|__________________________________________________________|
   ```
    1. 📁 - Select Folder
    1. ✍ - Edit Markdown
    1. 🔥 - Edit Markdown and Markdown Preview side by side
    1. 👀 - Markdown Preview
    1. ⚙ - Settings


2. Project Tab Page - ```# TODO: @surendar-283```

### 😃 Basic Features

1. Cut, Copy, Paste between```clipboard``` and the ```Editable Text Area```
1. Delete all, Select All, Undo, Redo
1. Keyboard shortcuts for the above two
1. Preview Markdown

### 😎 Ultimate Features

1. Auto save

### 🌊 Typical User Flow

1. Starting litEditor, User is presented with the TabLayout Window
2. ✍,🔥 & 👀 will be disabled
3. 📁 will be selected
4. after user selects a valid file in 📁.The disabled tabs(✍,🔥 & 👀) will be active
5. user edits the markdown in either ✍ or in one of the frames of 🔥
6. the edit is reflected in the preview(🔥 or 👀)
7. changes are saved as the user is editing
8. if the user were to switch to 📁, then continue from step 4.

### 💻 Systems Overview

- #### 👶 Initializing the systems
    - ```LitEditor``` is instantiated
    - which in turn instantiates ```other UIs```
    - ```📁 Page UI``` selects a file accordingly creates an ```EditorSession```
    - that ```EditorSession``` will be managed by ```LitEditor```
- #### 👨‍ Working of the systems
    - ```Markdown Editor UI in ✍ & 🔥``` notifies the ```EditorSession``` of any edits
    - ```EditorSession``` on receiving any edit notifications, delegates them to
        - ```FileSession``` which saves changes to the file
        - ```HtmlSession``` which converts the Markdown text to html
    - ```Markdown Preview UI in 🔥 & 👀``` display the html generated from ```HtmlSession```

- #### 💀 Termination of the systems (Lifecycle)
    - ```LitEditor``` - till the program exits
    - ```EditorSession``` - recreated for evey file selection in 📁
        - ```FileSession``` - follows ```EditorSession```'s Lifecycle
        - ```HtmlSession``` - follows ```EditorSession```'s Lifecycle

### 🧩 State Management

- #### Why ?
  Changes in state and effects of those changes are separated into different places for maintainability, and these are
  stream of changes.
  (ex - editing text in ```✍ or 🔥``` must be reflected in ```🔥, 👀 through HtmlSession``` and ```FileSession```)

- #### How ?
  We are going to follow a modified version of ```Observer Pattern ⚡```
    - #### Why modified ?
      In our particular use case for the ```Observer Pattern ⚡```, the observables will be listened from classes with
      well-defined lifecycle and only unlisten after that lifecycle terminates. if we followed the
      regular ```Observer Pattern ⚡```, we would have to listen and unlisten each observable manually. There is a better
      way.

    - #### How modified ?
        - Every class that wants to listen to an Observable extends ```Lifecycle``` that maintains whether it is active
          as a boolean
        - ```Observable``` provides observe method that takes a ```Lifecycle``` and a function as argument
        - When the value of the ```Observable``` changes, iterate all the observers, remove observers which are not
          active and notify only the active observers

    - #### More on this Particular Pattern
        - This pattern is a simplified version
          of [LiveData](https://developer.android.com/topic/libraries/architecture/livedata) in Android.   
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


2. File Tab Page - ```# TODO: @surendar-283```

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

### 💻 Logic Overview

- #### 👶 Initializing
    - ```lit_editor``` instantiates observables
        - ```use_file_logic``` & ```use_html_logic``` are called
        - ```other UIs``` are built passing their required ```Observables```
        - ```other UIs``` are placed according to layout
- #### 👨‍ Working
    - the observables passed from ```lit_editor``` help in communication
    - ```UI``` updates those observables
    - ```Logic``` observes those updates and acts accordingly

### 🧩 State Management

- #### Why ?
  Changes in state and effects of those changes are separated into different places for maintainability, and these are
  stream of changes.
  (ex - editing text in ```✍ or 🔥 - Markdown Editor``` must be reflected in ```🔥, 👀 - Markdown View```
  and ```use_file_logic```). We need a mechanism to effectively communicate and handle these changes.

- #### How ?
  We are going to follow a simplified the ```Observer Pattern ⚡```
    - #### Why simplified ?
      In our particular use case for the ```Observer Pattern ⚡```, the observables will be listened throughout the
      lifecycle of the program. if we followed the regular ```Observer Pattern ⚡```, we would have un-utilized
      functionality in observable. There is a simpler way.

    - #### How simplified ?
        - The ```Observable``` doesn't provide a way to stop receiving the changes
        - ```Observable``` provides ```observe``` method that takes a function (i.e ```Observer```) as argument
        - When the value of the ```Observable``` changes (by calling ```Observable.dispatch```), every observer is
          notified of the change


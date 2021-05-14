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
      - ```SessionState``` which records the state to provide Undo services. 
      - ```FileSession``` which saves changes to the file
      - ```HtmlSession``` which converts the Markdown text to html
   - ```Markdown Preview UI in 🔥 & 👀``` display the html generated from ```HtmlSession```
   
- #### 💀 Termination of the systems (Lifecycle)
   - ```LitEditor``` - till the program exits
   - ```EditorSession``` - recreated for evey file selection in 📁
      - ```SessionState``` - follows ```EditorSession```'s Lifecycle
      - ```FileSession``` - follows ```EditorSession```'s Lifecycle
      - ```HtmlSession``` - follows ```EditorSession```'s Lifecycle
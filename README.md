# 🔥 litEditor

Simple Markdown Editor made with Python Tkinter

### 🚀 Aim

To Develop a Markdown Editor guided by the following Principles :

1. Minimal Traditional Functionality
1. Non-Native UX Patterns
1. KISS (Keep it simple and stupid)

### 🌌 Abstract

For long have existed vast markdown editors and tbc...

### 👨‍💻 Markdown Language

- ### What is Markdown?
  Markdown is a way to style text on the web. You control the display of the document; formatting words as bold or italic, adding images, and creating lists are  just a few of the things we can do with Markdown.Mostly, Markdown is just regular text with a few non-alphabetic characters thrown in, like ```#``` or ```*```.
  
- ### Why Markdown?
   - ### Easy On The Eyes:
      The overriding design goal for Markdown’s formatting syntax is to make it as readable as possible.
   - ### Fewer Errors:
       Markdown’s simplicity and flexibility helps you make fewer mistakes, and errors are much easier to find.
   - ### Kill Your CMS(Content management system):
       Markdown can be written anywhere there’s a blinking cursor and shared in any format. It’s just plain text. You don’t need any WYSIWYG controls, because the Markdown characters actually look like the formatted results you’ll get.
       
### 🖥 HTML Viewer
  - A hypertext markup language (HTML) viewer is a tool that allows website designers to view and edit their work in real time. 
  - The HTML viewer displays code on one side of the screen and the webpage-in-progress on the other.
  - Also known as an HTML previewer or HTML editor, these tools are intended to reduce or eliminate broken or inefficient code.
  - HTML viewers can insert prewritten, frequently-used sections of code, or highlight certain lines of code.
  - One of the most useful features of an HTML viewer is the ability to split the screen between the webpage code and a preview of how the code will look when it is  uploaded to a server.
  
 
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
  We are going to follow the ```Observer Pattern ⚡```. Tkinter provides Variables for that. ```StringVar``` will be used
  mostly. 


from flask import Flask, render_template, request
import os
import difflib

tracker = Flask(__name__)

@tracker.route('/')
def index():
    return render_template('index.html')

@tracker.route('/', methods=['POST'])
def my_form_post():
    notes = request.form['text']
    filename = request.form['filename']
    if os.path.isfile(filename):
        with open(filename,'r') as rf:
            old_note = rf.read()
        differ = difflib.Differ()
        diff = differ.compare(old_note.split('\n'),notes.split('\n'))
        with open(filename,'w') as wf:
            wf.write(notes)
        return render_template('form.html',notes=diff,filename=filename)
    else:
        with open(filename,'w') as wf:
            wf.write(notes)
        return "File saved at location: " + filename

if __name__ == "__main__":
    tracker.run(debug=True)

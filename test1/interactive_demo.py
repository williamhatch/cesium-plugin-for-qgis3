import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web JavaScript interactive with QWebEngineView')

layout = QVBoxLayout()
win.setLayout(layout)

view = QWebEngineView()
view.setHtml('''
  <html>
    <head>
      <title>A Demo Page</title>

      <script language="javascript">
        // Completes the full-name control and
        // shows the submit button
        var g = ""
        function completeAndReturnName() {
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + '' + lname + "" + g;

          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';

          return full;
        }
      </script>
    </head>

    <body>
      <form>
        <label for="fname">First name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <label for="lname">Last name:</label>
        <input type="text" name="lname" id="lname"></input>
        <br />
        <label for="fullname">Full name:</label>
        <input disabled type="text" name="fullname" id="fullname"></input>
        <br />
        <input style="display: none;" type="submit" id="submit-btn"></input>
      </form>
    </body>
  </html>
''')

button = QPushButton('set full name')


def js_callback(result):
    print("--- call back ---")
    print(result)


def js_callback2(result):
    print("--- set var ---")
    print(result)


def complete_name():
    # set context from py to JS context
    view.page().runJavaScript('g="hello!";', js_callback2)
    # get return from JS
    view.page().runJavaScript('completeAndReturnName();', js_callback)


button.clicked.connect(complete_name)

layout.addWidget(view)
layout.addWidget(button)

win.show()
sys.exit(app.exec_())

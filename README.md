Thanks geodrinx/cesium but it is not updated since 8 years ago. :)

Just make some changes to adpat to QGIS3

Installation and test
-------------
1. Copy to the files to qgis plugin folder, normally located in the ~\AppData\Roaming\QGIS\QGIS3\profiles\default (windows)
2. Start the plugin server by running the following command:
   ```shell
   npx http-server -p . 8000
   ```
   make sure that npm is installed
3. Enable the cesium plugin from the plugin menu. (Just make sure cesium is checked)
4. Click from the menu: Plugins -> cesium -> cesium, it will auto open the browser.

(Change the default access token for cesium which can be applied from cesium official website)
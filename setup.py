from distutils.core import setup

setup (name = "gnomeconnectionmanager",
       version = "1.1.0",
       author = "Sebastian Jordan",
       author_email = "sebastian.jordan.mail@googlemail.com",
       description = ("A tabbed terminal connection manager for the gnome "
                      "environment"),
       license="GPL-3",
       keywords="tool terminal gnome",
       packages=["gnomeconnectionmanager"],
       package_dir={"gnomeconnectionmanager": "gnomeconnectionmanager"},
       package_data={"gnomeconnectionmanager" : 
                     ["lang/*",
                      "donate.gif",
                      "gnome-connection-manager.glade",
                      "icon.png",
                      "ssh.expect",]},
       requires= [ "pytgtk",
                   "gobject",
                   "vte",],
       scripts=['gcm',],
       include_package_data = True
   )

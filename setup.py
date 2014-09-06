from distutils.core import setup

setup (name = "gnome-connection-manager",
       version = "1.1.0",
       author = "Sebastian Jordan",
       author_email = "sebastian.jordan.mail@googlemail.com",
       description = ("A tabbed terminal connection manager for the gnome "
                      "environment"),
       license="GPL-3",
       keywords="tool terminal gnome",
       packages=["gnome-connection-manager"],
       package_data=["gnome-connection-manager/donate.gif",
                     "gnome-connection-manager/gnome-connection-manager.glade",
                     "gnome-connection-manager/icon.png",
                     "gnome-connection-manager/lang/*",
                     "ghome-connection-manager/ssh.expect"
                 ],
       requires= [ "pytgtk",
                   "gobject",
                   "vte",
               ],
       scripts=["gnome-connection-manager/gcm.py"]
   )

                

"""
Contains dialog boxed for the gnome connectino manager
"""

import gtk

def msgbox(text, parent=None):
    """
    Print a message box to the screen containing 'text' and a button

    text: Is the text that is displayed in the msgbox
    parent: is the parent of the message box
    """
    msgBox = gtk.MessageDialog(parent, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, text)
    msgBox.set_icon_from_file(ICON_PATH)
    msgBox.run()    
    msgBox.destroy()

def msgconfirm(text):
    """Open a confirm window

    arguments:
    text: The text that prompted to the user

    return:
    a GTK response Object.
    """
    msgBox = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_OK_CANCEL, text)
    msgBox.set_icon_from_file(ICON_PATH)
    response = msgBox.run()    
    msgBox.destroy()
    return response


def inputbox(title, text, default='', password=False):
    msgBox = EntryDialog(title, text, default, mask=password)
    msgBox.set_icon_from_file(ICON_PATH)
    if msgBox.run() == gtk.RESPONSE_OK:
        response = msgBox.value
    else:
        response = None
    msgBox.destroy()
    return response

def show_font_dialog(parent, title, button):
    if not hasattr(parent, 'dlgFont'):
        parent.dlgFont = None
        
    if parent.dlgFont == None:
        parent.dlgFont = gtk.FontSelectionDialog(title)
    fontsel = parent.dlgFont.fontsel
    fontsel.set_font_name(button.selected_font.to_string())    

    response = parent.dlgFont.run()

    if response == gtk.RESPONSE_OK:        
        button.selected_font = pango.FontDescription(fontsel.get_font_name())        
        button.set_label(button.selected_font.to_string())
        button.get_child().modify_font(button.selected_font)
    parent.dlgFont.hide()
    
def show_open_dialog(parent, title, action):        
    dlg = gtk.FileChooserDialog(title=title, parent=parent, action=action)
    dlg.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
    
    dlg.add_button(gtk.STOCK_SAVE if action==gtk.FILE_CHOOSER_ACTION_SAVE else gtk.STOCK_OPEN, gtk.RESPONSE_OK)        
    dlg.set_do_overwrite_confirmation(True)        
    if not hasattr(parent,'lastPath'):
        parent.lastPath = os.path.expanduser("~")
    dlg.set_current_folder( parent.lastPath )
    
    if dlg.run() == gtk.RESPONSE_OK:
        filename = dlg.get_filename()
        parent.lastPath = os.path.dirname(filename)
    else:
        filename = None
    dlg.destroy()
    return filename
            

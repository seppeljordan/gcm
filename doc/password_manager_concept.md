# Interface to gnome-keyring

We want to implement a interface to the gnome keyring.
We will approach this task by creating a new class called **password_manager**.

The password manage automatically stores the passwords in a gnome keyring and
looks up already saved passwords.

## Name of the database

We have to store the keyring in a manner so that it will not interfere with
the users other keyrings.  When we activate the gnome keyring support then we
will ask the user which keyring the want the keyring to be named.

# Pulic methods

`encrypt(password)`
The method will encrypt the password and store it in the gnome keyring.
It returns the ID of the password in the keyring.

`decrypt(id)`
This method will decrypt a password looking up the id in the keyring and 
returning the stored password.

`__init__(keyring_name)`
The constructor of this class takes the keyring name on initialization.
It creates a new keyring when it is not yet existing.

`delete()`
This method deletes the keyring associated with the object.
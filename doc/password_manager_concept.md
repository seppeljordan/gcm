# Interface to gnome-keyring

We want to implement a interface to the gnome keyring.
We will approach this task by creating a new class called **password_manager**.

The password manage automatically stores the passwords in a gnome keyring and
looks up already saved passwords.

## Name of the database

We have to store the keyring in a manner so that it will not interfere with

the users other keyrings.  When we activate the gnome keyring support then we
will ask the user which keyring the want the keyring to be named.

# Concept of storing the data

We want to store the server data completly in the keyring. The procedure that
stores the password data takes a dictionary with data. We use that to store any
data that referes to the a stored connection. The only thing that is stored
plain is the id that is refering to the stored information in the keyring.

# Pulic methods

* `encrypt(password)`
  The method will encrypt the password and store it in the gnome keyring.
  It returns the ID of the password in the keyring.
* `decrypt(id)`
  This method will decrypt a password looking up the id in the keyring and 
  returning the stored password.
* `__init__(keyring_name)`
  The constructor of this class takes the keyring name on initialization.
  It creates a new keyring when it is not yet existing.
* `delete_key(id)`
  This method will remove a single key from the keyring.
* `delete_keyring()`
  This method deletes the entire keyring associated with the object.
* `save_host(connection_id, attributes)`
  This method stores the information of a already existing connection into the 
  keyring.
* `create_sync(server_info)`
  This method creates a new entry in the keyring. `server_info` is a dictionary
  that stores all the important information about the connection.
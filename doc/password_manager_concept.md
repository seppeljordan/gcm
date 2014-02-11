Interface to gnome-keyring
====

We want to implement a interface to the gnome keyring.
We will approach this task by creating a new class called **password_manager**.

The password manage automatically stores the passwords in a gnome keyring and
looks already saved passwords up.

Lookup and storage of passwords
====

In a gnome keyring every item has an id.  We need to map the ids to the correct
passwords. To to this we need a mapping file and we will store it in the
directory "~/.gcm".
The file is called gcm.passwords.

We need a unique identification for our pairs of hosts and passwords and this
will be the group and the name of the host because it is not allowed in gcm
that there are two hosts in the same group with the same name.

The only possibility to change either the group/name or the password is the
"edit" action which triggers to run a gtk window for saving the configuration
for the chosen host. If we change the only the password then we can directly
change the password in the gnome keyring. If we change the name or the group we
have to change the right entry in the gcm.passwords file. If both changes then
we will change do both.
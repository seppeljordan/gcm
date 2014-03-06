"""
This file contains 'Host', a python class that represents the connection
data for a remote host, and its Utilityclass HostUtils
"""

import vte

class Host:
    def __init__(self, *args):
        try:
            self.i = 0
            self.group = self.get_arg(args, None)
            self.name =  self.get_arg(args, None)
            self.description =  self.get_arg(args, None)            
            self.host =  self.get_arg(args, None)
            self.user =   self.get_arg(args, None)
            self.password = self.get_arg(args, None)
            self.private_key = self.get_arg(args, None)
            self.port = self.get_arg(args, 22)
            self.tunnel = self.get_arg(args, '').split(",")
            self.type = self.get_arg(args, 'ssh')
            self.commands = self.get_arg(args, None)
            self.keep_alive = self.get_arg(args, 0)
            self.font_color = self.get_arg(args, '')
            self.back_color = self.get_arg(args, '')
            self.x11 = self.get_arg(args, False)
            self.agent = self.get_arg(args, False)
            self.compression = self.get_arg(args,False)
            self.compressionLevel = self.get_arg(args,'')
            self.extra_params = self.get_arg(args, '')
            self.log = self.get_arg(args, False)
            self.backspace_key = self.get_arg(args, int(vte.ERASE_AUTO))
            self.delete_key = self.get_arg(args, int(vte.ERASE_AUTO))
        except:
            pass
       

    def get_arg(self, args, default):
        arg = args[self.i] if len(args)>self.i else default
        self.i +=1
        return arg

    def __repr__(self):
        return "group=[%s],\t name=[%s],\t host=[%s],\t type=[%s]" % (self.group, self.name, self.host, self.type)

    def tunnel_as_string(self):
        return ",".join(self.tunnel)

    def clone(self):
        return Host(self.group, 
                    self.name, 
                    self.description, 
                    self.host, 
                    self.user, 
                    self.password, 
                    self.private_key, 
                    self.port, 
                    self.tunnel_as_string(), 
                    self.type, 
                    self.commands, 
                    self.keep_alive, 
                    self.font_color, 
                    self.back_color, 
                    self.x11, 
                    self.agent, 
                    self.compression, 
                    self.compressionLevel, 
                    self.extra_params, 
                    self.log, 
                    self.backspace_key, 
                    self.delete_key)

class HostUtils:
    @staticmethod
    def get_val(cp, section, name, default):
        try:
            return cp.get(section, name) if type(default)!=type(True) else cp.getboolean(section, name)
        except:
            return default
    
    @staticmethod
    def load_host_from_ini(cp, section, pwd=''):
        if pwd=='':
            pwd = get_password()
        group = cp.get(section, "group")
        name = cp.get(section, "name")
        host = cp.get(section, "host")
        user = cp.get(section, "user")
        password = decrypt(pwd, cp.get(section, "pass"))
        description = HostUtils.get_val(cp, section, "description", "")
        private_key = HostUtils.get_val(cp, section, "private_key", "")
        port = HostUtils.get_val(cp, section, "port", "22")
        tunnel = HostUtils.get_val(cp, section, "tunnel", "")
        ctype = HostUtils.get_val(cp, section, "type", "ssh")
        commands = HostUtils.get_val(cp, section, "commands", "").replace('\x00', '\n')
        keepalive = HostUtils.get_val(cp, section, "keepalive", "")
        fcolor = HostUtils.get_val(cp, section, "font-color", "")
        bcolor = HostUtils.get_val(cp, section, "back-color", "")
        x11 = HostUtils.get_val(cp, section, "x11", False)
        agent = HostUtils.get_val(cp, section, "agent", False)
        compression = HostUtils.get_val(cp, section, "compression", False)
        compressionLevel = HostUtils.get_val(cp, section, "compression-level", "")
        extra_params = HostUtils.get_val(cp, section, "extra_params", "")
        log = HostUtils.get_val(cp, section, "log", False)
        backspace_key = int(HostUtils.get_val(cp, section, "backspace-key", int(vte.ERASE_AUTO)))
        delete_key = int(HostUtils.get_val(cp, section, "delete-key", int(vte.ERASE_AUTO)))
        h = Host(group, name, description, host, user, password, private_key, port, tunnel, ctype, commands, keepalive, fcolor, bcolor, x11, agent, compression, compressionLevel,  extra_params, log, backspace_key, delete_key)
        return h

    @staticmethod
    def save_host_to_ini(cp, section, host, pwd=''):
        if pwd=='':
            pwd = get_password()
        cp.set(section, "group", host.group)
        cp.set(section, "name", host.name)
        cp.set(section, "description", host.description)
        cp.set(section, "host", host.host)
        cp.set(section, "user", host.user)
        cp.set(section, "pass", encrypt(pwd, host.password))
        cp.set(section, "private_key", host.private_key)
        cp.set(section, "port", host.port)
        cp.set(section, "tunnel", host.tunnel_as_string())
        cp.set(section, "type", host.type)
        cp.set(section, "commands", host.commands.replace('\n', '\x00'))
        cp.set(section, "keepalive", host.keep_alive)
        cp.set(section, "font-color", host.font_color)
        cp.set(section, "back-color", host.back_color)
        cp.set(section, "x11", host.x11)
        cp.set(section, "agent", host.agent)
        cp.set(section, "compression", host.compression)
        cp.set(section, "compression-level", host.compressionLevel)
        cp.set(section, "extra_params", host.extra_params)
        cp.set(section, "log", host.log)
        cp.set(section, "backspace-key", host.backspace_key)
        cp.set(section, "delete-key", host.delete_key)


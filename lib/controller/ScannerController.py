import os
import importlib
import json
import re
import lib.db.db
import lib.controller.DatabaseHandler


class ScannerController():
    def __init__(self):
        self.Module = None
        self.dir = os.getcwd()
        self.path = self.dir
        self.Scanner = None
        self.Name = None
        self.Database = lib.db.db.DBHandler()


    def Interactive(self):
        try:
            if self.Scanner:
                self.Name = self.Scanner.Name
            while True:
                cmd = raw_input('SWEP Scanner(%s):%s~$ ' %(str(self.Name), self.dir))
                if cmd == 'exit':
                    return
                self.InterpretCommand(cmd)
        except KeyboardInterrupt:
            print '[*] Exitting.'
            return
        except Exception, e:
            print '[!] Failed to load command: %s' %(str(e))


    def InterpretCommand(self, command):
        try:
            if command.strip(' ') == '':
                return
            Command = command.split(' ', 1)
            if Command[0] == 'load':
                self.Load(command)
            elif Command[0] == 'unload':
                self.Unload(command)
            elif Command[0] == 'interactive':
                self.Interactive()
            elif Command[0] == 'set':
                self.Set(command)
            elif Command[0] == 'unset':
                self.Unset(command)
            elif Command[0] == 'scan':
                self.Scan()
            elif Command[0] == 'list':
                self.List()
            elif Command[0] == 'info':
                self.info()
            elif Command[0] == 'cd':
                self._cd(command)
            elif Command[0] == 'help':
                self.help(command)
            else:
                os.system(command)
        except Exception ,e:
            print '[!] Failed to interpret command: %s' %(str(e))


    def CheckCommand(self, command, lenth): # Check length, Remove null and stuff
        NewList = []
        try:
            for item in command:
                if item == '':
                    continue
                if item not in NewList:
                    NewList.append(item)
            if len(NewList) != int(lenth):
                return 0
        except Exception, e:
            print '[!] Failed to check command: %s' %(str(e))
        return NewList


    def Load(self, module):
        CommandDict = module.split(' ', 1)
        CommandDict = self.CheckCommand(CommandDict, 2)
        if not CommandDict:
            self.help('load')
            return
        module = str(CommandDict[1])
        try:
            path = self.Database.Query('SELECT path FROM scanner WHERE name="%s"' %(module))[0][0]
            if not path:
                print '[!] Module not found.'
                self.LoadLegacy(CommandDict)
            self.Scanner = importlib.import_module('lib.scanner.' + path).Scanner()
            self.Name = self.Scanner.Name
            print '[*] Load complete.'
        except Exception, e:
            print '[!] Failed to load module from database %s: %s' %(module, e)
            print '[*] Falling back to legacy mode.'
            self.LoadLegacy(CommandDict)
        return


    def LoadLegacy(self, CommandDict):
        try:
            RawJson = json.load(open('%s/lib/scanner/scanner.json' %(self.path)))
        except Exception, e:
            print '[!] Failed to load scanner json file: %s' %(str(e))
            return
        try:
            ScannerList = RawJson['scanner']
            if CommandDict[1] not in ScannerList.keys():
                print '[!] Module %s not found.' %(str(CommandDict[1]))
                return
            ModuleName = RawJson['scanner'][CommandDict[1]][0]
            try:
                self.Scanner = importlib.import_module(ModuleName).Scanner()
                self.Name = self.Scanner.Name
            except Exception, e:
                print '[!] Failed to load scanner: %s' %(str(e))
                return
            print '[+] Load Success.'
        except Exception, e:
            print '[!] Failed to load scanner: %s' %(str(e))
        return



    def Unload(self, module):
        CommandDict = module.split(' ')
        CommandDict = self.CheckCommand(CommandDict, 1)
        if not CommandDict:
            self.help('unload')
        self.Scanner = None
        self.Name = None
        return


    def Set(self, var):
        CommandDict = var.split(' ')
        CommandDict = self.CheckCommand(CommandDict, 3)
        if not CommandDict:
            self.help('set')
            return
        try:
            if not self.Scanner:
                print '[!] Scanner not specified.'
                return
            self.Scanner.__dict__[CommandDict[1]] = CommandDict[2]
        except Exception, e:
            print '[!] Failed to set variable: %s' %(str(e))
        return


    def Unset(self, var):
        CommandDict = var.split(' ')
        CommandDict = self.CheckCommand(CommandDict ,2)
        if not CommandDict:
            self.help('unset')
        try:
            if not self.Scanner:
                print '[!] Scanner not specified.'
                return
            self.Scanner.__dict__[CommandDict[1]] = None
        except Exception, e:
            print '[!] Failed to unset variable: %s' %(str(e))
        return


    def List(self):
        try:
            ScannerList = self.Database.Query('SELECT * FROM scanner')
            if not ScannerList:
                self.ListJson()
                return
            print '[*] Incoming scanner list.'
            print '[*] Total %s exploit(s).' %(str(len(ScannerList)))
            print 'NAME                   DESCRIPTION'
            print '----                   -----------'
            for item in ScannerList:
                print item[0].ljust(23) + item[1]
            return
        except Exception ,e:
            print '[!] Failed to fetch scanner list: %s' %(str(e))


    def Scan(self):
        if not self.Scanner:
            print '[!] Scanner not specified.'
            return
        self.Scanner.Scan()
        return


    def _cd(self, path):
        CommandDict = path.split(' ', 1)
        try:
            if len(CommandDict) == 2:
                os.chdir(CommandDict[1])
            else:
                os.chdir(os.getenv('path'))
            self.dir = os.getcwd()
        except Exception, e:
            print 'Failed to change dir: %s' %(str(e))
        return


    def help(self, *module):
        if module:
            ModuleName = module[0].split(' ')
            if len(ModuleName) != 1:
                print '[*] help [load unload set unset list interactive scan info help]'
                return
            else:
                ModuleName = ModuleName[0]
            if ModuleName == 'load':
                print '[*] load: Load a module.\n   Usage: load [name] e.g: load test'
            elif ModuleName == 'unload':
                print '[*] unload: Unload a module.'
            elif ModuleName == 'set':
                print '[*] set: Set values.\n    Usage: set [parm value]'
            elif ModuleName == 'interactive':
                print '[*] interactive: Start SWEP Scanner interactive mode, Ctrl+D to exit.'
            elif ModuleName == 'unset':
                print '[*] unset: Unset a module.\n   e.g: unset [parm]'
            elif ModuleName == 'scan':
                print '[*] scan: Start scan.'
            elif ModuleName == 'list':
                print '[*] list: Show scanner(s) list.'
            elif ModuleName == 'info':
                print '[*] info: Show module info.'
            elif ModuleName == 'help':
                print '[*] help: Show help message. "help help" for argument list.\n    e.g: help *args'
            else:
                print '[*] help [load unload set unset list interactive scan info help]'
        else:
            print '[*] help [load unload set unset list interactive scan info help]'
        return


    def info(self):
        try:
            if self.Scanner:
                self.Scanner.info()
            else:
                print '[!] Scanner not specified.'
                return
        except Exception, e:
            print '[!] Failed to load scanner info: %s' %(str(e))
        return


    def ListJson(self):
        print '[*] Database not found, using legacy mode.'
        try:
            RawJson = json.load(open('%s/lib/scanner/scanner.json' %(self.path)))
        except Exception, e:
            print '[!] Failed to load json: %s' %(str(e))
            return
        ScannerList = RawJson['scanner']
        print '[*] SWEP Scanner list:'
        print 'NAME               DESCRIPTION'
        print '----               -----------'
        for name in ScannerList.keys():
            print "%s%s" %(str(name).ljust(19, ' '), ScannerList[name][1])
        return



def test():
    controller = ScannerController()
    controller.Load('load sql')

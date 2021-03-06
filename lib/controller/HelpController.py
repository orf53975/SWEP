class HelpController():
    def __init__(self):
        pass


    def usage(self,module):
        if module == 'search':
            print '[*] SWEP search: Search an exploit. Usage: search *args'
        elif module == 'use':
            print '[*] SWEP use: Load an exploit. Usage: use *args'
        elif module == 'back':
            print '[*] SWEP back: Back(Unload) an exploit. Usage: back'
        elif module == 'check':
            print '[*] SWEP check: Check target information. Usage: check [waf cms language db version site] site'
        elif module == 'load':
            print '[*] SWEP load: Load a site. Usage: load *args'
        elif module == 'unload':
            print '[*] SWEP unload: Unload site. Usage: unload'
        elif module == 'whois':
            print '[*] SWEP whois: Check site whois. Usage: whois *args'
        elif module == 'subnet':
            print '[*] SWEP subnet: Check site subnet. Usage: subnet [c/b] *args'
        elif module == 'addr':
            print '[*] SWEP addr: Get site address. Usage: addr *args'
        elif module == 'database':
            print '[*] SWEP Database: Access session database. Usage: database [search load insert update delete help] *args'
        elif module == 'set':
            print '[*] SWEP set: Set variable. Usage: set argument value'
        elif module == 'unset':
            print '[*] SWEP unset: Unset variable. Usage: unset argument'
        elif module == 'exploit':
            print '[*] SWEP exploit: Exploit site. Usage: exploit site'
        elif module == 'fingerprint':
            print '[*] SWEP fingerprint: Check site fingerprint. Usage: fingerprint site'
        elif module == 'grab':
            print '[*] SWEP grab: Grab specified page. Usage: grab url'
        elif module == 'info':
            print '[*] SWEP info: Show exploit info.'
        elif module == 'cd':
            print '[*] SWEP CD: So why you can see this?'
        elif module == 'database':
            self.help('database')
        elif module == 'site':
            print '[*] SWEP Site Module: site [whois subnet address fingerprint grab exploit check domain help] *args'
        elif module == 'db_search':
            print '[*] SWEP Host Database search: Search host. Usage: database search [keyword]'
        elif module == 'db_load':
            print '[*] SWEP Host Database load: Load specified host. Usage: database load [sessid]'
        elif module == 'db_update':
            print '[*] SWEP Host Database update: Update specified host. Usage: database update [sessid]'
        elif module == 'db_delete':
            print '[*] SWEP Host Database delete: Delete specified host. Usage: database delete [sessid]'
        elif module == 'swepdb_backup':
            print '[*] SWEP Database backup: Backup current SWEP Database. Usage: swepdb backup [filename]'
        elif module == 'swepdb_restore':
            print '[*] SWEPDB Database restore: Restore SWEP Database from file. Usage: swepdb restore [filename]'
        elif module == 'swepdb':
            print '[*] SWEPDB usage: swepdb [init update backup restore info help] *args'
        elif module == 'swepdb_init':
            print '[*] SWEPDB init: (DANGEROUS) Re-initialize SWEP Database. Usage: swepdb init'
        elif module == 'swepdb_update':
            print '[*] SWEPDB update: Update Exploit database. Usage: swepdb update'
        elif module == 'swepdb_info':
            print '[*] SWEPDB info: Show current database information and database backup. Usage: swepdb info'
        else:
            pass
        pass


    def help(self,module):
        if module == None:
            pass
        elif module == 'database':
            print '''
        /////////////////////////////////////////////////////////////
        SWEP database help
        Usage: database [search load insert update delete help] *args
        /////////////////////////////////////////////////////////////
        PARAM       DESCRIPTION                     USAGE
        -----       -----------                     -----
        search      Search session.                 database search [name]
        load        Load specified session.         database load [sessid]
        insert      Insert session.                 database insert
        update      Update session.                 database update [sessid]
        delete      Delete session.                 database delete [sessid]
        help        show this help. 
        '''
        elif module == 'site':
            print '''
        /////////////////////////////////////////////////////////////
        SWEP site help
        Usage: site [whois subnet [c/b] address fingerprint grab exploit check domain help] *args
        /////////////////////////////////////////////////////////////
        PARAM       DESCRIPTION                     USAGE
        -----       -----------                     -----
        whois       Get whois information.          site whois
        subnet      Get subnet information (c/b).   site subnet *args
        address     Get site address.               site address
        fingerprint Get site fingerprint.           site fingerprint
        grab        Grab site homepage.             site grab
        exploit     Exploit site.                   site exploit
        check       Check site information.         site check *args
        domain      Get sites on same host          site domain
        help        show this help.
        '''
        elif module == 'check':
            print '''
        /////////////////////////////////////////////////////////////
        SWEP site CheckModule help
        Usage: site check [cms version waf language db  update system] *args
        /////////////////////////////////////////////////////////////
        PARAM       DESCRIPTION                     USAGE
        -----       -----------                     -----
        cms         Check site CMS.                 site check cms
        version     Get site CMS version.           site check version
        waf         Check site WAF.                 site check waf
        language    Get site programming language.  site check language
        db          Get site database.              site check db
        update      Update site information.        site check update
        system      Check site operating system.    site check system
        help        Show this help
        '''
        elif module == 'swepdb':
            print '''
        /////////////////////////////////////////////////////////////
        SWEP SWEPDB help
        Usage: swepdb [init update backup restore info] *args
        /////////////////////////////////////////////////////////////
        PARAM       DESCRIPTION                     USAGE
        -----       -----------                     -----
        init        Initialize SWEP Database.       swepdb init
        update      Update SWEP Database.           swepdb update
        backup      Backup SWEP Database to file    swepdb backup *args
        restore     Restore SWEP Database from file swepdb restore *args
        info        Show SWEP Database info         swepdb info
        help        Show this help                  swepdb help
        '''
        elif module == 'scanner':
            print '''
        ////////////////////////////////////////////////////////////
        SWEP Scanner help
        Usage: scanner [load unload set unset list interactive scan info help] *args
        ////////////////////////////////////////////////////////////
        PARAM       DESCRIPTION                     USAGE
        -----       -----------                     -----
        load        Load a scanner.                 scanner load *args
        unload      Unload a scanner.               scanner unload *args
        set         Set a argument to value.        scanner set *args
        unset       Unset a argument.               scanner unset *args
        list        Show a scanner.                 scanner list
        interactive Start scanner interactive shell scanner interactive
        scan        Start scan                      scanner scan
        info        Show scanner info               scanner info
        help        Show this help                  scanner help
        '''
        elif module == 'help':
            print '''
        ////////////////////////////////////////////////////////////
        SWEP MAIN help
        Usage: None
        ////////////////////////////////////////////////////////////
        Welcome to SWEP Help.
        Type "help database" to get database help.
        Type "help check" to get information gathering module help.
        Type "help database" to get SWEPDB module help.
        Type "help site" to get scanner module help.
        '''
        else:
            pass
        pass

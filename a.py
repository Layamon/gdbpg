class dump_memory_contexts(gdb.Command):
    def __init__(self):
        super(dump_memory_contexts, self).__init__('dump_memory_contexts',
                                                   gdb.COMMAND_USER,
                                                   gdb.COMPLETE_SYMBOL)
    def invoke(self, argstr, from_tty):
        top = gdb.parse_and_eval('(AllocSetContext *) TopMemoryContext')
        self.show(top, '')
    def show(self, mcxt, indent):
        while mcxt:
            mcxt = gdb.parse_and_eval('(AllocSetContext *) {}'.format(mcxt))
            header = mcxt['header']
            name = header['name']
            allocated = int(header['mem_allocated'])
            child = header['firstchild']
            if child or allocated > 0:
                print('{}{}: {}: {}'.format(indent, mcxt, name, allocated))
            else:
                print('{}{}: {}: {}'.format(indent, mcxt, name, allocated))
            self.show(child, indent + '  ')
            mcxt = header['nextchild']
dump_memory_contexts()

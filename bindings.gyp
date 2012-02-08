{
  'targets': [
    {
      'target_name': 'o3',
      'sources': [ 'hosts/node-o3/sh_node.cc', 'hosts/node-o3/sh_node_libs.cc' ],
      'include_dirs' : [    'include',
                            'hosts',
                            'modules',
                            'deps' ],
      'libraries' : ['-lxml2'],
      'cflags' : ['-O3', '-msse2', '-ffast-math', '-fexceptions'],
      'cflags_cc' : ['-O3', '-msse2', '-ffast-math', '-fexceptions'],
      'linkflags' : ['LINKFLAGS']         
    }
  ]

}

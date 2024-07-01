#  using Puppet to make changes to our configuration file

file_line {'Turn off passwd auth':
	ensure => 'present',
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no'

}

file_line {'Turn off passwd auth':
        ensure => 'present',
        path   => '/etc/ssh/ssh_config',
        line   => 'IdentityFile ~/.ssh/school',

}
~            

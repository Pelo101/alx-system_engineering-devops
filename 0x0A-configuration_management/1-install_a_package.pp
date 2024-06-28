# Using Puppet, install flask from pip3.

exec {'install_flask and _werkzeug':
    command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.3',
    path    => ['/usr/bin', '/usr/local/bin'],

}

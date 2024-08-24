# Update limit request limint to prevent failures

exec { 'update_limit_and_restart' :
  command => "sed -i 's/1606441/2000000/' /etc/default/nginx && service nginx restart",
  path    => ['/bin', '/usr/bin'],
}

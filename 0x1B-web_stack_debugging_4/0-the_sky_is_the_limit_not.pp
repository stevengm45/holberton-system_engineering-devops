# Fix limit requests.
exec { 'replace':
  environment => ['DIR=/etc/default/nginx',
                  'OLD=15',
                  'NEW=2000'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => ['/usr/bin', '/bin']
}
# Restart Nginx server
exec { 'restart':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/bin']
}

# Changes to our configuration file with Puppet.
file_line { 'Disallow password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}
file_line { 'Use the private key ~/.ssh/holberton':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton'
}

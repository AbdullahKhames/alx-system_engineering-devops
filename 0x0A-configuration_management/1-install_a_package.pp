# This is a script to install flask version 2.1.0
package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
  name     => flask,
}

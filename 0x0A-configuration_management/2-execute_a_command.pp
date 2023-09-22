# This is a script kill process killmenow
exec { 'pkill':
  command => '/bin/pkill killmenow',
  onlyif  => '/bin/pgrep killmenow >/dev/null 2>&1',
}

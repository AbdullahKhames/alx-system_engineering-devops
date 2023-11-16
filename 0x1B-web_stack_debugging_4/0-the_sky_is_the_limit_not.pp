# This is a comment
# this configuration changes the maximum allowed open files by nginx
# we can know the maximum by  grep -i 'Max open files' /proc/$(cat /var/run/nginx.pid)/limits
# or cat /proc/$(cat /var/run/nginx.pid)/limits

exec { 'modify_file':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec { 'Restart-nginx':
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d/',
}

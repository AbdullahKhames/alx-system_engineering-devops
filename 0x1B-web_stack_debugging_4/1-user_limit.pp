# increase ulimit hard for holberton user
# also increase soft limit

exec{ 'increase_hard_limit_for_user_holberton':
    command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}

exec{ 'increase_soft_limit_for_user_holberton':
    command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}

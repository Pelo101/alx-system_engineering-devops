# A puppet to correct the file exstention of a wordpress file
$setting_file = '/var/www/html/wp-settings.php'

#Fix the class name extension

exec { 'replace_class_name':
command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${setting_file}",
path    => ['/bin', '/usr/bin']

}


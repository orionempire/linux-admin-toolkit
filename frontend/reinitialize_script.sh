#! /bin/bash

mysql -u root  -e 'DROP SCHEMA `linux-admin-toolkit`'
mysql -u root  -e 'CREATE SCHEMA `linux-admin-toolkit`'

cd /home/sysadmin/workspace/linux-admin-toolkit/frontend/

python manage.py syncdb --noinput

python manage.py createsuperuser --username sysadmin --email none@none.com --noinput

#delme hashes to -> pbkdf2_sha256$10000$Q6pHBZBRK3X2$AHfB8wkd/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M=
#includes escaped characters in hash
echo 'UPDATE `linux-admin-toolkit`.`auth_user` SET `password`='"'"pbkdf2_sha256\$10000\$Q6pHBZBRK3X2\$AHfB8wkd\/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M="'"' WHERE `id`='"'"1"';" |mysql -u root
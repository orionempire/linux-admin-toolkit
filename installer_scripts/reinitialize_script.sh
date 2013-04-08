#! /bin/bash
 
 #Version 00.00.09
 
rm ../data/database.db

python manage.py syncdb --noinput

python manage.py createsuperuser --username sysadmin --email sysadmin@linux-admin-toolkit.com --noinput

#delme hashes to -> pbkdf2_sha256$10000$Q6pHBZBRK3X2$AHfB8wkd/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M=
#includes escaped characters in hash 
#echo 'UPDATE `auth_user` SET `password`='"'"pbkdf2_sha256\$10000\$Q6pHBZBRK3X2\$AHfB8wkd\/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M="'"' WHERE `id`='"'"1"';" |sqlite3 ../data/database.db


#create view only user

cat <<EOF | python manage.py shell
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
user = User.objects.create_user('view', 'viewonly@nodomain.com', 'view')
permission = Permission.objects.get(codename="change_physical")
user.user_permissions.add(permission)
permission = Permission.objects.get(codename="change_virtual")
user.user_permissions.add(permission)
user.save()
EOF

python manage.py changepassword sysadmin
chown apache.apache ../data/database.db

echo "Intialization completed. Now import data." 
